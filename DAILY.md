# 매일 글 1편 작업 절차 (Claude가 따르는 순서)

API 키 없이, 대화창의 Claude가 직접 글과 이미지를 만듭니다. 매일 아침 예약 실행(루틴)이 이 절차를 시작합니다.

## 1. 주제 고르기
- `topics.csv`에서 `status=todo`인 첫 줄 (사업 기여도 순으로 정렬되어 있음)
- 사용자가 따로 주제를 주면 그것을 우선

## 2. 글 쓰기 → `posts/<오늘>-<id>/post.json`
- 반드시 `knowledge/company.md`(사실)와 `knowledge/style.md`(규칙)를 다시 읽고 씁니다
- JSON 형식: `title`, `body_markdown`, `tags`(8~12개), `fact_check`(사람이 확인할 사실 목록)
- 본문 맨 위 `[이미지: 01-cover.png]`, 중간에 설명 이미지 2~3장 `[이미지: 0N-name.png]`, 실제 사진 자리 1~2곳 `[사진: 설명]`
- 공백 포함 2,000~3,500자, 핵심 키워드 4~6회, 소제목 3~5개
- 마무리: 지능형 제어반 데이터 인프라로 연결 → 진단 신청(제조) 또는 협업 문의(IT) 링크 1개

## 3. 이미지 만들기 → `posts/<오늘>-<id>/images/`
- 설명 이미지 조각(`02-*.html` …)을 직접 작성. 첫 줄 `<!-- 1200x높이 -->`, `assets/image.css` 클래스 사용
  (`.kicker` `.flow/.node/.arrow` `.grid.c3/.card` `.steps/.step` `table.cmp` `.chips/.chip`)
- 회사 서식: 메인 파랑 #1857A5, 강조 빨강 #E83E30, Pretendard. 로고와 하단 표기는 자동으로 붙음
- 렌더:
  ```bash
  python -m blog.images posts/<dir> --cover "제목 첫줄\n*강조 단어*\n셋째 줄" --sub "부제" --kicker "INTELLIGENT CONTROL PANEL · 번호" --tags 태그1 태그2 태그3
  ```
- PNG를 열어 글자 잘림·넘침이 없는지 눈으로 확인

## 4. 미리보기·묶음 만들기
```bash
python -m blog.generate --id <id> --from-json posts/<dir>/post.json --date <오늘> --pack <scratchpad>/out
python -m unittest discover -s tests
```

## 5. 저장·전달
- `git add posts topics.csv && git commit && git push` (main)
- GitHub 이슈 생성: 제목 `[블로그 초안] <제목>`, 본문 `posts/<dir>/issue.md`, 라벨 `blog-draft`
- 사용자에게 zip(미리보기 + 이미지) 전송, 오늘의 제목과 확인할 사실 3줄 요약
