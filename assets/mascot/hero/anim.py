"""홈페이지 도감이 반복 영상: 정지 그림(진짜 로고 얹음) 위에 데이터 빛줄기·표시등·경고등 움직임을 직접 그린다. 8초, 30fps, 끝=처음."""
import math, numpy as np, cv2, subprocess, os
base = cv2.imread('base.png').astype(np.float32) / 255
H, W = base.shape[:2]; FPS, DUR = 30, 8.0; N = int(FPS * DUR)
rng = np.random.default_rng(3)
def bez(p0, p1, p2, p3, t):
    t = t[:, None]; return (1-t)**3*p0 + 3*(1-t)**2*t*p1 + 3*(1-t)*t**2*p2 + t**3*p3
# 도감이 왼쪽(제어반 뒤에서 나오는 것처럼)에서 화면 왼쪽으로 흐르는 빛줄기 7개
curves = []
for k in range(7):
    y0 = 300 + k * 38 + rng.uniform(-10, 10)
    p0 = np.array([815, y0]); p3 = np.array([-60, 140 + k * 85 + rng.uniform(-30, 30)])
    p1 = p0 + [-220, rng.uniform(-90, 60)]; p2 = p3 + [380, rng.uniform(-80, 80)]
    pts = bez(p0, p1, p2, p3, np.linspace(0, 1, 400)).astype(np.int32)
    curves.append((pts, rng.uniform(0, 1), rng.choice([1, 2])))
lineL = np.zeros((H, W), np.float32)
for pts, _, _ in curves: cv2.polylines(lineL, [pts.reshape(-1, 1, 2)], False, 0.18, 2, cv2.LINE_AA)
lineL = cv2.GaussianBlur(lineL, (0, 0), 1.2) + cv2.GaussianBlur(lineL, (0, 0), 6) * 1.5
fade = np.clip((np.arange(W)[None, :] - 0) / 120, 0, 1) * np.clip((830 - np.arange(W)[None, :]) / 60, 0, 1)
blue = np.array([1.0, 0.75, 0.35], np.float32)  # BGR: 하늘빛 파랑
os.makedirs('anim', exist_ok=True)
for f in range(N):
    t = f / N
    L = np.zeros((H, W), np.float32)
    for pts, ph, sp in curves:
        for j in range(3):                       # 줄마다 빛 알갱이 3개가 왼쪽으로 흐름(8초에 sp바퀴 → 끝=처음)
            u = ((t * sp + ph + j / 3) % 1)
            i = int(u * (len(pts) - 1)); x, y = pts[i]
            for tail in range(0, 26, 2):         # 꼬리
                ii = max(0, i - tail * 3); xx, yy = pts[ii]
                cv2.circle(L, (int(xx), int(yy)), 3, 1.0 - tail / 26, -1, cv2.LINE_AA)
    L = cv2.GaussianBlur(L, (0, 0), 2) * 0.9 + cv2.GaussianBlur(L, (0, 0), 9) * 1.6
    glow = (L + lineL * (0.8 + 0.2 * math.sin(2 * math.pi * t * 2))) * fade
    out = base + glow[..., None] * blue[None, None, :] * 0.85
    # 제어반 초록 표시등: 차례로 깜빡임
    for k, (x, y) in enumerate([(1305, 250), (1317, 250), (1329, 250), (1305, 262), (1317, 262), (1329, 262)]):
        on = 0.5 + 0.5 * math.sin(2 * math.pi * (t * 4 - k / 6))
        g = np.zeros((H, W), np.float32); cv2.circle(g, (x, y), 5, on, -1); g = cv2.GaussianBlur(g, (0, 0), 4)
        out += g[..., None] * np.array([0.25, 1.0, 0.35], np.float32) * 0.6
    # 꼭대기 빨간 경고등: 천천히 숨쉬듯
    pul = 0.5 + 0.5 * math.sin(2 * math.pi * t * 2)
    g = np.zeros((H, W), np.float32); cv2.circle(g, (1190, 68), 16, pul, -1); g = cv2.GaussianBlur(g, (0, 0), 14)
    out += g[..., None] * np.array([0.2, 0.25, 1.0], np.float32) * 0.9
    cv2.imwrite(f'anim/{f:03d}.png', (np.clip(out, 0, 1) * 255).astype(np.uint8))
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', 'anim/%03d.png', '-c:v', 'libx264', '-preset', 'slow', '-crf', '22',
                '-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-an', 'dogam_hero_loop.mp4'], check=True)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', 'dogam_hero_loop.mp4', '-c:v', 'libvpx-vp9', '-b:v', '0', '-crf', '34', '-an', 'dogam_hero_loop.webm'], check=True)
cv2.imwrite('dogam_hero_poster.jpg', (base * 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 90])
print('ok', N)
