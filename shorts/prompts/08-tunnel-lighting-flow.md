# 08편 장면 이미지 프롬프트 (구글 플로우)

08편 「고속도로 터널은 낮에 불을 더 세게 켭니다」의 이미지 32장, 인포그래픽 그림 6장, 영상 클립(선택) 3개를 구글 플로우(나노바나나 2)로 만들 때 씁니다.

## 1. 설정

- 에이전트 설정: 생성 전 확인 **안 함**, 비율 **9:16**, 생성 개수 **1**, 이미지 모델 **나노바나나 2**
- 운전석 시점 장면은 계기판 일부만 보이게 하고, 자동차 브랜드·로고가 나오면 다시 만듭니다.
- 표지판, 터널 이름판, 차 번호판에 글자가 들어가면 안 됩니다.

## 2. 공통 스타일 (맨 처음 한 번)

```
I will ask you for 32 images for one vertical YouTube Short about highway tunnel lighting: why tunnel entrances are lit brighter in the daytime than at night. Keep exactly the same look for all of them:
- Vertical 9:16 portrait.
- Clean 3D architectural-visualization style, like a premium engineering explainer: realistic materials but simplified, tidy shapes; calm, slightly desaturated colors (concrete grey, asphalt, mountain green, sky blue, warm tunnel lights).
- Camera mostly from the driver's seat point of view, or from a high three-quarter angle like a drone. For tunnels, clean side cutaway views are welcome.
- The ONLY accent color is glowing red (#E0322B). Use it only for: thin glowing neon outlines around the one key object, red map-pin markers with a white dot, thin dotted red lines, small empty solid red label boxes, and red arrows. Everything else stays neutral.
- Absolutely no text, letters, numbers, logos, car brands, road signs with writing, license plates or watermarks anywhere. Gauges and dials are blank.
- No faces. People only as small figures from far away or from behind.
- Keep the middle band of the frame (around 45-60% height) a little calmer, because a white subtitle will sit there.
Reply "ready" and wait.
```

## 3. 장면 프롬프트

### 묶음 1 (01~08): 훅과 블랙홀 현상

```
Keep the same style as before. Make these images one by one, one image per prompt.

Image 01. Driver's point of view on a sunny mountain highway, the top edge of the dashboard visible at the bottom, a tunnel entrance ahead in the mountainside, very bright midday sun. No red.

Image 02. Driver's point of view at the exact moment of entering the tunnel: the outside world is blazing bright, but the tunnel interior ahead looks almost pitch black. No red.

Image 03. A highway tunnel entrance seen from outside at a high angle at noon: inside the entrance, a dense row of bright tunnel lights glows strongly even in daylight. The entrance zone is traced with a thin glowing red outline.

Image 04. The same tunnel entrance as image 03 at night: only a few tunnel lights are on at the entrance, much dimmer, calm dark sky. No red.

Image 05. Close-up of a car speedometer at night glow, the needle pointing high, the dial face completely blank with no numbers or markings. No red.

Image 06. Driver's point of view just inside the tunnel: dim, the car ahead barely visible in the darkness, the bright entrance behind in the rear-view mirror. No red.

Image 07. The car ahead inside a dim tunnel, almost lost in the darkness, traced with a thin glowing red outline.

Image 08. Driver's point of view near the tunnel exit: the exit is a blinding white glare, the road ahead washed out by brightness. No red.
```

### 묶음 2 (09~16): 딜레마와 답

```
Keep the same style as before. Make these images one by one, one image per prompt.

Image 09. A tunnel interior lit as bright as daylight from end to end, almost glaring, cars driving through. No red.

Image 10. A stylized 3D relief map of a mountainous peninsula seen from above, no labels, with hundreds of tiny red map-pin markers scattered over the mountains where tunnels are.

Image 11. Close-up of an old-style electricity meter with its metal disc spinning fast, motion blur on the disc, the dial completely blank. No red.

Image 12. A dim tunnel with weak lighting seen from outside in daylight: the entrance looks like a black hole in the mountain. No red.

Image 13. Clean side cutaway of a long highway tunnel on a plain light background: ceiling lights are very dense near the entrance on the left and become more and more widely spaced deeper inside to the right. No red.

Image 14. Inside view looking deep into a tunnel: near the entrance the ceiling lights are packed close together and bright, farther inside they are fewer and softer. No red.

Image 15. A small brightness sensor box on a tall steel pole in front of a tunnel portal, its round lens facing the bright entrance, the lens glowing red.

Image 16. A grey electrical control cabinet beside a tunnel portal, a thin dotted red line running from the sensor pole to the cabinet.
```

### 묶음 3 (17~24): 날씨별 조명과 숫자

```
Keep the same style as before. Make these images one by one, one image per prompt.

Image 17. One image split into three vertical panels showing the same tunnel entrance: left on a sunny day with the entrance lights brightest, middle on a cloudy day with them a little dimmer, right at night with them dimmest. Thin white lines between panels. No text.

Image 18. High aerial view of a highway winding through mountains with several tunnel portals, a red map-pin marker above each portal.

Image 19. A tunnel entrance at dusk, the entrance lights gently dimming, warm sky. No red.

Image 20. A clean factory equipment room: motors and pumps with small sensors, thin red dotted lines from the sensors to a grey control cabinet.

Image 21. Driver's point of view on the sunny mountain highway again, closer to the tunnel entrance than image 01, same light. No red.

Image 22. The same tunnel entrance as image 03 at noon, seen a little closer, the bright entrance lights clearly visible one by one. No red.

Image 23. Close-up of LED tunnel luminaires on the tunnel wall near the entrance, glowing very bright in a tight row. No red.

Image 24. Close-up of a single tunnel lamp deep inside the tunnel, softly dimmed. No red.
```

### 묶음 4 (25~32): 클로즈업

```
Keep the same style as before. Make these images one by one, one image per prompt.

Image 25. A car entering a tunnel seen from behind and above, its headlights switching on, the bright outside behind it. No red.

Image 26. A very long tunnel interior in perspective, rows of lights receding into the distance, calm. No red.

Image 27. The tunnel entrance on a cloudy grey day, entrance lights on but softer. No red.

Image 28. The tunnel entrance on a bright sunny day, close view, entrance lights at full brightness. No red.

Image 29. The tunnel entrance at night, close view, only a few lights glowing. No red.

Image 30. Macro close-up of the round lens of a brightness sensor with the blue sky reflected in it, a faint red glow around the rim.

Image 31. A highway traffic control room with a large wall of dark blank screens, one operator seen small from behind. All screens blank. No red.

Image 32. Aerial view of a sunny mountain highway with a tunnel entrance in the middle, cars on the road. No red.
```

## 4. 인포그래픽 그림 6장 (선택, 크레딧이 있을 때만)

크레딧이 없으면 건너뜁니다. 그때는 아래 표의 선·테두리·핀·라벨을 제가 합성 단계에서 기본 사진 위에 직접 그리고, 말에 맞춰 한 칸씩 그려지게 움직입니다. 크레딧이 있으면 배경 그림을 고른 상태에서 하나씩 넣습니다. 글자와 숫자는 넣지 않고, 제가 합성할 때 정확히 얹습니다.

| 그림 | 얹는 것 | 제가 넣을 글자 |
|---|---|---|
| 03i | 입구 조명 줄을 따라 붉은 테두리, 빈 라벨 | "낮에 더 밝게" |
| 13i | 천장 조명 위로 입구에서 안쪽으로 내려가는 붉은 계단선 | "입구만 밝게" |
| 15i | 센서에서 제어반으로 붉은 점선, 빈 라벨 | "바깥 밝기 측정" |
| 17i | 세 칸의 입구 조명 영역에 붉은 테두리, 칸마다 빈 라벨 | "맑음 · 흐림 · 밤" |
| 10i | 핀이 더 촘촘해지고 빈 라벨 하나 | "2천 개+" |
| 18i | 터널 입구마다 붉은 테두리, 빈 라벨 | "252곳" |

```
Image 03i. Use image 03 exactly as it is. Add only: a glowing red outline tracing the row of bright entrance lights, and one small empty solid red label box above the entrance. No text, no numbers.

Image 13i. Use image 13 exactly as it is. Add only: a thick glowing red line drawn above the ceiling lights that starts high at the entrance on the left and steps down like a staircase toward the right, and one small empty solid red label box. No text, no numbers.

Image 15i. Use image 15 exactly as it is. Add only: a thin dotted red line from the sensor lens down the pole and along the ground to a grey control cabinet, and one small empty solid red label box near the sensor. No text, no numbers.

Image 17i. Use image 17 exactly as it is. Add only: a glowing red outline around the lit entrance zone in each of the three panels, and one small empty solid red label box at the top of each panel. No text, no numbers.

Image 10i. Use image 10 exactly as it is. Add only: many more tiny red map-pin markers so the mountains are dotted with them, and one small empty solid red label box in the corner. No text, no numbers.

Image 18i. Use image 18 exactly as it is. Add only: a glowing red outline around each tunnel portal, and one small empty solid red label box in the sky. No text, no numbers.
```

## 5. 영상 클립 (선택, 크레딧이 있을 때만)

크레딧이 없으면 건너뛰세요. 07편처럼 제가 사진으로 움직임을 만듭니다.

| 우선순위 | 시작 → 끝 | 쓰는 곳 |
|---|---|---|
| 1 | 01 → 02 | 첫 장면: 터널로 빨려 들어감 |
| 2 | 13 → 13i | "계단처럼 밝기를 낮춰 가죠" |
| 3 | 21 → 22 | 마지막 장면 (첫 장면과 이어짐) |

```
Clip 01→02. Driver's point of view driving fast along the sunny highway straight into the tunnel; as the car enters, the tunnel ahead turns almost black for a moment. No text.

Clip 13→13i. Slow pan along the tunnel cutaway from the entrance on the left to the inside on the right while a red staircase line draws itself above the ceiling lights. No text.

Clip 21→22. Driver's point of view approaching the tunnel entrance; the bright entrance lights come into view one by one. No text.
```

## 6. 소리 (이번 편부터)

- **배경음악:** 유튜브 스튜디오 → 오디오 보관함에서 "Cinematic" 또는 "Dramatic" 장르의 차분한 곡을 하나 골라 mp3로 보내 주세요. 무료이고 수익 창출 영상에도 쓸 수 있는 곡만 있습니다. 내레이션이 나올 때는 제가 음악 소리를 자동으로 줄입니다.
- **효과음:** 터널 진입 바람 소리, 라벨이 뜰 때, 숫자가 뜰 때, 계량기 회전음은 제가 만들어 넣습니다.

## 업로드 전에 지킬 것

- 실제 도로처럼 보이는 AI 이미지이므로 업로드할 때 유튜브의 '변경되거나 합성된 콘텐츠' 표시를 켭니다.
- 자동차 브랜드, 표지판 글자, 번호판, 사람 얼굴이 보이는 장면은 다시 만듭니다.
