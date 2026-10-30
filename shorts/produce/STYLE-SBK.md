# 건축사전풍 그림·클립 프롬프트 틀 (2026-10-28 대표이사 "신비한 건축사전이랑 영상은 똑같이 만들고 싶어")

**따라 하는 것은 화면 결(그림체·카메라·글자 얹는 법)뿐이다.** 그 채널의 주제·대본·제목은 따라 하지 않는다(따라 한 채널은 원본의 1~2%, `benchmark-competitors-2026-10.md`). 회사 이름·건축사전 이름은 프롬프트에도 넣지 않는다.

## ★ 10/30 샷 늘리기·움직임 다양화·환경음 (대표이사 "다른 채널에 비해 단조롭고 같은 화면이 반복되고 끊긴다", "샷을 늘리자", 다음 화부터 전부 적용, 이 절이 아래보다 우선)

48편(jetfan) 영상을 재 보니: 62초에 클립 14개(샷 14개), 클립마다 "slow push-in" 한 가지 움직임, 2초마다 같은 영상을 확대해 자르는 가짜 컷(같은 화면 반복), 24fps 클립을 60fps로 보간해 일렁임, 클립에 든 환경음은 버림.

| 항목 | 이전 | 10/30부터 |
|---|---|---|
| 샷 수 | 문장 1~2개당 클립 1개(1분에 12~14샷) | **문장마다 서로 다른 시작 그림 2장(A·B)**, 클립은 각각 **앞 3~4초만** 씀 → 1분에 **24~30샷** |
| 샷 A·B 짜기 | - | A = 넓은 장면(어디서), B = 다른 각도·다른 대상(클로즈업·부품·사람 손·반대편). **같은 구도의 확대판은 B가 아니다** |
| 카메라 | 거의 전부 slow push-in/orbit | 클립마다 **다른 움직임**: 빠른 푸시, 추적(tracking), 궤도, 위로 솟기(crane), 초점 이동(rack focus), 낮은 앵글 지나가기, 손으로 든 듯한 흔들림. **한 편에 같은 움직임 3번 이상 금지**(종류는 섞되 **진행 방향은 이어 맞춤**, 아래 "앞뒤 클립"), 기본은 앞으로 나아가는 카메라, "slow"는 한 편에 3번 안쪽 |
| 움직임 | 핵심 부분이 천천히 | **첫 1.5초 안에 동작 시작, 1.5초마다 새 일이 일어남**(물체가 움직이고, 손이 누르고, 연기·물·빛이 흐름) |
| 클립 안 컷 | "no cuts" | 한 샷은 컷 없이 이어서(샷 하나 = 한 테이크). 샷 사이 컷은 편집에서 |
| 소리 | "Audio: none", 효과음만 | **환경음을 살림**(기계 소리, 바람, 발소리). 프롬프트에 "Audio: natural ambient sound only, no music, no speech" |
| 확대 효과 | 클립에도 1.04→1.1 확대를 겹쳐 줌 | **클립 위 확대는 1.0→1.03 정도로 아주 약하게**(클립 자체의 카메라 움직임에 맡김) |
| 화질 | 20MB 안쪽(휴대폰으로 받기 편하라고 둔 제한, 1600k) | **업로드용은 제한 없음**: CRF 18, 최대 8Mbps(60초에 약 40~60MB, GitHub 100MB 안쪽). 클립 원본은 720×1280이라 비트레이트를 올려도 해상도는 그대로(업스케일은 따로 검토) |
| 앞뒤 클립 | 방향 무관 | **카메라·대상의 진행 방향을 앞뒤 클립끼리 맞춤**: 앞으로 가는 샷 뒤엔 앞으로 가는 샷, 왼쪽→오른쪽 뒤엔 왼쪽→오른쪽. 반대로 꺾는 컷은 일부러 놀랄 때만. 카드 장면 표에 "움직임 방향" 칸을 둠 |
| 합성 | 60fps 보간, 2초마다 확대 컷 | **원본 24fps 그대로, 24fps로 렌더, 확대 컷 없음**, 클립 환경음을 −24dB쯤 목소리 밑에 깔기(`compose/mixv2.sh`) |

**새 클립 공통 끝말 (이전 "Camera: one slow smooth move…" 대신, 10/30부터):**
```
One continuous shot, no cuts, no on-screen text. The subject moves clearly from the very first frame and something new happens about every 1.5 seconds. Same vivid explainer look, colors and light as the start frame. Audio: natural ambient sound of the scene only (machine hum, air, footsteps), no music, no speech. Absolutely no digits, numbers, letters, labels, percent signs, measurement lines, arrows or symbols ever appear; no logos.
```
클립 앞부분에 **카메라 움직임을 한 줄로 따로 적는다**: 예 `Camera: fast push-in.` / `Camera: low tracking shot sliding past.` / `Camera: crane up.` / `Camera: rack focus from the foreground part to the background.` / `Camera: handheld, slight natural shake.`

**★ 한 클립 3샷이 기본(10/30 시험 합격, 대표이사 "8초여도 다르네, 앞으로 이렇게 하자"):** 시험 클립 t1~t3(`shorts/media/test-multishot/`)에서 세 클립 모두 하드 컷이 2번 생겨 **8초 클립 하나가 서로 다른 각도의 샷 3개**가 됐다(크레딧 그대로). 시험에서 드러난 점:
- Veo는 컷을 정한 시각이 아니라 **대략 3등분(약 2.4초, 4.75초)** 에 넣는다 → 프롬프트도 `Shot 1 (0-2.6s) / Shot 2 (2.6-5.3s) / Shot 3 (5.3-8s)`로 쓴다. 합성에서 샷마다 따로 잘라 쓰므로 **나쁜 샷은 통째로 버릴 수 있다.**
- 샷마다 장면을 다시 해석해 **설비 모양·바닥색·건물이 바뀐다**(t1 원통 팬 → 네모 틀 팬 → 연기 뿜는 작은 팬, t3 단면 그림 → 실사). 그래서 **샷마다 다른 문장에 쓰고, 한 샷을 다른 샷과 이어 붙여 "같은 물건"처럼 보이게 하지 않는다.** 프롬프트에는 "same object, same shape and colors in every shot"을 넣는다.
- 복잡한 장면에서 **글자·숫자·표지가 더 자주 생긴다**(t3 기둥 "52", t2 바닥 흰 화살표·차 로고). 프롬프트에 `No signs, no markings, no numbers or letters on walls, pillars, floors or vehicles; no brand logos.`를 넣고, 합성에서 문제 샷은 뺀다.
- 소리는 그대로 나온다(환경음 −11~−39dB, 조용한 장면은 작음).
**프롬프트 틀:**
```
Three shots with hard cuts, one continuous scene in <장소>. Shot 1 (0-2.6s): <넓은 장면, 카메라 움직임>. HARD CUT. Shot 2 (2.6-5.3s): <부품 클로즈업, 움직임>. HARD CUT. Shot 3 (5.3-8s): <다른 각도·추적·크레인>. In every shot the <물건> keeps the same shape and colors. No signs, no markings, no numbers or letters on walls, pillars, floors or vehicles; no brand logos. <클립 공통 끝말>
```
이 방식이면 클립 12개로 샷 36개 → 1분 24~30샷을 크레딧 그대로 넘긴다. 문장마다 그림 2장(A·B)으로 가던 위 안은 **쓰지 않는다**(크레딧 2배). 시작 그림 1장 = 클립 1개 = 샷 3개.

**크레딧:** 클립 12~14개(편당 120~140)로 변함 없음. 한 Flow 계정으로 모자라면 둘로 나눠 만듦.

## 그 채널 화면에서 본 것 (상위 쇼츠 8편 첫 화면, 10/28)

| 특징 | 내용 | 우리 지금(42~44편) |
|---|---|---|
| 빛 | **밝은 낮, 흐린 하늘의 부드러운 빛**, 하늘·벽이 비어 있음 | 어두운 밤, 영화풍 조명 |
| 그림체 | 건축 설명용 3D(밝은 회색 콘크리트, 흰 면, 깨끗한 재질) + 실사 재질 | 실사 영화풍 |
| 구도 | **물건 하나를 화면 가운데에 크게**, 배경은 단순하거나 흐림 | 장면 전체(풍경) |
| 보여 주는 법 | **단면**(바닥판·벽·땅을 잘라 속을 보임), 투명·엑스레이, 아주 가까운 접사 | 겉모습 |
| 강조 | **가는 빨간 치수선**(양끝 화살표, 눈금), 핵심 부분만 **하늘색·빨간 빛** | 없음 |
| 큰 숫자 | 하늘 빈자리에 **진한 회색 큰 숫자**(테두리 없음), 핵심어는 빨간 글자 | 흰·노란 굵은 글자 + 검은 테두리 |
| 자막 | 화면 가운데 아래, **작은 흰 글자 + 옅은 그림자**, 두세 단어씩 | 같음 |
| 캐릭터 | 없음 | 도감이(섬네일·끝 두 장면) → **45편부터 뺌** |
| 구글 플로우 표시 | 오른쪽 아래 ✦ 그대로 | 같음 |

## 그림(Nano Banana) 끝에 붙이는 말 — 모든 그림 공통 (10/28 46편 비교 뒤 고침)

```
Clean engineering explainer 3D render, architectural visualization style: the camera is close to the subject and the hero object fills most of the frame, vivid saturated colors with strong warm-cool contrast (warm sunlit or glowing orange areas against cool blue or cyan), realistic textures, soft natural daylight, simple background, the key part highlighted only by a soft glow, no dimension lines, no measurement marks, no arrows. High detail, real-world scale. Absolutely no digits, numbers, letters, labels, percent signs, arrows or symbols anywhere; no logos; screens and labels are blank. No people's faces. Vertical 9:16.
```

## 장면 다섯 가지 (한 편 10장면을 이 중에서 섞는다)

| 이름 | 쓰는 때 | 그림 앞부분 예 (영어로, 물건만 바꿈) |
|---|---|---|
| A 거대한 물건 | 0초 훅, 숫자 장면 | `In a familiar Korean place (…), the hero object (…) shown enormous and isolated, towering over people-sized surroundings,` |
| B 단면 | 원리 설명 | `A clean cutaway cross-section through (… a wall / a floor slab / the ground / a door lock), revealing (…) inside,` |
| C 접사 | 부품 하나 | `Extreme close-up macro of (… one part), every texture visible, background softly blurred,` |
| D 엑스레이 | 건물·설비 전체에서 핵심만 | `A semi-transparent glass-like (… building / machine) with only (… the key part) glowing bright cyan inside,` |
| E 흐름 | 물·공기·전기·열이 움직임 | `Inside a cutaway of (…), (… cold air / water / electric current / heat) flowing visibly as a soft glowing stream from (…) to (…),` |

## 클립(Veo) 프롬프트 끝에 붙이는 말 (10/28 고침)

```
Camera: one slow smooth move as described, no cuts. The key part moves clearly from the very first frame. Same vivid explainer look, colors and light as the start frame. Audio: none. Absolutely no digits, numbers, letters, labels, percent signs, measurement lines, arrows or symbols ever appear; no logos.
```

## 10/29 빨간 치수선은 AI 프롬프트에서 뺌 (대표이사 "치수선 뭐냐")

- 건축사전의 시그니처(빨간 치수선 + 실제 치수)를 흉내 내려고 넣었지만, **숫자 없는 치수선은 뜻 없는 빨간 줄**이고, 영상 AI가 치수선을 보면 **숫자를 지어냄**(46편 c07 "480.25", c10 "220%·250%", 47편 c02 "201·31", c08 "35%·5%", c10 작은 숫자).
- 그래서 **그림·클립 프롬프트엔 치수선·화살표·측정 표시를 넣지 않는다.** 핵심 부분은 빛(glow)으로만 강조.
- 치수선과 숫자가 필요한 장면(실제 숫자가 있을 때만, 예: 15,000 km, 3.7km)은 **합성에서 Claude가 정확한 선과 숫자를 그린다.**

## 10/28 46편과 건축사전 첫 화면 비교 → 고친 것 (가장 우선)

| 차이 | 프롬프트(그림·클립) | 합성 |
|---|---|---|
| 우리는 빈 하늘이 많고 물건이 작음 | "위쪽 3분의 1 비우기" 뺌 → **물건에 바짝, 화면을 꽉 채움** | 큰 글자는 물건 옆 빈 곳에 |
| 우리는 옅은 회색·하늘색뿐 | **진한 색, 따뜻한 색과 차가운 색 대비**(노을·주황 빛 vs 파랑·하늘색) | - |
| AI가 치수선 옆에 숫자(480.25, 220%)를 지어냄 | **"치수선 포함 어디에도 숫자·글자·기호 없음"** 그림·클립 둘 다 | 숫자는 합성에서만 |
| 우리는 장면마다 제목 두 줄 | - | **큰 글자는 숫자 장면에만 하나**(10만 번+, 15,000 km+), 나머지는 짧은 빨간 이름표만 |
| 우리 자막은 아래쪽 작은 글자에 두꺼운 테두리 | - | **자막을 화면 가운데(높이 약 62%), 62px, 테두리 대신 옅은 그림자**, 노란 강조 없음 |

## 합성에서 바꿀 것 (Claude가 함)

- 큰 숫자: 위쪽 빈 하늘에 진한 회색(`#2B2B2B`) 큰 글자, 테두리 없음. 핵심어 한두 개만 빨간 글자(`#E53935`).
- 빨간 치수선 위에 숫자를 얹는다(그림 속 숫자는 AI가 틀리므로 그림엔 선만).
- 자막은 지금처럼 가운데 아래 작은 흰 글자.
- 한 장면 2초 안팎(2초 컷), 첫 1초는 그 편에서 가장 센 움직임.
- **도감이는 완전히 뺀다(10/28 대표이사).** 섬네일도 물건만. 그림·클립 프롬프트에 캐릭터 문장과 참고 이미지를 넣지 않는다.
