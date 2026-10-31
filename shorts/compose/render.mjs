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
page.setDefaultTimeout(0);   // 클립 프레임 수천 장을 읽는 동안 여러 렌더가 겹치면 30초를 넘김
await page.goto("file://" + dir + "/" + (process.env.SCENE || "scene.html"), { waitUntil: "domcontentloaded", timeout: 0 });
await page.evaluate(() => document.fonts.ready);
await page.evaluate(() => window.READY);
if (mode === "stills") {
  for (const t of arg.split(",").map(Number)) {
    if (await page.evaluate(() => typeof window.prepare === "function")) await page.evaluate(t => window.prepare(t - 0.2, t + 0.2), t);
    await page.evaluate(t => window.setTime(t), t);
    await page.screenshot({ path: `${dir}/still_${t.toFixed(2).padStart(6, "0")}.png` });
  }
} else {
  const fps = Number(fpsArg || 30);
  const dur = await page.evaluate(() => window.TL.duration);
  const n = Math.ceil(dur * fps);
  // 10/31: 컨테이너가 쉬는 사이 꺼져도 이어서 하도록 10초(CHUNK 프레임)씩 조각 파일로 만들고, 있는 조각은 건너뛴 뒤 이어 붙인다
  const CH = Number(process.env.CHUNK || fps * 10), fs = await import("fs");
  const cdir = dir + "/chunks_" + path.basename(arg, ".mp4"); fs.mkdirSync(cdir, { recursive: true });
  const parts = [];
  for (let c0 = 0, k = 0; c0 < n; c0 += CH, k++) {
    const part = `${cdir}/part_${String(k).padStart(3, "0")}.mp4`; parts.push(part);
    if (fs.existsSync(part)) { console.log(`skip ${k}`); continue; }
    if (await page.evaluate(() => typeof window.prepare === "function")) await page.evaluate(([a, b]) => window.prepare(a, b), [c0 / fps, Math.min(n, c0 + CH) / fps]);
    const tmp = part + ".tmp.mp4";
    const ff = spawn("ffmpeg", ["-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", String(fps), "-i", "-",
      "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", tmp], { stdio: ["pipe", "inherit", "inherit"] });
    for (let i = c0; i < Math.min(n, c0 + CH); i++) {
      await page.evaluate(t => window.setTime(t), i / fps);
      const buf = await page.screenshot({ type: "jpeg", quality: 92 });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once("drain", r));
    }
    ff.stdin.end();
    await new Promise(r => ff.on("close", r));
    fs.renameSync(tmp, part); console.log(`${Math.min(n, c0 + CH)}/${n}`);
  }
  fs.writeFileSync(cdir + "/list.txt", parts.map(p => `file '${p}'`).join("\n") + "\n");
  await new Promise(r => spawn("ffmpeg", ["-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", cdir + "/list.txt", "-c", "copy", arg], { stdio: "inherit" }).on("close", r));
}
await browser.close();
