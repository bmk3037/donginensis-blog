"""옆으로 돈 안전모용: 로고를 원통(안전모 둘레)에 감아 붙인다. 앞쪽(보는 사람 쪽)은 넓게, 돌아가는 쪽은 좁게.
   python3 helmet_logo_turn.py 원본 결과 안전모중심x 로고중심y 안전모반폭R 앞방향각도(도, 오른쪽+) 로고폭(호 길이 px) [휨]"""
import os, sys, math, numpy as np
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
cx, cy, R, turn, arc = int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5]), math.radians(float(sys.argv[6])), float(sys.argv[7])
bend = float(sys.argv[8]) if len(sys.argv) > 8 else 0.08
lg = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logo', 'logo_white.png')).convert('RGBA')
W = 1000; H = round(W * lg.height / lg.width)
a = np.asarray(lg.resize((W, H), Image.LANCZOS)).astype(float)
alpha_half = arc / (2 * R)
p0, p1 = turn - alpha_half, turn + alpha_half
x0, x1 = int(cx + R * math.sin(p0)), int(cx + R * math.sin(p1))
h = round(arc * lg.height / lg.width)
im = Image.open(src).convert('RGBA'); base = np.asarray(im).astype(float)
lay = np.zeros((h + int(h * 1.5), x1 - x0 + 1, 4))
for x in range(x0, x1 + 1):
    s = (x - cx) / R
    if abs(s) >= 1: continue
    phi = math.asin(s)
    u = (phi - p0) / (p1 - p0)
    if not 0 <= u <= 1: continue
    col = a[:, min(W - 1, int(u * W))]
    col = np.asarray(Image.fromarray(col[:, None].astype(np.uint8)).resize((1, h), Image.LANCZOS)).reshape(h, 4).astype(float)
    k = (u - 0.5) * 2
    dy = int(round(bend * h * 2.2 * k * k))
    vis = max(0.0, math.cos(phi)) ** 0.6           # 돌아가는 쪽은 흐리게
    col[:, 3] *= 0.95 * vis
    lay[dy:dy + h, x - x0] = col
L = Image.fromarray(lay.clip(0, 255).astype(np.uint8), 'RGBA')
im.alpha_composite(L, (x0, cy - h // 2))
im.convert('RGB').save(out, quality=95)
