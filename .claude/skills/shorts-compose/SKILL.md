---
name: shorts-compose
description: 타입캐스트 음성과 구글 플로우 이미지로 숏츠 영상을 합성한다(인포그래픽, 자막, 효과음, 배속). "합성해 줘", "영상 만들어 줘", mp3·zip·드라이브 링크를 받았을 때 쓴다.
---

# 숏츠 합성

`shorts/compose/README.md`를 읽고 그 순서와 화면 규칙대로 한다. 실제 예시는 `shorts/compose/template/`(21편 기준 틀)이다.

1. 처음이면 `bash shorts/compose/setup.sh`.
2. 그 편의 대본 파일(`shorts/daily/날짜/NN-slug.md` 또는 `shorts/scripts/`)에서 타입캐스트 대본·장면 배치표를 읽는다. 타입캐스트 대본의 문장으로 `lines.json`을 만든다(비트 번호 포함, 숫자는 자막용 아라비아 숫자 표기).
3. 음성은 `narration_raw.mp3`로, 이미지 zip은 `prep_images.py`로 준비한다. `all.png`를 보고 플로우 번호와 실제 이미지를 맞춘다. 빠진 이미지는 사용자에게 알린다.
4. `make.sh align`으로 시각을 잡는다. 결과가 94~100초가 되게 배속을 고르고, 어긋난 경계는 강제 경계로 고친다.
5. `template/scene.html`, `template/sfx.py`(시리즈 로고 "숨은 설비 도감" 포함)를 복사해 SCENES·KEYS·NAMES와 효과음 큐를 이 편에 맞게 다시 쓴다. 장면 배치표의 인포그래픽은 함수로 직접 그린다.
6. `make.sh stills`로 6~10장을 뽑아 한 장으로 붙여 사용자에게 먼저 보여 준다. 겹침과 잘림을 고친다.
7. 커버를 먼저 만든다: 대본 파일의 커버 문구로 작업 폴더에 `cover.json`을 쓰고 `make.sh cover`로 `cover.jpg`·`cover.png`(1080×1920)를 만든다. 공개 편은 `logo`를 비운다(회사 이름·로고 없음). 커버 문구가 없으면 훅으로 직접 짓는다. `cover.png`가 있으면 영상의 첫 1초가 커버 화면이 된다(첫 프레임 = 섬네일).
8. `make.sh video`로 최종 영상을 뽑고(20MB 안쪽) 사용자에게 파일로 보낸다. 고친 판은 `_v2`, `_v3`으로 이름을 올린다.
9. 영상과 `cover.jpg`를 함께 사용자에게 보낸다.

지킬 화면 규칙:
- 장면 안에서 다시 자르지 않는다.
- 순간 확대와 흐림을 쓰지 않는다.
- 흔들림은 가장 센 순간 한 곳에 0.5초만 쓴다.
- 3~4초마다 새 그림을 넣는다.
- 핵심어는 노란 자막으로 쓴다.
- 그래픽은 화면 위쪽에 둔다.

답하는 도중에 올라온 첨부는 저장되지 않으니, 답이 끝난 뒤 다시 올려 달라고 한다.

**10/30부터 합성(대표이사 "단조롭고 같은 화면 반복, 끊김", 최우선):** 클립 프레임은 `minterpolate` 보간 없이 **원본 24fps 그대로** 뽑아(`ffmpeg -i cNN.mp4 -vf scale=720:1280 -q:v 3 clipn/cNN/%03d.jpg`) `scene.html`의 `CFPS = 24`, 경로 `clipn/`로 쓰고 **24fps로 렌더**(`node ../../render.mjs video out.mp4 24`). **2초마다 확대해 자르는 자동 컷(cuts)은 쓰지 않는다.** 샷 사이 컷은 a·b 클립으로. 클립 환경음은 `ambient.wav`로 장면 위치에 맞춰 깔고(`shorts/compose/mixv2.sh`) 목소리 밑으로 −24dB쯤 둔다. 예: `work/jetfan`(48편 v2).
