"""62편 커버 시안(11/6 "좀 약한 것 같은데" → 숫자 크게·대비). python cover62.py → cover_D/E/F.jpg (work/62에서, 윈도 크롬)"""
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
 # D: 61편처럼 둘로 나눔 — 켜진 날(무지개) / 꺼진 날(흙탕물)
 "D": """<div class="bg" style="left:0;width:540px;background-image:url(img/09.webp);background-position:35% 50%"></div>
<div class="bg" style="left:540px;width:540px;background-image:url(img/03.webp);background-position:45% 50%"></div>
<div style="position:absolute;left:532px;top:0;bottom:0;width:16px;background:#E53935"></div>
<div class="shade" style="top:260px;height:640px"></div>
<div class="t y" style="top:330px;font-size:250px;-webkit-text-stroke:30px #000">117억</div>
<div class="t w" style="top:620px;font-size:150px;-webkit-text-stroke:22px #000">분수가 멈춘다?</div>""",
 # E: 숫자 하나를 아주 크게
 "E": """<div class="bg" style="left:0;right:0;background-image:url(img/09.webp)"></div>
<div class="shade" style="top:230px;height:720px"></div>
<div class="t y" style="top:290px;font-size:330px;-webkit-text-stroke:34px #000">117억</div>
<div class="t w" style="top:660px;font-size:170px;-webkit-text-stroke:24px #000">세금괴물?</div>""",
 # F: 영상 속 빨간 도장 그대로
 "F": """<div class="bg" style="left:0;right:0;background-image:url(img/09.webp)"></div>
<div class="shade" style="top:230px;height:740px"></div>
<div class="stamp" style="top:300px;font-size:260px">117억</div>
<div class="t w" style="top:690px;font-size:160px;-webkit-text-stroke:24px #000">세금괴물?</div>""",
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
subprocess.run(["node", "_c.mjs", *V], check=True)
for k in V: os.remove(f"_c_{k}.html")
os.remove("_c.mjs"); print("ok")
