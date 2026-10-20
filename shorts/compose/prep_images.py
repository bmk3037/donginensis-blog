"""플로우에서 받은 이미지 묶음(zip 또는 폴더)을 img/00.webp, 01.webp ... 로 바꾸고 번호 붙은 한눈 보기(all.png)를 만든다.
   작업 폴더 안에서: python3 -I ../../shorts/compose/prep_images.py images.zip
   파일 이름 순서가 프롬프트 번호 순서와 다를 수 있으니, all.png를 보고 장면 배치를 맞춘다."""
import glob, json, os, sys, tempfile, zipfile
from PIL import Image, ImageDraw

src = sys.argv[1]
if src.endswith(".zip"):
    tmp = tempfile.mkdtemp(prefix="flow_")
    zipfile.ZipFile(src).extractall(tmp)
    src = tmp
fs = sorted(f for f in glob.glob(os.path.join(src, "**", "*"), recursive=True)
            if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")) and "__MACOSX" not in f)
os.makedirs("img", exist_ok=True)
json.dump([os.path.relpath(f, src) for f in fs], open("index.json", "w"), ensure_ascii=False, indent=0)
thumbs = []
for i, f in enumerate(fs):
    im = Image.open(f).convert("RGB")
    im.save(f"img/{i:02d}.webp", quality=92)
    t = im.resize((216, 384)); d = ImageDraw.Draw(t)
    d.rectangle((0, 0, 40, 26), fill="black"); d.text((5, 6), str(i), fill="yellow")
    thumbs.append(t)
cols = 12; rows = (len(thumbs) + cols - 1) // cols
sheet = Image.new("RGB", (216 * cols, 384 * max(1, rows)), "black")
for i, t in enumerate(thumbs):
    sheet.paste(t, ((i % cols) * 216, (i // cols) * 384))
sheet.save("all.png")
print(len(fs), "장 → img/, 한눈 보기 all.png, 원래 이름 index.json")
