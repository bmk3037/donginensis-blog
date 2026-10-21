# 13-C 고객 제안 릴스: 5ms 드럼 동기, 이렇게 맞춥니다

**용도:** 드럼 동기 제어 시스템을 요청한 고객사에 보내는 제안 영상입니다. 공개 배포용 13편과 대본·이미지·프롬프트가 다릅니다.

**구성:** 이야기형 숏폼이 아닙니다. 요청 조건 → 결론 → 오차 예산 → 해결 방법 다섯 가지 → 플랫폼 → 증명 → 순서로, 5ms 안에서 어떻게 맞추는지만 말합니다. 말투는 "~합니다"이고, 고객사 기술팀 대상이라 용어와 숫자를 그대로 씁니다.

**지킬 선**

- 고객사 이름은 넣지 않습니다. 회사 이름은 끝 카드에만 넣습니다.
- 담배나 고속 다축 동기 실적이 있다고 말하지 않습니다. "설계상 가능", "제안", "먼저 증명"으로만 씁니다.
- 흡연 장면, 상표, 담뱃갑은 넣지 않습니다. 모든/항상/반드시 같은 말은 쓰지 않습니다.
- 숫자는 제안서의 오차 예산과 같습니다.

**분량:** 24문장, 타입캐스트 대본 공백 빼고 830자. 1.15배속으로 약 120초이고, 끝 카드 4.5초가 붙습니다. 이미지는 16장입니다.

## 대본

| # | 단락 | 내레이션(화면 자막) |
|---|---|---|
| 1 | 요청 | 요청하신 조건은 제품 간격 0.005초, 1분에 1만 2천 개비입니다. |
| 2 | 요청 | 직경이 다른 드럼들이 멈추지 않고, 이 간격 안에서 담배를 주고받아야 합니다. |
| 3 | 결론 | 결론부터 말씀드리면, 설계상 가능합니다. |
| 4 | 결론 | 다만 맞춰야 할 것은 0.005초가 아니라, 넘김 위상 오차 0.1~0.25밀리초입니다. |
| 5 | 결론 | 홈 20개 드럼이면 초당 3600도, 0.1밀리초는 0.36도입니다. |
| 6 | 오차 예산 | 저희는 이 0.1밀리초를 오차 예산으로 나눠 씁니다. |
| 7 | 오차 예산 | 드라이브 간 시계 차이 1마이크로초 아래, 20비트 엔코더 0.1마이크로초, 감속기 백래시 5에서 32마이크로초. |
| 8 | 오차 예산 | 남는 약 80마이크로초를 서보 추종 오차와 축 비틀림에 배정합니다. |
| 9 | 방법 1 | 첫째, 드럼과 칼을 가상 마스터 축에 전자 기어와 캠으로 묶습니다. |
| 10 | 방법 1 | 속도 동기가 아니라 위치 동기이므로, 시간 오차가 누적되지 않습니다. |
| 11 | 방법 2 | 둘째, EtherCAT 분산 클럭이나 Sercos III로 드라이브 시계를 1마이크로초 아래로 맞춥니다. |
| 12 | 방법 2 | 위치 루프와 보간은 드라이브 안에서 돌기 때문에, 버스 주기 1밀리초에서도 정밀도가 유지됩니다. |
| 13 | 방법 3 | 셋째, 통신과 드라이브의 고정 지연을 측정해, 속도에 비례한 위상 선행으로 보상합니다. |
| 14 | 방법 3 | 저속에서 고속까지 넘김 각도가 같게 유지됩니다. |
| 15 | 방법 4 | 넷째, 백래시입니다. 직결 또는 1아크분급 감속기로 기계 유격을 줄이고, |
| 16 | 방법 4 | 드럼 축 2차 엔코더로 위치 루프를 닫는 이중 루프로, 남은 유격과 비틀림을 제어합니다. |
| 17 | 방법 5 | 다섯째, 속도·가속도 피드포워드와 고강성 커플링으로 추종 오차를 줄입니다. |
| 18 | 플랫폼 | 플랫폼은 두 안입니다. 베코프 AX8000은 드럼 축 2차 엔코더를 드라이브 루프에 바로 쓸 수 있고, 슈나이더 PacDrive 3는 포장기계용 동기 라이브러리가 강점입니다. |
| 19 | 검증 | 실기 적용 전에, 두 안을 시험 장치에서 같은 기준으로 먼저 검증합니다. |
| 20 | 검증 | 인접 드럼의 부하측 엔코더 값을 같은 클럭 순간에 래치해, 목표 속도에서 몇 시간 동안 기록합니다. |
| 21 | 검증 | 합격 기준은 각도 차의 최댓값과 3시그마가 0.36도 이내입니다. |
| 22 | 검증 | 넘김 지점은 초당 1만 프레임 이상 고속 카메라로 함께 확인합니다. |
| 23 | 순서 | 진행은 도면 검토, 드럼별 오차 예산, 시험 장치 검증, 실기 적용 순입니다. |
| 24 | 마무리 | 제품 간격 0.005초, 위상 오차 0.1밀리초. 숫자로 검증하고 시작하겠습니다. |

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
| 0.36° | 홈 20개, 1분 1만 2천 개비 → 초당 10바퀴 = 3600°/초 × 0.1ms |
| 베코프 AX8000 2차 엔코더 / PacDrive 3 라이브러리 | 제안서 '베코프 vs 슈나이더 PacDrive 3 상세 비교' |

## 타입캐스트 대본 (속도 1.0, mp3 + srt)

```
요청하신 조건은 제품 간격 영 점 영영오 초, 일 분에 만 이천 개비입니다.
직경이 다른 드럼들이 멈추지 않고, 이 간격 안에서 담배를 주고받아야 합니다.
결론부터 말씀드리면, 설계상 가능합니다.
다만 맞춰야 할 것은 영 점 영영오 초가 아니라, 넘김 위상 오차 영 점 일에서 영 점 이오 밀리초입니다.
홈 스무 개 드럼이면 초당 삼천육백 도, 영 점 일 밀리초는 영 점 삼육 도입니다.
저희는 이 영 점 일 밀리초를 오차 예산으로 나눠 씁니다.
드라이브 간 시계 차이 일 마이크로초 아래, 이십 비트 엔코더 영 점 일 마이크로초, 감속기 백래시 오에서 삼십이 마이크로초.
남는 약 팔십 마이크로초를 서보 추종 오차와 축 비틀림에 배정합니다.
첫째, 드럼과 칼을 가상 마스터 축에 전자 기어와 캠으로 묶습니다.
속도 동기가 아니라 위치 동기이므로, 시간 오차가 누적되지 않습니다.
둘째, 이더캣 분산 클럭이나 서코스 쓰리로 드라이브 시계를 일 마이크로초 아래로 맞춥니다.
위치 루프와 보간은 드라이브 안에서 돌기 때문에, 버스 주기 일 밀리초에서도 정밀도가 유지됩니다.
셋째, 통신과 드라이브의 고정 지연을 측정해, 속도에 비례한 위상 선행으로 보상합니다.
저속에서 고속까지 넘김 각도가 같게 유지됩니다.
넷째, 백래시입니다. 직결 또는 일 아크분급 감속기로 기계 유격을 줄이고,
드럼 축 이차 엔코더로 위치 루프를 닫는 이중 루프로, 남은 유격과 비틀림을 제어합니다.
다섯째, 속도와 가속도 피드포워드, 고강성 커플링으로 추종 오차를 줄입니다.
플랫폼은 두 안입니다. 베코프 에이엑스 팔천은 드럼 축 이차 엔코더를 드라이브 루프에 바로 쓸 수 있고, 슈나이더 팩드라이브 쓰리는 포장기계용 동기 라이브러리가 강점입니다.
실기 적용 전에, 두 안을 시험 장치에서 같은 기준으로 먼저 검증합니다.
인접 드럼의 부하측 엔코더 값을 같은 클럭 순간에 래치해, 목표 속도에서 몇 시간 동안 기록합니다.
합격 기준은 각도 차의 최댓값과 삼 시그마가 영 점 삼육 도 이내입니다.
넘김 지점은 초당 만 프레임 이상 고속 카메라로 함께 확인합니다.
진행은 도면 검토, 드럼별 오차 예산, 시험 장치 검증, 실기 적용 순입니다.
제품 간격 영 점 영영오 초, 위상 오차 영 점 일 밀리초. 숫자로 검증하고 시작하겠습니다.
```

- 차분하고 신뢰감 있는 설명형 목소리를 고릅니다. 공개용보다 조금 느려도 됩니다.
- "팩드라이브 쓰리", "삼 시그마", "피드포워드"를 이상하게 읽으면 그 줄만 다시 만듭니다.

## 플로우 프롬프트 (16장, 한 줄에 한 장, 나노바나나 2, 9:16, 1장, 생성 전 확인 안 함)

```
A detailed model of a high-speed cigarette machine drum section with interlocking steel drums of different diameters, standing on an engineering desk covered with blueprints, a chrome stopwatch beside it with its hand glowing red. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
Extreme close-up of two adjacent rotating drums meeting tangentially, a single plain white rod suspended mid-transfer between their grooves, the tiny gap at the transfer point outlined in red. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
A transparent horizontal glass bar divided into five segments of very different lengths, the longest segment glowing red, floating over a dark engineering workspace. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
A translucent glowing virtual shaft floating above a cigarette machine's drum section, thin red lines linking it down to each drum and to a rotary knife. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
Row of compact servo drives in an open control cabinet joined by one glowing daisy-chained network cable, small floating clock faces above each drive all perfectly aligned, a red pulse traveling along the cable. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
Cutaway view of a servo drive showing a small glowing red control loop circling inside the drive housing, a slower white pulse arriving from the network cable. Vertical 9:16, clean 3D engineering-explainer render, soft light, slightly desaturated colors, no text, no logos, no license plates, no faces. Only accent color glowing red.
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
| 01 | 1~2 | 요청 조건: 제품 간격 5ms · 12,000개비/분 |
| 02 | 3~5 | 결론: 설계상 가능 · 위상 오차 0.1~0.25ms = 0.36~0.9° (홈 20개) |
| 03 | 6~8 | 오차 예산 막대(100µs): 시계 <1 · 엔코더 0.1 · 유격 5~32 · 추종+비틀림 ≈80 |
| 04 | 9~10 | ① 가상 기준 축 · 위치 동기(전자 기어·캠) |
| 05 | 11 | ② EtherCAT DC / Sercos III · 시계 차이 < 1µs |
| 06 | 12 | 위치 루프·보간은 드라이브 안 · 버스 1ms OK |
| 07 | 13~14 | ③ 지연 보상: 위상 선행 = 속도 × 지연 |
| 08 | 15 | ④ 백래시: 직결 또는 ≤1 arcmin 감속기 |
| 09 | 16 | 드럼 축 2차 엔코더 · 이중 루프 |
| 10 | 17 | ⑤ 속도·가속도 피드포워드 · 강성 커플링 |
| 11 | 18 | A안 베코프 AX8000 (2차 엔코더 드라이브 루프) / B안 PacDrive 3 (동기 라이브러리) |
| 12 | 19 | 두 안을 시험 장치에서 같은 기준으로 검증 |
| 13 | 20~21 | 부하측 엔코더 동시 래치 · 합격: 최댓값·3σ ≤ 0.36° |
| 14 | 22 | 고속 카메라 ≥10,000fps (1프레임 = 0.1ms) |
| 15 | 23 | 도면 검토 → 드럼별 오차 예산 → 시험 장치 검증 → 실기 적용 |
| 16 | 24 | 5ms · 0.1ms → 끝 카드 |

- 3번 장면의 오차 예산 막대는 합성에서 그래픽으로 그립니다(플로우 이미지는 배경).

## 끝 카드 (4.5초, 자막 없음)

- 드럼 동기 제어 시스템 / 제안
- 목표 제품 간격 5ms (1분 1만 2천 개비)
- 넘김 허용 오차 0.1~0.25ms 설계
- 시험 장치로 목표 속도에서 먼저 증명
- (주)동인엔시스 · 051-862-3668 · dongin@donginmne.com

## 전달 문안 (메일·메신저)

> 요청 주신 드럼 동기 제어 시스템에 대한 제안 영상(약 1분 30초)과 제안서를 보내 드립니다. 제품 간격 5ms에서 넘김 오차를 0.1~0.25ms 안으로 맞추는 방법과 오차 예산, 백래시 대책, 시험 장치로 먼저 증명하는 순서를 담았습니다. 검토 후 편하신 시간에 기술 미팅을 요청드립니다.

## 커버

| 항목 | 내용 |
|---|---|
| 머리표 | TECHNICAL PROPOSAL |
| 큰 제목 | 제품 간격 / [5ms] / 이렇게 맞춥니다 |
| 아래 문구 | 드럼 동기 제어 시스템 기술 제안 |
| 배경 그림 | 23 (가상 마스터 축 그림), 회사 로고 넣음 |

합성 폴더의 `cover.json` 예: `{"kick": "TECHNICAL PROPOSAL", "title": "제품 간격|[5ms]|이렇게 맞춥니다", "sub": "드럼 동기 제어 시스템 기술 제안"}`. `[ ]`는 노란 글자, `|`는 줄바꿈.

