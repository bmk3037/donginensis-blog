# 13-C 고객 제안 릴스: 드럼 동기 제어 + 데이터 연결

**용도:** 고객사 미팅·메일 전달용. 공개 배포용 13편(`13-sync-proposal.md`)과 대본·이미지·프롬프트가 다릅니다.

**지킬 선**

- 고객사 이름은 영상과 설명 어디에도 넣지 않습니다.
- 회사 이름은 끝 카드에만 넣습니다.
- 담배·고속 다축 동기 실적이 있다고 말하지 않습니다. "제안", "목표", "시험으로 증명"으로만 씁니다.
- 흡연 장면, 상표, 담뱃갑은 넣지 않습니다.
- 모든/항상/반드시 같은 말은 쓰지 않습니다. "AI가 고장을 예측한다"고 하지 않습니다.
- 숫자는 제안서와 같습니다: 5ms, 분당 1만 2천, 허용 오차 0.1~0.25ms, 시계 차이 1µs 아래.

**분량:** 24문장, 타입캐스트 대본 공백 빼고 672자. 1.15배속이면 약 95초이고, 끝 카드 4.5초가 붙습니다.

## 대본

| # | 비트 | 내레이션(화면 자막) |
|---|---|---|
| 1 | 1. 훅 | 여기, 담배 하나를 0.005초마다 넘겨야 하는 기계가 있습니다. |
| 2 | 1. 훅 | 1분에 1만 2천 개비, 지금 상용 기계보다 한 단계 빠른 박자죠. |
| 3 | 1. 훅 | 드럼끼리 담배를 떨어뜨리지 않고 넘기려면, 대체 얼마나 정확해야 할까요? |
| 4 | 2. 원리 | 답은 0.005초가 아닙니다. |
| 5 | 2. 원리 | 넘기는 순간의 어긋남은 1만분의 1초에서 1만분의 2.5초 안이어야 하죠. |
| 6 | 2. 원리 | 홈이 스무 개인 드럼이면, 1도의 3분의 1 남짓이죠. |
| 7 | 2. 원리 | 그런데 이 작은 틈을 갉아먹는 범인이 셋 있습니다. |
| 8 | 3. 설비 제어 | 첫째, 시계입니다. 드라이브마다 시계가 다르면 같은 명령도 어긋나죠. |
| 9 | 3. 설비 제어 | 그래서 드라이브를 한 시계에 묶어, 차이를 100만분의 1초 아래로 줄입니다. |
| 10 | 3. 설비 제어 | 둘째, 지연입니다. 통신 지연은 빨리 돌수록 위치를 더 밀어내죠. |
| 11 | 3. 설비 제어 | 그래서 속도만큼 위상을 미리 당겨, 넘김 각도를 같게 지킵니다. |
| 12 | 3. 설비 제어 | 셋째, 유격입니다. 감속기 톱니 사이의 작은 틈, 백래시죠. |
| 13 | 3. 설비 제어 | 유격이 작은 감속기나 직결로 틈을 줄이고, 드럼 축 엔코더로 실제 위치를 맞춥니다. |
| 14 | 3. 설비 제어 | 드럼과 칼은 속도가 아니라, 가상 기준 축의 위치를 따라 돕니다. |
| 15 | 4. 진짜 문제 | 자, 여기서 진짜 문제입니다. |
| 16 | 4. 진짜 문제 | 오늘 맞춘 박자도, 베어링이 닳고 축이 데워지면 조금씩 흔들립니다. |
| 17 | 4. 진짜 문제 | 그런데 돌리기만 하는 제어반은, 그 흔들림을 말해 주지 않습니다. |
| 18 | 5. 지능형 제어반·증명 | 그래서 지능형 제어반은 드럼마다 추종 오차와 토크, 온도를 계속 기록합니다. |
| 19 | 5. 지능형 제어반·증명 | 기준을 넘으면 먼저 알려, 멈추기 전에 손쓸 시간이 생길 수 있죠. |
| 20 | 5. 지능형 제어반·증명 | 그 숫자는 공장 시스템까지 그대로 이어집니다. |
| 21 | 5. 지능형 제어반·증명 | 베코프와 슈나이더 두 구성안은, 시험 장치에서 같은 기준으로 견줍니다. |
| 22 | 5. 지능형 제어반·증명 | 이웃한 두 드럼의 각도 차를 같은 순간에 찍어, 목표 속도에서 먼저 증명한 뒤 기계에 올립니다. |
| 23 | 6. 마무리 | 0.005초의 박자를 맞추는 것, 그리고 그 박자를 숫자로 지켜보는 것. |
| 24 | 6. 마무리 | 0.005초마다 담배 하나가 흔들림 없이 드럼을 건너가게, 그것이 이 제안의 목표입니다. |

## 숫자와 근거

| 숫자 | 근거 |
|---|---|
| 0.005초, 1분 1만 2천 개비 | 고객 요구 사양 |
| 상용 기계보다 한 단계 빠름 | 쾨르버 Protos-Neo 킹사이즈 1분 1만 개비(1개당 6ms), 제안서 참고 자료. "업계 최고"라고 하지 않습니다 |
| 허용 오차 1만분의 1~2.5초 | 제안서 오차 예산: 홈 간격의 2~5% |
| 1도의 3분의 1 남짓 | 홈 20개, 1분 1만 2천 개비 → 초당 10바퀴 = 3600°/초, 0.1ms → 0.36° |
| 시계 차이 100만분의 1초 아래 | EtherCAT 분산 클럭, Sercos III 동기(제안서 참고 자료) |
| 베코프 / 슈나이더 두 구성안 | 제안서 "베코프 vs 슈나이더 PacDrive 3" 비교. 비교 결과에 따라 이 줄은 바뀔 수 있습니다 |

## 타입캐스트 대본 (속도 1.0, mp3 + srt)

```
여기, 담배 하나를 영 점 영영오 초마다 넘겨야 하는 기계가 있습니다.
일 분에 만 이천 개비, 지금 상용 기계보다 한 단계 빠른 박자죠.
드럼끼리 담배를 떨어뜨리지 않고 넘기려면, 대체 얼마나 정확해야 할까요?
답은 영 점 영영오 초가 아닙니다.
넘기는 순간의 어긋남은 만분의 일 초에서 만분의 이 점 오 초 안이어야 하죠.
홈이 스무 개인 드럼이면, 일 도의 삼분의 일 남짓이죠.
그런데 이 작은 틈을 갉아먹는 범인이 셋 있습니다.
첫째, 시계입니다. 드라이브마다 시계가 다르면 같은 명령도 어긋나죠.
그래서 드라이브를 한 시계에 묶어, 차이를 백만분의 일 초 아래로 줄입니다.
둘째, 지연입니다. 통신 지연은 빨리 돌수록 위치를 더 밀어내죠.
그래서 속도만큼 위상을 미리 당겨, 넘김 각도를 같게 지킵니다.
셋째, 유격입니다. 감속기 톱니 사이의 작은 틈, 백래시죠.
유격이 작은 감속기나 직결로 틈을 줄이고, 드럼 축 엔코더로 실제 위치를 맞춥니다.
드럼과 칼은 속도가 아니라, 가상 기준 축의 위치를 따라 돕니다.
자, 여기서 진짜 문제입니다.
오늘 맞춘 박자도, 베어링이 닳고 축이 데워지면 조금씩 흔들립니다.
그런데 돌리기만 하는 제어반은, 그 흔들림을 말해 주지 않습니다.
그래서 지능형 제어반은 드럼마다 추종 오차와 토크, 온도를 계속 기록합니다.
기준을 넘으면 먼저 알려, 멈추기 전에 손쓸 시간이 생길 수 있죠.
그 숫자는 공장 시스템까지 그대로 이어집니다.
베코프와 슈나이더 두 구성안은, 시험 장치에서 같은 기준으로 견줍니다.
이웃한 두 드럼의 각도 차를 같은 순간에 찍어, 목표 속도에서 먼저 증명한 뒤 기계에 올립니다.
영 점 영영오 초의 박자를 맞추는 것, 그리고 그 박자를 숫자로 지켜보는 것.
영 점 영영오 초마다 담배 하나가 흔들림 없이 드럼을 건너가게, 그것이 이 제안의 목표입니다.
```

- 강조: 1줄 "영 점 영영오 초", 4줄 "아닙니다", 7줄 "범인이 셋", 15줄 "진짜 문제", 18줄 "지능형 제어반"
- "베코프", "엔코더", "백래시"를 이상하게 읽으면 그 줄만 다시 만듭니다.

## 플로우 프롬프트 (23장, 한 줄에 한 장, 나노바나나 2, 9:16, 1장, 생성 전 확인 안 함)

```
Close-up of a row of interlocking polished steel drums of different diameters on a high-speed cigarette making machine, plain white paper rods held in grooves around each drum, slight motion blur, one rod at the handover point between two drums glowing red. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
Wide view of a long modern cigarette making machine in a clean bright factory hall, a stream of plain white rods flowing through its drum section, speed streaks along the line. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
Extreme close-up of two adjacent rotating drums meeting tangentially, a single plain white rod suspended mid-transfer between their grooves, the tiny gap at the transfer point outlined in red. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
A large chrome stopwatch dial divided into many thin segments, one very thin segment glowing red, dark background. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
A long horizontal grey bar representing time, with a hair-thin red slice glowing at one edge, magnifying lens hovering over the slice, minimal dark background. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
Side view of a grooved drum with twenty evenly spaced grooves, a thin glowing red wedge marking a tiny angle between a groove and its target position, protractor-like arc lines. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
Three small red warning beacons placed on a machine: one on a network cable, one on a gearbox, one on a drum shaft, dim moody industrial lighting. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
Row of compact servo drives in an open control cabinet, each drive with a small floating analog clock face above it, the clock hands slightly out of step, one clock glowing red. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
The same row of servo drives connected by one glowing daisy-chained network cable, all floating clock faces now perfectly aligned, a red pulse traveling along the cable. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
A command pulse of light traveling along a cable toward a servo motor, arriving late, a stretched red wake showing the delay behind it. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
A rotating drum with a translucent ghost copy of itself rotated slightly ahead, a curved red arrow showing the phase lead between them. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
Cutaway of a precision gearbox, two meshing gear teeth with a tiny gap between them highlighted in glowing red, macro view. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
A servo motor directly coupled to a drum shaft without a gearbox, a second ring-shaped encoder mounted on the drum shaft glowing red, clean mechanical detail. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
A translucent glowing virtual shaft floating above a cigarette machine's drum section, thin red lines linking it down to each drum and to a rotary knife. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
Dramatic dark close-up of the drum handover point, harsh red rim light, tense atmosphere. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
Close-up of a worn ball bearing and a drum shaft with heat shimmer, a soft red thermal glow on the bearing. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
An ordinary open control panel with plain relays, contactors and terminal blocks, no screen, dim flat lighting. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. No red.
A modern intelligent control panel with a small touchscreen showing abstract waveform lines per drum, one line rising and glowing red, clean cabinet wiring. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
Hands of a technician holding a tablet near the machine, the tablet showing an abstract red alert symbol, factory background softly blurred. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
Streams of light flowing from a control panel across a factory to an office wall of monitors with abstract charts. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
A heavy steel test bench with two drums, servo motors and encoders, two different control cabinets standing side by side next to it, laboratory lighting, red status lights on both cabinets. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
A high-speed camera on a tripod aimed at the handover point of two test drums, a red ring around the transfer point, faint waveform glow in the air. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
Calm wide shot of the cigarette machine drum section running smoothly, plain white rods flowing, one rod at the handover point glowing red, same angle as the opening shot. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
```

## 장면 배치표

| 이미지 | 대본 줄 | 합성 글자·그래픽 |
|---|---|---|
| 01 | 1 | 0.005s 큰 숫자, 넘김 지점 링 |
| 02 | 2 | 1분 12,000개비 · 상용 10,000보다 20%↑ |
| 03 | 3 | ? 물음표, 넘김 지점 확대 |
| 04 | 4 | 0.005초 → X |
| 05 | 5 | 0.1~0.25ms (1/10,000~2.5/10,000초) |
| 06 | 6 | 약 0.36° (홈 20개 예시) |
| 07 | 7 | 범인 셋: 시계 · 지연 · 유격 |
| 08 | 8 | ① 시계 |
| 09 | 9 | 분산 클럭 · 차이 < 1µs |
| 10 | 10 | ② 지연 · 빠를수록 더 밀림 |
| 11 | 11 | 위상 선행 = 속도 × 지연 |
| 12 | 12 | ③ 유격(백래시) |
| 13 | 13 | 직결·1arcmin급 + 드럼 축 엔코더(이중 루프) |
| 14 | 14 | 가상 기준 축 · 위치 동기 |
| 15 | 15 | 진짜 문제 |
| 16 | 16 | 마모 · 열 → 박자 흔들림 |
| 17 | 17 | 돌리기만 하는 제어반 → ? |
| 18 | 18 | 지능형 제어반 · 추종 오차 · 토크 · 온도 |
| 19 | 19 | 먼저 알림 → 손쓸 시간 |
| 20 | 20 | 공장 시스템(MES)까지 연결 |
| 21 | 21 | A안 베코프 / B안 슈나이더 PacDrive 3 |
| 22 | 22 | 같은 순간 래치 · 최대값·3σ · 고속 카메라 |
| 23 | 23, 24 | 0.005s · 첫 장면으로 · 끝 카드 |

## 끝 카드 (4.5초, 자막 없음)

- 드럼 동기 제어 + 데이터 연결 / 제안
- 목표 제품 간격 5ms (1분 1만 2천 개비)
- 넘김 허용 오차 0.1~0.25ms 설계
- 시험 장치로 목표 속도에서 먼저 증명
- (주)동인엔시스 · 설비를 제어하고, 데이터를 연결하다 · 051-862-3668 · dongin@donginmne.com

## 전달 문안 (메일·메신저)

> 요청 주신 드럼 동기 제어 시스템에 대한 제안 영상(약 1분 40초)과 제안서를 보내 드립니다. 제품 간격 5ms에서 넘김 오차를 0.1~0.25ms 안으로 맞추는 방법, 백래시 대책, 데이터 연결 방안, 시험 장치로 먼저 증명하는 순서를 담았습니다. 검토 후 편하신 시간에 기술 미팅을 요청드립니다.
