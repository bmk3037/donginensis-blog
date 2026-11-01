# 유튜브·인스타 API 연결 순서 (대표이사가 직접, 2026-11-01)

비밀번호·2단계 인증이 들어가므로 대표이사가 직접 한다. 키·토큰은 **채팅에 붙이지 말고** 클라우드 환경 설정의 비밀값(secrets)에 넣는다. 다 넣으면 Claude가 업로드·숫자 수집 코드를 붙인다.

## A. 유튜브 (약 15분)
1. https://console.cloud.google.com → 새 프로젝트 "숨은설비이야기-업로드".
2. "API 및 서비스 → 라이브러리"에서 **YouTube Data API v3**, **YouTube Analytics API** 사용 설정.
3. "OAuth 동의 화면": 사용자 유형 **외부**, 앱 이름·이메일 입력, 범위에 `youtube.upload`, `youtube.force-ssl`, `yt-analytics.readonly` 추가. 테스트 사용자에 채널 계정 추가 → 마지막에 **"앱 게시(프로덕션)"** 누르기(테스트 상태면 토큰이 7일마다 끊김).
4. "사용자 인증 정보 → OAuth 클라이언트 ID": 유형 **"TV 및 입력 제한 기기"**(휴대폰으로 코드 입력하는 방식이라 비밀값이 채팅에 안 남음).
5. 나온 클라이언트 ID·보안 비밀을 비밀값 `YT_CLIENT_ID`, `YT_CLIENT_SECRET`으로 저장.
6. Claude에게 "유튜브 연결" → Claude가 짧은 코드를 보여 줌 → 휴대폰에서 google.com/device 열고 코드 입력, **채널 계정**으로 허용 → Claude가 받은 갱신 토큰을 `YT_REFRESH_TOKEN`으로 넣는 법을 안내.
- 주의: 구글 심사 전에는 API로 올린 영상이 **비공개로 잠김**. 그동안은 Claude가 비공개로 올리고 대표이사가 폰에서 "공개"를 누름. 심사 신청서(YouTube API 준수 감사)는 Claude가 초안을 씀.

## B. 인스타 (약 10분)
1. 인스타 앱: 계정이 **프로페셔널(크리에이터 또는 비즈니스)** 인지 확인. (계정 이름도 "숨은설비이야기"로 바꾸는 것을 권함)
2. https://developers.facebook.com → 앱 만들기 → 유형 "비즈니스" → 제품 **"Instagram"(Instagram 로그인 API)** 추가.
3. "API 설정 → 액세스 토큰 생성"에서 인스타 계정 연결 → 권한 `instagram_business_basic`, `instagram_business_content_publish`, `instagram_business_manage_comments`, `instagram_business_manage_insights`.
4. 나온 **장기 토큰**(60일, Claude가 만료 전에 자동 갱신)을 비밀값 `IG_ACCESS_TOKEN`으로 저장.
- 영상은 공개 주소가 있어야 올라감 → 우리 저장소(공개) 주소를 씀.
- 하루 25편까지 게시 가능.

## 연결 뒤 Claude가 하는 일
- "올려" 받은 편만 업로드(제목·설명·태그·썸네일·재생목록·번역·고정 댓글).
- 24시간·7일 뒤 조회수·좋아요·댓글·(인스타) 저장·공유·도달을 자동 기록 → `shorts/channel-feedback.md`.
- 다른 채널 분석: 인스타 "비즈니스 디스커버리"로 다른 계정 게시물·좋아요·댓글 수.
- 쇼츠 "조회수 대비 스와이프(계속 시청)"는 API에 없을 수 있어 스튜디오 화면이 계속 필요할 수 있음(연결 뒤 확인).
