"""도감이 안전모 앞면에 동인엔시스 흰 로고를 얹는다(진짜 로고 파일, 안전모 곡면에 맞춰 살짝 휘게)."""
import os, sys, numpy as np
from PIL import Image
src, out, cx, cy, w = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
bend = float(sys.argv[6]) if len(sys.argv) > 6 else 0.12
im = Image.open(src).convert('RGBA')
lg = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logo', 'logo_white.png')).convert('RGBA')
h = round(w * lg.height / lg.width)
lg = lg.resize((w, h), Image.LANCZOS)
a = np.asarray(lg).astype(float)
pad = int(h * 1.2)
canvas = np.zeros((h + pad, w, 4))
xs = np.linspace(-1, 1, w)
for x in range(w):  # 가운데는 그대로, 양 끝은 아래로 내려 둥근 안전모 앞면처럼
    dy = int(round(bend * h * 2.2 * xs[x] ** 2))
    canvas[dy:dy + h, x] = a[:, x]
# 양 끝은 곡면이라 조금 좁고 흐리게
fade = 1 - 0.35 * np.abs(xs) ** 3
canvas[..., 3] *= fade[None, :]
canvas[..., 3] *= 0.95
L = Image.fromarray(canvas.clip(0, 255).astype(np.uint8), 'RGBA')
im.alpha_composite(L, (cx - w // 2, cy - h // 2))
im.convert('RGB').save(out, quality=95)
