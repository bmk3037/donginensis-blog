# 13-C 고객 제안 릴스: 5ms 드럼 동기, 이렇게 맞춥니다

**용도:** 드럼 동기 제어 시스템을 요청한 고객사에 보내는 제안 영상입니다. 공개 배포용 13편과 대본·이미지·프롬프트가 다릅니다.

**구성:** 이야기형 숏폼이 아닙니다. 요청 조건 → 결론 → 오차 예산 → 해결 방법 다섯 가지 → 플랫폼 → 증명 → 순서로, 5ms 안에서 어떻게 맞추는지만 말합니다. 말투는 "~합니다"이고, 전문용어 대신 비유(지휘자, 하나의 시계, 과녁 앞 겨누기, 드럼에 눈 하나 더)로 설명합니다. 정확한 숫자와 용어는 제안서에 둡니다.

**지킬 선**

- 고객사 이름은 넣지 않습니다. 회사 이름은 끝 카드에만 넣습니다.
- 담배나 고속 다축 동기 실적이 있다고 말하지 않습니다. "설계상 가능", "제안", "먼저 증명"으로만 씁니다.
- 흡연 장면, 상표, 담뱃갑은 넣지 않습니다. 모든/항상/반드시 같은 말은 쓰지 않습니다.
- 숫자는 제안서의 오차 예산과 같습니다.

**분량:** 21문장, 타입캐스트 대본 공백 빼고 592자. 1.15배속으로 약 86초이고, 끝 카드 4.5초가 붙습니다. 이미지는 15장입니다.

## 대본

| # | 단락 | 내레이션(화면 자막) |
|---|---|---|
| 1 | 요청 | 요청하신 기계는 담배 하나를 0.005초마다 다음 드럼으로 넘겨야 합니다. |
| 2 | 요청 | 1분에 1만 2천 개비, 지금 상용 기계보다 빠른 속도입니다. |
| 3 | 결론 | 결론부터 말씀드리면, 설계상 가능합니다. |
| 4 | 결론 | 다만 진짜 맞춰야 할 것은 0.005초가 아니라, 넘기는 순간의 어긋남입니다. |
| 5 | 결론 | 이 어긋남을 1만분의 1초 안팎으로 묶어야, 담배가 떨어지지 않습니다. |
| 6 | 오차 계산 | 저희는 이 1만분의 1초를 예산처럼 나눠, 어디서 얼마나 틀어질 수 있는지 먼저 계산합니다. |
| 7 | 방법 1 | 첫째, 지휘자를 하나 둡니다. |
| 8 | 방법 1 | 드럼과 칼이 각자 속도를 맞추지 않고, 가상의 지휘자 축 위치를 그대로 따라갑니다. 그래서 오차가 쌓이지 않습니다. |
| 9 | 방법 2 | 둘째, 시계를 하나로 맞춥니다. |
| 10 | 방법 2 | 모터마다 따로 가던 시계를 100만분의 1초 안으로 맞춰, 같은 순간에 움직이게 합니다. |
| 11 | 방법 3 | 셋째, 늦는 만큼 미리 움직입니다. |
| 12 | 방법 3 | 움직이는 과녁의 앞을 겨누듯, 신호가 늦는 만큼 드럼 각도를 당겨 놓습니다. |
| 13 | 방법 4 | 넷째, 톱니 사이의 틈, 백래시를 잡습니다. |
| 14 | 방법 4 | 틈이 거의 없는 감속기나 직결로 줄이고, 드럼에 눈을 하나 더 달아 실제 위치를 직접 봅니다. |
| 15 | 방법 5 | 다섯째, 축을 단단히 잇고, 다음 움직임을 미리 알려 줘 뒤처짐을 줄입니다. |
| 16 | 장비 | 제어 장비는 베코프와 슈나이더, 두 가지 안을 같은 기준으로 비교해 드립니다. |
| 17 | 증명 | 그리고 기계에 올리기 전에, 시험 장치에서 먼저 증명합니다. |
| 18 | 증명 | 이웃한 두 드럼의 각도를 같은 순간에 찍어, 몇 시간 동안 기록하고, |
| 19 | 증명 | 넘기는 장면은 초고속 카메라로 함께 확인합니다. |
| 20 | 순서 | 도면 검토, 오차 계산, 시험 증명, 실기 적용. 이 순서로 진행합니다. |
| 21 | 마무리 | 0.005초마다 한 개비. 숫자로 증명하고 시작하겠습니다. |

## 숫자와 근거 (제안서와 같음)

| 숫자 | 근거 |
|---|---|
| 0.005초, 1분 1만 2천 개비 | 고객 요구 사양 |
| 넘김 오차 0.1~0.25ms | 홈 간격의 2~5% (홈 20개 예시: 0.36~0.9°) |
| 시계 차이 1µs 아래 | EtherCAT 분산 클럭, Sercos III 동기 |
| 엔코더 0.1µs | 20비트 절대값 엔코더, 3600°/초 기준 |
| 감속기 유격 수십 µs | 1·3·7 arcmin → 5·14·32µs |
| 남는 약 80µs | 100µs 예산에서 위 항목을 뺀 값 |
| 버스 1ms여도 됨 | 위치 루프·보간을 드라이브 안에서 할 때. 렌체 1ms/10ms 비교 자료 |
| 고속 카메라 1만 fps | 1프레임 = 100µs |
| 베코프 / PacDrive 3 | 제안서 비교 절. 비교 결과에 따라 17번 줄을 고칠 수 있습니다 |

## 타입캐스트 대본 (속도 1.0, mp3 + srt)

```
요청하신 기계는 담배 하나를 영 점 영영오 초마다 다음 드럼으로 넘겨야 합니다.
일 분에 만 이천 개비, 지금 상용 기계보다 빠른 속도입니다.
결론부터 말씀드리면, 설계상 가능합니다.
다만 진짜 맞춰야 할 것은 영 점 영영오 초가 아니라, 넘기는 순간의 어긋남입니다.
이 어긋남을 만분의 일 초 안팎으로 묶어야, 담배가 떨어지지 않습니다.
저희는 이 만분의 일 초를 예산처럼 나눠, 어디서 얼마나 틀어질 수 있는지 먼저 계산합니다.
첫째, 지휘자를 하나 둡니다.
드럼과 칼이 각자 속도를 맞추지 않고, 가상의 지휘자 축 위치를 그대로 따라갑니다. 그래서 오차가 쌓이지 않습니다.
둘째, 시계를 하나로 맞춥니다.
모터마다 따로 가던 시계를 백만분의 일 초 안으로 맞춰, 같은 순간에 움직이게 합니다.
셋째, 늦는 만큼 미리 움직입니다.
움직이는 과녁의 앞을 겨누듯, 신호가 늦는 만큼 드럼 각도를 당겨 놓습니다.
넷째, 톱니 사이의 틈, 백래시를 잡습니다.
틈이 거의 없는 감속기나 직결로 줄이고, 드럼에 눈을 하나 더 달아 실제 위치를 직접 봅니다.
다섯째, 축을 단단히 잇고, 다음 움직임을 미리 알려 줘 뒤처짐을 줄입니다.
제어 장비는 베코프와 슈나이더, 두 가지 안을 같은 기준으로 비교해 드립니다.
그리고 기계에 올리기 전에, 시험 장치에서 먼저 증명합니다.
이웃한 두 드럼의 각도를 같은 순간에 찍어, 몇 시간 동안 기록하고,
넘기는 장면은 초고속 카메라로 함께 확인합니다.
도면 검토, 오차 계산, 시험 증명, 실기 적용. 이 순서로 진행합니다.
영 점 영영오 초마다 한 개비. 숫자로 증명하고 시작하겠습니다.
```

- 차분하고 신뢰감 있는 설명형 목소리를 고릅니다. 공개용보다 조금 느려도 됩니다.
- "팩드라이브 쓰리", "삼 시그마", "피드포워드"를 이상하게 읽으면 그 줄만 다시 만듭니다.

## 플로우 프롬프트 (15장, 한 줄에 한 장, 나노바나나 2, 9:16, 1장, 생성 전 확인 안 함)

```
A detailed model of a high-speed cigarette machine drum section with interlocking steel drums of different diameters, standing on an engineering desk covered with blueprints, a chrome stopwatch beside it with its hand glowing red. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
Extreme close-up of two adjacent rotating drums meeting tangentially, a single plain white rod suspended mid-transfer between their grooves, the tiny gap at the transfer point outlined in red. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
A transparent horizontal glass bar divided into five segments of very different lengths, the longest segment glowing red, floating over a dark engineering workspace. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
A translucent glowing virtual shaft floating above a cigarette machine's drum section, thin red lines linking it down to each drum and to a rotary knife. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
Row of compact servo drives in an open control cabinet joined by one glowing daisy-chained network cable, small floating clock faces above each drive all perfectly aligned, a red pulse traveling along the cable. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
A rotating drum with a translucent ghost copy of itself rotated slightly ahead, a curved red arrow showing the phase lead between them. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
Cutaway of a precision gearbox, two meshing gear teeth with a tiny gap between them highlighted in glowing red, macro view. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
A servo motor coupled to a drum shaft, a second ring-shaped encoder mounted directly on the drum shaft glowing red, clean mechanical detail. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
A short rigid steel coupling between a servo motor and a drum shaft, thin red arrows ahead of the rotation suggesting feedforward, clean studio lighting. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
Two different industrial motion control cabinets standing side by side in a clean lab, doors open showing servo drives, one marked by a red status light on the left and one on the right. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
A heavy steel test bench with two grooved drums, servo motors and encoders, cables running to a control cabinet, laboratory lighting, red status light glowing. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
Two adjacent drums on a test bench with a synchronized red flash marker appearing on both drum shafts at the same instant, a faint waveform trace floating above. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
A high-speed camera on a tripod aimed at the handover point of two test drums, a red ring around the transfer point. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
Four stepping platforms rising diagonally like stairs in a clean abstract space, the last platform glowing red. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
Calm wide shot of a cigarette machine drum section running smoothly, plain white rods flowing, one rod at the handover point glowing red. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
```

## 장면 배치표

| 이미지 | 대본 줄 | 합성 글자·그래픽 |
|---|---|---|
| 01 | 1~2 | 요청: 0.005초마다 한 개비 (1분 12,000) |
| 02 | 3~5 | 설계상 가능 · 맞출 것 = 넘김 어긋남 약 1/10,000초 |
| 03 | 6 | 오차 예산 막대: 시계 · 엔코더 · 톱니 틈 · 따라가는 오차 |
| 04 | 7~8 | ① 지휘자 축 하나 (가상 기준 축) |
| 05 | 9~10 | ② 시계 하나로 (차이 < 100만분의 1초) |
| 06 | 11~12 | ③ 늦는 만큼 미리 (위상 선행) |
| 07 | 13 | ④ 톱니 틈 = 백래시 |
| 08 | 14 | 드럼에 눈 하나 더 (드럼 축 엔코더) |
| 09 | 15 | ⑤ 단단히 잇고 미리 알려 주기 |
| 10 | 16 | A안 베코프 / B안 슈나이더 |
| 11 | 17 | 시험 장치에서 먼저 증명 |
| 12 | 18 | 같은 순간 각도 기록 |
| 13 | 19 | 초고속 카메라로 넘김 확인 |
| 14 | 20 | 도면 검토 → 오차 계산 → 시험 증명 → 실기 적용 |
| 15 | 21 | 0.005초마다 한 개비 → 끝 카드 |

- 3번 장면의 오차 예산 막대는 합성에서 그래픽으로 그립니다(플로우 이미지는 배경).

## 끝 카드 (4.5초, 자막 없음)

- 드럼 동기 제어 시스템 / 제안
- 목표 제품 간격 5ms (1분 1만 2천 개비)
- 넘김 허용 오차 0.1~0.25ms 설계
- 시험 장치로 목표 속도에서 먼저 증명
- (주)동인엔시스 · 051-862-3668 · dongin@donginmne.com

## 전달 문안 (메일·메신저)

> 요청 주신 드럼 동기 제어 시스템에 대한 제안 영상(약 1분 30초)과 제안서를 보내 드립니다. 제품 간격 5ms에서 넘김 오차를 0.1~0.25ms 안으로 맞추는 방법과 오차 예산, 백래시 대책, 시험 장치로 먼저 증명하는 순서를 담았습니다. 검토 후 편하신 시간에 기술 미팅을 요청드립니다.
