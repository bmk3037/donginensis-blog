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

## 업로드 전에 지킬 것

- 실제 공항처럼 보이는 AI 이미지이므로 업로드할 때 유튜브의 '변경되거나 합성된 콘텐츠' 표시를 켭니다. 인천공항 실제 시설 사진처럼 소개하지 않습니다.
- 공항·항공사 로고나 글자가 들어간 장면, 사람 얼굴이 보이는 장면은 다시 만듭니다.
