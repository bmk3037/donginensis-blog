"""타입캐스트 API로 나레이션 mp3를 만든다(2026-11-01, 대표이사 유료 결제).
   키는 환경 변수 TYPECAST_API_KEY에서 읽는다(저장소·채팅에 적지 않는다).
   사용:
     python3 tts_typecast.py 대본.txt 결과.mp3            # 한 줄 = 한 문장, 줄마다 만들어 이어 붙임
     python3 tts_typecast.py 대본.txt 결과.mp3 --only 4    # 4번 줄만 다시(결과: 결과_04.mp3)
   목소리: 문정(Moonjung) tc_68f9c6a72f0f04a417bb136f, 모델 ssfm-v30(문정은 v30에만 있음), 속도 1.0, 감정 normal."""
import json, os, subprocess, sys, tempfile, urllib.request

VOICE, MODEL = "tc_68f9c6a72f0f04a417bb136f", "ssfm-v30"
URL = "https://api.typecast.ai/v1/text-to-speech"
GAP = 0.35  # 문장 사이 무음(초). 합성에서 emphasis.py가 다시 다듬는다


def speak(text, out, key):
    body = {"voice_id": VOICE, "text": text, "model": MODEL, "language": "kor",
            "prompt": {"emotion_preset": "normal", "emotion_intensity": 1.0},
            "output": {"volume": 100, "audio_pitch": 0, "audio_tempo": 1.0, "audio_format": "mp3"}}
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), method="POST",
                                 headers={"X-API-KEY": key, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r, open(out, "wb") as f:
        f.write(r.read())


def main():
    key = os.environ.get("TYPECAST_API_KEY")
    if not key:
        sys.exit("TYPECAST_API_KEY 환경 변수가 없습니다(클라우드 환경 설정의 Network secrets에 넣기).")
    src, out = sys.argv[1], sys.argv[2]
    only = int(sys.argv[sys.argv.index("--only") + 1]) if "--only" in sys.argv else None
    lines = [l.strip() for l in open(src, encoding="utf-8") if l.strip()]
    if only:
        dst = out.replace(".mp3", f"_{only:02d}.mp3")
        speak(lines[only - 1], dst, key); print(dst); return
    tmp = tempfile.mkdtemp()
    parts = []
    for i, l in enumerate(lines, 1):
        p = os.path.join(tmp, f"{i:02d}.mp3"); speak(l, p, key); parts.append(p); print(i, l[:30])
    sil = os.path.join(tmp, "sil.mp3")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"anullsrc=r=44100:cl=mono", "-t", str(GAP), "-q:a", "2", sil], check=True)
    lst = os.path.join(tmp, "list.txt")
    with open(lst, "w") as f:
        for i, p in enumerate(parts):
            f.write(f"file '{p}'\n")
            if i < len(parts) - 1: f.write(f"file '{sil}'\n")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-ar", "44100", "-ac", "1", "-b:a", "192k", out], check=True)
    print(out)


if __name__ == "__main__":
    main()
