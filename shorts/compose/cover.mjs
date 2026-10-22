// 커버(섬네일) 이미지 1080×1920을 만든다. 작업 폴더 안에서 실행한다: node ../../cover.mjs
// 작업 폴더의 cover.json을 읽는다. 예:
//   {"img": "11", "pos": "center 45%", "kick": "LNG 운반선의 비밀",
//    "title": "화물이|[저절로 끓는]|배", "sub": "증발가스 BOG는 어디로 갈까?", "logo": ""}
//   badge: false면 왼쪽 위 "숨은 설비 도감" 로고를 뺀다(기본은 넣음)
//   title: |는 줄바꿈, [ ]는 노란 글자. logo: 흰 로고 PNG 경로(회사 이름을 넣지 않는 공개 편은 비움)
// 결과: cover.jpg(올릴 파일), cover.png
import { createRequire } from "module";
import fs from "fs";
import path from "path";

const here = path.dirname(new URL(import.meta.url).pathname);
let chromium;
try { ({ chromium } = createRequire(here + "/")("playwright")); }
catch { ({ chromium } = createRequire((process.env.PLAYWRIGHT_DIR || "/opt/node-tools/node_modules") + "/")("playwright")); }

const dir = process.cwd();
const c = JSON.parse(fs.readFileSync(path.join(dir, "cover.json"), "utf8"));
const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;");
const title = esc(c.title).replace(/\[(.+?)\]/g, '<span class="y">$1</span>').split("|").join("<br>");
const logo = c.logo ? `<img class="logo" src="${path.resolve(dir, c.logo)}">` : "";

// 글자는 가운데에 모은다: 인스타 격자(3:4)나 유튜브에서 위아래가 잘려도 제목이 남는다.
// 배경은 조금 키워(inset 음수) 플로우 이미지 구석의 생성 표시를 화면 밖으로 민다.
const html = `<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:P;font-weight:700;src:url("fonts/Pretendard-Bold.woff2") format("woff2")}
@font-face{font-family:P;font-weight:800;src:url("fonts/Pretendard-ExtraBold.woff2") format("woff2")}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1920px;overflow:hidden;background:#0A2A55;font-family:P,sans-serif;word-break:keep-all}
.bg{position:absolute;inset:-15% -15% -15% -5%;background:url("img/${c.img}.webp") ${c.pos || "center"}/cover}
.ov{position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,16,32,.25) 0%,rgba(6,16,32,.55) 30%,rgba(6,16,32,.78) 50%,rgba(6,16,32,.55) 70%,rgba(6,16,32,.35) 100%)}
.box{position:absolute;left:70px;right:70px;top:50%;transform:translateY(-50%);text-align:center;color:#fff}
.kick{display:inline-block;font-weight:700;font-size:40px;letter-spacing:.04em;background:#E83E30;padding:12px 30px;border-radius:10px}
h1{font-weight:800;font-size:${c.size || 150}px;line-height:1.14;letter-spacing:-.03em;margin:44px 0 40px;text-shadow:0 6px 30px rgba(0,0,0,.6)}
h1 .y{color:#FFD43B}
.sub{font-weight:700;font-size:52px;color:#E8EEF6;text-shadow:0 4px 18px rgba(0,0,0,.7)}
.badge{position:absolute;left:46px;top:46px;width:124px;height:124px;border-radius:50%;background:#0A2A55;border:5px solid #fff;color:#fff;text-align:center;font-weight:800;box-shadow:0 4px 18px rgba(0,0,0,.35)}
.badge i{position:absolute;inset:8px;border:3px dashed #E5392B;border-radius:50%}
.badge b{display:block;font-size:23px;margin-top:30px;line-height:1.1}
.badge u{display:block;font-size:31px;color:#FFD43B;text-decoration:none}
.logo{position:absolute;left:50%;transform:translateX(-50%);bottom:150px;width:330px}
</style></head><body><div class="bg"></div><div class="ov"></div>
${c.badge === false ? "" : '<div class="badge"><i></i><b>숨은 설비</b><u>도감</u></div>'}<div class="box"><div class="kick">${esc(c.kick)}</div><h1>${title}</h1><div class="sub">${esc(c.sub)}</div></div>${logo}</body></html>`;
fs.writeFileSync(path.join(dir, "cover.html"), html);

const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
await page.goto("file://" + path.join(dir, "cover.html"));
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(200);
await page.screenshot({ path: path.join(dir, "cover.png") });
await page.screenshot({ path: path.join(dir, "cover.jpg"), type: "jpeg", quality: 90 });
await browser.close();
console.log("cover.jpg");
