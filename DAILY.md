# 매일 글 3편 작업 절차 (블로그마다 1편, Claude가 따르는 순서)

API 키 없이, 대화창의 Claude가 직접 글과 이미지를 만듭니다. 매일 아침 예약 실행(루틴)이 이 절차를 시작합니다.
**항상 하루 앞서** 준비합니다 (네이버 예약 발행용). 발행일 = 내일 날짜.

| 순서 | 블로그 | 주제 고르는 곳 |
|---|---|---|
| 1 | donginensis3047 · 동인엔시스 지능형 제어반 | `topics.csv`에서 `blog=donginensis3047` |
| 2 | donginensis · 동인엔시스 데이터 인프라 | `blog=donginensis` |
| 3 | bmk3037 · 동인엔시스 현장 이야기 | `blog=bmk3037` |

## 0. 준비
- `python -m blog.existing sync` — 세 블로그에 지금까지 발행된 글을 새로 받습니다 (담당자가 직접 올린 글도 겹침 검사에 포함)
- 블로그마다 `posts/<발행일>-<블로그>-*` 폴더가 이미 있으면 그 블로그는 건너뜁니다 (미리 써 둔 글)
- `knowledge/company.md`(사실)와 `knowledge/style.md`(규칙, 특히 '블로그 3개'·'동인엔시스가 검색되게')를 다시 읽습니다

## 1. 주제 고르기 (블로그마다)
- 그 블로그의 `status=todo` 첫 줄. 사용자가 주제를 주면 그것을 우선
- `existing/<블로그>.json` 제목을 보고, 이미 발행된 글과 같은 내용이면 다음 주제로 넘기고 사용자에게 알립니다
- todo가 5개 미만으로 남으면 사용자에게 새 주제 추가를 제안합니다 (company.md 사실 범위 안에서 후보를 같이 제시)

## 2. 글 쓰기 → `posts/<발행일>-<블로그>-<id>/post.json`
- 필드: `title`, `format`, `body_markdown`, `tags`(8~12), `fact_check`, `photos`, `personal_prompts`(2~3)
- `format`: 같은 블로그 바로 전 글과 다른 형식 (해설·Q&A·체크리스트·사례·비교·단계·용어·현장일지)
- 공백 제외 2,500~3,500자 (기준 3,000자), 소제목 5~8개, FAQ 3~5개(Q&A형 제외)
- **회사명:** 첫 문단에 '동인엔시스', 본문 3~6회, 회사가 하는 일을 알려 주는 문장 1개 (글마다 표현 바꾸기)
- **세 글끼리 겹치지 않게:** 같은 날 다른 블로그 글과 회사 소개·수집 항목·보안 설명·마무리 문구를 다르게
- 본문 맨 위 `[이미지: 01-cover.png]`, 설명 이미지 2~3장 `[이미지: 0N-name.png]`, 사진 2~3장 `[사진: 0N-photo-name.png]`
- 마무리: 그 주제의 `landing_url` 링크 1개 + 연락처 (문구는 매번 바꾸기)

## 3. 이미지 만들기 → `posts/<dir>/images/`
- 설명 이미지 조각(`02-*.html` …) 직접 작성. 첫 줄 `<!-- 1200x높이 -->`, `assets/image.css` 클래스 사용
- **대표 이미지(01-cover)는 각 블로그에 이미 올라간 썸네일과 같은 서식**으로 만듭니다 (사진 배경 + 라벨 + 빨간 밑줄 제목 + 아래 흰 띠 로고).
  블로그별 배경·라벨 모양·아래 띠 문구는 폴더 이름에서 자동:
  ```bash
  python -m blog.images posts/<dir> --cover "제목 첫줄\n*빨간 밑줄 줄*\n셋째 줄" --label "라벨(한글)" --en "영문 한 줄"
  ```
  - 제목은 3줄, 한 줄 9~11자 안팎. 빨간 밑줄은 한 줄에만
  - 라벨 예: 지능형 제어반 / 이상감지 체크리스트 / 도입 가이드 (3047), 데이터 수집 / 데이터 연동 가이드 / 설비데이터 기초 (donginensis), 수소·에너지 / 조선·해양 / 적용 사례 / 회사소개 (bmk3037)
  - 영문 예: PREDICTIVE MAINTENANCE, GLOSSARY, OT PARTNERSHIP, CLASS APPROVAL
  - 설명 이미지(02~)의 하단 블로그 이름도 폴더 이름에서 자동
- **사진 생성**: 각 `photos[].prompt`로 Figma `generate_image` (planKey `team::1685988044694788508`, model `gemini-3.1-flash-image`, 1536×1024)
  → `posts/<dir>/photos-src/<file>`로 내려받기 → 다시 `python -m blog.images posts/<dir>` 하면 '연출 이미지' 표기 후 images/에 저장
  - 실패(크레딧 소진 등)면 그대로 둡니다. 미리보기에 ChatGPT 프롬프트가 자동으로 나옵니다. 사용자에게 알려 주기
  - 사진을 열어 이상한 글자·다른 회사 로고·어색한 손이 없는지 확인, 문제 있으면 1번만 다시 생성
  - 세 블로그 사진이 비슷한 장면(같은 제어반 클로즈업 등)이 되지 않게 장면을 다르게
- PNG를 열어 글자 잘림·넘침 확인

## 4. 자동 검수 + 미리보기 (블로그마다)
```bash
python -m blog.generate --id <id> --from-json posts/<dir>/post.json --date <발행일> --pack <scratchpad>/out
```
- 글자 수, 저품질 검사, 겹침 검사 결과가 출력됩니다. **✗(FAIL)이 하나라도 있으면 post.json을 고치고 다시 실행**
- ⚠(WARN)는 확인하고, 둘 이유가 없으면 고칩니다
- 세 편을 모두 만든 뒤 마지막으로 한 번 더 세 편 모두 실행해, 서로 겹치지 않는지 확인
- `python -m unittest discover -s tests`

## 5. 저장·전달
- `git add posts topics.csv existing && git commit && git push` (main)
- GitHub 이슈 3개: 제목 `[<블로그 이름>] <제목>`, 본문 `posts/<dir>/issue.md`, 라벨 `blog-draft`
- 사용자에게 zip 3개 전송 + 표로 요약: 블로그 / 제목 / 형식 / 글자 수 / 확인할 사실 1줄

## 6. 쓰레드 3개 (회사 계정) → `threads/<발행일>.json`
- `knowledge/threads.md`(규칙)와 `knowledge/ceo_notes.md`(대표 답변)를 읽고 씁니다
- 아침 '생각' / 점심 '지식'(그날 블로그 글 하나를 3~5줄로, 문장 복사 금지) / 저녁 '질문' + 답글 초안 2~3개
- 경험담은 ceo_notes.md에 있는 대표 답변으로만, `source`에 날짜 표시. 쓴 답변은 ceo_notes.md에 `(사용: 날짜 슬롯)` 표시
- 링크는 사흘에 한 번 정도, 첫 댓글(`first_comment`)에만
- 오늘의 대표 질문(`question`) 1개
- 검수·미리보기: `python -m blog.threads threads/<발행일>.json` → ✗ 있으면 고치기 → `threads/<발행일>.html`을 사용자에게 전송
- 대표가 대화창에 질문 답을 주면 그대로 `knowledge/ceo_notes.md`에 `## 날짜 — 질문` 아래 원문으로 적고 커밋
