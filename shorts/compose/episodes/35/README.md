# 35편 아파트 쓰레기 관로 합성 파일

- 그림 14장(`work/35/img/NN.webp`), 타입캐스트 mp3, 클립 2개(c01 = 01 그림 시작, c10 = 10 그림 시작, Veo 3.1 Lite 10초 24fps).
- 음성: `make.sh align . 1.0 "$(cat force.json)"` → `FIRST_T=1.25 EDGE=0.06 python3 -I ../../episodes/32/emphasis32.py 1.1` → 끝 0.8초 무음 → 54.7초.
- 클립 프레임(60fps 보간): c01은 1.2초부터 5.0초(첫 문장 3초에 맞춰 1.6배속), c10은 1.0초부터 3.6초를 `minterpolate=fps=60:mi_mode=mci`로 `clip/cNN/%03d.jpg`.
- `bash make60.sh video . <절대경로>/35_body.mp4` → `FPS=60 RATE=1600k bash ../../append_cover.sh …`
