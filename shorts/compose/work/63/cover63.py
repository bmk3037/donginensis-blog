"""63편 커버 시안(이탄생 13편 틀)  — 원본: 62편 커버 시안(11/6 "좀 약한 것 같은데" → 숫자 크게·대비). python cover62.py → cover_D/E/F.jpg (work/62에서, 윈도 크롬)"""
import os, subprocess
D = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
CSS = """@font-face{font-family:P;src:url(fonts/Pretendard-ExtraBold.woff2)}
body{margin:0;width:1080px;height:1920px;overflow:hidden;background:#000;position:relative}
.bg{position:absolute;top:0;bottom:0;background-size:cover;background-position:50% 50%}
.t{position:absolute;left:0;right:0;text-align:center;font-family:P;white-space:nowrap;paint-order:stroke fill;letter-spacing:-6px}
.y{color:#FFD43B}.w{color:#fff}.r{color:#E53935}
.shade{position:absolute;left:0;right:0;background:linear-gradient(rgba(5,10,25,0),rgba(5,10,25,.72) 30%,rgba(5,10,25,.72) 70%,rgba(5,10,25,0))}
.stamp{position:absolute;left:50%;transform:translateX(-50%) rotate(-6deg);border:16px solid #E53935;border-radius:28px;padding:0 40px 18px;font-family:P;color:#E53935;background:rgba(255,255,255,.93);white-space:nowrap;letter-spacing:-6px}"""
V = {
 # A: 이탄생 100만+ 13편 틀 — 장소 이름만 가운데 크게
 "A": """<div class="bg" style="left:0;right:0;background-image:url(img/01.webp)"></div>
<div class="t w" style="top:760px;font-size:200px;-webkit-text-stroke:6px rgba(40,40,40,.85);text-shadow:0 6px 18px rgba(0,0,0,.5);letter-spacing:-4px;line-height:1.05">광안리<br>불꽃축제</div>""",
 # B: 장소 이름 + 61편식 숫자 대비 한 줄(작게)
 "B": """<div class="bg" style="left:0;right:0;background-image:url(img/01.webp)"></div>
<div class="t w" style="top:700px;font-size:200px;-webkit-text-stroke:6px rgba(40,40,40,.85);text-shadow:0 6px 18px rgba(0,0,0,.5);letter-spacing:-4px;line-height:1.05">광안리<br>불꽃축제</div>
<div class="t y" style="top:1150px;font-size:96px;-webkit-text-stroke:14px #000">서울 130억 · 부산 20억</div>""",

 # D~F: 장소 이름 + 궁금증 한 줄(11/6 대표이사 "섬네일에 궁금증이 있어야")
 "D": """<div class="bg" style="left:0;right:0;background-image:url(img/01.webp)"></div>
<div class="t w" style="top:660px;font-size:190px;-webkit-text-stroke:6px rgba(40,40,40,.85);text-shadow:0 6px 18px rgba(0,0,0,.5);letter-spacing:-4px;line-height:1.05">광안리<br>불꽃축제</div>
<div class="t y" style="top:1110px;font-size:104px;-webkit-text-stroke:15px #000">부산은 왜 20억?</div>""",
 "E": """<div class="bg" style="left:0;right:0;background-image:url(img/01.webp)"></div>
<div class="t w" style="top:660px;font-size:190px;-webkit-text-stroke:6px rgba(40,40,40,.85);text-shadow:0 6px 18px rgba(0,0,0,.5);letter-spacing:-4px;line-height:1.05">광안리<br>불꽃축제</div>
<div class="t y" style="top:1110px;font-size:104px;-webkit-text-stroke:15px #000">다리가 발사대?</div>""",
 "F": """<div class="bg" style="left:0;right:0;background-image:url(img/01.webp)"></div>
<div class="t w" style="top:660px;font-size:190px;-webkit-text-stroke:6px rgba(40,40,40,.85);text-shadow:0 6px 18px rgba(0,0,0,.5);letter-spacing:-4px;line-height:1.05">광안리<br>불꽃축제</div>
<div class="t y" style="top:1110px;font-size:104px;-webkit-text-stroke:15px #000">불꽃 30분, 다리는 닷새?</div>""",

 # G~I: 더 궁금하게(11/6 대표이사 "더더 궁금하게")
 "G": """<div class="bg" style="left:0;right:0;background-image:url(img/01.webp)"></div>
<div class="t w" style="top:430px;font-size:120px;-webkit-text-stroke:5px rgba(40,40,40,.85);text-shadow:0 6px 18px rgba(0,0,0,.5);letter-spacing:-3px">광안리 불꽃축제</div>
<div class="t y" style="top:640px;font-size:170px;-webkit-text-stroke:22px #000;line-height:1.15">서울은 무상<br>부산은 20억?</div>""",
 "H": """<div class="bg" style="left:0;right:0;background-image:url(img/01.webp)"></div>
<div class="t w" style="top:430px;font-size:120px;-webkit-text-stroke:5px rgba(40,40,40,.85);text-shadow:0 6px 18px rgba(0,0,0,.5);letter-spacing:-3px">광안리 불꽃축제</div>
<div class="t y" style="top:600px;font-size:330px;-webkit-text-stroke:34px #000">20억</div>
<div class="t w" style="top:1000px;font-size:120px;-webkit-text-stroke:18px #000">같은 불꽃, 부산은 왜?</div>""",
 "I": """<div class="bg" style="left:0;right:0;background-image:url(img/01.webp)"></div>
<div class="t w" style="top:430px;font-size:120px;-webkit-text-stroke:5px rgba(40,40,40,.85);text-shadow:0 6px 18px rgba(0,0,0,.5);letter-spacing:-3px">광안리 불꽃축제</div>
<div class="t y" style="top:640px;font-size:150px;-webkit-text-stroke:20px #000;line-height:1.15">다리에 뭘 달길래<br>닷새나 막을까?</div>""",

 # J~L: Codex 검수 반영판
 "J": """<div class="bg" style="left:0;right:0;background-image:url(img/01.webp)"></div>
<div class="t w" style="top:430px;font-size:120px;-webkit-text-stroke:5px rgba(40,40,40,.85);text-shadow:0 6px 18px rgba(0,0,0,.5);letter-spacing:-3px">광안리 불꽃축제</div>
<div class="t y" style="top:640px;font-size:150px;-webkit-text-stroke:20px #000;line-height:1.15">서울은 기업 부담<br>부산은 20억?</div>""",
 "K": """<div class="bg" style="left:0;right:0;background-image:url(img/01.webp)"></div>
<div class="t w" style="top:430px;font-size:120px;-webkit-text-stroke:5px rgba(40,40,40,.85);text-shadow:0 6px 18px rgba(0,0,0,.5);letter-spacing:-3px">광안리 불꽃축제</div>
<div class="t y" style="top:600px;font-size:330px;-webkit-text-stroke:34px #000">20억</div>
<div class="t w" style="top:1000px;font-size:110px;-webkit-text-stroke:17px #000">같은 기업 불꽃, 부산은 왜?</div>""",
 "L": """<div class="bg" style="left:0;right:0;background-image:url(img/01.webp)"></div>
<div class="t w" style="top:430px;font-size:120px;-webkit-text-stroke:5px rgba(40,40,40,.85);text-shadow:0 6px 18px rgba(0,0,0,.5);letter-spacing:-3px">광안리 불꽃축제</div>
<div class="t y" style="top:640px;font-size:150px;-webkit-text-stroke:20px #000;line-height:1.15">다리에 뭘 달길래<br>닷새 전부터 막을까?</div>""",

 # M~O: 추가 제안(11/6)
 "M": """<div class="bg" style="left:0;right:0;background-image:url(img/02.webp)"></div>
<div class="t w" style="top:430px;font-size:120px;-webkit-text-stroke:5px rgba(40,40,40,.85);text-shadow:0 6px 18px rgba(0,0,0,.5);letter-spacing:-3px">광안리 불꽃축제</div>
<div class="t y" style="top:640px;font-size:170px;-webkit-text-stroke:22px #000;line-height:1.15">광안대교가<br>발사대?</div>""",
 "N": """<div class="bg" style="left:0;right:0;background-image:url(img/01.webp)"></div>
<div class="t w" style="top:430px;font-size:120px;-webkit-text-stroke:5px rgba(40,40,40,.85);text-shadow:0 6px 18px rgba(0,0,0,.5);letter-spacing:-3px">광안리 불꽃축제</div>
<div class="t y" style="top:640px;font-size:170px;-webkit-text-stroke:22px #000;line-height:1.15">이 불꽃 20억<br>누가 낼까?</div>""",
 "O": """<div class="bg" style="left:0;right:0;background-image:url(img/01.webp)"></div>
<div class="t w" style="top:430px;font-size:120px;-webkit-text-stroke:5px rgba(40,40,40,.85);text-shadow:0 6px 18px rgba(0,0,0,.5);letter-spacing:-3px">광안리 불꽃축제</div>
<div class="t y" style="top:600px;font-size:210px;-webkit-text-stroke:26px #000">130억</div>
<div class="t w" style="top:820px;font-size:110px;-webkit-text-stroke:16px #000">vs</div>
<div class="t y" style="top:940px;font-size:210px;-webkit-text-stroke:26px #000">20억</div>""",

 # P~R: 밤 배경 + 장소 이름 크게(11/7 "광안리 불꽃이 너무 약해, 완전 밤 사진으로")
 "P": """<div class="bg" style="left:0;right:0;background-image:url(img/01_night.jpg)"></div>
<div class="t w" style="top:300px;font-size:230px;-webkit-text-stroke:24px #000;letter-spacing:-6px;line-height:1.02">광안리<br>불꽃축제</div>
<div class="t y" style="top:820px;font-size:130px;-webkit-text-stroke:18px #000;line-height:1.15">이 불꽃 20억<br>누가 낼까?</div>""",
 "Q": """<div class="bg" style="left:0;right:0;background-image:url(img/09_night.jpg)"></div>
<div class="t w" style="top:300px;font-size:230px;-webkit-text-stroke:24px #000;letter-spacing:-6px;line-height:1.02">광안리<br>불꽃축제</div>
<div class="t y" style="top:820px;font-size:130px;-webkit-text-stroke:18px #000;line-height:1.15">이 불꽃 20억<br>누가 낼까?</div>""",
 "R": """<div class="bg" style="left:0;right:0;background-image:url(img/14_night.jpg)"></div>
<div class="t w" style="top:300px;font-size:230px;-webkit-text-stroke:24px #000;letter-spacing:-6px;line-height:1.02">광안리<br>불꽃축제</div>
<div class="t y" style="top:820px;font-size:130px;-webkit-text-stroke:18px #000;line-height:1.15">이 불꽃 20억<br>누가 낼까?</div>""",
 "S": """<div class="bg" style="left:0;right:0;background-image:url(img/01_night.jpg)"></div>
<div class="t w" style="top:640px;font-size:230px;-webkit-text-stroke:24px #000;letter-spacing:-6px;line-height:1.02">광안리<br>불꽃축제</div>
<div class="t y" style="top:1160px;font-size:120px;-webkit-text-stroke:17px #000;line-height:1.15">이 불꽃 20억 누가 낼까?</div>""",
 "T": """<div class="bg" style="left:0;right:0;background-image:url(img/01_night2.jpg)"></div>
<div class="t w" style="top:640px;font-size:230px;-webkit-text-stroke:24px #000;letter-spacing:-6px;line-height:1.02">광안리<br>불꽃축제</div>
<div class="t y" style="top:1160px;font-size:120px;-webkit-text-stroke:17px #000;line-height:1.15">이 불꽃 20억 누가 낼까?</div>""",
 # C: 해변 관객 그림 + 장소 이름
 "C": """<div class="bg" style="left:0;right:0;background-image:url(img/01b.webp)"></div>
<div class="t w" style="top:520px;font-size:200px;-webkit-text-stroke:6px rgba(40,40,40,.85);text-shadow:0 6px 18px rgba(0,0,0,.5);letter-spacing:-4px;line-height:1.05">광안리<br>불꽃축제</div>""",
}
JS = """import { createRequire } from "module"; import { pathToFileURL } from "url";
const pw = createRequire("C:/Users/bmk30/donginensis-blog/shorts/compose/")("playwright");
const b = await pw.chromium.launch({ executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe" });
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
for (const k of process.argv.slice(2)) { await p.goto(pathToFileURL(`_c_${k}.html`).href); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
  await p.screenshot({ path: `cover_${k}.jpg`, type: "jpeg", quality: 92 }); }
await b.close();"""
for k, body in V.items():
    open(f"_c_{k}.html", "w", encoding="utf-8").write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>')
open("_c.mjs", "w", encoding="utf-8").write(JS)
import sys
K = sys.argv[1:] or list(V)
subprocess.run(["node", "_c.mjs", *K], check=True)
for k in V:
    if os.path.exists(f"_c_{k}.html"): os.remove(f"_c_{k}.html")
os.remove("_c.mjs"); print("ok")
