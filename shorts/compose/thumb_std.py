"""알고보니 표준 섬네일 (11/9 갱신: 장소 이름 + 가장 센 훅 한 줄, 훅은 노란색으로 크게)
알고보니 표준 섬네일 (11/9 대표이사: 섬네일도 통일 기준, 업로드시 잘 보이게).
사용: python thumb_std.py 그림.jpg "장소 이름" 결과.jpg [두번째 줄]
규칙(11/9 갱신): 1줄 장소 이름(흰색 크게) + 2줄 가장 센 훅(노란색 크게, 12자 안팎), 가운데(세로 약 50%). 훅은 대본의 첫 반전/왜-이유 문장에서 뽑는다.
잘 보이게: 글자 뒤 어두운 띠(그림이 밝을수록 진함), 두꺼운 어두운 테두리와 그림자, 인스타 프로필 격자(3:4 가운데 1080x1440) 안에 글자 전부, 왼쪽 위 알고보니 워터마크 알약."""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageStat

src, name, out = sys.argv[1:4]
sub = sys.argv[4] if len(sys.argv) > 4 else ""
W, H = 1080, 1920
FB = r"C:\Windows\Fonts\malgunbd.ttf"
im = Image.open(src).convert("RGB")
im = im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)
im = im.crop((0, 0, W, H)) if im.height >= H else im.resize((W, H))

probe = ImageDraw.Draw(im)
lines = [name] + ([sub] if sub else [])
fonts = []
for i, t in enumerate(lines):
    size = 230 if i == 0 else 150
    while True:
        f = ImageFont.truetype(FB, size)
        bb = probe.textbbox((0, 0), t, font=f, stroke_width=10)
        if bb[2] - bb[0] <= 900 or size < 60:
            break
        size -= 6
    fonts.append((t, f, bb[2] - bb[0], bb[3] - bb[1]))
gap = 40
total = sum(h for _, _, _, h in fonts) + gap * (len(fonts) - 1)
y0 = int(H * 0.50 - total / 2)

lum = ImageStat.Stat(im.crop((0, y0 - 80, W, y0 + total + 80)).convert("L")).mean[0]
alpha = int(60 + 110 * min(1, lum / 200))
band = Image.new("RGBA", im.size, (0, 0, 0, 0))
ImageDraw.Draw(band).rectangle((0, y0 - 70, W, y0 + total + 70), fill=(10, 20, 40, alpha))
band = band.filter(ImageFilter.GaussianBlur(40))
im = Image.alpha_composite(im.convert("RGBA"), band).convert("RGB")

y = y0
for t, f, w, h in fonts:
    x = (W - w) // 2
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).text((x + 5, y + 10), t, font=f, fill=(0, 0, 0, 170), stroke_width=10, stroke_fill=(0, 0, 0, 170))
    sh = sh.filter(ImageFilter.GaussianBlur(10))
    im.paste(sh, (0, 0), sh)
    ImageDraw.Draw(im).text((x, y), t, font=f, fill=((255, 255, 255) if t == name else (255, 212, 59)), stroke_width=10, stroke_fill=(15, 25, 50))
    y += h + gap

d = ImageDraw.Draw(im)
wm = ImageFont.truetype(FB, 54)
d.rounded_rectangle((60, 280, 300, 372), 46, fill=(10, 42, 85), outline=(255, 255, 255), width=5)
w1 = d.textlength("알고", font=wm)
w2 = d.textlength("보니", font=wm)
x0 = 180 - (w1 + w2) / 2
d.text((x0, 297), "알고", font=wm, fill=(255, 255, 255))
d.text((x0 + w1, 297), "보니", font=wm, fill=(255, 212, 59))
im.save(out, quality=93)
print("ok", out)
