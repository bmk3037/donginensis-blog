// scene_v2.html의 SCENES에서 클립 장면만 뽑아 JSON으로 출력(환경음 위치 계산용). 작업 폴더에서: node ../../dump_scenes.mjs > scenes.json
import { createRequire } from "module";
import path from "path";
const here = path.dirname(new URL(import.meta.url).pathname);
let chromium;
try { ({ chromium } = createRequire(here + "/")("playwright")); }
catch { ({ chromium } = createRequire((process.env.PLAYWRIGHT_DIR || "/opt/node-tools/node_modules") + "/")("playwright")); }
const dir = process.cwd();
const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
await page.goto("file://" + dir + "/" + (process.env.SCENE || "scene_v2.html"), { waitUntil: "domcontentloaded", timeout: 0 });
const out = await page.evaluate(() => ({
  duration: window.TL.duration,
  scenes: SCENES.filter(s => s[3].clip).map(s => ({ id: s[3].clip.id, a: s[1], b: s[2], from: s[3].clip.from, rate: s[3].clip.rate || 1, t0: s[3].clip.t0 ?? s[1] }))
}));
console.log(JSON.stringify(out));
await browser.close();
