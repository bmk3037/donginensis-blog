// 작업 폴더의 scene.html을 프레임마다 캡처해 ffmpeg로 묶는다. 작업 폴더 안에서 실행한다.
//   node ../../shorts/compose/render.mjs stills 2,12,20     정지 화면만(still_NN.png)
//   node ../../shorts/compose/render.mjs video out.mp4 30   전체 영상(소리 없음)
import { createRequire } from "module";
import { spawn } from "child_process";
import path from "path";

// playwright는 이 폴더의 node_modules(setup.sh가 설치)에서 찾고, 없으면 PLAYWRIGHT_DIR에서 찾는다
const here = path.dirname(new URL(import.meta.url).pathname);
let chromium;
try { ({ chromium } = createRequire(here + "/")("playwright")); }
catch { ({ chromium } = createRequire((process.env.PLAYWRIGHT_DIR || "/opt/node-tools/node_modules") + "/")("playwright")); }

const dir = process.cwd();
const [mode, arg, fpsArg] = process.argv.slice(2);
const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
await page.goto("file://" + dir + "/" + (process.env.SCENE || "scene.html"));
await page.evaluate(() => document.fonts.ready);
await page.evaluate(() => window.READY);
if (mode === "stills") {
  for (const t of arg.split(",").map(Number)) {
    await page.evaluate(t => window.setTime(t), t);
    await page.screenshot({ path: `${dir}/still_${t.toFixed(2).padStart(6, "0")}.png` });
  }
} else {
  const fps = Number(fpsArg || 30);
  const dur = await page.evaluate(() => window.TL.duration);
  const n = Math.ceil(dur * fps);
  const ff = spawn("ffmpeg", ["-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", String(fps), "-i", "-",
    "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", arg], { stdio: ["pipe", "inherit", "inherit"] });
  for (let i = 0; i < n; i++) {
    await page.evaluate(t => window.setTime(t), i / fps);
    const buf = await page.screenshot({ type: "jpeg", quality: 92 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once("drain", r));
    if (i % 300 === 0) console.log(`${i}/${n}`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on("close", r));
}
await browser.close();
