# 05편 장면 이미지 프롬프트 (신비한 건축사전 화면 느낌)

05편 「공장 벽의 회색 철문 상자는, 모터가 멈추기 전에 먼저 압니다」의 이미지 30장을 만들 때 씁니다. ChatGPT와 Gemini 모두에 쓸 수 있습니다. 건축사전 상위 영상은 편당 30~35장, 3초마다 새 그림이 나와서 같은 수준으로 맞췄습니다. 01~13은 1차 제작 때 만든 그림이고, 14~30을 새로 만듭니다.

## 건축사전 화면에서 가져온 것

건축사전 상위 영상의 화면을 보고 정리했습니다(한강 수중보, 봉우리를 잇는 성벽, 쓰레기 매립 덤프트럭 장면 등).

| 건축사전 | 이번 프롬프트 | 06편 실사풍과 다른 점 |
|---|---|---|
| 밝은 낮빛, 회색·흙색 위주의 차분한 색 | 밝고 고른 낮빛, 회색·강철색 위주 | 06편은 푸른 밤 톤이었습니다 |
| 드론처럼 높은 곳에서 비스듬히 내려다보는 시점, 단면 | 높은 3/4 시점과 위에서 본 시점, 모터 단면 | 06편은 사람 눈높이가 많았습니다 |
| 깔끔한 건축 시각화 풍 3D(나무·지형을 단순하게) | 단순하게 정리한 산업 시각화 3D | 06편은 사진에 가까운 실사였습니다 |
| 붉은색 하나만 강조색. 대상에 붉은 빛나는 외곽선, 흰 점이 있는 붉은 핀, 붉은 점선, 빈 붉은 라벨 상자, 붉은 화살표 | 같은 문법을 그림 안에 넣습니다 | 06편은 붉은 선을 합성에서만 얹었습니다 |
| 자막은 화면 한가운데, 흰 글자에 검은 테두리 | 그림 한가운데를 조금 비워 둡니다 | 06편은 아래 30%를 비웠습니다 |

라벨 상자 안의 글자와 숫자는 그림에 넣지 않고 합성 단계에서 한글로 얹습니다. 건축사전 화면에도 AI가 만든 영어 글자("CRITICAL CONVERGENCE")가 섞여 있는데, 우리는 이것을 피합니다.

## 쓰는 법

1. 새 대화에 **공통 스타일**을 먼저 붙여 넣습니다.
2. 같은 대화에서 01부터 13까지 순서대로 하나씩 만듭니다.
3. 글자나 숫자가 그림에 들어가면 "remove all text, letters and numbers, keep the red label boxes empty"라고 다시 요청합니다.
4. 붉은색이 너무 많아지면 "only one red-highlighted object, everything else neutral grey"라고 다시 요청합니다.
5. 다 만들면 제 답변이 끝난 뒤 새 메시지로 번호 순서대로 첨부해 주세요.

## 장면 구성

| 번호 | 비트 | 장면 | 합성할 때 얹는 것 |
|---|---|---|---|
| 01 | 1 | 공장 통로, 회색 상자들 | 천천히 내려가는 카메라 |
| 02 | 2 | 상자 하나만 붉은 외곽선 | 외곽선 깜박임, 빠른 확대 |
| 03 | 2 | 상자에서 모터로 붉은 점선 | 핀 튀어 오름, "10번 중 4번" |
| 04 | 3 | 위에서 본 라인, 모터마다 핀 | 핀이 차례로 켜짐, 순찰하는 사람 표시 |
| 05 | 3 | 멈춘 라인, 붉은 화살표 세 개 | 화면 흔들림, 경고 깜박임 |
| 06 | 4 | 모터 반 단면 | 베어링·코일 라벨 "베어링", "코일" |
| 07 | 4 | 베어링 확대 단면 | 붉은 열기 맥동, 떨림 |
| 08 | 4 | 모터 → 상자로 모이는 점선 | 점선 따라 흐르는 빛, 라벨 "온도·떨림", "온도", "전류" |
| 09 | 4 | 상자 앞면, 빈 화면 | 그래프 세 줄, 기준선 넘으면 붉게 깜박 |
| 10 | 5 | 모터 분해도 | "41%" 숫자 세기, 베어링 외곽선 |
| 11 | 5 | 코일 확대, 붉은 열기 | "+10℃", "수명 ½" 막대 줄어듦 |
| 12 | 6 | 펌프·송풍기·컨베이어, 핀 | 핀이 차례로 켜짐 |
| 13 | 6 | 처음의 통로, 문 닫힘 | 천천히 멀어지며 끝 |

## 공통 스타일 (먼저 붙여 넣기)

```
I will ask you for 13 images for one vertical YouTube Short about electric motors in a factory and the grey control cabinets on the factory wall. Keep exactly the same look for all of them:
- Vertical 9:16 portrait, 1024x1792 or the closest you support.
- Clean 3D architectural-visualization style, like a premium engineering explainer: realistic materials but simplified, tidy shapes; soft bright daylight or bright even factory lighting; calm, slightly desaturated colors (light grey, steel, concrete, muted green-grey floor).
- Camera mostly from a high three-quarter angle or straight from above, like a drone looking down. For machines, use clean cutaway views sliced in half to show the inside.
- The ONLY accent color is glowing red (#E0322B). Use it only for: thin glowing neon outlines around the one key object, red map-pin markers with a white dot and a soft red ring on the ground, thin dotted red lines connecting points, small empty solid red rectangular label boxes, and red arrows. Everything else stays neutral.
- Absolutely no text, letters, numbers, logos, brand marks or watermarks anywhere. Red label boxes must stay empty.
- No faces. People only as small figures seen from far away or from behind.
- Keep the middle band of the frame (around 45-60% height) a little calmer, because a white subtitle will sit there.
Reply "ready" and wait for my first image.
```

## 장면 프롬프트

### 01 — 공장 통로의 회색 상자들

```
Image 01. High three-quarter view looking down a long, clean factory aisle. Along one wall stands a neat row of identical tall grey steel electrical cabinets with closed doors. A single small worker seen from behind walks past them. Bright, even light, polished concrete floor. No red in this image.
```

### 02 — 하나만 붉게 빛나는 상자

```
Image 02. The same row of grey cabinets from a slightly closer high angle. Exactly one cabinet in the middle is traced with a thin glowing red neon outline; all other cabinets stay plain grey. Calm and clean.
```

### 03 — 상자에서 모터로 이어지는 점선

```
Image 03. High three-quarter view: the red-outlined grey cabinet on the left, and a few meters away on the floor a large industrial electric motor driving a pump. A thin dotted red line runs from the cabinet along the floor to the motor. A red map-pin marker with a white dot stands on top of the motor, with a soft red ring on the floor. One small empty red label box floats beside the pin.
```

### 04 — 위에서 본 생산라인

```
Image 04. Top-down drone view of a long factory production line: conveyors, rollers and dozens of identical electric motors placed at regular intervals along the line. A small red map-pin marker stands over each motor. One small worker seen from above walks along the aisle beside the line. Bright, orderly, lots of grey and steel.
```

### 05 — 멈춘 라인

```
Image 05. High three-quarter view of the same production line, now completely stopped and slightly dimmer. One motor in the middle is traced with a glowing red neon outline, and three thick red arrows point down at it from above, converging on it. Everything else neutral grey.
```

### 06 — 반으로 가른 모터

```
Image 06. Clean cutaway of a large industrial electric motor sliced in half lengthwise, on a light grey studio background, seen from a high three-quarter angle. Visible inside: the copper windings (coils) around the stator, the rotor and shaft, and the ball bearings at both ends of the shaft. The bearings are traced with a glowing red neon outline; the copper coils have a thinner red outline. Two small empty red label boxes connected by thin red lines to the bearing and the coil.
```

### 07 — 베어링 확대

```
Image 07. Macro cutaway of a ball bearing at the end of a motor shaft: inner ring, steel balls, outer ring, a thin film of grease. A soft red heat glow radiates from the balls and the outer ring. Clean light grey background, sharp engineering-visualization look.
```

### 08 — 모터에서 상자로 모이는 선

```
Image 08. High three-quarter view: the half-cutaway motor on the right, the grey electrical cabinet on the left. Small red map-pin markers sit on three points of the motor: the bearing, the copper coil, and the power cable entry. From each pin a thin dotted red line runs across the floor and all three lines converge into the cabinet. Three small empty red label boxes next to the pins.
```

### 09 — 상자 앞면의 빈 화면

```
Image 09. Front view of an open grey industrial electrical cabinet: neat wiring, breakers and terminal rows, and a large blank dark display screen mounted in the upper half of the door. Bright even light. The screen must be completely blank and dark. No red in this image.
```

### 10 — 모터 분해도

```
Image 10. Exploded view of an industrial electric motor laid out on a light grey surface from a high angle, like an engineering infographic: housing, stator with copper coils, rotor and shaft, two ball bearings, end covers, fan, each part floating apart in a neat line. The two bearings are traced with a bold glowing red neon outline, the copper coil with a thinner red outline, all other parts plain. One empty red label box near the bearings.
```

### 11 — 뜨거워진 코일

```
Image 11. Close cutaway of motor copper windings packed in the stator slots, thin insulation layers visible between them. A soft red heat glow rises from the copper. On the left side, empty space on a clean grey background where a thermometer graphic will be added later.
```

### 12 — 펌프, 송풍기, 컨베이어

```
Image 12. High three-quarter view of a factory utility area: a water pump with its motor, a large ventilation fan with its motor, and a section of conveyor with its motor, neatly arranged in a row. A red map-pin marker with a white dot stands over each motor, with soft red rings on the floor, and thin dotted red lines run from all three toward a grey cabinet in the background.
```

### 13 — 다시 처음의 통로

```
Image 13. The same long factory aisle as image 01, from the same high three-quarter angle, the row of grey cabinets with closed doors, the aisle empty and calm, slightly warmer late-afternoon light. No red in this image.
```

## 추가 장면 프롬프트 (14~30)

새 대화에서 하면 **공통 스타일**을 먼저 다시 붙여 넣고 시작합니다. 같은 대화에서 이어 하셔도 됩니다. 붉은 강조가 없는 장면은 "No red in this image."가 맞습니다.

| 번호 | 대본 | 합성할 때 얹는 것 |
|---|---|---|
| 14 | 두꺼비집이겠거니 | "두꺼비집?" 핀 |
| 15 | 차단기와 전선만 가득 | 차단기 줄에 테두리 |
| 16 | 하루 종일 돌아갑니다 | 시계 게이지 |
| 17 | 사람 귀에 소리가 잡힐 때쯤 | 귀 옆 소리 물결 |
| 18 | 정해진 날 점검, 그 사이 | 비어 있는 밤 통로 |
| 19 | 수십 대 모터 | 핀이 차례로 켜짐, "수십 대" |
| 20 | 라인이 통째로 | 경고 깜박임 |
| 21 | 상자가 듣게 했습니다 | 선을 따라 상자로 흐르는 빛 |
| 22 | 쇠구슬이 굴러가며 | 회전 화살표 |
| 23 | 자석의 힘으로 | 자기력선 흐름 |
| 24 | 닳거나 기름이 마르면 | 붉은 열기, 떨림 |
| 25 | 전류가 평소보다 커지면 | 전류 막대가 올라감 |
| 26 | 자동차 경고등처럼 | 경고등 깜박임 |
| 27 | 큰 모터 수천 대 | "100마력 이상", "수천 대" |
| 28 | 멈추기 전에 손쓸 시간 | "교체" 라벨 |
| 29 | 물·바람·물건 | 흐름선 세 줄 |
| 30 | 체온과 맥박 | 화면에 심장박동 선 |

### 14 — 닫힌 철문 확대

```
Image 14. Closer high three-quarter view of three identical tall grey steel electrical cabinets standing side by side against a factory wall, doors closed, simple handles, ventilation louvers. Bright even light. No red in this image.
```

### 15 — 차단기와 전선만 가득한 상자

```
Image 15. Front view of an open grey electrical distribution cabinet in a factory: only rows of circuit breakers, copper busbars and neatly bundled cables inside, no screens or computers. Bright even light, clean and orderly. No red in this image.
```

### 16 — 밤에도 돌아가는 라인

```
Image 16. High three-quarter view of a long factory production line at night: conveyors and motors running under bright overhead lights, the large windows dark blue outside, no people. Calm, slightly cooler tones. No red in this image.
```

### 17 — 귀를 기울이는 작업자

```
Image 17. A factory worker in grey work clothes and a white hard hat, seen from behind, crouching next to a running industrial electric motor and leaning his head close to it as if listening. High three-quarter angle, bright even light, no face visible. No red in this image.
```

### 18 — 아무도 없는 밤의 통로

```
Image 18. Top-down drone view of an empty factory aisle at night beside a production line with motors running, only a few overhead lights on, long shadows, nobody around. Quiet mood. No red in this image.
```

### 19 — 모터 수십 대가 깔린 공장

```
Image 19. Very wide, high aerial view of a huge factory floor with several parallel production lines, dozens of identical electric motors placed at regular intervals along every line. Tiny red map-pin markers with a white dot stand over every motor. Bright, orderly, mostly grey.
```

### 20 — 멈춰서 물건이 쌓인 라인

```
Image 20. High three-quarter view of a stopped conveyor line: boxes piled up and pushed together at one point of the conveyor, the motor next to them traced with a glowing red neon outline, a single amber warning beacon on. Everything else neutral grey.
```

### 21 — 상자로 들어오는 센서선

```
Image 21. Close high-angle view of the bottom of a grey electrical cabinet: several thin sensor cables enter through neat cable glands, the cables run across the floor toward a motor in the background. The cables glow with a thin red neon light. Clean, bright.
```

### 22 — 쇠구슬 베어링 단면

```
Image 22. Clean engineering cutaway of a single deep-groove ball bearing on a light grey studio background, high three-quarter angle: outer ring, inner ring, a ring of polished steel balls held by a cage, a thin film of grease. Precise, minimal, no red.
```

### 23 — 코일과 회전자, 자기력선

```
Image 23. Cutaway of an electric motor stator with copper coils surrounding the rotor, seen from a high three-quarter angle on a light grey background. Thin glowing red curved field lines loop from the coils through the rotor, suggesting the magnetic force that turns it. No text.
```

### 24 — 닳고 기름이 마른 베어링

```
Image 24. Macro cutaway of a worn ball bearing: dull scratched steel balls, pitted marks on the outer race, dark dried-up grease, a few metal particles. A faint red heat glow around the balls. Light grey background, engineering-visualization style.
```

### 25 — 단자함 속 전선 세 가닥

```
Image 25. Close view of an open terminal box on top of an industrial electric motor: three thick power cables connected to three terminals, the three cables glowing with a thin red neon outline. Bright, clean, high three-quarter angle.
```

### 26 — 자동차 계기판 경고등

```
Image 26. Close view of a generic modern car instrument cluster at dusk, gauges dark, a single red warning lamp glowing in the middle. No brand, no logo, no letters or numbers on the dashboard; the lamp is a simple glowing symbol.
```

### 27 — 큰 모터 수천 대

```
Image 27. Very wide high aerial view inside a huge power plant equipment hall: long rows of large industrial electric motors and pumps, hundreds of identical units in perspective, steel walkways between them. Bright, orderly, mostly grey. No red in this image.
```

### 28 — 라인은 돌고, 베어링을 미리 교체

```
Image 28. A maintenance technician seen from behind at a clean workbench, fitting a new ball bearing onto a motor shaft, while in the background the production line keeps running. The new bearing has a thin glowing red outline. Bright, calm.
```

### 29 — 물·바람·물건을 옮기는 모터

```
Image 29. High three-quarter view of a factory utility area: a water pump pushing water through pipes, a large fan blowing air into a duct, and a conveyor carrying boxes, each driven by its own electric motor. Thin glowing blue flow lines show the water, the air and the boxes moving. No red in this image.
```

### 30 — 화면이 달린 회색 상자

```
Image 30. Close front view of a grey industrial electrical cabinet door with a small built-in display screen at eye level, the screen dark and completely blank. Clean, bright, slightly warm late-afternoon light. No red in this image.
```

## 업로드 전에 지킬 것

- 실사처럼 보이는 AI 이미지이므로, 업로드할 때 유튜브의 '변경되거나 합성된 콘텐츠' 표시를 켭니다(`structure.md` 4장).
- 모터 단면(06, 07, 10, 11, 22, 23, 24)은 AI가 부품 위치를 틀리게 그리기 쉽습니다. 베어링이 축 끝에, 코일이 바깥 고정자에 있는지 확인하고 쓰겠습니다.
