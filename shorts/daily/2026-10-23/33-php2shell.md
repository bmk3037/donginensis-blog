# 33. 로그인 없이 열리는 문: PHP 치명적 취약점(PHP2Shell)

- 분류: 지금 뉴스(2026-10-21 공개, 10/23 대표이사 "PHP 이슈가 난리인데 지금 … 쇼츠로 만들자"). 그림 **사실적인 시네마틱 3D**, 클립은 **훅 1~2개만**(대표이사 선택).
- 32번은 해저터널(지식컷 그대로, 다른 세션)에 비워 둠.
- 우리 홈페이지(donginensis.com)는 GitHub Pages 정적 HTML, 문의 폼은 Google Apps Script로 보냄 → PHP를 쓰지 않아 이번 건과 무관(10/23 확인).
- 겁주기 금지: "공격 시도 관측"과 "성공 사례는 아직 확인 안 됨"을 같이 말함. 버전 번호는 설명란에만.

## 아주 쉽게 판 (10/23 대표이사 "아주 쉽게")

- 어려운 말 다 뺌: CVE, CVSS, 서버 언어, 2200만, 엠바고, CISO 숫자 → 설명란에만.
- 비유 하나로 끝까지: **사이트 = 집, 구멍 = 열쇠 없이 열리는 문, 패치 = 새 자물쇠.**
- 큰 글자 2개만: "9.2", "열에 일곱".

## 첫 3초

| 항목 | 내용 |
|---|---|
| 첫 문장 | **"내가 가입한 사이트, 문이 열려 있을지도 몰라요."** (21자, 약 2.9초) |
| 첫 장면 | 클립 c01: 끝없는 복도의 문들이 0초부터 하나씩 열리며 빨간 빛이 새어 나옴 |
| 첫 제목(0~2.2초) | 작은 글자 "내가 가입한 사이트" / 큰 글자 **"문이 열려 있다?"** |
| 다른 안 | "비밀번호 없이 열리는 문이, 인터넷에 생겼어요." / "열 곳 중 일곱 곳이 쓰는 도구에, 구멍이 났어요." |

## 공유

| 항목 | 내용 |
|---|---|
| 공유 대상 | 회사 홈페이지·쇼핑몰 관리하는 사람 |
| 공유 한 문장 | "회사 홈페이지 관리하는 분께, 이 영상 보내 주세요." (20번) |
| 설명란 📌 | ① PHP 버전 확인(8.5.12·8.4.27·8.3.36·8.2.35 이상) ② 호스팅 업체에 패치 확인 ③ 사이트마다 다른 비밀번호 |
| 설명란 질문 | "우리 회사 홈페이지, 무엇으로 만들었는지 알고 계신가요?" |

## 대본 (21문장, 공백 제외 470자, 1.15배속 약 70초)

| 번호 | 내레이션 | 그림·클립 |
|---|---|---|
| 1 | 내가 가입한 사이트, 문이 열려 있을지도 몰라요. | 01 · **c01** |
| 2 | 지난 10월 21일, 인터넷 사이트를 만드는 도구에서 큰 구멍이 발견됐어요. | 02 |
| 3 | 도구 이름은 PHP예요. | 02 |
| 4 | 이 구멍으로는, 비밀번호 없이도 사이트 뒤의 컴퓨터를 마음대로 조종할 수 있었죠. | 03 · **c02** |
| 5 | 열쇠 없이 남의 집 문을 여는 것과 같아요. | 04 |
| 6 | 위험 점수는 10점 만점에 9.2점이었어요. | 05 (큰 글자 "9.2") |
| 7 | 그런데 이 도구, 정말 많이 쓰여요. | 06 |
| 8 | 무엇으로 만들었는지 알려진 사이트만 보면, 열 곳 중 약 일곱 곳이 PHP거든요. | 06 (큰 글자 "열에 일곱") |
| 9 | 더 큰 문제는, 고친 버전이 정식으로 나오기도 전에 문 여는 시연 영상이 먼저 퍼졌다는 거예요. | 07 |
| 10 | 실제로 문을 열어 보려는 시도도 보였대요. | 08 |
| 11 | 다만 열린 곳은 아직 확인되지 않았고요. | 08 |
| 12 | 그래서 우리 정부도 사이버 경보를 한 단계 올렸어요. | 09 |
| 13 | 해결 방법은 간단해요, 고친 새 버전으로 바꾸는 거예요. | 10 |
| 14 | 낡은 자물쇠를 새것으로 바꾸는 것처럼요. | 11 |
| 15 | 우리는 사이트마다 비밀번호를 다르게 쓰는 게 좋아요. | 12 |
| 16 | 한 곳이 뚫려도, 다른 곳까지 번지지 않게요. | 12 |
| 17 | 공장도 똑같아요. | 13 |
| 18 | 지능형 제어반은 인터넷과 연결된 쪽과, 기계를 움직이는 쪽을 나눠 둬요. | 14 |
| 19 | 한쪽에 구멍이 나도, 기계까지 바로 번지지 않게요. | 15 |
| 20 | 회사 홈페이지 관리하는 분께, 이 영상 보내 주세요. | 16 |
| 21 | 문은 하나만 열려도, 집 전체가 위험해지니까요. | 17 (01과 같은 복도, 첫 장면으로 이어짐) |

## 사실 확인

| 내용 | 출처 | 원문 표현 |
|---|---|---|
| 10월 21일 패치 공개 | [CERT-EU 2026-018](https://cert.europa.eu/publications/security-advisories/2026-018/) | "The PHP team released the fixes today, 21 October 2026 at 13:30 UTC, in PHP versions 8.5.12, 8.4.27, 8.3.36 and 8.2.35." |
| 두 취약점, 로그인 없이 원격 코드 실행 | CERT-EU, [ZDNet Korea](https://zdnet.co.kr/view/?no=20261022095839) | "Both vulnerabilities can allow unauthenticated remote code execution." / "별도의 로그인이나 인증 절차 없이 외부에서 임의로 코드를 실행하거나 시스템을 장악할 수 있다" |
| 9.2점, 치명적 | CERT-EU, [Google Cloud](https://cloud.google.com/blog/ko/products/identity-security/responding-to-core-php-vulnerabilities-cve-2026-109618-cve-2026-109619?hl=ko), ZDNet(티오리) | "with a CVSS score of 9.2" / "심각(Critical) 등급인 9.2점" / "CVSS v4.0 기준 9.2점(Critical)" |
| 열 곳 중 약 일곱 곳 | [W3Techs](https://w3techs.com/technologies/details/pl-php) (2026-10-23) | "PHP is used by 69.3% of all the websites whose server-side programming language we know." |
| 약 2200만 개 노출 추정 | ZDNet(팔로알토) | "세계적으로 약 2200만 개의 PHP 인스턴스가 외부에 노출된 것으로 추정" |
| 발표 전 시연 영상·패치 파일 유출 | ZDNet(티오리) | "공식 보안 권고가 발표되기도 전에 개념증명(PoC) 시연 영상과 패치가 적용된 바이너리가 유출되면서" |
| 6시간 넘게 먼저, 재단 비판 | [파이낸셜뉴스](https://www.fnnews.com/news/202610220955424545) | "'체인가드'가 공식 배포 예정시간보다 약 6시간 이상 앞서서 패치가 적용된 이미지를 기습 공개" / "체인가드가 일방적으로 엠바고를 깼다" |
| 공격 시도 관측, 성공 사례 미확인 | [보안뉴스](https://www.boannews.com/news/articleView.html?idxno=146621) | "실제 공격 시도가 관측되고 있으며"(클라우드플레어 CTO) / "다만 현재까지 공격에 성공한 사례는 확인되지 않았다." |
| 경보 관심 → 주의, CISO 2만 8천·기반시설 111곳 | ZDNet, [서울신문](https://www.seoul.co.kr/news/economy/2026/10/23/20261023500201) | "민간 분야 사이버위기 경보를 '관심'에서 '주의'로 상향" / "정보보호최고책임자(CISO) 2만 8000명과 주요 기반시설 111곳 등에 패치를 요청" |
| 국내 현황 파악 안 됨 | 서울신문(KISA 원장) | "취약한 PHP 버전 보유 현황과 패치 완료율은 아직 파악되지 않았으며" |
| 고친 버전·EOL | CERT-EU, Google Cloud | 8.5.12·8.4.27·8.3.36·8.2.35 / "PHP 8.1 이하 버전에 대해서는 수정 사항을 릴리스하지 않습니다"(단 CERT-EU: 7.4·8.0·8.1 최소 소스 패치 공개 → 설명란에만) |
| 제어망·데이터망 분리, 서버는 직접 제어 안 함, 최종 제어 PLC | `knowledge/company.md` | "인터록과 최종 제어는 현장 PLC 담당, 서버는 설비를 직접 제어하지 않음. 제어망과 데이터망 분리" |

## 검수 기록

| 번호 | 걸린 것 | 고친 것 |
|---|---|---|
| 1 | "세계 웹사이트 70%" 기사마다 70·75·80% | W3Techs 69.3%를 "무엇으로 만들었는지 알려진 사이트만 보면 열 곳 중 약 일곱 곳" |
| 2 | 원격 코드 실행 | "비밀번호 없이 사이트 뒤의 컴퓨터를 마음대로 조종"(ZDNet "시스템을 장악할 수 있다") |
| 3 | 공격 성공 | "시도는 보였지만 열린 곳은 아직 확인 안 됨"(보안뉴스) |
| 4 | 정부 대응 | "경보를 한 단계 올림"(관심 → 주의) |
| 5 | "사이트마다 다른 비밀번호" | 숫자 없는 일반 보안 수칙, 이번 취약점을 막는 방법이라고는 말하지 않음("한 곳이 뚫려도 번지지 않게") |
| 6 | "웹이 뚫려도 공장은 안전" 장담 | "바로 번지지 않게 나눠 둔다"까지만(company.md: 제어망·데이터망 분리, 최종 제어는 PLC) |

## 타입캐스트 대본 (속도 1.0, mp3)

```
내가 가입한 사이트, 문이 열려 있을지도 몰라요.
지난 시월 이십일 일, 인터넷 사이트를 만드는 도구에서 큰 구멍이 발견됐어요.
도구 이름은 피에이치피예요.
이 구멍으로는, 비밀번호 없이도 사이트 뒤의 컴퓨터를 마음대로 조종할 수 있었죠.
열쇠 없이 남의 집 문을 여는 것과 같아요.
위험 점수는 십 점 만점에 구 점 이 점이었어요.
그런데 이 도구, 정말 많이 쓰여요.
무엇으로 만들었는지 알려진 사이트만 보면, 열 곳 중 약 일곱 곳이 피에이치피거든요.
더 큰 문제는, 고친 버전이 정식으로 나오기도 전에 문 여는 시연 영상이 먼저 퍼졌다는 거예요.
실제로 문을 열어 보려는 시도도 보였대요.
다만 열린 곳은 아직 확인되지 않았고요.
그래서 우리 정부도 사이버 경보를 한 단계 올렸어요.
해결 방법은 간단해요, 고친 새 버전으로 바꾸는 거예요.
낡은 자물쇠를 새것으로 바꾸는 것처럼요.
우리는 사이트마다 비밀번호를 다르게 쓰는 게 좋아요.
한 곳이 뚫려도, 다른 곳까지 번지지 않게요.
공장도 똑같아요.
지능형 제어반은 인터넷과 연결된 쪽과, 기계를 움직이는 쪽을 나눠 둬요.
한쪽에 구멍이 나도, 기계까지 바로 번지지 않게요.
회사 홈페이지 관리하는 분께, 이 영상 보내 주세요.
문은 하나만 열려도, 집 전체가 위험해지니까요.
```

강조: 4번 "비밀번호 없이도", 6번 "구 점 이 점", 11번 "다만".

## 플로우 프롬프트: 사실적인 시네마틱 3D

- 01을 먼저 만들고, 나머지는 01을 참고 이미지로 붙여 색·빛을 맞춥니다. 17은 01과 같은 복도라 **01을 꼭 참고로**.
- 반복 모티프: 열린 문틈의 빨간 빛(위험) / 파란 빛(안전). 그림에 글자 없음.

### 1단계: 그림 17장

```
01 | A very long dim hotel-like corridor with dozens of identical closed doors on both sides stretching into the distance, several doors already slightly ajar with intense red light spilling out through the gaps onto the floor, cold blue ambient light elsewhere. Photorealistic cinematic 3D render, moody film lighting, shallow depth of field, realistic materials. Recurring motif: red light leaking through an open door or gap means danger, calm blue light means safe. People only seen from behind or as silhouettes, no faces. No text, no letters, no numbers, no logos, no readable screens. Vertical 9:16.
02 | A dark room with a laptop on a desk, its screen showing an abstract website layout made of blank grey blocks, a thin crack of red light running across the screen like a split, blue night light from a window. Photorealistic cinematic 3D render, moody film lighting, shallow depth of field, realistic materials. Recurring motif: red light leaking through an open door or gap means danger, calm blue light means safe. People only seen from behind or as silhouettes, no faces. No text, no letters, no numbers, no logos, no readable screens. Vertical 9:16.
03 | Over-the-shoulder view of a hooded figure seen from behind in a dark room typing on a keyboard, beyond the monitor a glass wall reveals a server room whose rack lights are starting to turn from blue to red. Photorealistic cinematic 3D render, moody film lighting, shallow depth of field, realistic materials. Recurring motif: red light leaking through an open door or gap means danger, calm blue light means safe. People only seen from behind or as silhouettes, no faces. No text, no letters, no numbers, no logos, no readable screens. Vertical 9:16.
04 | A gloved hand pushing open the front door of a modern apartment without any key, the lock hanging broken, red light spilling out from inside onto a dark hallway. Photorealistic cinematic 3D render, moody film lighting, shallow depth of field, realistic materials. Recurring motif: red light leaking through an open door or gap means danger, calm blue light means safe. People only seen from behind or as silhouettes, no faces. No text, no letters, no numbers, no logos, no readable screens. Vertical 9:16.
05 | Close-up of a large industrial analog gauge dial in a dark control room, its needle pushed far into the red zone near the maximum, red glow reflecting on the glass. Photorealistic cinematic 3D render, moody film lighting, shallow depth of field, realistic materials. Recurring motif: red light leaking through an open door or gap means danger, calm blue light means safe. People only seen from behind or as silhouettes, no faces. No text, no letters, no numbers, no logos, no readable screens. Vertical 9:16.
06 | Aerial night view of a dense city of glass office towers, roughly seven out of every ten buildings lit in the same cool blue color while the rest are warm white, a few of the blue buildings showing a thin red glow at their doors. Photorealistic cinematic 3D render, moody film lighting, shallow depth of field, realistic materials. Recurring motif: red light leaking through an open door or gap means danger, calm blue light means safe. People only seen from behind or as silhouettes, no faces. No text, no letters, no numbers, no logos, no readable screens. Vertical 9:16.
07 | Many hands holding smartphones in a dark crowd, every screen showing the same blurred video of a door being forced open with red light, the video spreading from phone to phone. Photorealistic cinematic 3D render, moody film lighting, shallow depth of field, realistic materials. Recurring motif: red light leaking through an open door or gap means danger, calm blue light means safe. People only seen from behind or as silhouettes, no faces. No text, no letters, no numbers, no logos, no readable screens. Vertical 9:16.
08 | A security operations center at night seen from behind the analysts, a wall of large screens showing abstract world maps with many red blinking dots, blue desk lights. Photorealistic cinematic 3D render, moody film lighting, shallow depth of field, realistic materials. Recurring motif: red light leaking through an open door or gap means danger, calm blue light means safe. People only seen from behind or as silhouettes, no faces. No text, no letters, no numbers, no logos, no readable screens. Vertical 9:16.
09 | Night skyline of Seoul with the river and bridges, a large warning beacon light on top of a tall building switching from blue to amber, the city calm below. Photorealistic cinematic 3D render, moody film lighting, shallow depth of field, realistic materials. Recurring motif: red light leaking through an open door or gap means danger, calm blue light means safe. People only seen from behind or as silhouettes, no faces. No text, no letters, no numbers, no logos, no readable screens. Vertical 9:16.
10 | A technician seen from behind closing a server rack door and turning its lock, the red light inside fading back to calm blue. Photorealistic cinematic 3D render, moody film lighting, shallow depth of field, realistic materials. Recurring motif: red light leaking through an open door or gap means danger, calm blue light means safe. People only seen from behind or as silhouettes, no faces. No text, no letters, no numbers, no logos, no readable screens. Vertical 9:16.
11 | Close-up of two hands replacing an old rusty door lock with a new shiny one on an apartment front door, the old lock lying on the floor, warm safe light. Photorealistic cinematic 3D render, moody film lighting, shallow depth of field, realistic materials. Recurring motif: red light leaking through an open door or gap means danger, calm blue light means safe. People only seen from behind or as silhouettes, no faces. No text, no letters, no numbers, no logos, no readable screens. Vertical 9:16.
12 | A key ring on a wooden table holding many different keys, each key a different shape and color, beside a row of different front doors in soft blue light. Photorealistic cinematic 3D render, moody film lighting, shallow depth of field, realistic materials. Recurring motif: red light leaking through an open door or gap means danger, calm blue light means safe. People only seen from behind or as silhouettes, no faces. No text, no letters, no numbers, no logos, no readable screens. Vertical 9:16.
13 | A large clean factory floor at night with motors, pumps and conveyor lines, a tall industrial control panel standing in the middle under work lights. Photorealistic cinematic 3D render, moody film lighting, shallow depth of field, realistic materials. Recurring motif: red light leaking through an open door or gap means danger, calm blue light means safe. People only seen from behind or as silhouettes, no faces. No text, no letters, no numbers, no logos, no readable screens. Vertical 9:16.
14 | Cutaway view of a factory building split by a thick glass wall: on the left an office side with computers and a server with blue data lines flowing out to the internet, on the right the machine side with motors and a control panel connected by separate orange cables, the two sides not crossing. Photorealistic cinematic 3D render, moody film lighting, shallow depth of field, realistic materials. Recurring motif: red light leaking through an open door or gap means danger, calm blue light means safe. People only seen from behind or as silhouettes, no faces. No text, no letters, no numbers, no logos, no readable screens. Vertical 9:16.
15 | The same split factory: red light spreading across the office side on the left stops at the thick glass wall, while the machine side on the right stays calm in blue light with the motors running. Photorealistic cinematic 3D render, moody film lighting, shallow depth of field, realistic materials. Recurring motif: red light leaking through an open door or gap means danger, calm blue light means safe. People only seen from behind or as silhouettes, no faces. No text, no letters, no numbers, no logos, no readable screens. Vertical 9:16.
16 | An office worker seen from behind at a desk late in the evening, looking at a company website on a monitor made of blank layout blocks, a phone in hand about to send a message. Photorealistic cinematic 3D render, moody film lighting, shallow depth of field, realistic materials. Recurring motif: red light leaking through an open door or gap means danger, calm blue light means safe. People only seen from behind or as silhouettes, no faces. No text, no letters, no numbers, no logos, no readable screens. Vertical 9:16.
17 | The same long corridor of doors as the reference image, all doors now closed in calm blue light except one single door slightly ajar with a thin line of red light spilling across the floor. Photorealistic cinematic 3D render, moody film lighting, shallow depth of field, realistic materials. Recurring motif: red light leaking through an open door or gap means danger, calm blue light means safe. People only seen from behind or as silhouettes, no faces. No text, no letters, no numbers, no logos, no readable screens. Vertical 9:16.
```

## 3단계: 클립 2개 (훅만, 새 플로우 프로젝트, 출력 1, "10크레딧, 동영상 1개" 확인)

#### 33편 c01 — 시작 그림: 01번 그림 (첫 장면, Veo 3.1 Fast 권장)

```
From the very first frame, the doors along the corridor swing open one after another toward the camera, each releasing a burst of red light onto the floor, the camera gliding forward down the corridor. Keep the same photorealistic look, colors and lighting as the start frame. No on-screen text, no letters, no numbers, no logos, no camera cuts.
```

#### 33편 c02 — 시작 그림: 03번 그림

```
The hooded figure presses a key and the server racks beyond the glass turn from blue to red one row after another, the red light spreading toward the camera. The figure stays seen only from behind. Keep the same photorealistic look, colors and lighting as the start frame. No on-screen text, no letters, no numbers, no logos, no camera cuts.
```

## 커버

| 항목 | 내용 |
|---|---|
| 머리표 | 지금 뉴스 |
| 큰 제목 | 비밀번호 없이 / [열리는] 문 |
| 아래 문구 | 내가 가입한 사이트는 괜찮을까 |
| 배경 그림 | 01 또는 04 |

## 설명란

```
로그인도 없이 남의 서버에 명령을 내릴 수 있는 구멍. 10월 21일 공개된 PHP 치명적 취약점(통칭 PHP2Shell) 이야기입니다.

서버 언어가 알려진 웹사이트 열 곳 중 약 일곱 곳(W3Techs 69.3%)이 쓰는 PHP에서 위험도 9.2점(치명적)의 원격 코드 실행 취약점 두 개(CVE-2026-109618, CVE-2026-109619)가 공개됐습니다. 정식 발표 전에 시연 영상과 패치 파일이 먼저 퍼졌고, 정부는 민간 사이버위기 경보를 '주의'로 올렸습니다. 보안업체들은 공격 시도를 관측했다고 밝혔지만, 공격에 성공한 사례는 아직 확인되지 않았습니다.

📌 홈페이지 담당자라면
1. PHP 버전 확인 → 8.5.12 · 8.4.27 · 8.3.36 · 8.2.35 이상으로
2. 호스팅 업체에 패치 적용 여부 확인(워드프레스만 업데이트해서는 서버 PHP가 바뀌지 않습니다)
3. 패치 후 접속 기록 점검

우리 회사 홈페이지, PHP 몇 버전인지 알고 계신가요?
회사 홈페이지를 관리하는 분께 보내 주세요.

출처: CERT-EU(2026-018), Google Cloud 보안 블로그, W3Techs(2026.10.23), ZDNet Korea·파이낸셜뉴스·보안뉴스·서울신문(2026.10.22~23)

설비를 제어하고, 데이터를 연결하다. ㈜동인엔시스
※ 영상의 그림은 AI로 만든 이미지입니다.

#PHP #보안취약점 #PHP2Shell #해킹 #홈페이지보안 #사이버보안 #숨은설비도감
```
