# 동인엔시스 네이버 블로그 초안 자동화

[blog.naver.com/donginensis](https://blog.naver.com/donginensis)에 올릴 글의 초안을 매주 자동으로 만들어
**donginensis.com으로 방문자를 보내기 위한** 도구입니다.

네이버 블로그는 공식 글쓰기 API가 없어서 완전 자동 발행은 할 수 없습니다. 무리하게 자동으로 올리면(매크로)
블로그가 저품질 판정을 받을 수 있습니다. 그래서 이 도구는 **초안 작성까지 자동**으로 하고,
**검수·사진·발행은 사람이** 합니다. 글 1편에 10~15분 정도 걸립니다.

## 매주 흐름

```
월요일 오전 9시  초안 2편 자동 작성 → GitHub 이슈로 검수 요청 (메일 알림)
      ↓
담당자          이슈에서 사실 확인 체크 → preview.html 열기 → [본문 복사]
      ↓
네이버 블로그    붙여넣기 → 노란 상자를 현장 사진으로 교체 → 태그 입력 → 예약 발행
      ↓
GitHub 이슈     네이버 글 주소를 댓글로 남기고 이슈 닫기 → 주제 목록에 '발행됨' 자동 기록
```

## 처음 한 번 설정

1. **Anthropic API 키 발급**: https://console.anthropic.com → API Keys → Create Key
   (글 1편에 수백 원 수준. 콘솔에서 월 사용 한도를 정해 두세요)
2. 이 저장소 **Settings → Secrets and variables → Actions → New repository secret**
   - 이름: `ANTHROPIC_API_KEY` / 값: 위에서 받은 키
3. **Actions** 탭 → "주간 블로그 초안" → **Run workflow** 로 한 번 시험해 보세요.

## 폴더 구성

| 경로 | 내용 | 누가 고치나 |
|---|---|---|
| `knowledge/company.md` | 회사 자료(제품, 실적, 인증). **AI는 여기 적힌 사실만 씁니다** | 새 실적·인증이 생기면 추가 |
| `knowledge/style.md` | 말투, 네이버 검색 노출 규칙, 금지 사항 | 원하는 글 스타일이 바뀌면 |
| `topics.csv` | 주제 목록 (36개 준비됨). `status`: todo → drafted → published | 엑셀로 열어 주제 추가 |
| `posts/날짜-번호/` | 만들어진 초안. `preview.html`(붙여넣기용), `post.md`, `meta.json` | 자동 생성 |
| `blog/` | 프로그램 코드 | — |

`posts/2026-10-13-001/`에 샘플 글 1편이 들어 있습니다. `preview.html`을 내려받아 브라우저로 열어 보세요.

## 주제 추가하는 법

`topics.csv`를 엑셀이나 GitHub 웹에서 열어 맨 아래에 한 줄을 추가합니다.

| 칸 | 예시 |
|---|---|
| id | 37 (겹치지 않는 번호) |
| status | todo |
| category | 제조 / 조선해양 / 수소 / IT협업 / 사례 / 회사 등 |
| title | 가제목 |
| keyword | 사람들이 네이버에 검색할 말 (예: 송풍기 베어링 온도) |
| landing_url | 글 끝에서 보낼 홈페이지 주소 |
| brief | 다룰 내용 한두 줄 |

**가장 좋은 주제는 고객이 실제로 물어본 질문**입니다. 영업·현장에서 받은 질문을 그대로 주제로 넣어 주세요.

## 홈페이지 유입 확인

글 속 donginensis.com 링크에는 `utm_source=naver_blog&utm_campaign=post001` 같은 꼬리표가 자동으로 붙습니다.
홈페이지에 Google Analytics나 네이버 애널리틱스가 설치되어 있으면 **어느 글에서 몇 명이 들어왔는지** 볼 수 있습니다.
(아직 없다면 홈페이지에 분석 도구를 먼저 설치하는 것을 권합니다.)

## 내 컴퓨터에서 직접 실행

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=...        # Windows: set ANTHROPIC_API_KEY=...
python -m blog.generate             # 다음 주제 1편
python -m blog.generate --id 17     # 17번 주제
python -m blog.generate --dry-run   # API 호출 없이 프롬프트만 확인
python -m blog.mark --id 17 --status published
python -m unittest discover -s tests
```

## 네이버 블로그 운영 팁

- **꾸준함이 가장 중요합니다.** 주 2편을 같은 요일·시간에 예약 발행하세요.
- **직접 찍은 사진**을 4장 이상 넣으세요. 제작 공정, 현장 설치, 시운전 사진이 가장 좋습니다.
- 블로그 프로필과 상단 메뉴에 홈페이지 링크를 걸어 두세요.
- 글에 달린 댓글·문의에는 하루 안에 답하세요.
- 같은 내용을 홈페이지 보도자료와 블로그에 똑같이 올리지 마세요. 네이버는 중복 글을 낮게 평가합니다.
