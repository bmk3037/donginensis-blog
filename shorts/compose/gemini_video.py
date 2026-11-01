"""Gemini API로 영상(유튜브 주소 또는 로컬 mp4)을 초 단위로 분석한다(2026-11-01).
   키는 환경 변수 GEMINI_API_KEY(클라우드 환경 비밀값). 채팅·저장소에 적지 않는다.
   사용: python3 gemini_video.py <유튜브주소|파일.mp4> 결과.md [모델=gemini-pro-latest]"""
import base64, json, os, sys, time, urllib.request

PROMPT = """이 쇼츠 영상을 처음부터 끝까지 초 단위로 분석해서 아래 형식의 표와 목록으로만 한국어로 답해 줘. 추측은 "추정"이라고 표시해.
1. 기본: 전체 길이(초), 채널 이름(보이면), 영상 제목(보이면).
2. 첫 5초(0~5초)를 0.5초 단위로: [시각 | 화면에 보이는 것(구도·카메라 움직임) | 화면 글자(내용·위치: 위/가운데/아래·크기) | 내레이션 말].
3. 컷 목록(화면이 확 바뀌는 순간 전부): [번호 | 시각(초, 소수점 1자리) | 컷 전 장면 → 컷 후 장면 | 장면 종류: 하늘 부감/단면 그래픽/실내/근접/지도/기타].
4. 큰 글자·그래픽이 뜨는 순간 전부: [시각 | 글자 내용 | 위치 | 색 | 떠 있던 시간(초)].
5. 자막: 위치(위/가운데/아래), 한 번에 몇 어절, 색·테두리.
6. 내레이션 전문을 문장마다 [시작 시각 | 문장]으로.
7. 수수께끼 구조: 처음 던진 질문(시각·문장), 그 답이 나온 순간(시각·문장), 중간의 작은 질문들(시각·문장).
8. 첫 문장의 형식을 한 줄로(예: "여기 [익숙한 장소]에는 [상식과 모순되는 사실]이 있습니다.").
9. 끝 5초: 마지막 문장, 화면, 구독·공유 유도 문구가 있는지.
10. 숫자: 영상에 나온 숫자와 단위를 시각과 함께 전부.
11. 화면 그림체(실사/AI 3D/미니어처 등)와 카메라 움직임의 특징을 3줄로."""

def main():
    src, out = sys.argv[1], sys.argv[2]
    model = sys.argv[3] if len(sys.argv) > 3 else "gemini-pro-latest"
    key = os.environ["GEMINI_API_KEY"]
    if src.startswith("http"):
        part = {"file_data": {"file_uri": src}}
    else:
        part = {"inline_data": {"mime_type": "video/mp4", "data": base64.b64encode(open(src, "rb").read()).decode()}}
    body = {"contents": [{"parts": [part, {"text": PROMPT}]}],
            "generationConfig": {"temperature": 0.2, "mediaResolution": "MEDIA_RESOLUTION_HIGH"}}
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"x-goog-api-key": key, "Content-Type": "application/json"})
            d = json.load(urllib.request.urlopen(req, timeout=600)); break
        except urllib.error.HTTPError as e:
            msg = e.read().decode()[:500]; print("HTTP", e.code, msg)
            if e.code in (429, 500, 503) and attempt < 2: time.sleep(20); continue
            sys.exit(1)
    text = "".join(p.get("text", "") for p in d["candidates"][0]["content"]["parts"])
    open(out, "w", encoding="utf-8").write(f"<!-- Gemini {model} 분석: {src} -->\n\n" + text)
    print(out, len(text), "자")

if __name__ == "__main__":
    main()
