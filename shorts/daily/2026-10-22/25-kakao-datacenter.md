# 25. 구글도 카카오도 멈췄다: 데이터센터를 멈춘 전원

- 분류: 사건 이야기 E3(조회수용, 벤치마크 @2tan_saeng 방식). 2026-10-22 대표이사 선택("카카오톡 멈춘 주말", 그림은 건축 모형).
- 제목 후보: ① 구글도 카카오도, 멈춘 이유는 전원이었다 ② 카톡이 닷새 동안 못 돌아온 진짜 이유 ③ 은행 앱을 멈춘 데이터센터의 전기
- **지금 뜨거운 뉴스로 훅(10/22 대표이사 "확실한 후킹, 핫한 주제")**: 이틀 전(2026-10-20) 구글 클라우드 런던 구역이 '전원 문제'로 멈춰 영국 은행 앱과 카드 결제가 멈춤 → 우리가 겪은 카카오톡(2022)으로 이어 감. 뉴스가 식기 전에 **가능한 한 빨리 올림**(일정 당김).
- **벤치마크 적용:** "~요" 말투, "처음부터 보죠" 시간순, 진짜 문제(구조·이중화), 결과, 반전(감시 시스템은 있었다), 마지막에 제목 문장.
- 그림: 건축 모형판(9·15, 포스코 편과 같은 세계). **벤치마크 비교(10/22) 반영:** 모형이 화면 끝까지(받침·책상·벽 없음), 차분한 낮 햇빛과 초록·파랑, 빨간 정보는 그림 속 3D 표시(점선 화살표, ✕, 핀). 클립 8개(Lite, 약 80크레딧, 매일 받는 크레딧으로). 앞뒤 그림 쌍 4개(00, 01, 04, 08).
- 합성: 클립 장면은 길게(6~8초), 큰 글자는 3번 이하(진짜 문제, 127시간 33분, 끝 제목). 첫 화면은 커버 카드 대신 첫 장면 위에 제목 한 줄.
- 회사 간 책임 공방(SK C&C ↔ 카카오)은 다루지 않음. 정부 조사 결과와 보도된 사실만 씀. 우리 제어반이 이 사고를 막았을 거라는 말은 하지 않음.

## 대본

| 비트 | 내레이션 |
|---|---|
| 1. 훅 | 2026년 10월 20일 아침, 영국에서 카드 결제와 은행 앱이 한꺼번에 멈췄어요. |
|  | 구글은 데이터센터 한 구역의 '전원 문제' 때문이라고 밝혔죠. |
|  | 그런데 우리도 똑같은 일을 겪었어요. 2022년 10월 15일, 카카오톡이 멈춘 주말이죠. |
|  | 그날 불은 밤에 꺼졌는데, 왜 완전한 복구엔 닷새가 넘게 걸렸을까요? |
| 2. 처음부터 | 처음부터 보죠. |
|  | 오후 3시 19분, 데이터센터 지하 3층 배터리실에서 불이 납니다. |
|  | 정전이 나도 서버를 지키려고 둔, 무정전 전원장치용 리튬이온 배터리였죠. |
|  | CCTV에는 불이 나기 직전, 배터리에서 튄 스파크가 찍혀 있었어요. |
|  | 자동소화설비가 가스를 뿜었지만, 리튬이온 배터리 불은 가스로 잘 꺼지지 않아요. |
|  | 결국 소방당국은 물을 쓰려고, 오후 4시 52분쯤 전체 전력 차단을 요청합니다. |
| 3. 진짜 문제 | 그런데 진짜 문제는 따로 있었어요. |
|  | 배터리실과 전원장치 사이는, 천장이 트인 벽으로만 나뉘어 있었거든요. |
|  | 불의 열기에 전원장치가 멈췄고, 배터리실 위를 지나던 전력선까지 망가졌죠. |
|  | 정부 조사에선 카카오의 서버 이중화가 미흡했다는 지적도 나왔어요. |
| 4. 결과 | 불은 밤 11시 45분에 꺼졌지만, 카카오가 정상화된 건 20일 밤 11시였어요. |
|  | 장애 복구에만 127시간 33분이 걸렸죠. |
| 5. 반전·제어반 | 놀라운 건, 이 배터리를 지켜보는 감시 시스템이 있었다는 거예요. |
|  | 하지만 불이 나기 직전까지, 이상 징후는 나타나지 않았어요. |
|  | 그래서 화재 뒤 조사에선, 그 배터리의 기록 데이터가 주목받았죠. |
|  | 지능형 제어반도 설비의 전류와 전압, 온도를 쉬지 않고 모아 기록해요. |
|  | 기준을 넘으면 먼저 알리고, 무슨 일이 있었는지 거슬러 볼 수 있게 남겨 두죠. |
| 6. 마무리 | 설비를 움직이는 것과, 그 기록을 남기는 것. 둘 다 있어야 하는 이유예요. |
|  | 런던의 은행 앱도, 판교의 카카오톡도, 멈춘 이유는 결국 전원이었습니다. |

23문장, 공백 제외 668자. 1.13배속에서 약 98~100초.

## 사실 확인

| 숫자·표현 | 출처 | 원문 표현 |
|---|---|---|
| 2026-10-20 아침 영국 런던 구글 클라우드 장애, 은행 앱·카드 결제 멈춤 | [The Register 2026-10-20](https://www.theregister.com/paas-and-iaas/2026/10/20/google-cloud-says-a-power-event-caused-todays-outage/5304160), [ABC News 2026-10-20](https://www.abc.net.au/news/2026-10-20/google-cloud-failure-europe-banks/107290238), [technology.org 2026-10-21](https://www.technology.org/2026/10/21/google-cloud-london-outage-revolut-uk-banks-power-event/) | 구글 상태 페이지: 시작 10/19 23:08 PDT = 런던 10/20 07:08 / ABC 제목 "European banks, websites hit as Google Cloud data centre goes offline for hours" / 은행 앱의 카드 결제·송금 장애 |
| 구글: 한 구역의 '전원 문제' | 같은 기사(구글 상태 페이지 인용) | "Due to a power event we had suffered an outage within europe-west2-b zone. The power event is mitigated." |
| 10월 15일 오후 3시 19분, 지하 3층 배터리실, 밤 11시 45분 진화 | [데일리안 2022-12-06](https://www.dailian.co.kr/news/view/1180889/), [뉴스토마토 2022-12-06](https://newstomato.com/ReadNews.aspx?no=1164795) | "지난 10월 15일 오후 3시 19분 SK C&C 판교 데이터센터 지하 3층 배터리실에 화재가 발생해 같은 날 오후 11시 45분에 완전히 진화됐으며" (일부 보도는 3시 33분) |
| 2022년 10월 15일은 토요일 | 달력 | |
| 무정전 전원장치(UPS)용 리튬이온 배터리 | [아이뉴스24 2022-12-06](https://www.inews24.com/view/1545987), 데일리안 | "리튬이온 배터리가 일부 무정전 전원 장치(UPS)와 물리적으로 완벽히 분리되지 않은 공간" |
| CCTV에 스파크 | [데일리안 2022-10-23](https://www.dailian.co.kr/news/view/1164999/) | "CCTV 영상에는 화재 직전 배터리에서 스파크가 일어난 뒤 불이 시작되고, 자동소화설비가 정상 작동해 할로겐 가스가 분사되는 장면이 담겼다." |
| 가스로 잘 안 꺼짐 | [데일리안 2022-12-06](https://www.dailian.co.kr/news/view/1180889/) | "가스 소화 장비가 작동했지만 가스 소화가 어려운 리튬이온 배터리 화재 특성 상 초기 진압에 한계가 있었다" |
| 물을 쓰려고 오후 4시 52분쯤 전체 전력 차단 요청 | [뉴시스 2022-10-18](https://mobile.newsis.com/view/NISX20221018_0002052323) | "소방당국은 물을 쓸 수밖에 없다는 판단 하에 오후 4시52분께 전체 전력 차단을 요청했다." |
| 천장이 트인 벽, 열기로 UPS 멈춤, 배터리실 위 전력선 손상 | [뉴스토마토](https://newstomato.com/ReadNews.aspx?no=1164795), [데일리안 2022-12-06](https://www.dailian.co.kr/news/view/1180889/) | "배터리실이 일부 UPS와 천장 공간이 미분리된 격벽으로만 나눠져 있어 화재 열기 등으로 UPS 작동이 중지됐다." / "전력선이 포설된 전기설비가 배터리실 위에 위치해 있어 화재로 인해 전력선이 손상됐고" |
| 정부: 카카오 서버 이중화 미흡 | [데일리안 2022-12-06](https://www.dailian.co.kr/news/view/1180889/) | "주요 원인은 '화재에 취약한 데이터센터 구조'와 '카카오의 서버 이중화 미흡'" |
| 20일 밤 11시 정상화, 127시간 33분 | [아이뉴스24 2022-12-06](https://www.inews24.com/view/1545987) | "카카오는 20일 오후 11시 서비스가 정상화 됐으며, 장애 복구에 총 127시간 33분이 소요됐다." |
| 감시 시스템(BMS)은 있었지만 이상 징후 없음 | 같은 기사, 데일리안 2022-12-06 | "배터리 온도 등을 모니터링하는 시스템(BMS)을 갖추고 있었으나, 화재 발생 직전까지 화재에 대한 이상징후가 나타난 바는 없었던 것으로 나타났다." |
| 배터리 기록 데이터가 주목받음 | [데일리안 2022-10-23](https://www.dailian.co.kr/news/view/1164999/) | 제목 "'카카오 먹통' 판교 데이터센터 화재 전 '배터리관리시스템 데이터' 주목" |

참고(대본에는 안 씀): 2023년 국과수 감정에서 "배터리 셀 내부 경년열화에 따른 절연파괴로 발생한 단락"이 발화 원인으로 작용했을 가능성([아이뉴스24 2023-03-30](https://www.inews24.com/view/1580504)). 지능형 제어반 설명은 `knowledge/company.md` 안에서만 씀.

## 검수 기록

| 번호 | 걸린 것 | 고친 것 |
|---|---|---|
| 1 | "카카오톡 이용자 4750만" — 원문 확인 못 함 | 넣지 않음 |
| 2 | "택시·송금이 안 됐다" — 이번에 원문 확인 못 함 | "카카오의 다른 서비스들도 줄줄이" |
| 3 | 카톡 메시지 복구 시각(16일 새벽) — 관련 기사 미리보기에만 있음 | 넣지 않음 |
| 4 | 화재 시각 3시 19분 / 3시 33분 보도 차이 | 정부 발표와 같은 3시 19분 |
| 5 | 발화 원인(배터리 결함 여부)은 책임 공방 중이었음 | "배터리에서 튄 스파크"(CCTV)까지만. 누구 잘못인지 말하지 않음 |
| 7 | 구글 장애의 '비상 발전기가 안 켜졌다'는 한 매체만 보도 | 넣지 않음. 구글이 밝힌 '전원 문제'까지만 |
| 8 | 은행 이름(레볼루트 등) | 넣지 않음. "영국 은행 앱과 카드 결제" |
| 9 | "이번 주"는 올리는 날에 따라 틀려짐 | 날짜로 "2026년 10월 20일 아침" |
| 6 | "감시가 있었는데도 못 막았다"가 우리 제품 홍보와 부딪힘 | 막는다고 하지 않고 "기록을 남겨 거슬러 본다"로 이음(기록하고, 기준을 넘으면 먼저 알린다) |

## 타입캐스트 대본 (속도 1.0, mp3)

```
이천이십육 년 시월 이십일 아침, 영국에서 카드 결제와 은행 앱이 한꺼번에 멈췄어요.
구글은 데이터센터 한 구역의 전원 문제 때문이라고 밝혔죠.
그런데 우리도 똑같은 일을 겪었어요. 이천이십이 년 시월 십오일, 카카오톡이 멈춘 주말이죠.
그날 불은 밤에 꺼졌는데, 왜 완전한 복구엔 닷새가 넘게 걸렸을까요?
처음부터 보죠.
오후 세 시 십구 분, 데이터센터 지하 삼 층 배터리실에서 불이 납니다.
정전이 나도 서버를 지키려고 둔, 무정전 전원장치용 리튬이온 배터리였죠.
씨씨티비에는 불이 나기 직전, 배터리에서 튄 스파크가 찍혀 있었어요.
자동소화설비가 가스를 뿜었지만, 리튬이온 배터리 불은 가스로 잘 꺼지지 않아요.
결국 소방당국은 물을 쓰려고, 오후 네 시 오십이 분쯤 전체 전력 차단을 요청합니다.
그런데 진짜 문제는 따로 있었어요.
배터리실과 전원장치 사이는, 천장이 트인 벽으로만 나뉘어 있었거든요.
불의 열기에 전원장치가 멈췄고, 배터리실 위를 지나던 전력선까지 망가졌죠.
정부 조사에선 카카오의 서버 이중화가 미흡했다는 지적도 나왔어요.
불은 밤 열한 시 사십오 분에 꺼졌지만, 카카오가 정상화된 건 이십일 밤 열한 시였어요.
장애 복구에만 백이십칠 시간 삼십삼 분이 걸렸죠.
놀라운 건, 이 배터리를 지켜보는 감시 시스템이 있었다는 거예요.
하지만 불이 나기 직전까지, 이상 징후는 나타나지 않았어요.
그래서 화재 뒤 조사에선, 그 배터리의 기록 데이터가 주목받았죠.
지능형 제어반도 설비의 전류와 전압, 온도를 쉬지 않고 모아 기록해요.
기준을 넘으면 먼저 알리고, 무슨 일이 있었는지 거슬러 볼 수 있게 남겨 두죠.
설비를 움직이는 것과, 그 기록을 남기는 것. 둘 다 있어야 하는 이유예요.
런던의 은행 앱도, 판교의 카카오톡도, 멈춘 이유는 결국 전원이었습니다.
```

강조하면 좋은 곳: 4번 "왜 닷새 넘게", 8번 "스파크", 11번 "진짜 문제", 16번 "127시간 33분", 17번 "감시 시스템이 있었다"

## 플로우 프롬프트: 건축 모형판 (24장)

- 모든 줄에 같은 스타일 문장이 들어 있어 한 세계로 보입니다.
- **만드는 순서 (꼭 지켜 주세요)**
  1. **00A를 맨 먼저** 만듭니다. 이 그림이 영상 전체의 톤 기준입니다.
  2. 나머지 그림은 만들 때마다 **00A를 참고 이미지(스타일 참고)로 붙여** 색과 질감을 맞춥니다.
  3. **B 그림은 새로 만들지 말고, 짝인 A 그림을 참고 이미지로 붙인 뒤 "편집"으로** 만듭니다. B 줄 맨 앞 [ ]에 어떤 그림을 붙일지 적어 두었습니다. 구도가 그대로여야 합성에서 같은 화면 안에서 바뀌는 효과를 쓸 수 있습니다.
  4. 편집 결과는 레이어로 쌓이니 **A와 B를 따로따로 내려받아** 주세요.
- 그림 안에 글자·숫자는 넣지 않습니다.

```
00A | A street corner in a London-like city model on a weekday morning: red double-decker bus, a small cafe and a bank branch, tiny white figures paying with cards at shop counters and using phones. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
00B | [00A 그림을 참고 이미지로 붙이고 편집] Edit the reference image (00A). Keep exactly the same camera angle, framing, composition, buildings, objects and figures as the reference image; do not move or redraw anything else. Change only this: the card terminals and phone screens are dark, small red 3D X markers float above the counters, the tiny figures stand waiting, puzzled. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
00C | Cutaway of a large data center campus model with three identical halls side by side; the middle hall is completely dark while the other two are lit, a small red 3D lightning-bolt marker above the dark hall. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
01A | A city plaza model on a Saturday afternoon: many tiny white figures walking and sitting, most of them holding tiny phones whose screens glow softly, cafes and trees around. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
01B | [01A 그림을 참고 이미지로 붙이고 편집] Edit the reference image (01A). Keep exactly the same camera angle, framing, composition, buildings, objects and figures as the reference image; do not move or redraw anything else. Change only this: now every tiny phone screen is dark, the figures have stopped and look at their phones or at each other, puzzled. A few small red 3D X markers float above the crowd. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
02 | A street corner model: a row of tiny taxis waiting, tiny white figures holding up phones, a small shop with a card terminal, everyone paused and confused. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
03 | A modern office district model with glass-and-white towers; in the center a large windowless white cube building (a data center), shown as a cutaway so its three basement levels are visible below the ground. A red 3D map pin stands on top of the building, and a red dashed line runs down to the deepest basement room. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
04A | Cutaway of the deepest basement room of the data center model: neat rows of tall white battery rack cabinets, cable trays overhead, calm and orderly, nobody inside. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
04B | [04A 그림을 참고 이미지로 붙이고 편집] Edit the reference image (04A). Keep exactly the same camera angle, framing, composition, buildings, objects and figures as the reference image; do not move or redraw anything else. Change only this: one battery rack in the middle now glowing red from inside with a small flame and grey smoke rising to the ceiling. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
05 | High-angle close-up, like a security camera view, of one white battery rack in the model with a single tiny bright red spark jumping from it. A small red 3D circle outline marks the spot on the floor. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
06 | The battery room model filled with a white cloud of extinguishing gas from ceiling nozzles, the red glow of the burning rack still visible through the cloud. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
07 | Street-level model at the data center entrance: a red fire truck, tiny white firefighter figures pulling hoses down a ramp toward the basement, late afternoon. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
08A | A huge server hall model inside the data center: long rows of white server racks with tiny lights, cool and orderly. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
08B | [08A 그림을 참고 이미지로 붙이고 편집] Edit the reference image (08A). Keep exactly the same camera angle, framing, composition, buildings, objects and figures as the reference image; do not move or redraw anything else. Change only this: every server light is off, the hall is dark and silent. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
09 | Cutaway of two adjoining basement rooms in the model: on the left the battery room with a glowing red rack, on the right a room with large power units (UPS cabinets); the wall between them stops short of the ceiling, leaving an open gap, and red heat haze flows over the top of the wall into the power room. A red 3D dashed arrow arcs over the wall through the gap. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
10 | Close-up of cable trays running along the ceiling above the battery room in the model, the thick power cables scorched and glowing red in one section. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
11 | Two data center buildings in the city model far apart: the near one is packed with server racks and is dark, the far one is almost empty with only a few racks lit. A red dashed line on the ground connects the two buildings. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
12 | The data center model at night, the fire out, a thin trail of smoke, tiny firefighters rolling up hoses, the building dark. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
13 | Inside the server hall model at night, tiny white engineer figures with laptops working beside the racks, some racks lit again, others still dark, long night of repair. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
14 | A small security office model with a monitor showing a calm flat line graph (no text), a tiny white figure watching, nothing unusual on the screen. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
15 | Tiny white investigator figures in the burned battery room model examining a blackened rack, one holding a laptop connected to it by a red cable. A small red 3D document icon floats above the laptop. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
16 | A factory model interior: a large electric motor driving machinery on a clean floor, a grey control panel cabinet beside it with its door open, small sensors and thin red wires running to the motor. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
17 | A small office desk model with a monitor showing simple line graphs and one small red alert light, the city visible through the window. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
18 | The city plaza model at dusk, tiny white figures holding phones whose screens glow again, the data center cube lit in the distance, calm. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
```

## 클립 8개 (플로우 → 프레임 투 비디오, 9:16, 8초, 소리 없음, 모두 Veo 3.1 Lite, 약 80크레딧)

- **매일 받는 50크레딧으로 하루 4~5개씩, 이틀에 나눠 만들면** 월 1,000크레딧은 쓰지 않습니다.
- 그림을 먼저 만든 뒤, 그 그림을 시작 프레임으로 넣어 주세요. 파일 이름에 c01~c08을 붙여 주세요.
- 마음에 안 들어도 다시 돌리지 말고 그대로 보내 주세요. 쓸 만한 부분만 잘라 쓰고, 안 되면 정지 그림으로 대신합니다.
- 우선순위: 크레딧이 모자라면 c01(런던 훅), c02, c06, c05 순서로 먼저 만들어 주세요.

| 클립 | 시작 그림 | 들어갈 자리 |
|---|---|---|
| c01 | 00A | 훅: 런던 거리의 카드 결제기·휴대폰이 하나씩 꺼짐 |
| c02 | 04A | "오후 3시 19분, 불이 납니다" |
| c03 | 06 | "가스를 뿜었지만" |
| c04 | 07 | "물을 쓰려고" |
| c05 | 08A | "전체 전력 차단" (서버 불이 줄줄이 꺼짐) |
| c06 | 09 | 진짜 문제: 열기가 벽을 넘어감 |
| c07 | 13 | "127시간 33분" (밤샘 복구) |
| c08 | 18 | 마지막 장면: 휴대폰이 다시 켜짐 |

```
c01 | 시작 프레임 00A | Slow push along the London-like street model; one by one the card terminals and phone screens go dark, the tiny figures stop and look at their phones. Same architectural scale model look, tilt-shift focus and lighting as the start frame. No text, no logos, no camera shake, no camera cuts. Vertical 9:16.
c02 | 시작 프레임 04A | Slow push toward the middle battery rack; a tiny red spark flickers, then a red glow grows inside the rack and grey smoke starts rising to the ceiling. Same architectural scale model look and lighting as the start frame. No text, no logos, no camera cuts. Vertical 9:16.
c03 | 시작 프레임 06 | Static view, very slow push; the white extinguishing gas keeps billowing from the ceiling nozzles, but the red glow of the burning rack keeps flickering through the cloud. Same architectural scale model look and lighting as the start frame. No text, no logos, no camera cuts. Vertical 9:16.
c04 | 시작 프레임 07 | Slow drone glide toward the entrance; tiny firefighter figures run down the ramp pulling the hoses, the red truck's lights blinking. Same architectural scale model look and lighting as the start frame. No text, no logos, no camera cuts. Vertical 9:16.
c05 | 시작 프레임 08A | Slow push along the server hall; row by row, from the far end toward the camera, the tiny server lights switch off until the whole hall is dark. Same architectural scale model look and lighting as the start frame. No text, no logos, no camera cuts. Vertical 9:16.
c06 | 시작 프레임 09 | Slow sideways drift from the battery room to the power room; red heat haze rolls over the top of the dividing wall through the open gap and the power cabinets' small lights go out. Same architectural scale model look and lighting as the start frame. No text, no logos, no camera cuts. Vertical 9:16.
c07 | 시작 프레임 13 | Slow push along the server racks at night; tiny engineer figures type on laptops and the dark racks light up again one by one. Same architectural scale model look and lighting as the start frame. No text, no logos, no camera cuts. Vertical 9:16.
c08 | 시작 프레임 18 | Slow high drone glide over the plaza at dusk; the tiny phone screens light up again one after another, the data center glowing in the distance. Same architectural scale model look and lighting as the start frame. No text, no logos, no camera cuts. Vertical 9:16.
```

## 장면 배치표

| 문장 | 그림 | 장면 속 빨간 딱지·그래픽 |
|---|---|---|
| 1. 2026년 10월 20일 아침, 영국에서… | 00A (c01) → 00B | 빨간 달력 "2026.10.20", 딱지 "카드 결제 멈춤" |
| 2. 구글은 데이터센터 한 구역의 '전원 문제'… | 00C | 어두운 건물에 빨간 번개 표시, 딱지 "전원 문제" |
| 3. 그런데 우리도 똑같은 일을… 카카오톡이 멈춘 주말 | 01A → 01B | 빨간 달력 "2022.10.15 토", 휴대폰 위 빨간 ✕ |
| 4. 그날 불은 밤에 꺼졌는데… | 08B | 강조: 큰 글자 "왜 닷새나?" |
| 5. 처음부터 보죠. | 03 | 시계가 거꾸로 감 |
| 6. 오후 3시 19분… | 04A → 04B (c02) | 빨간 시계 "15:19" |
| 7. 정전이 나도 서버를 지키려고… | 04A | 딱지 "UPS용 리튬이온 배터리" |
| 8. CCTV에는 불이 나기 직전… | 05 | 강조: 번쩍임 + "스파크" |
| 9. 자동소화설비가 가스를 뿜었지만… | 06 (c03) | 딱지 "가스 소화", 빨간 ✕ |
| 10. 결국 소방당국은 물을 쓰려고… | 07 (c04) → 08A (c05) | 빨간 시계 "16:52", "전체 전력 차단" (서버 불이 꺼짐) |
| 11. 그런데 진짜 문제는… | 09 | 강조: 번쩍임 + "진짜 문제" |
| 12. 배터리실과 전원장치 사이는… | 09 (c06) | 벽 위 빈틈에 빨간 화살표 "천장이 트인 벽" |
| 13. 불의 열기에 전원장치가… | 10 | 딱지 "전원장치 정지", "전력선 손상" |
| 14. 정부 조사에선… | 11 | 딱지 "서버 이중화 미흡" |
| 15. 불은 밤 11시 45분에… | 12 → 13 | 빨간 시계 "23:45", 달력 "20일 23:00" |
| 16. 장애 복구에만 127시간 33분… | 13 (c07) | 강조: 큰 숫자 "127시간 33분" |
| 17. 놀라운 건… 감시 시스템이 있었다 | 14 | 딱지 "배터리 감시 시스템(BMS)" |
| 18. 하지만 불이 나기 직전까지… | 14 | 그래프 평평, "이상 징후 없음" |
| 19. 그래서 화재 뒤 조사에선… | 15 | 딱지 "기록 데이터" |
| 20. 지능형 제어반도… | 16 | 센서 옆 "전류 · 전압 · 온도" |
| 21. 기준을 넘으면 먼저 알리고… | 17 | 그래프가 기준선을 넘으며 빨간 "알림", "기록 보관" |
| 22. 설비를 움직이는 것과… | 16 | "설비 제어 + 기록" |
| 23. 런던의 은행 앱도, 판교의 카카오톡도… | 00A → 18 (c08) | 제목처럼 크게 "멈춘 이유는 전원" |

## 커버 (이전 편들과 같은 형식)

| 항목 | 내용 |
|---|---|
| 머리표 | 구글도, 카카오도 멈췄다 |
| 큰 제목 | 카톡을 / 멈춘 건 / [불꽃 하나] |
| 아래 문구 | 이번엔 런던 은행 앱까지? |
| 배경 그림 | 04B (불붙은 배터리실) 또는 01B |

## 설명란

```
2026년 10월 20일, 영국의 은행 앱과 카드 결제가 한꺼번에 멈췄습니다. 구글은 데이터센터 한 구역의 '전원 문제'라고 밝혔습니다.
우리도 겪은 일입니다. 2022년 10월 15일, 카카오톡이 멈춘 주말. 시작은 데이터센터 지하 배터리실의 불꽃 하나였고, 완전한 복구엔 127시간 33분이 걸렸습니다.

설비를 움직이는 것만큼, 설비의 기록을 남기는 것이 중요한 이유입니다.

여러분은 그 주말에 무엇을 하고 계셨나요?

설비를 제어하고, 데이터를 연결하다. ㈜동인엔시스
※ 영상의 그림은 AI로 만든 이미지입니다.

#구글먹통 #카카오톡 #카톡먹통 #데이터센터 #정전 #지능형제어반 #숨은설비도감
```

## 받은 클립 확인 (10/22, zip 18)

| 클립 | 파일 | 결과 |
|---|---|---|
| c01 | Figures_looking_at_phones_on | 0~3.5초 좋음(사람이 걷고 버스가 움직임). 3.5초부터 큰 검은 네모가 떠다녀서 앞부분만 쓰고 00B 그림으로 넘김 |
| c02 | Smoke_rising_from_battery_rack | 좋음(빨간 불빛이 커지고 연기) |
| c03 | Gas_billowing_from_ceiling_nozzles | 좋음(가스가 건물 위로 뿜어 나옴) |
| c04 | Firefighter_running_toward_entra… | 좋음(소방차와 소방관 움직임) |
| c05 | Server_lights_switching_off | 아주 좋음(단지 전체가 어두워짐) |
| c06 | Drift_from_battery_room | 아주 좋음(빨간 열기가 벽을 넘고 옆방이 꺼짐) |
| c07 | Engineers_activating_server_racks | 움직임 적음, 쓸 만함 |
| c08 | Drone_gliding_over_plaza | 좋음. 다만 오른쪽 아래에 "9:16" 글자가 찍힘 → 확대로 잘라 냄 |

모든 클립 오른쪽 아래의 ✦·"Veo" 표시는 합성에서 확대해 화면 밖으로 밀어냄. 클립 소리는 쓰지 않음.

## 다시 만들기 (10/22, 클립 확인 뒤)

설정: 출력 수 1, 모델 Veo 3.1 Lite, **비율은 설정에서 9:16**(프롬프트에 비율 글자 없음). 우선순위 순서.

| 순서 | 무엇 | 시작 그림(받은 파일 이름) | 왜 |
|---|---|---|---|
| 1 | 클립 c01 (훅) | `Red_bus_in_city_model` | 첫 3초가 가장 중요한데, 지난번엔 3.5초부터 검은 네모가 떠다님 |
| 2 | 클립 c07 | `Engineers_working_in_server_hall` (어두운 홀) | 지난번엔 거의 안 움직임 |
| 3 | 그림 01B (편집) | `Miniature_city_plaza_model_figures`를 참고 이미지로 붙이고 편집 | 지난번 01B는 구도가 달라 같은 화면 안 변화를 못 씀 |
| 4 (선택) | 클립 c08 | `City_plaza_model_at_dusk` | 지난번엔 "9:16" 글자와 너무 많은 불빛. 안 만들어도 확대로 씀 |

```
c01 | 시작 프레임 Red_bus_in_city_model | Slow gentle push toward the street corner. The tiny figures walk and the red bus drives slowly, then the warm glow inside the shop windows and the small lights on the shop counters go out one after another from left to right, and the figures stop walking and look around, puzzled. Keep the same architectural scale model look, colors and lighting as the start frame. Nothing new appears in the air. No on-screen text, no letters, no numbers, no logos, no camera cuts.
c07 | 시작 프레임 Engineers_working_in_server_hall | Slow push forward along the dark server hall. The ceiling lights of the hall switch back on section by section, from the far end toward the camera, until the whole hall is bright and the server racks glow softly again; the tiny engineer figures stay at their places. Keep the same architectural scale model look as the start frame. No on-screen text, no letters, no numbers, no logos, no camera cuts.
01B | [Miniature_city_plaza_model_figures 그림을 참고 이미지로 붙이고 편집] Edit the reference image (01A). Keep exactly the same camera angle, framing, composition, buildings, objects and figures as the reference image; do not move or redraw anything else. Change only this: the tiny figures have stopped walking and are looking down at the small phones in their hands or at each other, puzzled, and a few small red 3D X markers float just above the crowd. Highly detailed architectural scale model world made of white and warm beige materials with soft green trees and calm blue water, like a museum city model that fills the entire frame edge to edge (no table, no model base, no studio wall, no model edges visible), tilt-shift photography with shallow depth of field, soft natural daylight with gentle shadows, slightly muted natural colors, calm and clean. People are tiny plain white figures without faces. The only accent color is red, used for small 3D markers placed in the scene. Composition: the subject sits in the lower two-thirds and the upper third is calm for overlay graphics. Vertical 9:16. No text, no letters, no numbers, no logos, no faces.
c08 | 시작 프레임 City_plaza_model_at_dusk | Slow high drone glide over the plaza at dusk. The warm lights in the windows of the surrounding buildings and the data center cube turn on one after another, calm and quiet. Keep the same architectural scale model look as the start frame. No on-screen text, no letters, no numbers, no logos, no camera cuts.
```

## 합성 기록 (10/22)

- 클립 8개(c01·c07은 다시 만든 것), 그림 38장, mp3 112.9초 → `emphasis.py 1.14 3,7,10,15,16 3:0.25,10:0.4,15:0.35`, 문장 경계 `{"10":53.95}` 고정 → 98.2초, -14.6 LUFS.
- 벤치마크 반영: 첫 화면은 커버 카드 대신 첫 클립 위 제목 "구글도, 카카오도 / 멈췄다", 큰 글자 3번("진짜 문제", "127시간 33분", "멈춘 이유는 전원"), 클립 장면을 길게.
- 그림·클립 오른쪽 아래 ✦·"Veo" 표시와 c08의 "9:16" 글자는 잘라 냄(그림은 아래 8%, 클립은 10%·c08은 20%).
- v2: "127시간 33분" 강조 때 앞 문장 딱지가 겹쳐 숨김.
