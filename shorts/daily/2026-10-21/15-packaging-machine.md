# 15. 하루에 상자 270만 개를 접는 기계 (포장기계)

- **제목:** 하루에 상자 270만 개를 접고 붙이는 기계
- **다른 후보:** 「시속 42km로 종이를 접는 기계」, 「과자 상자는 시속 42km로 접힙니다」
- **분류:** 시리즈 B 「공장이 멈추지 않는 이유」(PLAN.md B4). 회사 실적(company.md): 포장기계 제어시스템. 고객사 이름은 넣지 않습니다.
- **길이:** 23문장, 공백 빼고 642자. 1.12~1.14배속이면 약 95초입니다.
- **편집:** 18편 v2 방식(쉼표마다 컷, 움직이는 숫자, 같은 색 보정)으로 합성합니다.

## 대본

| # | 비트 | 내레이션(자막) |
|---|---|---|
| 1 | 1. 훅 | 여기 하루에 상자 270만 개를 접고 붙일 수 있는 기계가 있습니다. |
| 2 | 1. 훅 | 바로 여러분이 매일 뜯는 과자 상자, 약 상자가 만들어지는 곳이죠. |
| 3 | 1. 훅 | 대체 납작한 종이를, 어떻게 이렇게 빨리 상자로 바꿀까요? |
| 4 | 2. 원리 | 먼저 두꺼운 종이를 찍어 내, 펼친 상자 모양으로 자릅니다. |
| 5 | 2. 원리 | 이 종이가 벨트에 실려 달리면서, 날개를 하나씩 접고 풀을 바른 뒤 꾹 눌러 붙이죠. |
| 6 | 2. 원리 | 벨트 속도는 최대 분당 700미터, 시속 42킬로미터입니다. |
| 7 | 2. 원리 | 도심을 달리는 자동차만큼 빠르게, 종이가 접히는 겁니다. |
| 8 | 2. 원리 | 그런데 이 속도에선, 풀 한 줄의 타이밍이 상자 하나를 좌우합니다. |
| 9 | 3. 설비 제어 | 센서가 달려오는 상자의 앞끝과 뒤끝을 읽고, 그 사이에만 풀을 쏘죠. |
| 10 | 3. 설비 제어 | 상자가 제시간에 센서를 지나가지 않으면, 걸렸다고 보고 기계를 세웁니다. |
| 11 | 3. 설비 제어 | 벨트를 돌리는 모터의 속도와 풀 쏘는 순간을 한 박자로 맞추는 게, 제어반의 일입니다. |
| 12 | 4. 진짜 문제 | 자, 여기서 진짜 문제입니다. |
| 13 | 4. 진짜 문제 | 상자가 한 번 걸리면 줄 전체가 서고, 비뚤어지거나 풀이 잘못 묻은 상자는 밀어내 버려야 합니다. |
| 14 | 4. 진짜 문제 | 최대 속도로 보면, 1초만 서도 상자 서른 개를 놓치는 셈이죠. |
| 15 | 4. 진짜 문제 | 벨트와 베어링이 닳으면 모터는 조금씩 더 힘을 씁니다. |
| 16 | 4. 진짜 문제 | 그런데 정해진 대로 돌리기만 하는 제어반은, 그 변화를 말해 주지 않습니다. |
| 17 | 5. 지능형 제어반 | 그래서 필요한 게 지능형 제어반입니다. |
| 18 | 5. 지능형 제어반 | 벨트 모터마다 전류와 온도, 떨림을 쉬지 않고 기록하죠. |
| 19 | 5. 지능형 제어반 | 언제 몇 번 멈췄는지, 상자를 몇 개 버렸는지도 함께 남깁니다. |
| 20 | 5. 지능형 제어반 | 숫자가 기준을 넘으면 먼저 알리고, 그 기록은 사무실 화면까지 이어지죠. |
| 21 | 5. 지능형 제어반 | 어느 구간 모터가 지쳐 가는지 보이니, 멈추기 전에 정비 계획을 세울 수 있죠. |
| 22 | 6. 마무리 | 빠르게 접는 것과, 그 속도가 흔들리는 걸 숫자로 보는 것. |
| 23 | 6. 마무리 | 오늘 여러분이 뜯은 상자 하나도, 시속 42킬로미터로 접혀 나온 것일지 모릅니다. |

## 사실 확인

| 대본 | 근거 |
|---|---|
| 하루 270만 개 | "up to 2.7 million perfectly executed boxes per day" BOBST 2021 보도자료 [bobst.prezly.com](https://bobst.prezly.com/bobst-ultimate-masterfold-75110-folder-gluer-pushes-the-boundaries-of-productivity-with-a-fresh-new-look) |
| 분당 700미터 = 시속 42킬로미터 | "Operating speed up to 700 m/min", 사양 20~700 m/min [BOBST 제품 페이지](https://www.bobst.com/eu/en/products/folding-gluing/masterfold-75-110). 700×60÷1000 = 42 (계산) |
| 1초만 서도 상자 서른 개 | 270만 ÷ 86,400초 ≈ 31 (최대 속도 기준 계산, 대본에 "최대 속도로 보면" 명시) |
| 센서가 앞끝·뒤끝을 읽고 그 사이에만 풀 | 시작·정지 센서로 상자 앞끝·뒷끝을 감지해 풀 줄의 위치를 확인 [US5375722](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5375722) |
| 제시간에 센서를 안 지나가면 걸린 것으로 보고 멈춤 | 정해진 시간 안에 센서를 지나지 않으면 걸림 신호 → 정지 [US5137506](https://patents.google.com/patent/US5137506), [US6440049](https://patents.google.com/patent/US6440049) |
| 비뚤어지거나 풀이 잘못 묻은 상자는 밀어냄 | "a kicker arm bumps the carton" [US5375722](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5375722) |
| 벨트·베어링이 닳으면 모터가 더 힘을 씀 | 마찰이 늘면 부하가 느는 일반 원리. 숫자는 쓰지 않음 |
| 시간당 5만 상자(기획 카드) | 이번 확인에서 공식 출처를 다시 찾지 못해 뺌 |

## 검수 기록

| 회차 | 본 것 | 고친 것 |
|---|---|---|
| 1 | 숫자 | 출처를 다시 못 찾은 "1초에 14개(시간당 5만)" 대신 공식 보도자료의 "하루 270만 개"로 훅 교체 |
| 1 | 길이 | 559자 → 642자: 속도 비유, 멈춤 손실(계산), 정비 계획 문장 추가 |
| 2 | 일반 제어반 표현 | "정해진 대로 돌리기만 하는 제어반은 그 변화를 말해 주지 않는다"로 기능 비교 |
| 2 | 과장 | 정비 문장은 "보이니, 정비 계획을 세울 수 있죠"로 가능성만 말함. AI 예측 표현 없음 |
| 2 | 뼈대 | 훅 → 원리(찍기·접기·풀·속도) → 30초 예고(풀 타이밍) → 설비 제어(센서·속도) → 진짜 문제(걸림·폐기·마모) → 지능형 제어반 → 첫 장면으로 |

## 타입캐스트 대본 (속도 1.0, mp3 + srt)

```
여기 하루에 상자 이백칠십만 개를 접고 붙일 수 있는 기계가 있습니다.
바로 여러분이 매일 뜯는 과자 상자, 약 상자가 만들어지는 곳이죠.
대체 납작한 종이를, 어떻게 이렇게 빨리 상자로 바꿀까요?
먼저 두꺼운 종이를 찍어 내, 펼친 상자 모양으로 자릅니다.
이 종이가 벨트에 실려 달리면서, 날개를 하나씩 접고 풀을 바른 뒤 꾹 눌러 붙이죠.
벨트 속도는 최대 분당 칠백 미터, 시속 사십이 킬로미터입니다.
도심을 달리는 자동차만큼 빠르게, 종이가 접히는 겁니다.
그런데 이 속도에선, 풀 한 줄의 타이밍이 상자 하나를 좌우합니다.
센서가 달려오는 상자의 앞끝과 뒤끝을 읽고, 그 사이에만 풀을 쏘죠.
상자가 제시간에 센서를 지나가지 않으면, 걸렸다고 보고 기계를 세웁니다.
벨트를 돌리는 모터의 속도와 풀 쏘는 순간을 한 박자로 맞추는 게, 제어반의 일입니다.
자, 여기서 진짜 문제입니다.
상자가 한 번 걸리면 줄 전체가 서고, 비뚤어지거나 풀이 잘못 묻은 상자는 밀어내 버려야 합니다.
최대 속도로 보면, 일 초만 서도 상자 서른 개를 놓치는 셈이죠.
벨트와 베어링이 닳으면 모터는 조금씩 더 힘을 씁니다.
그런데 정해진 대로 돌리기만 하는 제어반은, 그 변화를 말해 주지 않습니다.
그래서 필요한 게 지능형 제어반입니다.
벨트 모터마다 전류와 온도, 떨림을 쉬지 않고 기록하죠.
언제 몇 번 멈췄는지, 상자를 몇 개 버렸는지도 함께 남깁니다.
숫자가 기준을 넘으면 먼저 알리고, 그 기록은 사무실 화면까지 이어지죠.
어느 구간 모터가 지쳐 가는지 보이니, 멈추기 전에 정비 계획을 세울 수 있죠.
빠르게 접는 것과, 그 속도가 흔들리는 걸 숫자로 보는 것.
오늘 여러분이 뜯은 상자 하나도, 시속 사십이 킬로미터로 접혀 나온 것일지 모릅니다.
```

- 강조: 1번 "이백칠십만 개", 3번 "대체", 7번 "풀 한 줄의 타이밍", 11번 "진짜 문제", 15번 "지능형 제어반"

## 플로우 프롬프트 (22장, 한 줄에 한 장, 나노바나나 2, 9:16, 1장, 생성 전 확인 안 함)

```
01 | A long clean factory hall with a folding-carton folder-gluer line; flat printed cardboard blanks stream in at one end and folded boxes stack up at the other end, one box glowing red. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
02 | A kitchen table with plain unbranded snack boxes and a small medicine box, morning light. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. No red.
03 | Close-up of a tall stack of flat printed cardboard blanks, one blank lifted slightly, mysterious mood. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. No red.
04 | A flatbed die-cutting machine pressing a large sheet of cardboard, the cutting outlines glowing red. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
05 | A flat unfolded box net lying on a table, its fold lines glowing red. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
06 | Folder-gluer conveyor belts carrying flat carton blanks while metal guides fold the side flaps over, slight motion blur. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. No red.
07 | Close-up of a small glue nozzle spraying a thin line of glue onto a moving carton flap, the glue line glowing red. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
08 | Carton blanks racing along fast belts with long speed streaks, a single red streak. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
09 | A city street with cars driving at speed, motion blur, daytime. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. No red.
10 | Tense extreme close-up of a glue nozzle just above the fast-moving edge of a carton, a thin red timing line between them. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
11 | A small photoelectric sensor beside a belt shining a thin red beam onto the leading edge of a passing carton. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
12 | A carton jammed and crumpled between belt sections, the machine stopping, a red warning lamp glowing. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
13 | A control panel cabinet with rows of inverters next to the folder-gluer, thin red lines running to the belt motors. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
14 | Dark dramatic close-up of a crumpled carton stuck in the machine, harsh red rim light. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
15 | A small mechanical kicker arm pushing crooked rejected cartons out of a neat stack, the rejected cartons outlined in red. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
16 | An empty stopped conveyor belt with a faint glowing red stopwatch hologram floating above it. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
17 | Close-up of a worn rubber drive belt and a bearing, the worn spots glowing red. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
18 | An ordinary gray control panel with only switches, push buttons and indicator lamps, no screen, standing next to the machine. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. No red.
19 | A modern control panel with its door open, neat wiring and a small screen showing simple line graphs, one line rising and glowing red. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
20 | Close-up of a belt drive motor with small sensors on its housing, thin red lines running from the sensors to a control panel. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
21 | An office with large monitors showing simple line charts and counters, faint streams of light flowing in from the factory floor. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. No red.
22 | The same factory hall as the first image, folded boxes stacking up neatly, one box glowing red, calm mood. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
```

## 장면 배치표

| 이미지 | 대본 줄 | 합성 글자·그래픽 |
|---|---|---|
| 01 | 1 | 하루 270만 개 |
| 02 | 2 | 과자 상자 · 약 상자 |
| 03 | 3 | ? |
| 04 | 4 | 찍어 내 자르기 |
| 05 | 5 앞 | 펼친 상자 모양 |
| 06 | 5 뒤, 22 | 접고 · 풀 · 누르기 |
| 07 | 9 뒤 | 그 사이에만 풀 |
| 08 | 6 | 분당 700m = 시속 42km |
| 09 | 7 | 도심 자동차만큼 |
| 10 | 8 | 풀 한 줄의 타이밍 |
| 11 | 9 앞 | 센서가 앞끝·뒤끝을 읽는다 |
| 12 | 10 | 제시간에 안 오면 멈춤 |
| 13 | 11 | 모터 속도 + 풀 타이밍 = 제어반 |
| 14 | 12 | 진짜 문제 |
| 15 | 13, 19 | 줄 전체가 서고 · 밀어내 버림 |
| 16 | 14 | 1초 = 상자 30개 |
| 17 | 15, 21 | 닳으면 모터가 더 힘을 쓴다 |
| 18 | 16 | 돌리기만 하는 제어반 → … |
| 19 | 17 | 지능형 제어반 |
| 20 | 18 | 전류 · 온도 · 떨림 기록 |
| 21 | 20 | 먼저 알림 · 사무실 화면까지 |
| 22 | 23 | 시속 42km로 접힌 상자 |

- 움직이는 숫자: 8번 장면에서 속도계가 0 → 700m/분(시속 42km)으로 올라감, 1번 장면에서 0 → 270만 개 세기, 16번 장면에서 초시계 1초 = 상자 30개

## 커버

| 항목 | 내용 |
|---|---|
| 머리표 | 포장 공장의 비밀 |
| 큰 제목 | 하루 / [270만 개] / 상자를 접는다 |
| 아래 문구 | 납작한 종이를 어떻게 이렇게 빨리? |
| 배경 그림 | 01 |

합성 폴더의 `cover.json` 예: `{"kick": "포장 공장의 비밀", "title": "하루|[270만 개]|상자를 접는다", "sub": "납작한 종이를 어떻게 이렇게 빨리?"}`

## 설명란

```
하루에 상자 270만 개. 납작한 종이가 시속 42km로 달리며 접히고 붙습니다.
벨트 모터의 속도와 풀 쏘는 순간을 맞추는 제어, 그리고 모터의 전류·온도·떨림과 멈춘 기록을 남겨 먼저 알려 주는 데이터 연결까지.

동인엔시스는 포장기계 제어시스템을 맡아 왔습니다.
설비를 제어하고, 데이터를 연결하다. ㈜동인엔시스
※ 영상의 그림은 AI로 만든 이미지입니다.

#포장기계 #상자 #스마트팩토리 #지능형제어반 #동인엔시스
```
