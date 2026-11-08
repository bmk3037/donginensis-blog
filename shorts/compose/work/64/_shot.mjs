import { createRequire } from "module"; import { pathToFileURL } from "url";
const pw = createRequire("C:/Users/bmk30/donginensis-blog/shorts/compose/")("playwright");
const b = await pw.chromium.launch({ executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe", args: ["--allow-file-access-from-files"] });
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
const errs = []; p.on("pageerror", e => errs.push(e.message));
await p.goto(pathToFileURL("scene_2tan.html").href); await p.evaluate(() => window.READY);
for (const t of process.argv.slice(2)) { await p.evaluate(t => window.setTime(+t), t); await p.waitForTimeout(150); await p.screenshot({ path: `_shot_${t}.jpg`, type: "jpeg", quality: 80 }); }
console.log("errors:", errs.length ? errs.join(" | ") : "none"); await b.close();
