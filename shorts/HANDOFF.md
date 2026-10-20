# 전기 숏츠 만들기: 처음 맡는 사람을 위한 안내

공장 전기·제어반 회사 채널에 올릴 "신비한 건축사전" 같은 전기 숏츠(95~100초)를 만드는 일입니다. 사람이 하는 일은 세 가지뿐입니다. **주제 고르기, 타입캐스트로 음성 만들기, 구글 플로우로 이미지 만들기.** 나머지(기획안, 사실 확인, 대본, 검수, 프롬프트, 영상 합성)는 Claude가 합니다.

## 1. 준비물

| 무엇 | 왜 | 비고 |
|---|---|---|
| Claude 계정(Pro 이상) | Claude Code(웹·앱)로 기획과 합성을 시킴 | claude.ai/code에서 씁니다 |
| GitHub 계정 | 대본·프롬프트·합성 도구가 저장소 `bmk3037/donginensis-blog`에 있음 | 저장소 주인이 Settings → Collaborators에서 초대해야 합니다. claude.ai의 GitHub 연결도 해 둡니다 |
| 타입캐스트 계정 | 내레이션 음성 | 회사 채널 업로드는 상업적 이용이라 유료 플랜이 필요합니다. 시험은 무료로 됩니다 |
| 구글 계정(플로우 사용 가능) | 장면 이미지 | 플로우(나노바나나 2). 영상 클립은 크레딧이 들어 쓰지 않습니다 |
| 구글 드라이브 | 이미지 zip을 Claude에게 넘길 때 | 공유: "링크가 있는 모든 사용자" |

## 2. 처음 한 번

1. claude.ai/code에서 저장소 `bmk3037/donginensis-blog`를 고르고 새 세션을 엽니다.
2. 아래 **붙여넣기 ①**을 그대로 보냅니다. Claude가 합성 도구를 깔고 시험 화면을 보여 준 뒤, 매일 아침 기획안이 오도록 예약 작업을 만듭니다.

## 3. 매일 하는 일

| 순서 | 누가 | 무엇 |
|---|---|---|
| 1 | Claude(자동) | 오전 7시 37분, 기획안 6개와 추천 3개를 휴대폰 알림으로 보냄 |
| 2 | 사람 | 알림을 눌러 그 대화창에 만들 3편 번호를 보냄(예: `1, 4, 5`). 직접 생각한 주제를 적어도 됨 |
| 3 | Claude | 3편의 대본을 확인·검수하고, 타입캐스트 대본과 플로우 프롬프트를 저장소에 올림 |
| 4 | 사람 | 타입캐스트로 음성(4장), 플로우로 이미지(5장)를 만듦 |
| 5 | 사람 | **붙여넣기 ②**와 함께 음성·이미지를 보냄 |
| 6 | Claude | 정지 화면 미리보기 → 확인 → 완성 영상(mp4)을 보냄 |

## 4. 타입캐스트

1. 대본 파일의 "타입캐스트 대본" 칸을 통째로 복사해 붙여 넣습니다. 한 줄에 한 문장이고 숫자는 한글로 적혀 있습니다.
2. 목소리는 채널에서 쓰던 목소리를 매번 똑같이 씁니다. 처음 정할 때는 차분한 다큐 내레이션 톤으로 고릅니다.
3. **속도는 1.0** 그대로 둡니다. 빠르기는 합성할 때 음 높이를 그대로 둔 채 1.12~1.18배로 맞춥니다.
4. 전체를 **mp3 한 파일**로, 가능하면 **자막(srt)**도 함께 받습니다.
5. 단어를 엉뚱하게 읽으면 그 단어만 바꿔 그 줄을 다시 만듭니다. 예: "돕니다" → "돌아갑니다".

## 5. 구글 플로우

1. 새 프로젝트를 만들 때마다 에이전트 설정을 다시 확인합니다.
   - 생성 전 확인: **안 함**
   - 비율: **9:16**
   - 생성 개수: **1**
   - 모델: **나노바나나 2**
2. 대본 파일의 "플로우 프롬프트"를 **한 줄씩** 붙여 넣습니다. 한 줄에 이미지 한 장입니다. 여러 줄을 한 번에 넣으면 한 장만 나오고 멈추는 일이 많습니다.
3. 글자, 로고, 번호판, 얼굴이 나온 그림은 다시 만듭니다.
4. 다 만들면 **프롬프트 번호 순서대로** 내려받아 zip 하나로 묶습니다. 파일이 크면 구글 드라이브에 올리고 링크를 줍니다.

## 6. 꼭 지킬 규칙 (대표이사)

- 법규나 KEC, 설계기준의 숫자는 원문을 확인하기 전에는 쓰지 않습니다.
- "모든, 항상, 반드시" 같은 일반화를 쓰지 않습니다.
- 영상에 회사 이름을 넣지 않습니다. 회사 이야기는 `knowledge/company.md`에 있는 것만 씁니다.
- "AI가 고장을 예측한다"고 쓰지 않습니다.
- 대본의 숫자에는 모두 출처가 있어야 합니다.

## 7. 막힐 때

| 증상 | 해결 |
|---|---|
| 아침 알림이 안 옴 | 같은 저장소 세션에서 `오늘 기획안 6개 만들어 줘`라고 보내면 같은 일을 합니다 |
| 첨부가 안 올라감 | 파일이 너무 큽니다. 구글 드라이브에 올리고 링크 공유를 "링크가 있는 모든 사용자"로 바꿉니다 |
| 보낸 파일을 Claude가 못 봄 | Claude가 답하는 도중에 올리면 저장되지 않습니다. 답이 끝난 뒤 다시 올립니다 |
| 플로우가 한 장만 만들고 멈춤 | 한 줄씩 넣습니다. 그래도 멈추면 설정의 "생성 전 확인: 안 함"을 다시 봅니다 |
| 완성 영상이 흔들리거나 정신없음 | Claude에게 "흔들림 빼 줘", "컷 줄여 줘"처럼 말하면 고칩니다. 규칙은 `shorts/compose/README.md`에 있습니다 |

## 8. 어디에 무엇이 있나

- 기획 지침: `shorts/daily/GUIDE.md`
- 매일 결과물: `shorts/daily/날짜/`
- 쓴 주제와 후보 주제: `shorts/daily/topics.md`
- 대본 규칙: `shorts/structure.md`
- 합성 도구: `shorts/compose/`. 예시는 `example-08/`입니다.
- Claude용 스킬: `.claude/skills/shorts-plan`, `.claude/skills/shorts-compose`
- 예전 편(01~08)의 대본과 프롬프트: `shorts/scripts/`, `shorts/prompts/`

---

## 붙여넣기 ① 처음 한 번 (새 세션에)

```
이 저장소로 전기 숏츠 만드는 일을 처음부터 맡게 됐어. 브랜치 claude/shorts-daily로 옮겨서 작업해 줘.

1. shorts/HANDOFF.md, shorts/daily/GUIDE.md, shorts/structure.md, shorts/compose/README.md를 끝까지 읽어 줘.
2. bash shorts/compose/setup.sh로 합성 도구를 준비해 줘.
3. 준비가 됐는지 확인해 줘. example-08의 lines.json과 scene.html로 이미지 없이(회색 대기 화면) align을 글자 수 어림으로 돌리고, 정지 화면 3장을 뽑아 보여 줘. align.py에 음성 대신 - 를 넣으면 돼.
4. 매일 오전 7시 37분(한국 시간)에 새 세션으로 도는 예약 작업을 만들어 줘. 휴대폰 알림을 켜고, 예약 작업 문구는 shorts/HANDOFF.md 맨 아래 "예약 작업 문구"를 그대로 써 줘.
5. 끝나면 예약 시각과, 내가 매일 할 일을 짧게 정리해 줘.
```

## 붙여넣기 ② 합성 (음성·이미지를 만든 뒤)

```
NN편 합성해 줘. shorts-compose 스킬과 shorts/compose/README.md 순서대로 해 줘.
- 대본: shorts/daily/날짜/NN-slug.md
- 음성: 첨부한 mp3(+srt)
- 이미지: 첨부한 zip (또는 드라이브 링크: )
정지 화면 미리보기를 먼저 보여 주고, 내가 괜찮다고 하면 전체 영상을 만들어 줘.
```

## 붙여넣기 ③ 예약 없이 그날 바로

```
shorts-plan 스킬대로 오늘 기획안 6개 만들어 줘. 내가 번호를 고르면 그 3편으로 대본이랑 타입캐스트 대본, 플로우 프롬프트까지 만들어 줘.
```

## 예약 작업 문구

예약 작업이 매일 새 세션에 보내는 지시입니다. 붙여넣기 ①을 보내면 Claude가 이 문구로 예약 작업을 만듭니다.

```
You are preparing today's Shorts ideas for this company's channel. Write everything in Korean.

1. Repository: GitHub bmk3037/donginensis-blog. If it is not already in your working directory, attach it with the add_repo tool (access: push), then clone it.
2. Run git fetch origin claude/shorts-daily and git checkout claude/shorts-daily. If the branch is missing, stop and report that.
3. Read shorts/daily/GUIDE.md and every file it lists to read first.

STAGE 1 (do now):
- Follow GUIDE.md section 1: write 6 fact-checked ideas to shorts/daily/YYYY-MM-DD/ideas.md, using today's date in Korea time.
- Commit and push.
- Show each idea's number, working title and hook first line, plus your top 3 picks.
- Ask: "만들 3편의 번호를 알려 주세요. 직접 생각한 주제를 적어 주셔도 됩니다."
- Then STOP. Do not write scripts before the user answers.

STAGE 2 (only after the user replies with numbers or their own idea):
- Follow GUIDE.md sections 2–7 for the chosen 3 episodes:
  - fact-check;
  - script;
  - two-pass review;
  - rewrite;
  - Typecast script;
  - Flow one-line prompts and scene map.
- Commit and push.
- Summarize the titles, character counts, image counts, file paths and any dropped numbers.

Hard rules:
- No legal, KEC or design-standard numbers unless checked in the original text.
- No 모든/항상/반드시 generalizations.
- Company facts only from knowledge/company.md.
- No company name in the narration.
- Never claim that AI predicts failures.
- No model identifiers in files or commits.

Push with git push -u origin claude/shorts-daily, retrying up to 4 times on network errors. Never open a pull request.
```
