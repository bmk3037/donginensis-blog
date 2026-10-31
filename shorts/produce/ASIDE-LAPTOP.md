# 노트북 Aside 설정 (이 파일 하나로 PC Aside와 똑같이 일하기)

대표이사 10/31: "노트북에서도 바로 작업해도 똑같은 퀄리티". **규칙·카드·프롬프트는 전부 GitHub에 있고, 노트북 Aside는 그것을 읽고 그대로 따라 한다.** 노트북 안에 따로 저장한 규칙·프롬프트·예전 기억은 쓰지 않는다(PC와 달라지는 원인).

- 저장소: `bmk3037/donginensis-blog`, 브랜치 **`claude/shorts-daily`** (다른 브랜치에 올리지 않는다)
- 문서는 항상 **GitHub의 최신 파일을 다시 열어서** 읽는다(링크 아래).

## 1. 먼저 읽을 문서 (이 순서)

1. `shorts/produce/ASIDE-MAKE.md` — 맨 위 "★ 10/31 한 번에 만들기"와 "0-3. 형식 B v4 제작 순서"가 기본
2. `shorts/produce/STYLE-V4.md` — 형식 B v4 규칙(그림·클립 프롬프트 틀, 합격선)
3. 작업할 편의 카드 `shorts/produce/NN.md` — 프롬프트는 **한 글자도 바꾸지 않는다**
4. 올리기 작업일 때만 `shorts/upload/ASIDE.md`와 편의 업로드 카드 `shorts/upload/NN.md`

링크: https://github.com/bmk3037/donginensis-blog/blob/claude/shorts-daily/shorts/produce/ASIDE-MAKE.md · https://github.com/bmk3037/donginensis-blog/blob/claude/shorts-daily/shorts/produce/STYLE-V4.md · https://github.com/bmk3037/donginensis-blog/tree/claude/shorts-daily/shorts/produce

## 2. 시작 전 점검 (노트북에서 처음 한 번, 이후에는 로그인만 확인)

아래를 하나씩 열어 보고, **되는 것과 안 되는 것을 표로 보고한다.** 안 되면 그 지점에서 멈추고 대표이사에게 알린다(로그인·캡차·결제 화면이 나와도 멈춘다).

| 점검 | 확인 방법 | 합격 |
|---|---|---|
| GitHub 쓰기 | 브랜치 `claude/shorts-daily`에서 `shorts/media/laptop-check.md` 파일을 새로 만들어 "노트북 연결 확인 + 날짜"만 한 줄 적고 커밋 | 커밋이 올라감 |
| 구글 플로우 | labs.google/flow 접속 → **PRO(또는 Ultra) 계정**으로 로그인 → 새 프로젝트 만들기 화면 | 로그인됨, 계정 이름은 보고하지 않고 "PRO 계정 A/B"처럼 구분만 |
| 플로우 클립 설정 | 동영상 → 프레임 → Veo 3.1 Lite → 9:16 → x1, 설정 메뉴 **"무음 동영상 반환" 꺼짐**, 내려받기에 **"1080p 업스케일링"** 선택이 보임 | 모두 보임. 1080p가 안 보이면 그 계정으로 클립을 만들지 않고 보고 |
| 타입캐스트 | studio.typecast.ai 로그인 → 직전 편 프로젝트가 보임 → 문정 캐릭터, 속도 1.0 | 보임 |
| 유튜브 | 스튜디오에서 채널 이름이 **숨은 설비 도감**(또는 "숨은 설비도감") | 이름 일치 |
| 인스타 | 프로페셔널 계정 프로필이 열림 | 열림 |

## 3. 공통 규칙 (PC와 같은 것, 어겨서는 안 되는 것)

1. **카드를 만들기 직전에 GitHub에서 다시 연다.** 카드의 영어 프롬프트·한국어 대본은 한 글자도 바꾸거나 지어내지 않는다.
2. **로그인·캡차·결제·요금제 화면, 크레딧 부족이 나오면 멈추고 알린다.** 유료 결제는 누르지 않는다. 크레딧이 모자라면 다른 PRO 계정으로 이어서 만든다(계정은 A/B로만 적음).
3. **GitHub 공개 저장소에 이메일·사람 이름·계정 아이디를 쓰지 않는다**(NOTES.md, 보고서, 커밋 메시지 모두).
4. 생성이 실패하면 같은 번호를 **한 번만** 다시 한다. 또 실패하면 건너뛰고 NOTES에 적는다.
5. 파일 이름은 카드대로(s01, e02, c01, voice.mp3). 번호가 틀리면 장면이 뒤섞인다.
6. 올릴 곳은 `shorts/media/NN/in/`(img/, clip/, voice.mp3, NOTES.md). 노트북 다운로드 폴더에 남기지 않는다.
7. **한 번에 만들기가 기본**: 그림 → 음성 → 클립을 멈추지 않고, 끝나면 마지막에 `DONE.md`(`NN: 재료 완료`)를 만든다. 일부만 되었으면 DONE.md를 만들지 않는다.
8. **Flow 함정** (이미 겪은 것):
   - 참고 이미지는 생성할 때마다 프롬프트에서 빠진다 → **그림마다 다시 붙인다.**
   - 프레임 고르기 창에는 이전 항목이 미리 선택돼 있다 → **"애셋 검색"에 sNN을 쳐서 하나만 남기고 "프롬프트에 추가"**, 넣기 전에 시작·종료 칸의 그림이 맞는지 확인.
   - 종료 그림은 새로 그리지 않고 **시작 그림을 열어 "어떤 내용을 변경하려 하시나요?"로 편집**한다(시점 유지). 편집본은 같은 애셋의 새 버전이니 받을 때 버전 확인.
   - 그림은 "1K 원본 크기", 클립은 **"1080p 업스케일링됨"**으로 받는다. 클립에는 소리가 들어 있어야 한다.
9. 사진을 먼저 보고 싶다는 말이 있을 때만 0단계(그림)에서 멈춘다. 평소에는 멈추지 않는다.
10. **올리기는 업로드 카드의 승인이 "예"일 때만** 한다. 스레드는 올리지 않는다(유튜브 쇼츠·인스타 릴스만). 이미 올라간 영상이 보이면 지우지 말고 주소를 보고하고 멈춘다.

## 4. 보고 (끝날 때마다, ASIDE-MAKE.md "5. 보고" 표 그대로)

맨 위에 "DONE.md 올림/안 올림", 그림·음성·클립 개수, 해상도(1080p/720p인 번호), 다시 만든 번호, 막힌 곳, GitHub 커밋 주소를 적는다. **PC와 노트북의 결과가 같도록** 어느 컴퓨터에서 했는지는 "노트북"이라고만 적는다.

## 5. 노트북 Aside에 붙여 넣을 말 (이 한 덩어리를 그대로)

```
아래 문서를 GitHub(브랜치 claude/shorts-daily)에서 열어 읽고, 그 규칙 그대로 일해 줘. 이 노트북에 저장된 예전 규칙이나 프롬프트는 쓰지 말고 항상 GitHub 최신 파일을 다시 열어.
1) https://github.com/bmk3037/donginensis-blog/blob/claude/shorts-daily/shorts/produce/ASIDE-LAPTOP.md (이 파일: 점검표, 공통 규칙)
2) https://github.com/bmk3037/donginensis-blog/blob/claude/shorts-daily/shorts/produce/ASIDE-MAKE.md ("★ 10/31 한 번에 만들기"와 "0-3. 형식 B v4 제작 순서")
3) https://github.com/bmk3037/donginensis-blog/blob/claude/shorts-daily/shorts/produce/STYLE-V4.md
먼저 ASIDE-LAPTOP.md의 "2. 시작 전 점검"을 하나씩 해서 표로 보고해 줘(GitHub 쓰기 시험은 shorts/media/laptop-check.md 한 줄). 안 되는 것이 있으면 거기서 멈추고 알려 줘. 이메일·이름·계정 아이디는 GitHub에 적지 마.
점검이 끝나면 다음 지시를 기다려 줘.
```

**작업을 시킬 때(점검 통과 뒤):** PC에서 쓰던 문구와 똑같이 붙이면 된다.
```
https://github.com/bmk3037/donginensis-blog/blob/claude/shorts-daily/shorts/produce/ASIDE-MAKE.md 지침의 "★ 10/31 한 번에 만들기"를 읽고,
https://github.com/bmk3037/donginensis-blog/blob/claude/shorts-daily/shorts/produce/NN.md 제작 카드를 GitHub에서 다시 열어, 그림 → 음성 → 클립을 멈추지 말고 이어서 모두 만들어 줘.
프롬프트는 한 글자도 바꾸지 말고, 클립은 1080p 업스케일로 받을 수 있는 PRO 계정에서 소리를 켠 채 만들어. 크레딧이 모자라면 다른 PRO 계정으로 이어서 만들고, 결제 화면은 누르지 마.
shorts/media/NN/in/ 에 img/, voice.mp3, clip/, NOTES.md를 올리고, 다 끝나면 마지막에 DONE.md를 만들어 "NN: 재료 완료"로 커밋해. 이메일·이름·계정 아이디는 적지 마. 보고해 줘.
```
(NN은 카드 번호.)
