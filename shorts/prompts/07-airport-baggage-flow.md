# 07편 장면 이미지 프롬프트 (구글 플로우)

07편 「인천공항 바닥 아래엔 184km짜리 길이 숨어 있습니다」의 이미지 23장과 영상 클립 3개를 구글 플로우(나노바나나 2)로 만들 때 씁니다. 화면 문법은 04·05편과 같습니다.

## 1. 플로우 설정

- 에이전트 설정: 생성 전 확인 **안 함**, 비율 **9:16**, 생성 개수 **1**, 이미지 모델 **나노바나나 2**
- 04편 때처럼 플로우가 장수를 늘려 만들어도 괜찮습니다. 제가 골라 씁니다.
- 실제 공항 이름, 항공사 로고, 표지판 글자가 들어가면 안 됩니다. 꼬리표의 바코드는 **줄무늬만** 있어야 합니다.

## 2. 장면 구성

| 번호 | 대본 | 합성할 때 얹는 것 |
|---|---|---|
| 05, 03 | 바닥 아래 184km짜리 길이 숨은 건물, 인천공항 | "184km" |
| 01, 02, 04 | 달리는 건 가방, 하루 16만 개, 대체 어떻게? | "하루 16만 개+", 큰 "?" |
| 06–08 | 마라톤 4번, 초속 7m, 갈림길 | "마라톤 × 4", "초속 7m" |
| 09–11 | 사람이 옮기면? 빠르게 돌리면? | "1초에 2개", 엉킴·막힘 경고 |
| 12–16 | 꼬리표 바코드가 주소, 스캐너, 갈림길, 엑스레이, 지난 꼬리표 | 바코드 스캔선, 방향 화살표, "지난 꼬리표 ✕" |
| 17 | 모터를 숫자로 지켜본다 | 모터마다 핀과 숫자 |
| 18–20 | 100만 개당 2개 vs 111개, 8억 개, 지구 18바퀴 | 막대 비교, 숫자 세기 |
| 21–23 | 공장 컨베이어도 같다, 다시 체크인 | "184km", 마지막 문장 |

## 3. 공통 스타일 (맨 처음에 한 번)

```
I will ask you for 23 images for one vertical YouTube Short about the baggage handling system hidden under a big international airport: hundreds of conveyor belts, junctions, scanners and electric motors that carry each checked bag to the right airplane. Keep exactly the same look for all of them:
- Vertical 9:16 portrait.
- Clean 3D architectural-visualization style, like a premium engineering explainer: realistic materials but simplified, tidy shapes; bright even light; calm, slightly desaturated colors (light grey, steel, black rubber belts, a few muted colored suitcases).
- Camera mostly from a high three-quarter angle or from above, like a drone. Use clean cutaway views to show what is under the floor.
- The ONLY accent color is glowing red (#E0322B). Use it only for: thin glowing neon outlines around the one key object, red map-pin markers with a white dot, thin dotted red lines, small empty solid red label boxes, red arrows, and red scanner light. Everything else stays neutral.
- Absolutely no text, letters, numbers, logos, airline names, airport names, signs or watermarks anywhere. Baggage tags show only barcode stripes, never digits or letters.
- No faces. People only as small figures seen from far away or from behind, or only their hands.
- Keep the middle band of the frame (around 45-60% height) a little calmer, because a white subtitle will sit there.
Reply "ready" and wait.
```

## 4. 장면 프롬프트

### 묶음 1 (01~08)

```
Keep the same style as before. Make these images one by one, one image per prompt.

Image 01. An airport check-in counter seen from the side at a high angle: a suitcase rides on the short conveyor belt and is about to disappear through the black rubber strip curtain into the wall. Only a hand on the suitcase handle is visible. No red.

Image 02. Clean cutaway under the airport terminal floor: below the check-in hall, a huge maze of conveyor belts on several levels, criss-crossing, with suitcases riding on them. The single conveyor coming down from the check-in counter is traced with a thin glowing red outline.

Image 03. High aerial drone view of a large modern international airport terminal with several airplanes at the gates, early morning light. No logos. No red.

Image 04. Top-down view of one suitcase arriving at a junction where one conveyor splits into three directions. Large empty space around it. No red.

Image 05. Very wide high aerial cutaway of the whole baggage system under the airport: endless conveyor lines running in all directions like a city road map, tiny suitcases on them. No red.

Image 06. A single long straight conveyor belt stretching to the horizon in a vast empty grey hall, vanishing point perspective. No red.

Image 07. A suitcase riding in a small grey tray on a high-speed track, strong motion blur on the track and background, the suitcase sharp. A thin red glow line along the track.

Image 08. Top-down view of a repeating pattern of conveyor junctions and side belts, like a circuit board, with a few suitcases. No red.
```

### 묶음 2 (09~16)

```
Keep the same style as before. Make these images one by one, one image per prompt.

Image 09. A baggage handler seen from behind in a work vest, lifting one suitcase from a mountain of hundreds of suitcases in a grey hall. No face. No red.

Image 10. Suitcases jammed and piled on top of each other at a conveyor junction, one tipping over. A thin red glowing outline around the jam.

Image 11. A stopped conveyor belt with a long line of suitcases backed up behind one point, a red warning light glowing above. High three-quarter angle.

Image 12. Macro close-up of a white paper baggage tag looped around a suitcase handle. The tag shows only black barcode stripes, no digits, no letters, no logo. Soft light. No red.

Image 13. A scanner arch over a conveyor belt; a suitcase passes underneath while thin red laser lines sweep across its baggage tag. No text.

Image 14. At a conveyor junction, a grey diverter arm pushes a suitcase sideways onto a side belt. A red arrow on the floor shows the new direction.

Image 15. A suitcase entering an X-ray inspection tunnel built into the conveyor line, the tunnel opening glowing softly. No screens with text. No red.

Image 16. Close-up of a suitcase handle with two paper baggage tags: one new and clean, one old, faded and crumpled. The old tag is traced with a glowing red outline. Barcode stripes only, no digits or letters.
```

### 묶음 3 (17~23)

```
Keep the same style as before. Make these images one by one, one image per prompt.

Image 17. Low view under a long conveyor line: a row of small electric drive motors under the belt, each with a small red map-pin marker above it. Grey control cabinet in the background.

Image 18. Suitcases riding up a belt loader into the open cargo hold of an airplane on the apron, morning light. No logos. No red.

Image 19. The airport apron at dusk seen from high above, airplanes parked at the gates, calm and orderly. Keep the upper half of the frame as empty sky. No red.

Image 20. The Earth seen from space with a thin continuous line of tiny suitcases wrapping around it many times, glowing faintly red. Black space background.

Image 21. A factory production line with long conveyors and electric motors, a small red map-pin marker over each motor, high three-quarter angle.

Image 22. Baggage claim carousel in the arrival hall, suitcases coming out through the rubber curtain onto the moving carousel. No people's faces. No red.

Image 23. The same check-in counter as image 01, the suitcase now gone through the rubber curtain, the belt empty, calm light. No red.
```

## 5. 영상 클립 3개 (시작·끝 사진)

설정: 비율 **9:16**, 길이 **8초**, 개수 **1개**. 끝 사진을 넣는 칸이 없으면 시작 사진만 넣습니다.

| 클립 | 시작 사진 | 끝 사진 | 쓰는 곳 |
|---|---|---|---|
| A | 01 체크인 벨트 | 02 바닥 아래 컨베이어 미로 | 훅 세 번째 문장 "그 길을 달리는 건 … 우리가 부친 가방" |
| B | 13 스캐너 문 | 14 갈림길 밀대 | "스캐너가 바코드를 읽으면, 갈림길마다 방향이 정해집니다" |
| C | 22 수하물 찾는 곳 | (없음) | 마지막 장면 |

```
Clip A (start 01, end 02). The suitcase rides through the rubber curtain, then the camera follows it down through the floor into the huge maze of conveyors below, where it joins the glowing red belt. Smooth, calm, no text.

Clip B (start 13, end 14). The suitcase passes under the scanner arch while red laser lines read its tag, then rides on to the junction where the diverter arm pushes it onto the side belt. Smooth, no text.

Clip C (start 22). Suitcases slide one by one through the rubber curtain onto the moving carousel; camera slowly pushes in. No text.
```

## 6. 건축사전 방식: 같은 장면 두 장(배경 → 인포그래픽) + 잇는 영상

핵심 장면 6개는 건축사전처럼 **같은 장면을 두 장** 만듭니다. 배경 그림(위 01~23 중 하나)을 만든 다음, 그 그림을 고른 상태에서 아래 **인포그래픽 프롬프트**로 화살표·선·빈 라벨을 얹은 그림(05i 같은 이름)을 하나 더 만듭니다. 그다음 두 장을 **시작 → 끝**으로 넣어 8초 영상을 만들면, 화면 안에서 선과 화살표가 그려지며 나타납니다.

- **글자와 숫자는 넣지 않습니다.** 건축사전 화면에도 한글이 깨진 장면이 섞여 있습니다. 우리는 감수한 숫자가 핵심이라, "184km" 같은 글자는 제가 합성할 때 정확히 얹습니다. 그래서 인포그래픽 그림에는 **빈 붉은 라벨 상자**만 둡니다.
- **영상은 크레딧이 듭니다.** 크레딧이 모자라면 두 장(배경, 인포그래픽)만 만들어 주셔도 됩니다. 제가 두 장을 이어 "배경 → 선이 그려지며 인포그래픽" 움직임을 합성합니다. 영상만큼 살아 있지는 않지만 같은 느낌을 냅니다.
- 순서: 배경 그림 → 인포그래픽 그림 → (크레딧이 있으면) 잇는 영상. 위 5절 클립 A·B·C는 그대로 둡니다.

| 장면 | 배경 | 인포그래픽 그림에 얹는 것 | 제가 넣을 글자 | 쓰는 곳 |
|---|---|---|---|---|
| 1 | 03 공항 항공 | 터미널 바닥 아래로 붉은 점선 길이 사방으로 뻗음 | "184km" | 훅 첫 문장 |
| 2 | 05 컨베이어 미로 | 미로를 따라 굵은 붉은 경로선 하나, 끝에 붉은 핀 | "마라톤 × 4" | 184km = 마라톤 4번 |
| 3 | 04 갈림길 | 세 방향 붉은 화살표, 가운데 빈 라벨 | "?" | "대체 어떻게 길을 찾을까요?" |
| 4 | 12 꼬리표 | 바코드 둘레 붉은 테두리, 붉은 선으로 빈 라벨 연결 | "가방의 주소" | "바코드가 가방의 주소" |
| 5 | 17 벨트 아래 모터 | 모터마다 붉은 핀과 작은 빈 라벨, 제어반으로 붉은 점선 | "온도·떨림·전류" | 모터를 숫자로 지켜본다 |
| 6 | 20 지구 | 가방 줄이 지구를 여러 번 감는 붉은 궤도선 | "8억 개", "지구 18바퀴" | 숫자 비트 |

### 인포그래픽 그림 프롬프트 (배경 그림을 고른 상태에서 하나씩)

```
Image 03i. Use image 03 exactly as it is, same camera and composition. Add only: a cutaway glimpse under the terminal floor with thin dotted red lines spreading out in every direction like a road network, and one small empty solid red label box near the top. No text, no numbers.

Image 05i. Use image 05 exactly as it is. Add only: one thick glowing red route line following the conveyors through the whole maze from one corner to the other, with a red map-pin marker at the end, and one small empty solid red label box. No text, no numbers.

Image 04i. Use image 04 exactly as it is. Add only: three thick red arrows on the three outgoing conveyors, and one small empty solid red label box above the suitcase. No text, no numbers.

Image 12i. Use image 12 exactly as it is. Add only: a glowing red outline around the barcode stripes, and a thin red line from the barcode to one small empty solid red label box. Do not add or change any letters or digits.

Image 17i. Use image 17 exactly as it is. Add only: a small red map-pin marker with a tiny empty red label box above every motor, and thin dotted red lines from all motors to the grey control cabinet. No text, no numbers.

Image 20i. Use image 20 exactly as it is. Add only: several glowing red orbit lines looping around the Earth where the suitcases travel, and two small empty solid red label boxes in the black space. No text, no numbers.
```

### 잇는 영상 프롬프트 (시작: 배경, 끝: 인포그래픽)

설정: 비율 **9:16**, 길이 **8초**, 개수 **1개**. 건축사전처럼 8초를 "넓게 → 다가가기 → 선이 다 그려진 화면" 세 구간으로 짜서, 어디를 잘라도 자연스럽게 씁니다.

```
Clip 03→03i. The camera holds the aerial view of the airport for 2 seconds, then slowly pushes in while thin red dotted lines draw themselves outward under the terminal like a growing road map; hold on the finished map for the last 2 seconds. No text.

Clip 05→05i. Slow push-in over the conveyor maze while one glowing red route line draws itself along the conveyors from corner to corner and a red pin drops at the end. Hold for the last 2 seconds. No text.

Clip 04→04i. The suitcase waits at the junction while three red arrows draw onto the three outgoing belts one by one; a red label box pops in above the suitcase. No text.

Clip 12→12i. Slow macro push-in on the baggage tag while a red outline traces around the barcode and a thin red line extends to a label box. Do not change the barcode. No text.

Clip 17→17i. Camera glides along under the conveyor while red pins pop up above each motor one by one and dotted red lines run to the control cabinet. No text.

Clip 20→20i. The Earth slowly rotates while glowing red orbit lines wrap around it one after another. No text.
```

## 업로드 전에 지킬 것

- 실제 공항처럼 보이는 AI 이미지이므로 업로드할 때 유튜브의 '변경되거나 합성된 콘텐츠' 표시를 켭니다. 인천공항 실제 시설 사진처럼 소개하지 않습니다.
- 공항·항공사 로고나 글자가 들어간 장면, 사람 얼굴이 보이는 장면은 다시 만듭니다.
