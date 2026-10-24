# 숨은 설비 도감 캐릭터 (2026-10-24 대표이사 결정)

대표이사(10/24): "숨은 설비 도감도 캐릭터가 스토리, 공유와 댓글, 회사 문구는 없이 진행한다."

## 주인공: 도감이 (캐릭터 시트 v1, 10/24 대표이사가 플로우로 만듦)

시트: `shorts/assets/character/dogam_sheet_v1.png` (앞·옆·뒤·손 흔들기 + 표정 6개). **모든 장면 그림에 이 시트를 참고 이미지로 붙입니다.**

| 항목 | 내용 |
|---|---|
| 정체 | 숨은 설비를 찾아다니는 현장 엔지니어. 매 편 "순찰"을 가서 평소 못 보는 곳의 설비를 만난다 |
| 생김새 | 3D 만화풍(2.5등신), 파란 안전모(턱끈), 짧은 검은 머리, 큰 갈색 눈, 파란 작업 점퍼에 은색 반사띠, 남색 카고바지, 검은 장갑·작업화, 손에 검은 견고한 태블릿 |
| 소품의 뜻 | 태블릿 = 설비 데이터를 보는 화면. 설비 상태를 확인하는 장면에 씀 |
| 성격 | 호기심 많고 잘 놀람. 설비를 친구처럼 대함. 아는 척하지 않고 같이 알아냄 |
| 말투 | 존댓말 1인칭: "여러분, 저 지금 바다 밑 48m에 왔어요!", "어, 이게 왜 이래요?" |
| 목소리 | 타입캐스트 밝고 또렷한 목소리 하나로 고정(모든 편 같게) |
| 금지 | 실사 사람 얼굴(만화풍만), 안전모·옷에 회사 이름·로고·글자, 실존 인물 |

장면 프롬프트에 넣을 고정 문장:
```
the cute chibi 3D field engineer Dogam from the reference character sheet (royal-blue hard hat with chin strap, short black hair, big brown eyes, royal-blue work jacket with silver reflective stripes, navy cargo pants, black gloves and boots, holding a rugged black tablet), same face and proportions as the sheet
```

**그림 스타일:** 도감이가 만화풍이라, 배경도 같은 "Pixar-like 3D animation" 세계로 맞춥니다(사실적인 시네마틱 3D와 섞으면 따로 놀아 보임). 밝고 색이 많은 세계라 32편에서 지적된 "짙은 청록 한 색" 문제도 같이 풀립니다.

## 설비 캐릭터 (편마다)

- 그 편의 주인공 설비에 아주 단순한 얼굴을 준다: 계기판 바늘이 눈썹처럼 움직이거나, 표시등 두 개가 눈. 입은 없거나 작은 틈.
- 설비는 자기 이야기를 짧게 말하기도 한다(1~2문장, 다른 목소리). 예: 펌프 "저 하루 24시간 돌아요."
- 설비의 고생·위기가 이야기의 중심. "아무도 내가 지쳐 가는 걸 몰라요"가 자주 나오는 감정선.

## 이야기 뼈대 (캐릭터판 6비트)

| 비트 | 시간 | 할 일 |
|---|---|---|
| 1. 도착(훅) | 0–3초 | 도감이가 말이 안 되는 장면 앞에 이미 와 있음. 첫 문장은 도감이의 놀람 + 보는 사람의 관심사(20자 안팎). 첫 장면은 움직이는 클립 |
| 2. 궁금증 | 3–12초 | "대체 ~일까요?" 도감이가 묻고, 보는 사람도 같이 궁금해짐 |
| 3. 만남 | 12–35초 | 그 일을 해내는 설비를 만남. 원리를 도감이가 직접 보고 알아냄(숫자·출처 규칙 그대로) |
| 4. 위기 | 35–55초 | 설비가 지치거나 멈출 뻔한 순간. 도감이가 놀람. 무엇이 문제인지 보여 줌 |
| 5. 반전·해결 | 55–80초 | 문제를 푸는 방법(발상 전환). 설비가 다시 살아나거나 고마워함 |
| 6. 공유 + 댓글 | 80–95초 | 공유 한 문장("배 타는 친구한테 보내 주세요") + **댓글 질문 한 문장**("다음엔 도감이가 어디로 순찰 갈까요? 댓글로 알려 주세요"). 마지막 장면은 첫 장면으로 이어지게 |

- 매 편 끝에 같은 말("다음엔 어디로 순찰 갈까요?")로 댓글을 부르고, 실제 댓글이 생기면 다음 편 첫머리나 끝에 그 댓글을 띄워 "댓글 주제로 왔다"를 보여 준다(지식컷 방식). **없는 댓글은 지어내지 않는다.**
- 설명란에도 공유 대상 한 줄과 댓글 질문 한 줄을 넣는다.
- **회사 문구 없음:** 영상에도 설명란에도 회사 이름·슬로건("설비를 제어하고, 데이터를 연결하다. ㈜동인엔시스")을 넣지 않는다. 설명란 끝은 "※ 영상의 그림은 AI로 만든 이미지입니다."로 끝낸다.

## (처음 제안했던 로봇 시트 프롬프트, 쓰지 않음)

```
Character sheet of a small cute inspection robot mascot named Dogam: a short round body in bright orange with soft rounded edges, a round dark glass screen head showing two large expressive glowing white LED eyes (no mouth, no human face), a short antenna on top ending in a small red flashlight, one rubber wheel at the bottom and two short jointed arms with simple gripper hands, a tiny analog gauge on its chest. Shown four times on one sheet: front view, side view, back view, and a three-quarter view waving. Below, a row of six head close-ups with different LED eye expressions: curious, surprised, worried, happy, determined, sleepy. Pixar-like 3D animation style, soft studio lighting, plain light grey background, consistent proportions and colors in every view. No text, no letters, no numbers, no logos.
```

대표이사가 사람 엔지니어 캐릭터로 만들어 위 시트 v1로 확정했습니다.
