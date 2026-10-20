# 13. 담배 하나에 0.006초, 이 기계는 박자를 어떻게 맞출까

- 제목: 담배 하나에 0.006초, 이 기계는 박자를 어떻게 맞출까. 다른 후보: 「크기가 다른 드럼들이 0.006초 박자를 놓치지 않는 비밀」
- 분류: 제어반·데이터 (고객 제안 겸용). 담배 광고로 보이지 않게 흡연 장면·상표·담뱃갑을 넣지 않습니다
- 길이: 95~100초 목표, 내레이션 공백 제외 687자, 22문장
- 이미지: 플로우 22장 + 합성 그래픽
- 회사 이름은 영상에 넣지 않음. 관련 실적은 설명란에만.

## 대본

| 비트 | 내레이션 |
|---|---|
| 1. 훅 | 여기 담배 하나에 0.006초밖에 주지 않는 기계가 있습니다. |
|  | 바로 1분에 1만 개비를 만드는, 여러분이 길에서 보는 담배의 제조기죠. |
|  | 크기가 다른 드럼들이 이 박자로 담배를 주고받는데, 대체 어떻게 한 번도 놓치지 않을까요? |
| 2. 균열 | 드럼은 홈에 담배를 진공으로 붙여 돌다가, 넘기는 순간 다음 드럼에 건넵니다. |
|  | 이때 허용되는 어긋남은 0.006초가 아니라, 1만분의 1초 수준이어야 하죠. |
|  | 그런데 속도가 빨라질수록, 옛날 방식으로는 이 박자를 맞추기 어려워집니다. |
| 3. 딜레마 | 예전엔 모터 하나에 기어를 줄줄이 물렸는데, 기어마다 생기는 작은 틈, 백래시가 쌓이거든요. |
|  | 드럼마다 모터를 달아도, 각자 속도로만 돌면 차이가 쌓여 어긋나고요. |
|  | 그래서 답은 박자를 하나로 만드는 겁니다. |
|  | 보이지 않는 기준 축 하나를 두고, 모든 드럼과 칼이 그 위치를 따라가게 하죠. |
|  | 드라이브끼리는 100만분의 1초 단위로 시계를 맞추고, 늦게 닿는 신호는 미리 당겨 줍니다. |
|  | 남은 백래시는 드럼에 직접 단 엔코더로 재서, 그 자리에서 바로잡고요. |
| 4. 발상 전환 | 자, 여기서 진짜 문제입니다. |
|  | 박자를 완벽하게 맞춰도, 기계는 매일 조금씩 지칩니다. |
|  | 감속기가 닳아 백래시가 커지고, 모터가 뜨거워지고, 담배 가루가 진공 팬을 막습니다. |
|  | 그런데 돌리기만 하는 제어반은, 박자가 흔들리기 시작했다는 걸 말해 주지 않습니다. |
| 5. 숫자 | 그래서 필요한 게 지능형 제어반입니다. |
|  | 축마다 기준과 얼마나 어긋났는지, 백래시가 얼마나 커졌는지 쉬지 않고 기록하죠. |
|  | 숫자가 기준을 넘으면 먼저 알리고, 그 기록은 멀리 있는 담당자 화면까지 이어집니다. |
| 6. 마무리 | 0.006초의 박자를 맞추는 것과, 그 박자가 흔들리는 순간을 숫자로 보는 것. |
|  | 설비를 제어하고 데이터를 연결해야, 멈추기 전에 손쓸 수 있습니다. |
|  | 지금 이 순간에도 어느 공장에선, 0.006초마다 담배 하나가 드럼을 건너가고 있습니다. |

## 사실 확인

| 내용 | 출처와 원문 |
|---|---|
| 1분에 1만 개비 → 개비당 0.006초 | [Körber Protos-Neo 자료](https://insights.koerber-technologies.com/hubfs/KTE-1210_hilite_01_2025_en_Protos-Neo.pdf?hsLang=en) "King Size Speed: 10,000 cpm". 60 ÷ 10,000 = 0.006초 |
| 허용 어긋남은 1만분의 1초(0.1ms) 수준 | 설계 가이드: 넘김 허용 오차를 홈 간격의 2%로 잡으면 0.006초 × 2% ≈ 0.12ms. 고객 제안서 오차 예산(0.1~0.25ms)과 같은 근거. 기계마다 달라 "수준"으로 씀 |
| 모터 하나 + 기어 방식의 한계, 축마다 서보 + 하나의 기준(마스터)으로 동기, 속도별 위상 보정 | 필립모리스 특허 [EP1113729B1](https://patents.google.com/patent/EP1113729B1/en): "single drive … reduction gearing … bulky and inflexible", 축별 서보, "synchronised to the cut off motor", 속도에 따라 위상 조정 |
| 드라이브끼리 100만분의 1초 단위로 시계를 맞춤 | EtherCAT 분산 클럭 1µs 아래([Kollmorgen](https://webhelp.kollmorgen.com/kas4.02/Content/3.UnderstandKAS/EtherCAT/EtherCAT%20Distributed%20Clock.htm), [IEICE 2024](https://global.ieice.org/en_transactions/fundamentals/10.1587/transfun.2024EAL2042/_pdf_advpub), 중소 규모 시스템 기준) |
| 드럼 쪽 엔코더로 유격을 바로잡음(이중 루프), 감속기 마모로 유격 증가 | 제어 공학 일반(부하측 엔코더 풀 클로즈드 루프). 고객 제안서 백래시 대책과 같은 내용 |
| 지능형 제어반: 기록, 기준 알람, 원격 화면 | `knowledge/company.md`. 축별 추종 오차·유격 기록은 이번 제안 시스템의 기능으로 설명하며, 회사 실적처럼 쓰지 않음 |
| 쓰지 않기로 한 것 | 고객사 이름과 고객 목표 속도(분당 1만 2천 개), 1분 2만 개 주장(미확인), 흡연 장면·상표·담뱃갑, "절대 멈추지 않는다" 같은 단정 |

## 검수 기록

| 차수 | 걸린 점 | 고친 것 |
|---|---|---|
| 1차 | "옛날 방식으로는 거의 불가능"은 과장(기어식 기계도 분당 수천 개를 만들었음) | "속도가 빨라질수록 맞추기 어려워진다"로 낮춤 |
| 1차 | "멈추지 않고 달릴 수 있다"는 단정 | "멈추기 전에 손쓸 수 있다"로 바꿈 |
| 1차 | 705자로 김 | 설비 제어 비트 문장을 줄여 686자 |
| 2차(고객 제안 겸용) | 고객 목표(5ms)를 공개 영상에 쓰면 고객 정보가 드러남 | 공개 숫자는 상용 기계(1분 1만 개, 0.006초)로만. 고객용은 끝 화면만 바꾼 별도 판으로 |
| 2차 | "설비 제어 + 데이터 연결" 공식 | 비트 3 = 박자를 하나로(설비 제어), 비트 4 = 맞춰도 지치는데 돌리기만 하는 제어반은 말이 없음, 비트 5 = 지능형 제어반 |

## 타입캐스트 대본

속도 1.0, 문장 사이 쉼 0.3~0.5초. mp3와 자막(srt)을 함께 받습니다. 숫자는 한글로 적었습니다.

```
여기 담배 하나에 영 점 영영육 초밖에 주지 않는 기계가 있습니다.
바로 일 분에 만 개비를 만드는, 여러분이 길에서 보는 담배의 제조기죠.
크기가 다른 드럼들이 이 박자로 담배를 주고받는데, 대체 어떻게 한 번도 놓치지 않을까요?
드럼은 홈에 담배를 진공으로 붙여 돌다가, 넘기는 순간 다음 드럼에 건넵니다.
이때 허용되는 어긋남은 영 점 영영육 초가 아니라, 만분의 일 초 수준이어야 하죠.
그런데 속도가 빨라질수록, 옛날 방식으로는 이 박자를 맞추기 어려워집니다.
예전엔 모터 하나에 기어를 줄줄이 물렸는데, 기어마다 생기는 작은 틈, 백래시가 쌓이거든요.
드럼마다 모터를 달아도, 각자 속도로만 돌면 차이가 쌓여 어긋나고요.
그래서 답은 박자를 하나로 만드는 겁니다.
보이지 않는 기준 축 하나를 두고, 모든 드럼과 칼이 그 위치를 따라가게 하죠.
드라이브끼리는 백만분의 일 초 단위로 시계를 맞추고, 늦게 닿는 신호는 미리 당겨 줍니다.
남은 백래시는 드럼에 직접 단 엔코더로 재서, 그 자리에서 바로잡고요.
자, 여기서 진짜 문제입니다.
박자를 완벽하게 맞춰도, 기계는 매일 조금씩 지칩니다.
감속기가 닳아 백래시가 커지고, 모터가 뜨거워지고, 담배 가루가 진공 팬을 막습니다.
그런데 돌리기만 하는 제어반은, 박자가 흔들리기 시작했다는 걸 말해 주지 않습니다.
그래서 필요한 게 지능형 제어반입니다.
축마다 기준과 얼마나 어긋났는지, 백래시가 얼마나 커졌는지 쉬지 않고 기록하죠.
숫자가 기준을 넘으면 먼저 알리고, 그 기록은 멀리 있는 담당자 화면까지 이어집니다.
영 점 영영육 초의 박자를 맞추는 것과, 그 박자가 흔들리는 순간을 숫자로 보는 것.
설비를 제어하고 데이터를 연결해야, 멈추기 전에 손쓸 수 있습니다.
지금 이 순간에도 어느 공장에선, 영 점 영영육 초마다 담배 하나가 드럼을 건너가고 있습니다.
```

강조: 셋째·넷째 문장의 "대체 ~일까요?", 중간 훅 "그런데 여기서 진짜 문제가 생깁니다.", 비트 4 첫 두 문장.

자막 노란 핵심어: 0.006초, 1만분의 1초, 백래시, 기준 축, 지능형 제어반, 데이터

## 플로우 프롬프트 (한 줄에 한 장)

설정: 생성 전 확인 안 함, 9:16, 생성 개수 1, 나노바나나 2. 한 줄씩 붙여 넣고, 받은 그림은 번호 순서대로 저장합니다.

```
01 | A long, clean cigarette making machine in a bright modern factory hall, a chain of polished drums of different sizes along its side, white paper rods moving across them, no people; the chain of drums traced with a thin glowing red outline. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
02 | Extreme slow-motion close-up: a single white rod frozen in mid-transfer between two fluted drums, crisp detail, dark background. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. No red.
03 | Close-up of several fluted metal drums of different diameters turning side by side, white rods held in their grooves, motion blur. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. No red.
04 | Extreme close-up of one drum surface with fine grooves and tiny suction holes; small red arrows show air being sucked inward. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
05 | The handover point between two drums: one white rod caught mid-transfer; a thin red dotted arc marks the handover point. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
06 | A large minimalist stopwatch with a completely blank face and one thin red hand, floating over the blurred machine. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
07 | A vintage machine driven by one large electric motor with a long train of gears, shafts and belts, warm old factory light. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. No red.
08 | Macro close-up of two meshing gear teeth with a small visible gap between them, the gap traced with a thin glowing red outline. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
09 | Two drums whose grooves are slightly misaligned at the handover point, one white rod tipping and about to fall, tense. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. No red.
10 | A glowing translucent ghost shaft floating above the machine, with thin red dotted lines linking it down to every drum and the knife. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
11 | Inside a control cabinet: a row of servo drives connected by one network cable, tiny red light pulses travelling along the cable in step. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
12 | A drum mounted directly on a hollow-shaft servo motor, with a slim encoder ring on the drum shaft; the encoder ring traced with a thin glowing red outline. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
13 | The machine at night in a dark factory, only its drums lit, tense mood. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. No red.
14 | Cutaway of a worn gearbox with slightly worn gear teeth and a little metal dust. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. No red.
15 | An electric motor on the machine with a soft red-orange heat glow around its housing. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
16 | A vacuum fan duct and filter clogged with fine brown tobacco dust, viewed close up. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. No red.
17 | An old plain gray industrial control panel cabinet with only switches, push buttons and indicator lamps on its closed door, no screen, standing quietly next to a running machine. Set in a factory beside the machine. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. No red.
18 | A modern gray control panel cabinet with its door open and a small blank screen showing simple line graphs; thin dotted red lines run from it to the drums and the motors. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
19 | A monitor showing one blank line graph rising toward a dashed threshold line, the last point glowing red, no text. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
20 | An empty office desk at night with a monitor showing blank line graphs and one red alert light, factory visible through the window, no people. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
21 | A maintenance technician seen from behind, walking toward the machine with a toolbox, calm morning light. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. No red.
22 | The same slow-motion close-up as image 02: a single white rod in mid-transfer between two fluted drums. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. No red.
```

## 장면 배치표

| 문장 | 이미지 | 합성 그래픽·글자 |
|---|---|---|
| 1. 여기 담배 하나에 0.006초밖에 주지 … | 02, 01 | "0.006초" 큰 숫자 |
| 2. 바로 1분에 1만 개비를 만드는, 여러분… | 01, 03 | "1분 1만 개비" |
| 3. 크기가 다른 드럼들이 이 박자로 담배를 … | 03 | 큰 "?" |
| 4. 드럼은 홈에 담배를 진공으로 붙여 돌다가… | 04, 05 | "홈 + 진공 → 넘김" |
| 5. 이때 허용되는 어긋남은 0.006초가 아… | 06 | "허용 오차 ≈ 1만분의 1초(0.1ms)" 시계 바늘이 아주 조금만 움직임 |
| 6. 그런데 속도가 빨라질수록, 옛날 방식으로… | 07 | "빨라질수록 어려워진다" 예고 |
| 7. 예전엔 모터 하나에 기어를 줄줄이 물렸는… | 07, 08 | 기어 사이 틈이 붉게 커지는 그래픽 "백래시가 쌓인다" |
| 8. 드럼마다 모터를 달아도, 각자 속도로만 … | 09 | "각자 돌면 어긋난다" |
| 9. 그래서 답은 박자를 하나로 만드는 겁니다… | 10 | "박자를 하나로" 큰 글자 |
| 10. 보이지 않는 기준 축 하나를 두고, 모든… | 10 | ① "설비 제어: 기준 축 하나 → 모든 축이 위치로 따라감" |
| 11. 드라이브끼리는 100만분의 1초 단위로 … | 11 | "100만분의 1초로 시계를 맞춤 · 늦는 신호는 미리" |
| 12. 남은 백래시는 드럼에 직접 단 엔코더로 … | 12 | "드럼 엔코더로 백래시 바로잡기(이중 루프)" |
| 13. 자, 여기서 진짜 문제입니다.… | 13 | "진짜 문제" 화면 어둡게 |
| 14. 박자를 완벽하게 맞춰도, 기계는 매일 조… | 13 | "기계는 매일 지친다" |
| 15. 감속기가 닳아 백래시가 커지고, 모터가 … | 14, 15, 16 | 세 장면 빠르게: 마모 · 열 · 분진, 짧은 흔들림 0.5초(이 편의 가장 센 순간) |
| 16. 그런데 돌리기만 하는 제어반은, 박자가 … | 17 | "돌리기만 하는 제어반" → 말풍선 "…" |
| 17. 그래서 필요한 게 지능형 제어반입니다.… | 18 | "지능형 제어반" 큰 글자 |
| 18. 축마다 기준과 얼마나 어긋났는지, 백래시… | 19 | ② "데이터: 어긋남 · 백래시 변화 기록" 그래프 |
| 19. 숫자가 기준을 넘으면 먼저 알리고, 그 … | 19, 20 | 기준선을 넘으면 붉게 깜빡 "알림", 붉은 점선이 화면까지 |
| 20. 0.006초의 박자를 맞추는 것과, 그 … | 21 | "박자를 맞추는 것 + 흔들림을 보는 것" |
| 21. 설비를 제어하고 데이터를 연결해야, 멈추… | 18 | "설비를 제어하고, 데이터를 연결하다" 큰 글자 |
| 22. 지금 이 순간에도 어느 공장에선, 0.0… | 22 | 첫 장면 구도로 끝, 반복 재생 |

## 설명란

1분에 1만 개비, 담배 하나에 0.006초. 크기가 다른 드럼들이 이 박자를 놓치지 않으려면 모든 축을 하나의 기준에 위치로 묶고, 유격까지 숫자로 지켜봐야 합니다.

지능형 제어반은 설비를 제어하면서 운전 데이터를 함께 모으고, 설정 기준을 벗어나면 알람을 보냅니다.

#모션제어 #서보 #동기제어 #지능형제어반 #공장자동화

## 두 가지 판

| | 공개용 (채널·릴스) | 고객 제안용 (미팅·메일) |
|---|---|---|
| 숫자 | 상용 기계 기준: 1분 1만 개비, 0.006초, 허용 오차 1만분의 1초 수준 | 고객 목표: 제품 간격 5ms(0.005초), 1분 1만 2천 개비, 허용 오차 0.1~0.25ms |
| 내레이션 | 아래 타입캐스트 대본 그대로 | 아래 **고객용 교체 줄 5줄**만 따로 만들어 바꿔 끼움(나머지 17줄 공용) |
| 끝 화면 | 첫 장면으로 돌아가 반복 재생 | 마지막 2~3초에 끝 카드: 회사 이름, "드럼 동기 제어 + 데이터 연결 제안", 문의처 |
| 회사·고객사 이름 | 영상에 넣지 않음(회사는 설명란에만) | 회사는 끝 카드에만, 고객사 이름은 넣지 않음 |

### 고객용 교체 줄 (타입캐스트에서 이 5줄만 추가로 만들어 주세요)

| 바꾸는 줄 | 공개용 | 고객용 |
|---|---|---|
| 1 | 여기 담배 하나에 영 점 영영육 초밖에 주지 않는 기계가 있습니다. | 여기 담배 하나에 영 점 영영오 초를 목표로 하는 기계가 있습니다. |
| 2 | 바로 일 분에 만 개비를 만드는, 여러분이 길에서 보는 담배의 제조기죠. | 일 분에 만 이천 개비, 지금 상용 기계보다 한 단계 빠른 박자죠. |
| 5 | 이때 허용되는 어긋남은 영 점 영영육 초가 아니라, 만분의 일 초 수준이어야 하죠. | 이때 허용되는 어긋남은 영 점 영영오 초가 아니라, 만분의 일에서 만분의 이 점 오 초 사이여야 하죠. |
| 20 | 영 점 영영육 초의 박자를 맞추는 것과, 그 박자가 흔들리는 순간을 숫자로 보는 것. | 영 점 영영오 초의 박자를 맞추는 것과, 그 박자가 흔들리는 순간을 숫자로 보는 것. |
| 22 | 지금 이 순간에도 어느 공장에선, 영 점 영영육 초마다 담배 하나가 드럼을 건너가고 있습니다. | 이제 영 점 영영오 초마다, 담배 하나가 흔들림 없이 드럼을 건너가게 됩니다. |

- "상용 기계보다 한 단계 빠른"의 근거: 쾨르버 Protos-Neo 킹사이즈 1분 1만 개(1개당 6ms)보다 20% 빠름. "업계 최고"라는 말은 1분 2만 개 주장 자료가 있어 쓰지 않습니다.
- 허용 오차 0.1~0.25ms는 제안서의 오차 예산(홈 간격의 2~5%)과 같은 숫자입니다.
- 고객용 끝 문장은 약속처럼 들리지 않도록, 계약 전에는 "건너가게 하는 것이 목표입니다"로 바꿀 수 있습니다.
