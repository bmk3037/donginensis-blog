# 32편 해저터널(지식컷식) 합성 파일

다시 합성할 때: 그림 48장(`img/NN.webp`, `NNb.webp`), 클립 c01·c06·c09, `narration.mp3`를 작업 폴더 `work/32/`에 다시 받아 넣고 아래 순서로 만듭니다.

1. 첫 문장 안 쉼 줄이기: 원래 mp3의 2.80~3.20초를 잘라 `narration_raw.mp3`.
2. `bash ../../make.sh align . 1.0 "$(cat force.json)"` (문장 경계 27곳을 쉼 위치로 고정)
3. `FIRST_T=1.3 EDGE=0.06 python3 -I emphasis32.py 1.22 12,20 12:0.12,20:0.25` → 약 92.2초(문장 사이 쉼 거의 없음, 첫 문장 3.4초)
4. 클립 프레임(60fps 보간): c01은 1.0초부터 4.2초, c06은 0~3.4초, c09는 0~2.6초를 `minterpolate=fps=60:mi_mode=mci`로 `clip/cNN/%03d.jpg`.
5. `bash make60.sh video . <절대경로>/32_v1_body.mp4` → `append_cover.sh`로 끝에 커버 1초.

화면: 로고·첫 제목 없음, 흰 자막만(노란 핵심어 없음), 빨간 글자+흰 테두리 라벨, 그려지는 눈금·괄호·과녁·화살표, 밝기·대비 올림, 장면 사이 겹침 0.05초.
