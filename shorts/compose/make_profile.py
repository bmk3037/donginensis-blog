"""알고보니 채널 프로필 이미지·워터마크 만들기 (11/9). 결과: shorts/brand/
 - avatar_800.png  : 유튜브·인스타 프로필 사진(원형으로 잘려도 글자가 안 잘리게 가운데)
 - watermark_150.png : 유튜브 스튜디오 > 맞춤설정 > 브랜딩 > 동영상 워터마크(투명 배경 150x150)
 - banner_2560x1440.png : 유튜브 배너(가운데 1546x423 안전 영역)"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "brand")
os.makedirs(OUT, exist_ok=True)
FB = r"C:\Windows\Fonts\malgunbd.ttf"
NAVY, YEL, WHITE = (10, 42, 85), (255, 212, 59), (255, 255, 255)


def draw_name(d, cx, cy, size, shadow=False):
    f = ImageFont.truetype(FB, size)
    w1, w2 = d.textlength("알고", font=f), d.textlength("보니", font=f)
    x = cx - (w1 + w2) / 2
    y = cy - size * 0.62
    d.text((x, y), "알고", font=f, fill=WHITE)
    d.text((x + w1, y), "보니", font=f, fill=YEL)


# 프로필 800x800
a = Image.new("RGB", (800, 800), NAVY)
d = ImageDraw.Draw(a)
d.ellipse((40, 40, 760, 760), outline=WHITE, width=14)
draw_name(d, 400, 400, 150)
a.save(os.path.join(OUT, "avatar_800.png"))

# 워터마크 150x150 (투명, 흰 테두리 원)
w = Image.new("RGBA", (150, 150), (0, 0, 0, 0))
d = ImageDraw.Draw(w)
d.ellipse((4, 4, 146, 146), fill=NAVY + (255,), outline=WHITE + (255,), width=4)
draw_name(d, 75, 75, 31)
w.save(os.path.join(OUT, "watermark_150.png"))

# 배너 2560x1440
b = Image.new("RGB", (2560, 1440), NAVY)
d = ImageDraw.Draw(b)
draw_name(d, 1280, 700, 230)
f = ImageFont.truetype(FB, 64)
t = "누구나 아는 곳의 숨은 사연"
d.text((1280 - d.textlength(t, font=f) / 2, 830), t, font=f, fill=WHITE)
b.save(os.path.join(OUT, "banner_2560x1440.png"))
print("ok", OUT)
