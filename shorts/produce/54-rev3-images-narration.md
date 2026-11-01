# 크린넷 시작 이미지 편집·시험 검수·확인 자료 반영 내레이션 Rev.3

2026-11-01 작성. 영상 최종본이 아닌 제작 지시·대본이다. 기존 Rev.2의 사실 확인 대기 항목과 일부 표현을 아래 내용으로 갱신한다. 실제 녹음 길이는 아직 측정하지 않았다.

## 1. 시작 이미지 편집
각 블록은 해당 이미지 하나를 열어 편집할 완전한 프롬프트다. 전체 모음 이미지를 한 번에 재생성하지 않는다. s08은 분리·압축 두 시점으로 나눠 총 21개 참조 이미지를 준비한다. 영상용 프롬프트는 Rev.2를 함께 사용한다.

### s01_clean — 도시 전경
```text
Edit the supplied image only. Preserve its camera, crop, miniature scale, architectural layout, materials and lighting unless explicitly changed below. Remove green scene IDs, all existing letters, numbers, logos, overlay stars, numeric signboards and explanatory arrows. Restore the background naturally. Do not add replacement writing. Keep white unpainted figurines. Vertical 9:16. Remove the floating numeric sign and red flow arrows. Preserve the city and pipe network. Keep all transport pipes below the road, visible only in the existing model cutaway. Retain one small bag clearly inside one exposed pipe branch. Do not add branches, openings or vehicles.
```

### s02_clean — 주민과 투입구
```text
Edit the supplied image only. Preserve its camera, crop, miniature scale, architectural layout, materials and lighting unless explicitly changed below. Remove green scene IDs, all existing letters, numbers, logos, overlay stars, numeric signboards and explanatory arrows. Restore the background naturally. Do not add replacement writing. Keep white unpainted figurines. Vertical 9:16. Remove the red X. Keep the parked truck, sidewalk and buildings unchanged. Show one resident carrying one bag toward an existing upright mailbox-shaped inlet within the same frame. If the inlet is missing, place one at the already established apartment entrance, without moving buildings.
```

### s03_clean — 봉투 투입 직전
```text
Edit the supplied image only. Preserve its camera, crop, miniature scale, architectural layout, materials and lighting unless explicitly changed below. Remove green scene IDs, all existing letters, numbers, logos, overlay stars, numeric signboards and explanatory arrows. Restore the background naturally. Do not add replacement writing. Keep white unpainted figurines. Vertical 9:16. Preserve the scene and replace only the inlet with the approved upright stainless-steel mailbox-shaped inlet. Use a small square front door, already open on one visible hinge. Place one white bag in the resident's hand just outside that opening. Keep the other hand separate from the bag. Remove the red dashed box. No round top lid or extra door.
```

### s04_clean — 밸브 닫힘
```text
Edit the supplied image only. Preserve its camera, crop, miniature scale, architectural layout, materials and lighting unless explicitly changed below. Remove green scene IDs, all existing letters, numbers, logos, overlay stars, numeric signboards and explanatory arrows. Restore the background naturally. Do not add replacement writing. Keep white unpainted figurines. Vertical 9:16. Make an explanatory cutaway of the existing chute-to-pipe junction. Show several bags supported above one closed discharge gate. Keep the technician outside the pipe on the existing platform. Make the gate leaf and its unobstructed opening distinguishable from the fixed housing. Preserve the chamber, main pipe and camera. Remove the arrow. No bag intersects a solid wall.
```

### e04_clean — 밸브 열림
```text
Edit the supplied image only. Preserve its camera, crop, miniature scale, architectural layout, materials and lighting unless explicitly changed below. Remove green scene IDs, all existing letters, numbers, logos, overlay stars, numeric signboards and explanatory arrows. Restore the background naturally. Do not add replacement writing. Keep white unpainted figurines. Vertical 9:16. Edit the approved s04_clean directly. Keep exactly the same camera, crop, pipe shell, housing, supports, platform, technician and light. Change only the visible discharge gate from its closed position to its approved open position; place the lowest two bags below the gate inside the connected pipe. Preserve the gate's physical attachment. Do not change the diameter, camera angle or housing. Other bags remain above.
```

### s05_clean — 송풍기실
```text
Edit the supplied image only. Preserve its camera, crop, miniature scale, architectural layout, materials and lighting unless explicitly changed below. Remove green scene IDs, all existing letters, numbers, logos, overlay stars, numeric signboards and explanatory arrows. Restore the background naturally. Do not add replacement writing. Keep white unpainted figurines. Vertical 9:16. Remove all red arrows and text. Preserve the blower housings, opaque ducts and guards. Keep the engineer beside the existing panel with hands resting. If the reference has a visible coupling, retain it without changing its shape. Do not expose hidden impellers or invent additional controls. No airborne dust.
```

### s06_clean — 관내 이송 단면
```text
Edit the supplied image only. Preserve its camera, crop, miniature scale, architectural layout, materials and lighting unless explicitly changed below. Remove green scene IDs, all existing letters, numbers, logos, overlay stars, numeric signboards and explanatory arrows. Restore the background naturally. Do not add replacement writing. Keep white unpainted figurines. Vertical 9:16. Remove the numeric board, speed lines and above-ground wind effects. Put the hat securely on the person's head and restore upright trees. Preserve the sidewalk above and buried pipe below. Keep the pipe closed except for the explanatory viewing cutaway. Place two or three small bags entirely inside the pipe, aligned in one transport direction. No opening from the pipe to the street.
```

### s07_clean — 사람 없는 관 내부
```text
Edit the supplied image only. Preserve its camera, crop, miniature scale, architectural layout, materials and lighting unless explicitly changed below. Remove green scene IDs, all existing letters, numbers, logos, overlay stars, numeric signboards and explanatory arrows. Restore the background naturally. Do not add replacement writing. Keep white unpainted figurines. Vertical 9:16. Remove every person, walkway, handrail, lamp, cable and red streak from inside the pipe. Restore a continuous cylindrical steel interior in the same perspective. Keep only a few bags smaller than the pipe diameter, arranged toward the distant bend. Preserve readable bag edges. The distant pipe remains enclosed, without a bright outdoor exit. Do not turn it into a railway or pedestrian tunnel.
```

### s08a_clean — 분리기 설명 단면
```text
Edit the supplied image only. Preserve its camera, crop, miniature scale, architectural layout, materials and lighting unless explicitly changed below. Remove green scene IDs, all existing letters, numbers, logos, overlay stars, numeric signboards and explanatory arrows. Restore the background naturally. Do not add replacement writing. Keep white unpainted figurines. Vertical 9:16. Derive this view from s08, preserving the same plant equipment and materials. Frame the separator in a clear explanatory cutaway with one existing inlet duct, a separate upper air outlet and a lower waste discharge toward the compactor. Show one small group of bags inside the separation chamber near the downward waste path. Keep waste out of the upper air outlet. No arrows. This is a conceptual process model, not a surveyed installation.
```

### s08b_clean — 압축기 시작 상태
```text
Edit the supplied image only. Preserve its camera, crop, miniature scale, architectural layout, materials and lighting unless explicitly changed below. Remove green scene IDs, all existing letters, numbers, logos, overlay stars, numeric signboards and explanatory arrows. Restore the background naturally. Do not add replacement writing. Keep white unpainted figurines. Vertical 9:16. Derive this view from the same s08 plant. Show an explanatory side cutaway of the compactor connected to the existing container. Make one ram, its straight guide and the waste chamber clearly distinguishable. Place the ram at its retracted starting position, with a small amount of waste ahead of it. Preserve the container and fixed equipment. No truck loading, exposed worker inside the machine or detached container.
```

### s09_clean — 지역 분포 배경
```text
Edit the supplied image only. Preserve its camera, crop, miniature scale, architectural layout, materials and lighting unless explicitly changed below. Remove green scene IDs, all existing letters, numbers, logos, overlay stars, numeric signboards and explanatory arrows. Restore the background naturally. Do not add replacement writing. Keep white unpainted figurines. Vertical 9:16. Remove the monetary sign, invented place labels and red pins. Preserve the existing model terrain and lighting without claiming geographic precision. Keep the scene clean for later editorial graphics. For the final national location graphic, use a separately verified outline of South Korea and manually positioned markers for Sejong, Yeongjong and Songdo; do not invent a national installation count.
```

### s10_clean — 두꺼운 관벽 비교
```text
Edit the supplied image only. Preserve its camera, crop, miniature scale, architectural layout, materials and lighting unless explicitly changed below. Remove green scene IDs, all existing letters, numbers, logos, overlay stars, numeric signboards and explanatory arrows. Restore the background naturally. Do not add replacement writing. Keep white unpainted figurines. Vertical 9:16. Remove all dimension text, tags and measuring lines. Preserve the pipe outer profile, cross-section plane, supports, inspector and lighting. Make the initial visible steel wall clear and solid, with no holes. Do not alter the elbow or position. This is a qualitative conceptual comparison, not a calibrated thickness drawing.
```

### e10_clean — 얇아진 국부 관벽 비교
```text
Edit the supplied image only. Preserve its camera, crop, miniature scale, architectural layout, materials and lighting unless explicitly changed below. Remove green scene IDs, all existing letters, numbers, logos, overlay stars, numeric signboards and explanatory arrows. Restore the background naturally. Do not add replacement writing. Keep white unpainted figurines. Vertical 9:16. Edit s10_clean directly. Preserve the exact outer pipe profile, cross-section plane, camera, supports, inspector and light. Change only one visible local portion of the inner wall to show thinning and corrosion. Keep the outer diameter and the rest of the pipe unchanged. No new through-hole, collapsed rim or enlarged opening. Do not insert measurements or simulate a precise thickness ratio.
```

### s11_clean — 부식 점검
```text
Edit the supplied image only. Preserve its camera, crop, miniature scale, architectural layout, materials and lighting unless explicitly changed below. Remove green scene IDs, all existing letters, numbers, logos, overlay stars, numeric signboards and explanatory arrows. Restore the background naturally. Do not add replacement writing. Keep white unpainted figurines. Vertical 9:16. Remove the human inspector from inside the pipe. Replace that person with one small wheeled inspection camera robot, much smaller than the pipe bore, carrying an attached headlight. Preserve the existing corrosion and residue. No added severe damage, falling rust, new hole or moving waste. Keep the pipe enclosed. This is a conceptual inspection scene.
```

### s12_clean — 운영비 배경
```text
Edit the supplied image only. Preserve its camera, crop, miniature scale, architectural layout, materials and lighting unless explicitly changed below. Remove green scene IDs, all existing letters, numbers, logos, overlay stars, numeric signboards and explanatory arrows. Restore the background naturally. Do not add replacement writing. Keep white unpainted figurines. Vertical 9:16. Remove the monetary board and all writing on papers and screens. Keep existing coin stacks at a fixed height and count, retaining their miniature material. Preserve the room, table and window view. Keep figurines seated with papers resting flat. Leave a clean area for a later caption. Do not add a recognizable real official.
```

### s13_clean — 영종 비가동 상징
```text
Edit the supplied image only. Preserve its camera, crop, miniature scale, architectural layout, materials and lighting unless explicitly changed below. Remove green scene IDs, all existing letters, numbers, logos, overlay stars, numeric signboards and explanatory arrows. Restore the background naturally. Do not add replacement writing. Keep white unpainted figurines. Vertical 9:16. Remove the monetary board and unsupported exaggerated cobwebs, debris or overgrowth. Preserve the intact seaside pavement and buildings. Standardize the waste inlets to the approved upright mailbox type, covered by secured grey tarps. Keep the figurine standing beside an inlet without uncovering it. This is a symbolic miniature representation, not a documentary photograph.
```

### s14_clean — 준공 시설
```text
Edit the supplied image only. Preserve its camera, crop, miniature scale, architectural layout, materials and lighting unless explicitly changed below. Remove green scene IDs, all existing letters, numbers, logos, overlay stars, numeric signboards and explanatory arrows. Restore the background naturally. Do not add replacement writing. Keep white unpainted figurines. Vertical 9:16. Remove the year pin, ceremonial ribbon, celebration crowd and flags. Keep the same completed, clean plant and equipment layout. Use a quiet daylight view without visible operation. Preserve roofline, roads, camera and surrounding buildings. Do not create a photographed opening ceremony or suggest that the plant has begun operation.
```

### e14_clean — 장기 미가동 비교
```text
Edit the supplied image only. Preserve its camera, crop, miniature scale, architectural layout, materials and lighting unless explicitly changed below. Remove green scene IDs, all existing letters, numbers, logos, overlay stars, numeric signboards and explanatory arrows. Restore the background naturally. Do not add replacement writing. Keep white unpainted figurines. Vertical 9:16. Edit s14_clean directly. Preserve identical daylight, camera, roofline, road layout and intact equipment. Add only restrained surface weathering while showing no operating activity. No crowd, heavy weeds, collapsed structure, boarded ruins or dramatic darkness. Keep the building whole. No year label; dates will be added in editing.
```

### s16_clean — 송도 검토·점검
```text
Edit the supplied image only. Preserve its camera, crop, miniature scale, architectural layout, materials and lighting unless explicitly changed below. Remove green scene IDs, all existing letters, numbers, logos, overlay stars, numeric signboards and explanatory arrows. Restore the background naturally. Do not add replacement writing. Keep white unpainted figurines. Vertical 9:16. Remove the crane, lifted or removed inlets, flatbed truck, red X and excavation. Restore intact pavement and firmly installed waste inlets. Preserve the Songdo-style seaside skyline. Place two white maintenance figurines outside the equipment, one holding a blank clipboard. No demolition or removal. The image communicates inspection and consideration only.
```

### s17_clean — 일부 비가동 상징
```text
Edit the supplied image only. Preserve its camera, crop, miniature scale, architectural layout, materials and lighting unless explicitly changed below. Remove green scene IDs, all existing letters, numbers, logos, overlay stars, numeric signboards and explanatory arrows. Restore the background naturally. Do not add replacement writing. Keep white unpainted figurines. Vertical 9:16. Preserve the road above and buried pipe below. Keep one small truck on the existing lane and one motionless bag inside the dark pipe. Remove arrows, airflow effects, warning flashes and pipe glows. Keep the collection building intact. No image-wide collapse or implication of a nationwide shutdown.
```

### s15_clean — 엔딩
```text
Edit the supplied image only. Preserve its camera, crop, miniature scale, architectural layout, materials and lighting unless explicitly changed below. Remove green scene IDs, all existing letters, numbers, logos, overlay stars, numeric signboards and explanatory arrows. Restore the background naturally. Do not add replacement writing. Keep white unpainted figurines. Vertical 9:16. Preserve the city layout, underground cross-section, evening light and miniature materials. Remove all text, arrows, flashing warnings and flowing effects. Keep the buried pipes still and naturally dark; retain normal city lights above. Keep a clear area for an editorial end caption. Do not add streets, branches, signs or new people.
```

## 2. c04·c07·c08 생성 결과 검수
실제 클립을 아직 받지 않아 합격 판정을 내리지 않았다. MP4 원본 c04, c07, c08a, c08b를 받으면 전체 재생과 정지 프레임을 함께 확인한다. 장면 이미지로는 역주행·깜빡임·프레임 간 구조 변형을 판정하지 않는다.
- c04: 0~2초 대기, 2~3초 밸브 개방, 3~5초 최하단 봉투 두 개 배출, 5~8초 정착. 고정 구도·단일 밸브·고정 관벽 유지. 봉투가 벽을 통과하거나 밸브 하우징이 녹으면 재생성.
- c07: 봉투는 근경에서 먼 굴곡 방향으로만 이동. 사람·난간·터널등·카메라 쪽 봉투·밝은 외부 출구가 생기면 재생성.
- c08a: 분리기 케이싱은 고정, 쓰레기는 하부로, 상부 공기 출구에는 쓰레기가 없어야 함.
- c08b: 같은 시설의 압축기에서 한 번의 직선 행정, 접촉한 쓰레기만 밀림, 컨테이너 고정. 노출된 작업자·장비 회전·자동 생성 쓰레기·트럭 상차가 있으면 재생성.
- 카메라 흔들림이나 음향만 문제이고 유효 구간이 충분하면 편집 보완. 구조 오류·잘못된 방향·잘못된 사실 표현이면 편집으로 숨기지 말고 수정.
- 결과 보고 형식: 컷 / 문제 시간대 / 실제 관찰 / 합격·편집 보완·재생성 / 수정 문장. 실제로 보지 않은 프레임은 판정하지 않음.

## 3. 사실 검토와 사용 결정
- 세종 246km: 운영 중 시설 기술진단 범위의 총 관로 길이로 보도 확인. 전체 길이와 한 봉투의 이동거리를 구분.
- 수거 운전: 제조사 공식 설명은 저장량 센서에 의한 자동 수거 운전도 설명하므로 ‘정해진 시간에만’이라는 단정 삭제.
- 관내 20~30m/s: KDS 33 55 05 재게시 자료에 일반폐기물 공기속도 범위가 있으나 공식 원문은 이번에 직접 읽지 못함. 세종 실측값도 확인 못함. 최종 음성에서 수치 제외. 제조사의 봉투 이송속도 약 70km/h와 공기속도를 같은 물리량으로 간주하지 않음.
- 2km: 제조사 설명의 가능한 집하장 거리 사례이며 모든 세종 시설의 실측 이송거리 아님. 최종 음성에서 제외.
- 전국 30여곳·1.7~2조원: 2026-09-28 대전일보 사설의 추산 표현 확인. 공식 집계 원문과 범위·연도 확인이 되지 않아 최종 음성·숫자판에서 제외.
- 20.9→1.94mm: 2026-10-21 뉴스피치/오마이뉴스 보도에서 제5집하장 일부 관로 사례로 확인. 진단 원문과 측정표는 미확보. 최종 음성은 ‘보도됐다’고 한정. 수치 자체를 독립적으로 검증 완료했다고 표현하지 않음.
- 음식물 원인·14년: 2026-09-29 연합뉴스는 세종시의 원인 설명과 관계 기관 반박을 함께 보도함. 단일 확정 원인처럼 말하지 않고 시의 설명으로 귀속. ‘염분이 정확히 14년 만에 쇠관을 갉아먹음’ 단정 삭제.
- 운영비: 2023-11-14 공식 시의회 회의록에서 2022년 약105억원, 2023년 약120억원 소요 예상 답변 확인. 현재 매년 동일 금액 단정 대신 2022년 약105억원 사용.
- 영종: 2026-09-14 연합뉴스에서 총사업비1,530억원·2014년12월준공·11년넘게미가동 확인. 2026-09-26 이데일리도 미가동 보도. 확인 자료의 기준일을 음성·자막에 명시. 2026-11-01은 준공 12주년 전이므로 ‘12년 동안 한 번도’ 단정 삭제.
- 송도: 2026-05-04 인천시 공식 공고에서 단계적 폐쇄 기술진단 용역 확인. 2026-05-17 연합뉴스는 대상이 2·4공구라고 명시. 송도 전체 철거·철거완료 표현 금지. 최종 문장은 ‘기술진단 발주’라는 확인된 사건으로 작성.
- 현재 전체 크린넷 정지: 근거 없음. 비가동·부식·폐쇄 검토의 지역별 사례를 구분. 엔딩은 유지관리 과제로 변경.

## 4. 녹음용 최종 대본
세종시 땅 밑엔, 쓰레기가 지나가는 관이 총 이백사십육 킬로미터나 깔려 있습니다.
아파트에서 버린 봉투를, 집하장까지 땅속으로 보내거든요.
우체통처럼 생긴 이 통, 크린넷 투입구예요.
봉투는 아래에 모였다가, 수거 운전이 시작되면 배출 밸브를 통과합니다.
집하장의 커다란 송풍기가, 관 속에 이송 기류를 만드는 거죠.
봉투를 움직이는 건, 지상에 부는 바람이 아니라 관 안의 공기입니다.
쓰레기는 이 관을 따라, 떨어져 있는 집하장으로 이동해요.
거기서 공기와 쓰레기를 나누고, 압축해 컨테이너에 담습니다.
세종과 영종, 송도. 여러 신도시가 이런 시스템을 선택했죠.
그런데 세종 일부 관로는, 두께가 일 점 구사 밀리미터까지 줄었다고 보도됐어요.
세종시는 음식물 찌꺼기가, 관로 부식을 앞당긴다고 설명합니다.
운영비도 적지 않습니다. 세종은 이천이십이 년에만, 약 백오억 원이 들었어요.
영종하늘도시에는, 천오백삼십억 원을 들인 시설이 있습니다.
이천십사 년 말 준공됐지만, 이천이십육 년 구월에도 가동하지 못한 상태로 보도됐죠.
송도 이·사공구는, 단계적 폐쇄를 위한 기술진단까지 발주했습니다.
쓰레기차를 줄이려던 시스템. 이제는 오래 유지하는 방법이 과제가 됐습니다.
몰랐다면 좋아요, 신도시 사는 친구에게 보내 주세요.
우리 동네 길 밑에는, 이런 이야기가 숨어 있었습니다.

## 5. 대본 변경에 따른 화면 수정
- c06: 풍속숫자판을 재합성하지 않음. ‘관내 기류로 이송’ 사용.
- c07: ‘2km’ 자막 삭제.
- c09: 30개 핀·2조원 삭제. 확인한 세종·영종·송도 세 지역만 표시.
- c10: 특정 관로 보도 사례, 출처와 2026-10-21 표기. 숫자 비교는 고정 이미지 편집. 20.9→1.94mm 보도 내용을 화면에 사용할 경우 ‘세종 제5집하장 일부 관로·보도 기준’을 함께 표시.
- c11: ‘14년·염분이 원인’ 단정 자막 대신 ‘관로 부식 문제’와 시 설명임을 표기.
- c12: ‘2022년 운영비 약105억원’, ‘세종시의회 2023-11-14 답변’.
- c13: ‘영종하늘도시·총사업비1,530억원’.
- c14: ‘2014년12월 준공→2026년9월 미가동 보도’. ‘12년’ 고정문구 삭제.
- c16: ‘송도2·4공구·단계적 폐쇄 기술진단 발주(2026년5월)’.
- c17: 실제 어느 도시 전체가 정지한 것처럼 보이는 자막 삭제. ‘일부 비가동시설 개념 재현’. 새 엔딩 대사와 시각적 비중을 맞춰 정지 시설 컷이 너무 길지 않게 사용.
- 음성이 달라졌으므로 기존93초 배분은 확정값으로 재사용하지 않고 녹음 후 조정.

## 참고 자료
- [제조사 공식 시스템 설명](https://www.envacgroup.com/discover-the-envac-system/systems-and-solutions/stationary-pneumatic/)
- [제조사 거리·이송 설명](https://www.envacgroup.com/envac-city/envac-city-cities/)
- [세종 기술진단 246km 보도·2025-04-23](https://www.fnnews.com/news/202504231559419400)
- [세종 운영비 공식 회의록·2023-11-14](https://council.sejong.go.kr/cms/mntsViewer.do?mntsId=6075)
- [부식·음식물수거 논의·2026-09-29](https://www.yna.co.kr/view/AKR20260928146800063)
- [일부 관로 두께 보도·2026-10-21](https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CMPT_CD=RPORT&CNTN_CD=A0003277358)
- [영종 준공·사업비·미가동 보도·2026-09-14](https://www.yna.co.kr/view/AKR20260914069800065)
- [영종 미가동 후속보도·2026-09-26](https://m1.edaily.co.kr/News/Read?mediaCodeNo=257&newsId=02109046645584056)
- [송도 공식 용역공고·2026-05-04](https://www.incheon.go.kr/IC010307/view?curPage=93&gosigbn=A&sno=66177)
- [송도 대상구역 보도·2026-05-17](https://www.yna.co.kr/view/AKR20260515100900065)
- [전국합계 추산의 사설 출처·2026-09-28](https://v.daum.net/v/pBnHYCfzw0)

