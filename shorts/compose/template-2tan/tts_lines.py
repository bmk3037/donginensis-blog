"""이탄생 그림판 음성: 문장마다 타입캐스트로 따로 만들고(경계가 정확), 0.3초 쉼으로 이어 붙인 뒤 문장 시각을 고정해 정렬한다.
   작업 폴더(work/NN)에서:  TYPECAST_API_KEY=... python3 ../../template-2tan/tts_lines.py say.txt [piljae|moonjung] [배속=1.06]
   say.txt = 읽을 문장(숫자는 한글로), 한 줄 한 문장. disp.txt가 있으면 자막용(숫자는 아라비아), 없으면 say에서 자동 바꿈.
   결과: lines/NN.mp3·wav, narration_raw.mp3, lines.json, timeline_raw.js, timeline.js, narration.wav
   키는 환경 변수에서만 읽는다(저장소·채팅에 적지 않음)."""
import json, os, re, subprocess, sys, urllib.request
VOICES = {"piljae": ("tc_68257f68bc6e3c161ab5078d", "ssfm-v30"), "moonjung": ("tc_68f9c6a72f0f04a417bb136f", "ssfm-v31")}
src = sys.argv[1]; voice = sys.argv[2] if len(sys.argv) > 2 else "piljae"; rate = sys.argv[3] if len(sys.argv) > 3 else "1.06"
VID, MODEL = VOICES[voice]; key = os.environ.get("TYPECAST_API_KEY") or sys.exit("TYPECAST_API_KEY 없음")
T = os.path.dirname(os.path.abspath(__file__)); GAP = 0.15  # 11/5 이탄생 비교: 말 빠르기 6.5~7.4자/초, 59편 5.9 → 쉼 줄임
say = [l.strip() for l in open(src, encoding="utf-8") if l.strip()]
os.makedirs("lines", exist_ok=True)
for i, t in enumerate(say, 1):
    out = f"lines/{i:02d}.mp3"
    if os.path.exists(out): continue          # 문장을 고치면 그 번호 mp3만 지우고 다시 돌린다
    body = {"voice_id": VID, "text": t, "model": MODEL, "language": "kor", "prompt": {"emotion_preset": "normal", "emotion_intensity": 1.0},
            "output": {"volume": 100, "audio_pitch": 0, "audio_tempo": 1.0, "audio_format": "mp3"}}
    req = urllib.request.Request("https://api.typecast.ai/v1/text-to-speech", data=json.dumps(body).encode(), method="POST",
                                 headers={"X-API-KEY": key, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r, open(out, "wb") as f: f.write(r.read())
    print(i, t[:30])
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono", "-t", str(GAP), "gap.wav"], check=True)
starts, t, lst = [], 0.0, open("list.txt", "w")
for i in range(1, len(say) + 1):
    w = f"lines/{i:02d}.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"lines/{i:02d}.mp3", "-af",
                    "silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,apad=pad_dur=0.05",
                    "-ar", "44100", "-ac", "1", w], check=True)
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", w], capture_output=True, text=True).stdout)
    starts.append(t); t += d; lst.write(f"file '{os.path.abspath(w)}'\n")
    if i < len(say): lst.write(f"file '{os.path.abspath('gap.wav')}'\n"); t += GAP
lst.close()
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", "list.txt", "-ar", "44100", "-ac", "1", "-b:a", "192k", "narration_raw.mp3"], check=True)
if os.path.exists("disp.txt"): disp = [l.strip() for l in open("disp.txt", encoding="utf-8") if l.strip()]
else: disp = [s.rstrip(".?") for s in say]
json.dump([{"beat": 1, "text": d, "say": s} for d, s in zip(disp, say)], open("lines.json", "w"), ensure_ascii=False, indent=0)
force = {str(k): round(starts[k + 1] - GAP + 0.01, 3) for k in range(len(say) - 1)}
if not os.path.exists("fonts"): os.symlink(os.path.join(T, "..", "fonts"), "fonts")
subprocess.run(["bash", os.path.join(T, "make60.sh"), "align", ".", "1.0", json.dumps(force)], check=True, capture_output=True)
subprocess.run(["python3", os.path.join(T, "..", "emphasis.py"), rate, "99"], check=True)
print("원본", round(t, 2), "초 → 배속", rate)
