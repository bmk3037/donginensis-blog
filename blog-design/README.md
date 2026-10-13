# 네이버 블로그 화면 디자인 (회사 서식 적용)

지금 블로그 상단과 **같은 구조(로고 → 큰 배너 → 버튼 5개)**를 유지하고, 문구와 색만 회사소개서·홈페이지 서식으로 바꾼 안입니다.
전체 모습: `images/preview-layout.png`

## 파일

| 파일 | 용도 | 크기 |
|---|---|---|
| `images/hero.png` | 큰 배너 (스킨 배경 또는 타이틀) — 글자는 가운데 966px 안에 있어 화면 폭이 달라도 잘리지 않음 | 1920×600 |
| `images/btn-1-home.png` | 버튼 1: 공식 홈페이지 (지금과 같음) | 150×166 |
| `images/btn-2-panel.png` | 버튼 2: 지능형 제어반 | 150×166 |
| `images/btn-3-check.png` | 버튼 3: 적용 진단 신청 | 150×166 |
| `images/btn-4-partner.png` | 버튼 4: IT기업 협업 | 150×166 |
| `images/btn-5-profile.png` | 버튼 5: 회사소개서 | 150×166 |
| `images/profile.png` | 블로그 프로필 사진 | 600×600 |
| `images/banner-inquiry.png`, `banner-partner.png` | 사이드 위젯 배너 (선택) | 340×400 |

## 버튼별 연결 주소

| 버튼 | 주소 |
|---|---|
| 공식 홈페이지 | https://donginensis.com/?utm_source=naver_blog&utm_medium=blog_menu |
| 지능형 제어반 | https://donginensis.com/?utm_source=naver_blog&utm_medium=blog_menu#product |
| 적용 진단 신청 | https://donginensis.com/manufacturing.html?utm_source=naver_blog&utm_medium=blog_menu#inquiry |
| IT기업 협업 | https://donginensis.com/partner.html?utm_source=naver_blog&utm_medium=blog_menu#inquiry |
| 회사소개서 | https://donginensis.com/files/DONG-IN-ENSIS_Company-Profile_KR.pdf |

## 네이버에 적용하는 방법 (PC)

지금 화면을 만든 방식 그대로 **같은 자리의 이미지만 바꾸는 것**이 가장 쉽습니다.

1. **큰 배너**: 블로그 관리 → 꾸미기 설정 → 디자인 설정 → 세부 디자인 설정(리모콘)
   → 지금 배너가 들어간 곳(스킨 배경 또는 타이틀)에서 `hero.png`로 바꾸기
2. **버튼**: 블로그 관리 → 꾸미기 설정 → 레이아웃·위젯 설정 → 지금 버튼 위젯을 열어 이미지 주소와 연결 주소만 바꾸기
   - 버튼 이미지는 인터넷 주소가 필요합니다. 비공개 글에 버튼 이미지를 올린 뒤, 이미지에서 오른쪽 클릭 → "이미지 주소 복사"
   - 위젯 HTML 예시:
     ```html
     <a href="연결 주소" target="_blank"><img src="이미지 주소" width="150" height="166"></a>
     ```
3. **프로필**: 블로그 관리 → 기본 설정 → 블로그 정보 → 블로그 프로필 이미지에 `profile.png`

배너 높이나 폭이 지금 설정과 다르면, 리모콘에 표시된 현재 크기를 알려 주세요. 그 크기에 맞춰 다시 만들어 드립니다.
