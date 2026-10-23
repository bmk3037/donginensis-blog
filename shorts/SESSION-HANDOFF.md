# 새 세션 이어받기 (2026-10-23 기준)

새 세션을 열면 이 파일부터 읽습니다. 일반 안내는 `HANDOFF.md`, 기획 규칙은 `daily/GUIDE.md`, 합성 도구는 `compose/README.md`.

## 1. 기본

- 저장소 `bmk3037/donginensis-blog`, 브랜치 **`claude/shorts-daily`** (push: `git push -u origin claude/shorts-daily`, PR 만들지 않음). **공개 저장소**라 남의 대본 원문·고객 이름은 올리지 않습니다.
- 사람(대표이사 백민기)이 하는 일: 주제 고르기, 타입캐스트 mp3, 구글 플로우 그림·클립(Veo 3.1 Lite, 클립 1개 약 10크레딧). 나머지(기획, 사실 확인, 대본, 프롬프트, 합성, 전달)는 Claude.
- 새 컨테이너에는 `shorts/compose/work/`(git 제외)와 `/home/user/final/`이 **없습니다.** 다시 합성하려면 그림 zip·클립·mp3를 다시 받아야 합니다. 31편의 장면·효과음·문장·시각 파일과 음성은 `shorts/compose/episodes/31/`에 올려 두었습니다.
- 합성 도구 처음 한 번: `bash shorts/compose/setup.sh`.

## 2. 꼭 지킬 규칙 (요약, 자세한 건 GUIDE.md)

- 법규·KEC 숫자는 원문 확인 전에는 안 씀. "모든·항상·반드시" 안 씀. 숫자마다 출처.
- 회사 이름은 설명란에만, 회사 사실은 `knowledge/company.md`만. "AI가 예측" 대신 "기록하고, 기준을 넘으면 먼저 알린다". 고객 이름·진행 중 프로젝트를 실적처럼 쓰지 않음.
- 설명란 끝: "※ 영상의 그림은 AI로 만든 이미지입니다."
- 사용자가 "다 됐다"고 하기 전엔 합성하지 않음. 답하는 도중 올린 첨부는 저장 안 될 수 있으니 다시 올려 달라고 함.
- **주제마다 그림 스타일을 먼저 물어봄**(건축 모형 도시 / 3D 설명 렌더 / 미니어처 디오라마 / 클레이 / 사실적인 시네마틱 3D).
- 프롬프트 전달: 1단계(A·단독 그림)와 2단계(B = A를 참고 이미지로 붙여 편집) 따로. 클립은 "NN편 cNN — 시작 그림: 파일" 블록 하나씩, 블록 안은 영어만, "Vertical 9:16" 쓰지 않음(설정에서), 끝에 "No on-screen text, no letters, no numbers, no logos, no camera cuts." 새 플로우 프로젝트, 출력 1, "10크레딧, 동영상 1개" 확인.
- 1단계 zip을 받으면 **번호표**(받은 파일 이름 ↔ 번호)와 순서 정리 zip을 줌. 플로우는 다시 만든 그림을 참고 그림 이름으로 저장하기도 하니 파일 내용을 비교해 확인.
- 사건형은 클립, 설명형(대중적이지 않은 것)은 클립 없이 합성 효과.
- 영상 시작은 움직이는 첫 장면 + 제목 한 줄(커버 카드 없음), 섬네일은 끝에 1초(`append_cover.sh`).

### 10/23에 새로 정한 것

- **첫 3초 규칙**: 첫 문장은 3초 안(20자 안팎), 주제가 아니라 보는 사람의 관심사(우리 집·내 돈·내 가족·내 몸)로 시작. 첫 장면은 이미 움직이는 클립, 0초 시작, 앞 무음 잘라 냄. 기획안마다 "첫 3초" 칸 + 다른 안 2개. (GUIDE 3장)
- **끝 저장 카드 빼기**("마지막에 저장해 두세요는 빼자, 이상해"). 3줄 요약은 설명란 📌에만.
- **자막 검은 테두리 기본**(밝은 화면에서 안 보였음): `#sub`에 800/50px + `-webkit-text-stroke: 10px rgba(0,0,0,.88); paint-order: stroke fill;`
- `make.sh video` 결과 경로는 절대 경로로.
- 타입캐스트 한 문장 다시 받기: 원래 음성에서 그 문장 구간을 잘라 새 mp3(앞뒤 무음 조금 남김)로 바꿔 끼운 뒤 `align`부터 다시(31편 19번 문장 예).
- 첫 문장 안 쉼이 길면 원본 음성에서 쉼을 0.3초 안팎으로 줄여 첫 문장을 3초 안에 맞춤(31편).

## 3. 편 상태

| 편 | 상태 | 남은 일 |
|---|---|---|
| 24 포스코 힌남노 | ✅ 클립판 완성 | - |
| 25 구글·카카오 데이터센터 | ✅ | - |
| 26 볼티모어 다리 | ✅ 클립 없이 | 사용자가 클립 만들면 v2 |
| 27 선박 주배전반 | ✅ 미니어처·클레이 | - |
| 28 청라 스프링클러 | 기획 완료(`daily/2026-10-22/28-…`) | 그림 15장·클립 6개·mp3 대기 |
| 29 자판기 동전 | ✅ | - |
| 30 컨테이너선(숨은 설계사전 그대로) | 기획 완료(`daily/2026-10-22/30-…`) | 그림 18장·클립 18개·mp3 대기 → 벤치마크식 합성 |
| 31 경량칸막이 | ✅ v5 완성: 첫 장면을 새 벽 그림 2장(`01a`→`01b`)으로, 저장 카드 뺌, 19번 문장 교체, c02 클립 | - (4장은 기록용) |
| **32 해저터널(지식컷 그대로)** | 기획 완료(`daily/2026-10-23/32-undersea-tunnel.md`). 대표이사 결정: 올릴 버전만(시험판 없음), 시네마틱 3D 단면, 제어반 이야기 없음 | 그림 24장 zip → 번호표 → 클립 24개 → mp3(1.0) → 합성(60fps, 로고·첫 제목 없이) |

## 4. (해결됨, v5) 31편 첫 장면 벽

대표이사: "첫 장면 0이 베란다 문이 저게 맞아?" → 01 그림(c01 클립)의 벽이 베란다 가운데 혼자 서 있는 좁은 판이라 실제 경량칸막이(옆집 베란다와 맞닿은 **베란다 끝 벽, 바닥부터 천장까지**)와 다릅니다. 06·19 그림(베란다 끝 벽)을 참고 이미지로 붙여 다시 만들고, 받으면 `episodes/31` 파일로 다시 합성합니다(01 그림은 13번 문장 c01 재사용 장면에도 쓰임).

01 다시 (06 그림을 참고 이미지로 붙여 새로 만들기):
```
01 | Close low-angle shot inside a narrow Korean apartment balcony, looking toward its far end: the end wall of the balcony is a plain white wall that runs from the floor to the ceiling and from the outer window to the inner wall, separating this balcony from the neighbor's balcony. A person's foot in a sneaker is in the middle of a hard kick, striking the lower middle of that end wall, which is already cracking with white gypsum dust bursting out and a sliver of daylight from the neighbor's balcony showing through the crack. Long sliding windows run along one side, a laundry rack and plant pots along the other. Photorealistic cinematic 3D render, a typical Korean apartment, documentary realism, natural soft light, shallow depth of field, muted colors with warm highlights. Recurring motif: the thin balcony partition wall to the neighbor is outlined by a faint red glow. People only seen from behind or as silhouettes, no faces. No text, no letters, no numbers, no logos. Vertical 9:16.
```

c01 다시 (시작 그림: 새 01, Veo 3.1 Fast 권장):
```
The foot completes the kick and breaks straight through the white end wall of the balcony within the first second, gypsum pieces and white dust flying toward the camera, bright daylight from the neighbor's balcony bursting through the jagged hole. Handheld documentary feel, slow motion after the impact. Keep the same photorealistic look, colors and lighting as the start frame. No on-screen text, no letters, no numbers, no logos, no camera cuts.
```

합성 메모: c01은 `clip/c01/`(fps30, 위 기준 0.9 자르기, 720×1280), 첫 장면은 0초부터 1배속, 13번 문장 뒤 절반은 40프레임부터 0.9배속. 클립 소리 앞 2.2초는 `c01_audio.wav`로 효과음에 섞음.

## 5. 다음 할 일: 32편 해저터널, 지식컷과 똑같이

대표이사(10/23): "진짜 딱 원하는 게 이거다 … 똑같이 벤치마킹해 보자", "똑같은 주제로 똑같이 만들어 볼래? 얼마나 똑같이 나오는지", "이미지만 변경해서?"

1. `benchmark-jisikcut.md`를 읽고, 그 안 "다시 받는 법"으로 릴스를 받아 받아쓰기·프레임을 만듭니다(받아쓴 원문은 저장소에 올리지 않음).
2. 대표이사 뜻은 "대본은 그대로, 이미지만 우리 것으로 바꿔 얼마나 똑같이 나오는지 보기". **시험용으로는 그렇게 하되, 남의 대본이라 그 버전은 올리지 않는다**고 먼저 말하고, 올릴 버전은 같은 구조로 대본을 새로 쓰자고 제안합니다(보령해저터널·거가대로 가덕해저터널 숫자는 원문 확인).
3. 장면표: 약 45컷(2초 안팎), 클립 약 23개 × 2컷. 스타일은 사실적인 시네마틱 3D 단면 + 가는 빨간 주석선 모티프(글자 없이), 한글 빨간 라벨은 합성에서.
4. 기획 파일 `daily/2026-10-23/32-undersea-tunnel.md`(첫 3초, 대본/타입캐스트 대본, 1단계 그림 프롬프트, 클립 블록, 설명란). 그림 zip → 번호표 → 클립 → mp3 → 합성(로고·첫 제목·큰 글자 없이 자막 + 빨간 주석, 60fps 시험) → 벤치마크와 나란히 비교 이미지.

## 6. 새 세션에 붙여 넣을 말

```
shorts/SESSION-HANDOFF.md를 읽고 이어서 해 줘. 브랜치는 claude/shorts-daily.
먼저 32편 해저터널(지식컷 그대로) 기획부터 시작하자.
```
