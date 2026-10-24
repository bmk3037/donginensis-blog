# 32편 캐릭터판(도감이) 합성 파일 — 클립 없이 (10/24 대표이사 "클립은 일단 없이")

그림 26장(`work/32c/img/NN.webp`, 번호표는 `daily/2026-10-24/32c-…md`), `narration_raw.mp3`(타입캐스트 1.0)를 `work/32c/`에 넣고:

1. `scene.html`, `sfx.py`, `lines.json`을 작업 폴더로 복사
2. `bash ../../make.sh align . 1.0` → `EDGE=0.06 python3 -I ../../emphasis.py 1.15` (문장 사이 쉼 거의 없이)
3. 끝 0.8초 무음 붙이고 `timeline.js` duration·마지막 b 늘리기(README 규칙)
4. `bash make60.sh video . <절대경로>/32c_body.mp4` → `FPS=60 RATE=1600k bash ../../append_cover.sh 32c_body.mp4 cover.jpg <결과>.mp4` (고화질판은 만들지 않음, 10/24)

클립 대신: 01·07은 빠르게 다가가기, 05는 흔들림, 07·11·18은 번쩍임, 문장이 긴 장면은 `cuts: 2`(같은 그림 안에서 한 번 당겨 찍기). 밝은 3D 애니메이션 그림이라 밝기 보정은 32편보다 약하게(1.04). 회사 문구 없음.
