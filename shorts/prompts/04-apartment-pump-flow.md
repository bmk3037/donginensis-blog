# 04편 장면 이미지 프롬프트 (구글 플로우)

04편 「아파트 단수, 지하 펌프는 몇 달 전부터 알고 있었습니다」의 이미지 27장을 구글 플로우(나노바나나 2)로 만들 때 씁니다. 화면 문법은 05편과 같은 건축사전식입니다. 밝은 낮빛, 높은 시점과 단면, 붉은색 하나만 강조색으로 씁니다. 영상 클립 3개는 크레딧이 남을 때만 만드는 선택 사항입니다.

## 1. 플로우 준비 (처음 한 번)

1. 구글에서 "Flow"를 검색해 Google Labs의 Flow에 들어가 새 프로젝트를 만듭니다.
2. 왼쪽 아래 **에이전트**를 누르고, 오른쪽 에이전트 설정에서 세 가지를 바꿉니다.
   - 생성하기 전에 확인: **안 함** (항상으로 두면 한 장마다 멈춥니다)
   - 이미지 비율: **9:16**
   - 만드는 이미지 개수: **1** (2로 두면 크레딧이 두 배로 듭니다)
3. 이미지 모델은 **나노바나나 2**를 고릅니다.
4. 이미지에 크레딧이 드는지는 자료마다 달라서 확인하지 못했습니다. 첫 묶음을 만든 뒤 크레딧이 줄었는지 한 번 봐 주세요.

## 2. 만드는 순서

1. **시험 묶음:** 아래 **공통 스타일**과 **묶음 1의 01~03**만 붙여 넣어 결과를 봅니다. 마음에 안 들면 이 단계에서 고칩니다. 처음부터 전부 돌리면 다시 만들 때 손해가 큽니다.
2. **나머지:** 묶음 1의 남은 장면, 묶음 2, 묶음 3을 차례로 붙여 넣습니다. 묶음마다 맨 앞에 "Keep the same style as before."가 들어 있습니다.
3. **고칠 때:** 글자나 숫자가 들어간 장면은 "Image NN: remove all text, letters and numbers, keep the red label boxes empty"로 다시 요청합니다.
4. **내려받기:** 오른쪽 위 점 세 개 → **프로젝트 다운로드**로 한꺼번에 받습니다. 파일 이름이 뒤죽박죽이어도 괜찮습니다. 제가 그림을 보고 번호를 맞춥니다.
5. **보내기:** 05편 때처럼 구글 드라이브에 zip으로 올리고 공유를 "링크가 있는 모든 사용자"로 바꿔 알려 주세요.

## 3. 장면 구성

| 번호 | 대본 | 합성할 때 얹는 것 |
|---|---|---|
| 01–02 | 물이 갑자기 끊기면 | 물방울이 멈춤 |
| 07 | 몇 달 전부터 신호를 | 붉은 테두리 깜박임, "몇 달 전" |
| 03–04 | 도로 밑 수돗물 압력만으로는 | 위로 가는 화살표가 중간에서 멈춤 |
| 05 | 10미터마다 1기압 | 붉은 치수선이 층마다 쌓임, "10m = 1기압" |
| 06 | 80미터, 8기압 | "80m", "8기압" 숫자가 올라감 |
| 09, 18 | 지하의 펌프, 하루 300리터 | 파란 물길, "300L", "150병" |
| 11, 10, 08 | 펌프가 멈추면, 고장 나면 고치면? | 펌프 붉게 깜박, 창문 불이 꺼짐, 압력 바늘이 떨어짐 |
| 19, 12 | 정기 점검하면? | 점검일 하루만 표시된 달력, "그 사이?" |
| 13 | 고장을 기다리는 대신 | 센서선을 따라 흐르는 데이터 점 |
| 14–16 | 베어링, 미세하고 빠른 떨림, 전류 | "베어링" 라벨, 진동 파형, 전류 막대 |
| 17 | 그래프가 슬금슬금 | 제어반 화면 그래프 |
| 15, 21, 20 | 석 달에서 여섯 달, 다른 펌프가 대신 | "3~6개월", "수리 중", "운전 중" |
| 22–24 | 공장에선 예지보전 | 핀, "예지보전" 라벨 |
| 25–27 | 물이 콸콸 | 천천히 멀어지며 끝 |

## 4. 공통 스타일 (맨 처음에 한 번)

```
I will ask you for 27 images for one vertical YouTube Short about the water pumps in the basement of Korean high-rise apartments, and the electric motors that drive them. Keep exactly the same look for all of them:
- Vertical 9:16 portrait.
- Clean 3D architectural-visualization style, like a premium engineering explainer: realistic materials but simplified, tidy shapes; soft bright daylight or bright even indoor light; calm, slightly desaturated colors (light grey, concrete, steel, white tiles, muted blue water).
- Camera mostly from a high three-quarter angle or from above, like a drone. For buildings and machines, use clean cutaway views sliced open to show the inside.
- The ONLY accent color is glowing red (#E0322B). Use it only for: thin glowing neon outlines around the one key object, red map-pin markers with a white dot, thin dotted red lines, small empty solid red rectangular label boxes, and red arrows. Water may be shown as a thin glowing blue line. Everything else stays neutral.
- Absolutely no text, letters, numbers, logos, brand marks or watermarks anywhere. Red label boxes stay empty. Gauge dials are blank.
- No faces. People only as small figures seen from far away or from behind, or only their hands.
- Keep the middle band of the frame (around 45-60% height) a little calmer, because a white subtitle will sit there.
Reply "ready" and wait.
```

## 5. 장면 프롬프트

### 묶음 1 (01~09)

```
Keep the same style as before. Make these images one by one, one image per prompt.

Image 01. Morning in a clean Korean apartment bathroom: a hand turns a chrome faucet over a white sink, but only a few drops fall. Soft morning light. No red.

Image 02. Macro close-up of a dry chrome faucet spout with one last droplet hanging, white tiles softly blurred behind. No red.

Image 03. Aerial drone view at sunrise of a Korean high-rise apartment complex, several 30-story towers, light morning haze. No red.

Image 04. Clean cutaway of a city street: the large water main pipe under the asphalt, and a smaller branch pipe running from it toward the base of an apartment tower. The water main is traced with a thin glowing red neon outline.

Image 05. Clean side cutaway of a single 30-story apartment tower on a plain light grey background: one vertical water riser pipe runs from a pump room in the basement up to the top floor. Keep the left third of the frame empty for a height scale. No red.

Image 06. Looking straight down from the rooftop edge of a 30-story apartment tower to the tiny parking lot far below, dizzying height, morning light. No red.

Image 07. Wide high-angle view of a clean apartment basement pump room: a booster pump set of three identical pumps on one steel frame, with pipes and valves. The pump set is traced with a glowing red neon outline.

Image 08. Close-up of a round pressure gauge on a pipe in the pump room. The dial face is completely blank, no numbers and no markings, only the needle. No red.

Image 09. The same side cutaway of the apartment tower as image 05: the basement pump glows red, and a thin glowing blue line of water rises up the riser pipe to the upper floors.
```

### 묶음 2 (10~18)

```
Keep the same style as before. Make these images one by one, one image per prompt.

Image 10. Night view of the apartment towers, windows lit randomly with no pattern, quiet and calm. No red.

Image 11. Close view of one pump motor in the basement pump room at the moment it starts, slight motion blur on the coupling, a thin glowing red ring around the motor.

Image 12. A building manager in a grey uniform seen from behind, crouching beside a pump in the basement pump room with his head tilted as if listening. No face visible. No red.

Image 13. A small sensor attached to the housing of a pump motor; a thin cable glowing red runs from the sensor along the floor to a grey control panel on the wall.

Image 14. Clean cutaway of a pump motor sliced in half lengthwise on a light grey background: copper coils, rotor and shaft, and the ball bearings at both ends of the shaft traced with a glowing red neon outline. One small empty red label box connected by a thin red line to a bearing.

Image 15. Macro cutaway of a ball bearing inside a motor: polished steel balls, inner and outer rings, a faint red glow. Keep the right third of the frame as clean dark empty space.

Image 16. Open terminal box on top of a pump motor: three thick power cables connected to three terminals, the cables traced with a thin glowing red outline.

Image 17. Grey control panel on the pump room wall with a large blank dark screen in the upper half. The screen must be completely blank. No red.

Image 18. High-angle view of hundreds of identical 2-liter clear plastic water bottles standing in a neat grid on a light grey floor. No labels, no text. No red.
```

### 묶음 3 (19~27)

```
Keep the same style as before. Make these images one by one, one image per prompt.

Image 19. Early morning apartment complex, many windows lit warm at the same time, soft blue dawn sky. No red.

Image 20. Top-down view of the three-pump booster set in the basement pump room, the three pumps clearly separated with empty floor around them. No red.

Image 21. A technician seen from behind repairing one of the three pumps, its casing opened and traced with a glowing red outline, while the other two pumps keep running. No face.

Image 22. Very wide high aerial view of a factory floor with dozens of identical electric motors along production lines, a small red map-pin marker over every motor.

Image 23. One image split vertically by a thin white line: on the left, the apartment basement pump room with its three pumps; on the right, a factory motor hall with a row of motors. Same high angle on both sides. No red.

Image 24. A calm control room with a large wall of dark blank screen tiles; one operator seen small from behind. All screens blank. No red.

Image 25. Close-up of the same bathroom faucet as image 01, now with water gushing strongly, sparkling in morning light. No red.

Image 26. Sunrise over the apartment complex, wide view, warm golden light. No red.

Image 27. The basement pump room again, calm, the three pumps running quietly, soft light, camera slightly lower than image 07. No red.
```

## 6. 영상 클립 (선택, 크레딧이 남을 때)

정지 이미지만으로도 제가 움직임을 넣어 완성합니다. 크레딧이 남으면 아래 세 장면만 8초 영상으로 만들어 주세요. 하나에 넓게 → 다가가기 → 마무리 세 구간을 넣어, 어디를 잘라도 자연스럽게 씁니다.

- 설정: 비율 **9:16**, 길이 **8초**, 개수 **1개**. 시작 이미지로 해당 번호 이미지를 넣습니다.
- 영상 모델별 크레딧은 공식 가격을 확인하지 못했습니다. 한 개를 먼저 만들어 보고 남은 크레딧을 봐 주세요.

```
Clip A (start from image 09). Slow camera push-in on the apartment tower cutaway. The glowing blue water line rises steadily from the basement pump up the riser pipe to the top floor. First 3 seconds wide, then push in, last 2 seconds hold on the top floors. No text.

Clip B (start from image 11). The pump motor starts: the coupling begins to turn and reaches full speed, a soft red ring pulses once around the motor. Camera slowly orbits a little to the right. No text.

Clip C (start from image 25). Water gushing from the faucet in slow motion, sparkling morning light, camera slowly pulls back to show the sink. No text.
```

## 업로드 전에 지킬 것

- 실사처럼 보이는 AI 이미지이므로, 업로드할 때 유튜브의 '변경되거나 합성된 콘텐츠' 표시를 켭니다(`structure.md` 4장).
- 모터 단면(14, 15)은 AI가 부품 위치를 틀리게 그리기 쉽습니다. 베어링이 축 끝에 있는지 확인하고 쓰겠습니다.
- 사람 얼굴이 보이는 장면(12, 21)은 다시 만듭니다.
