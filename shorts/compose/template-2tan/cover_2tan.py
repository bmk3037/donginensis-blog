"""채널 통일 커버(섬네일): python3 cover_2tan.py 편번호 그림.jpg "위 작은 줄(장소·대상)" "가운데 큰 줄(훅)" "아래 줄(궁금증)" 결과.jpg [그림 위치 x% y% 확대%]
   규칙(11/4): 왼쪽 위 채널 로고, 위 흰 줄 → 노란 큰 줄 → 흰 줄, 도장·번호 없음(11/4 대표이사 "숨은설비 #은 빼자").
   인스타 프로필 격자(3:4 가운데) 안에 글자가 다 들어가게 세로 300~1500px 안에 둔다. 1080×1920 jpg."""
import sys, os, subprocess, tempfile, shutil
nn, img, a, b, c, out = sys.argv[1:7]
pos = sys.argv[7:10] if len(sys.argv) >= 10 else ["50", "55", "118"]
T = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(T, "..", "fonts")
d = tempfile.mkdtemp(); shutil.copy(img, os.path.join(d, "bg.jpg"))
for f in ("Pretendard-ExtraBold.woff2",): shutil.copy(os.path.join(F, f), os.path.join(d, f))
html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:P;src:url(Pretendard-ExtraBold.woff2)}}
body{{margin:0;width:1080px;height:1920px;overflow:hidden;background:#000}}
.bg{{position:absolute;inset:0;background:url(bg.jpg) {pos[0]}% {pos[1]}%/auto {pos[2]}%}}
.shade{{position:absolute;left:0;right:0;top:220px;height:760px;background:linear-gradient(rgba(10,20,40,.0),rgba(10,20,40,.55) 25%,rgba(10,20,40,.55) 70%,rgba(10,20,40,0))}}
.t{{position:absolute;left:40px;right:40px;text-align:center;font-family:P;white-space:nowrap;paint-order:stroke fill}}
.a{{top:330px;font-size:84px;color:#fff;-webkit-text-stroke:14px #000}}
.b{{top:450px;font-size:150px;color:#FFD43B;-webkit-text-stroke:22px #000;letter-spacing:-4px}}
.c{{top:660px;font-size:72px;color:#fff;-webkit-text-stroke:12px #000}}
.badge{{position:absolute;left:44px;top:250px;width:118px;height:118px;border-radius:50%;background:#0A2A55;border:5px solid #fff;color:#fff;font-family:P;text-align:center;font-size:22px;line-height:1.1;display:flex;flex-direction:column;justify-content:center;opacity:0}}
.badge b{{color:#FFD43B;font-size:25px}}
.stamp{{position:absolute;left:60px;top:1390px;padding:6px 26px 10px;border:8px solid #E53935;border-radius:14px;background:rgba(255,255,255,.92);color:#E53935;font-family:P;font-size:58px;transform:rotate(-5deg)}}
</style></head><body><div class="bg"></div><div class="shade"></div>
<div class="t a">{a}</div><div class="t b">{b}</div><div class="t c">{c}</div>
<script>
function fit(){{document.querySelectorAll('.t').forEach(e=>{{let fs=parseFloat(getComputedStyle(e).fontSize);const s=document.createElement('span');s.style.display='inline-block';s.innerHTML=e.innerHTML;e.innerHTML='';e.appendChild(s);while(s.getBoundingClientRect().width>1000&&fs>40){{fs-=4;e.style.fontSize=fs+'px';}}}});}}
document.fonts.ready.then(fit);
</script></body></html>'''
open(os.path.join(d, "c.html"), "w").write(html)
js = f'''import {{ createRequire }} from "module";
let pw; try {{ pw = createRequire("{os.path.join(T, '..')}/")("playwright"); }} catch {{ pw = createRequire("/opt/node-tools/node_modules/")("playwright"); }}
const b = await pw.chromium.launch(); const p = await b.newPage({{ viewport: {{ width: 1080, height: 1920 }} }});
await p.goto("file://{d}/c.html"); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
await p.screenshot({{ path: "{os.path.abspath(out)}", type: "jpeg", quality: 92 }}); await b.close();'''
open(os.path.join(d, "s.mjs"), "w").write(js)
subprocess.run(["node", os.path.join(d, "s.mjs")], check=True); shutil.rmtree(d); print(out)
