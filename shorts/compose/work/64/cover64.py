"""64편 커버 시안 A·B·C (work/64에서 python cover64.py, 윈도 크롬)"""
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
 "A": """<div class="bg" style="left:0;right:0;background-image:url(img/t01night.jpg)"></div><div class="t w" style="top:600px;font-size:300px;-webkit-text-stroke:26px #000;letter-spacing:-8px;line-height:1.02">마곡</div><div class="t y" style="top:930px;font-size:118px;-webkit-text-stroke:17px #000;line-height:1.15">보일러가 도로 밑에?</div>""",
 "B": """<div class="bg" style="left:0;right:0;background-image:url(img/t01night.jpg)"></div><div class="t w" style="top:560px;font-size:280px;-webkit-text-stroke:26px #000;letter-spacing:-8px;line-height:1.02">마곡</div><div class="t y" style="top:870px;font-size:112px;-webkit-text-stroke:17px #000;line-height:1.2">9천 세대가<br>한꺼번에 꺼진 이유</div>""",
 "C": """<div class="bg" style="left:0;right:0;background-image:url(img/t01night.jpg)"></div><div class="t w" style="top:560px;font-size:180px;-webkit-text-stroke:22px #000;letter-spacing:-6px;line-height:1.05">보일러 없는 집</div><div class="t y" style="top:800px;font-size:140px;-webkit-text-stroke:18px #000;line-height:1.15">보일러는 어디?</div>""",
}
JS ="""import { createRequire } from "module"; import { pathToFileURL } from "url";
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
