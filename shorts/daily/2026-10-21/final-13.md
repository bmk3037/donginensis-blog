# 13. 담배 하나에 0.006초, 이 기계는 박자를 어떻게 맞출까 — 최종 내레이션·프롬프트 (붙여넣기용)

타입캐스트는 속도 1.0, mp3와 srt를 함께 받습니다. 플로우는 설정(생성 전 확인 안 함, 9:16, 1장, 나노바나나 2) 후 **한 줄씩** 넣고 번호대로 저장합니다. 흡연 장면, 상표, 담뱃갑, 글자가 나온 그림은 다시 만듭니다. 공개용과 고객 제안용은 같은 음성·이미지로 만들고, 합성할 때 화면 글자와 끝 카드만 바꿉니다.

## 타입캐스트

```
여기 담배 하나에 영 점 영영육 초밖에 주지 않는 기계가 있습니다.
바로 일 분에 만 개비를 만드는, 여러분이 길에서 보는 담배의 제조기죠.
크기가 다른 드럼들이 이 박자로 담배를 주고받는데, 대체 어떻게 한 번도 놓치지 않을까요?
드럼은 홈에 담배를 진공으로 붙여 돌다가, 넘기는 순간 다음 드럼에 건넵니다.
이때 허용되는 어긋남은 영 점 영영육 초가 아니라, 그보다 수십 배 작은 순간이어야 하죠.
그런데 속도가 빨라질수록, 옛날 방식으로는 이 박자를 맞추기 어려워집니다.
예전엔 모터 하나에 기어를 줄줄이 물렸는데, 기어마다 생기는 작은 유격이 쌓이거든요.
드럼마다 모터를 달아도, 각자 속도로만 돌면 차이가 쌓여 어긋나고요.
그래서 답은 박자를 하나로 만드는 겁니다.
보이지 않는 기준 축 하나를 두고, 모든 드럼과 칼이 그 위치를 따라가게 하죠.
드라이브끼리는 백만분의 일 초 단위로 시계를 맞추고, 늦게 닿는 신호는 미리 당겨 줍니다.
남은 유격은 드럼에 직접 단 엔코더로 재서, 그 자리에서 바로잡고요.
자, 여기서 진짜 문제입니다.
박자를 완벽하게 맞춰도, 기계는 매일 조금씩 지칩니다.
감속기가 닳아 유격이 커지고, 모터가 뜨거워지고, 담배 가루가 진공 팬을 막습니다.
그런데 돌리기만 하는 제어반은, 박자가 흔들리기 시작했다는 걸 말해 주지 않습니다.
그래서 필요한 게 지능형 제어반입니다.
축마다 기준과 얼마나 어긋났는지, 유격이 얼마나 커졌는지 쉬지 않고 기록하죠.
숫자가 기준을 넘으면 먼저 알리고, 그 기록은 멀리 있는 담당자 화면까지 이어집니다.
영 점 영영육 초의 박자를 맞추는 것과, 그 박자가 흔들리는 순간을 숫자로 보는 것.
설비를 제어하고 데이터를 연결해야, 멈추기 전에 손쓸 수 있습니다.
지금 이 순간에도 어느 공장에선, 영 점 영영육 초마다 담배 하나가 드럼을 건너가고 있습니다.
```

## 플로우

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
