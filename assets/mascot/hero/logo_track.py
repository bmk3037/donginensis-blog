"""홈페이지 클립: Veo가 그린 가짜 마크를 프레임마다 지우고, 그 자리(안전모 앞)에 진짜 로고를 안전모 방향에 맞춰 감아 붙인다."""
import json, math, glob, numpy as np, cv2
from PIL import Image
fs = sorted(glob.glob('fr/*.png'))
tr = json.load(open('track.json'))
CX, R = 852, 118                       # 안전모 가운데 x, 반폭(정면에 가까운 프레임에서 잼)
ex = np.array([b[0] + b[2] / 2 if b else np.nan for _, b, _, _ in tr]); ey = np.array([b[1] + b[3] / 2 if b else np.nan for _, b, _, _ in tr])
first = int(np.where(~np.isnan(ex))[0][0])
ex[:first], ey[:first] = ex[first], ey[first]
for arr in (ex, ey):                     # 빠진 프레임은 앞 값으로, 그다음 5프레임 평균으로 떨림 줄이기
    for i in range(len(arr)):
        if np.isnan(arr[i]): arr[i] = arr[i - 1]
    arr[:] = np.convolve(np.pad(arr, 3, mode='edge'), np.ones(7) / 7, mode='valid')
ex = 870 + (ex - 870) * 0.5   # Veo 마크는 돌아간 프레임에서 앞쪽보다 더 옆에 그려져 있어 절반만 따라감
lg = np.asarray(Image.open('/home/user/donginensis-blog/assets/logo/logo_white.png').convert('RGBA').resize((1000, 183), Image.LANCZOS)).astype(float)
ARC = 140; LH = round(ARC * 110 / 600)
lgs = np.asarray(Image.fromarray(lg.astype(np.uint8)).resize((1000, LH), Image.LANCZOS)).astype(float)
for i, f in enumerate(fs):
    a = cv2.imread(f)
    b = tr[i][1]
    if b:
        x, y, w, h, _ = b; pad = 7
        m = np.zeros(a.shape[:2], np.uint8)
        cv2.ellipse(m, (x + w // 2, y + h // 2), (w // 2 + pad, h // 2 + pad), 0, 0, 360, 255, -1)
        a = cv2.inpaint(a, m, 6, cv2.INPAINT_TELEA)
    rgb = cv2.cvtColor(a, cv2.COLOR_BGR2RGB).astype(float)
    turn = math.asin(max(-0.95, min(0.95, (ex[i] - CX) / R)))
    half = ARC / (2 * R); p0, p1 = turn - half, turn + half
    x0, x1 = int(CX + R * math.sin(p0)), int(CX + R * math.sin(p1))
    top = int(round(ey[i] + 4 - LH / 2))
    for xx in range(x0, x1 + 1):
        s = (xx - CX) / R
        if abs(s) >= 1: continue
        phi = math.asin(s); u = (phi - p0) / (p1 - p0)
        if not 0 <= u <= 1: continue
        col = lgs[:, min(999, int(u * 1000))]
        k = (u - 0.5) * 2; dy = int(round(0.06 * LH * 2.2 * k * k))
        al = col[:, 3:4] / 255 * 0.95 * max(0.0, math.cos(phi)) ** 0.6
        ys = slice(top + dy, top + dy + LH)
        rgb[ys, xx] = rgb[ys, xx] * (1 - al) + col[:, :3] * al
    Image.fromarray(rgb.clip(0, 255).astype(np.uint8)).save(f.replace('fr/', 'out/'))
print('done', len(fs), 'first emblem frame', first)
