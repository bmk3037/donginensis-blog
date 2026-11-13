# 01편 장면 이미지 프롬프트와 내레이션 (ChatGPT·타입캐스트용)

01편 「비 오는 날 차단기가 떨어지는 진짜 이유」를 06편처럼 실사풍 이미지와 타입캐스트 음성으로 만들 때 씁니다. 장면 이미지 6장과 인포그래픽 바탕 3장, 모두 9장입니다. 붉은 전류선, 화살표, 그래프, 글자는 이미지에 넣지 않고 합성 단계에서 얹습니다.

## 쓰는 법

1. ChatGPT 새 대화에 **공통 스타일**을 먼저 붙여 넣습니다.
2. 같은 대화에서 장면 6장, 이어서 인포그래픽 바탕 3장을 만듭니다.
3. 글자나 숫자가 그림에 들어가면 "remove all text and numbers"라고 다시 요청합니다.
4. 제 답변이 끝난 뒤 새 메시지로 아래 순서대로 첨부합니다(s1 → s2 → s3 → i3 → i4 → s5 → s6 → i6 → s7).

## 장면 구성

| 비트 | 이미지 (순서) | 합성할 때 얹는 것 |
|---|---|---|
| 1. 장면 열기 | `s1_corridor` | 빗줄기 움직임, 천천히 다가가기 |
| 2. 균열 | `s2_panel` | 내려간 레버 주변 붉은 맥박 |
| 3. 딜레마 | `s3_wall` → `i3_wall` | 벽 속 전선을 따라 흐르는 붉은 선, 콘센트 뒤로 스미는 물방울 표시 |
| 4. 발상 전환 | `i4_section` | 들어가는 선과 돌아오는 선 위로 흐르는 붉은 전류선 두 줄, 한 줄이 습기 쪽으로 새어 땅으로 빠짐, 회로가 끊기는 표시 |
| 5. 속도 | `s5_trip` | 붉은 빛이 꺼지는 순간, 느린 재생 |
| 6. 지금 여기로 | `s6_factory` → `i6_monitor` → `s7_end` | 멈추는 라인, 제어반 화면에 조금씩 오르는 그래프, 마지막 복도 |

## 공통 스타일 (먼저 붙여 넣기)

```
I will ask you for several images for one vertical short video about why a home circuit breaker trips on rainy days. Keep the same look for all of them:
- Vertical 9:16 portrait image, 1024x1792 or the closest you support.
- Photorealistic 3D render, calm engineering-documentary mood, cinematic but not dramatic.
- Cool blue-grey palette with soft warm interior light. Clean, uncluttered composition.
- Modern Korean apartment and Korean factory settings, realistic.
- Keep the bottom 30% of the frame calm and simple (dark floor, wall or shadow), because subtitles go there.
- Absolutely no text, letters, numbers, labels, logos, brand marks or watermarks anywhere, including on breakers and devices.
- No visible faces. People only as back views or silhouettes.
Reply "ready" and wait for my first scene.
```

## 장면 프롬프트

### `s1_corridor.png` — 비 오는 아파트 복도

```
Scene 1. A Korean apartment corridor on a rainy evening, heavy rain streaking down the corridor window, wet reflections on the floor. Beside a front door, a small grey residential electrical panel door hangs open; inside, one breaker lever is switched down. Cool blue tones with a faint warm light from the panel. Eye-level, slightly wide.
```

### `s2_panel.png` — 내려간 차단기 확대

```
Scene 2. Macro close-up inside a residential electrical panel: a neat row of white circuit breakers, one lever flipped down, clean and undamaged. Soft side light, shallow depth of field, faint reflections of rain-blue light on the plastic.
```

### `s3_wall.png` — 벽 속으로 스미는 물기

```
Scene 3. Inside an apartment room on a rainy day: a wall outlet near the floor, a faint damp stain spreading on the wallpaper around it, rain visible through a window in the background. Moody, quiet, realistic.
```

### `s5_trip.png` — 누전차단기가 떨어지는 순간

```
Scene 5. Dramatic macro close-up of a residential earth-leakage circuit breaker at the instant it trips: the lever snapping downward with a slight motion blur, a dark background, a crisp rim light along the edges. High-speed-photography feeling.
```

### `s6_factory.png` — 멈춘 생산라인

```
Scene 6. Inside a clean Korean factory: a long production line with conveyors and machines that has just stopped, a single amber warning light glowing, the hall quiet and slightly dim. Wide shot, no people.
```

### `s7_end.png` — 다시 비 오는 복도

```
Scene 7. The same Korean apartment corridor on a rainy evening, now the electrical panel door is closed and the corridor lights are warm and steady. Calm, reassuring ending mood.
```

## 인포그래픽 바탕 프롬프트

먼저 아래를 한 번 붙여 넣습니다.

```
Next I need 3 clean background images for animated infographics. Same photorealistic look as before, but clean cutaway or diagram-like views.
- Vertical 9:16, same size as before.
- Clean compositions with calm empty areas where I will add glowing lines and graphs later.
- Absolutely no text, numbers, arrows, labels, glowing lines or diagrams drawn on the image.
Reply "ready".
```

### `i3_wall.png` — 벽 단면

```
Infographic base 3. Cutaway cross-section of an apartment wall: the plaster cut open to show electrical cables running inside the wall down to a wall outlet, a little moisture visible around the cable behind the outlet. Clean, technical, evenly lit, dark neutral background.
```

### `i4_section.png` — 분전반 단면

```
Infographic base 4. Clean cutaway view of a residential electrical panel on a dark background: one earth-leakage breaker in the center, two insulated wires (one going in, one coming back) running straight down in parallel from the breaker to a wall outlet at the bottom, and a ground terminal on one side. Simple, symmetrical, lots of dark empty space around the wires.
```

### `i6_monitor.png` — 제어반 화면

```
Infographic base 6. Close view of an open grey industrial control cabinet in a factory: neat wiring and breakers, and a large blank dark display screen in the upper half of the cabinet. Cool industrial light. The screen must be completely blank.
```

## 타입캐스트 내레이션 (한 줄에 한 문장, 20줄)

목소리는 차분하고 신뢰감 있는 다큐·내레이션 톤, 속도는 전체 80~95초에 맞춥니다. 문장 사이 쉼은 0.3~0.5초로 둡니다. 숫자는 없습니다.

```
장마철만 되면 차단기가 툭 떨어지는 집, 있죠.
대부분 차단기가 고장 났다고 생각하는데요.
대부분 차단기는 멀쩡합니다.
오히려 그 순간, 집 안에서 제일 열심히 일하고 있는 중이에요.
전기가 어디서 새는지 찾으려면 벽 속 전선을 다 뜯어봐야 합니다.
그렇다고 사람이 감전된 다음에 알면 늦죠.
그래서 누전차단기는 새는 곳을 찾지 않습니다.
대신 들어간 전기와 돌아온 전기를 계속 비교하죠.
정상이라면 둘은 똑같아야 하거든요.
콘센트나 낡은 전선 피복에 습기가 스며서 전기가 땅으로 새면, 둘 사이에 차이가 생깁니다.
차단기는 그 차이를 잡는 순간 회로를 끊어요.
새는 전기가 정해진 크기를 넘으면, 차단기는 순식간에 회로를 끊습니다.
사람이 다치기 전에 끊는 게 이 차단기의 일이거든요.
공장은 사정이 다릅니다.
차단기 하나가 떨어지면 라인이 통째로 멈추거든요.
그런데 차단기는 끊기만 할 뿐, 기록은 남기지 않습니다.
그래서 누설전류 감시 장치를 단 제어반은 새는 전기의 양을 계속 재서 남겨 두죠.
끊는 데서 그치지 않고 그 변화를 기록하면, 조금씩 커지는 숫자에서 이상 징후를 먼저 읽을 수 있거든요.
집에서 비만 오면 차단기가 떨어진다면 고장이 아니라 신호입니다.
반복되면 꼭 전기 점검을 받으세요.
```

| 줄 | 강조 | 이유 |
|---|---|---|
| 3 | "멀쩡합니다" | 균열 비트의 반전 |
| 8 | "비교하죠" | 원리의 핵심 |
| 16 | "기록은 남기지 않습니다" | 데이터로 넘어가는 지점 |
| 20 | 문장 전체를 또박또박 | 안전 안내 |
