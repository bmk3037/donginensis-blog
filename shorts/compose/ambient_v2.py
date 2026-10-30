"""장면별 클립 환경음을 장면 위치에 맞춰 한 트랙(ambient.wav)으로. 작업 폴더에서: python3 ../../ambient_v2.py scenes.json 클립폴더
   클립 소리는 평균 −24dB 근처로 맞추되(+12/−6dB 안), 목소리가 나오면 mixv2.sh가 줄인다."""
import json, re, subprocess, sys, os
sc = json.load(open(sys.argv[1])); clipdir = sys.argv[2]; dur = sc["duration"]
specs = []
for s in sc["scenes"]:
    c0 = max(0.0, (s["from"] - 1) / 24.0); d = s["b"] - s["a"]; rate = s["rate"]
    if rate < 0:                                  # 거꾸로 재생한 장면: 소리는 앞으로 재생(환경음이라 무방)
        c0 = max(0.0, c0 - d); rate = abs(rate)
    specs.append((s["id"], s["a"], d, c0, rate))
def has_audio(p):
    return bool(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=codec_type", "-of", "csv=p=0", p], capture_output=True, text=True).stdout.strip())
specs = [x for x in specs if has_audio(f"{clipdir}/{x[0]}.mp4")]
if not specs:   # 클립에 소리가 없는 옛 편(프롬프트 "Audio: none"): 무음 트랙
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-t", str(dur), "-i", "anullsrc=r=44100:cl=stereo", "ambient.wav"], check=True)
    print("ambient: 클립에 소리 없음 → 무음"); sys.exit(0)
def tempo_chain(r):
    if abs(r - 1) < 1e-3: return ""
    out = []
    while r > 2.0: out.append("atempo=2.0"); r /= 2.0
    while r < 0.5: out.append("atempo=0.5"); r /= 0.5
    out.append(f"atempo={r:.3f}")
    return "," + ",".join(out)
cmd = ["ffmpeg", "-y", "-loglevel", "error"]; filt = []
for k, (c, a, d, c0, rate) in enumerate(specs):
    src = d * rate; path = f"{clipdir}/{c}.mp4"
    r = subprocess.run(["ffmpeg", "-ss", str(c0), "-t", str(src), "-i", path, "-vn", "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True).stderr
    m = re.search(r"mean_volume: (-?[\d.]+) dB", r); mv = float(m.group(1)) if m else -60
    gain = max(-6, min(12, -24 - mv))
    af = f"atrim=0:{src:.3f},asetpts=PTS-STARTPTS" + tempo_chain(rate) + f",volume={gain:.1f}dB,afade=t=in:d=0.12,afade=t=out:st={max(0, d - 0.18):.2f}:d=0.18,adelay={int(a * 1000)}:all=1"
    cmd += ["-ss", str(c0), "-t", f"{src + 0.05:.3f}", "-i", path]
    filt.append(f"[{k}:a]aformat=sample_rates=44100:channel_layouts=stereo,{af}[a{k}]")
cmd += ["-filter_complex", ";".join(filt) + ";" + "".join(f"[a{k}]" for k in range(len(specs))) + f"amix=inputs={len(specs)}:duration=longest:normalize=0,atrim=0:{dur}[o]", "-map", "[o]", "-ar", "44100", "ambient.wav"]
subprocess.run(cmd, check=True); print("ambient ok", len(specs), "clips")
