# 39편 재료 메모 (Aside, 2026-10-25)

## 카드 39와 달라진 점 (사용자 승인)
- 도감이 등장: s01, s02, s05, s09, s10. s07은 도감이 팔(파란 소매+장갑)만. s03, s04, s06, s08은 사물만(사람 없음).
  - 카드의 "10개 모두 도감이"를 사용자가 "도감이 없어도 되면 없어도 되고, 후킹·좋아요 우선"으로 바꿈.
- s01·s02 멀티탭은 6구(대본 "구멍 6개"), s05는 히터를 벽 콘센트에 바로 꽂는 장면, s06은 멀티탭 3개 직렬 연결 + 벽 쪽 선 과열(작은 불꽃).
- 그림은 자체 검수 통과(손 개수, 소매, 양쪽 플러그 선 없음, 대본 일치).

## 음성
- voice.mp3: 타입캐스트 캐릭터 문정(38편과 같음), 속도 1.0, 약 71.0초. 카드의 15:06 수정본 대본 14문장 그대로.

## 클립 (Veo 3.1 Lite, 9:16, 8초, 720x1280, 무음)
- c01~c05: 완료(Flow 계정 mbiz3047). 
  - c01: 0~3초에 멀티탭에서 번개 같은 큰 스파크(대본보다 강함, 후킹용), 이후 차단기함을 가리킴.
  - c04: 4~6초에 멀티탭·가전에서 큰 불길이 치솟음(프롬프트는 '달아오름'이었으나 더 강하게 나옴). 편집 때 짧게 쓰거나 앞부분만 쓰기 권장.
  - c02, c03, c05: 프롬프트대로.
- c06~c10: 완료(Flow 계정 bmk3037, 프로젝트 꿀팁도감 39).
  - c06: 시작 그림에 이미 불꽃이 있어서, 프롬프트에서 불을 뺐는데도 불꽃이 계속되고 3초 뒤부터 검은 연기가 짙게 올라옴. c04와 불 장면이 겹치니 편집 때 짧게(0~3초 위주) 쓰기 권장.
  - c07: 스위치 끄고 천으로 닦는 동작은 맞음. 다만 3~6초 오른쪽 위에 살색 덩어리(팔/얼굴 일부)가 잠깐 비침 → 0~3초와 7초 이후 위주로 쓰기 권장.
  - c08: 불 없이 핀 사이로 주황빛 전기 줄기가 번지고 스파크(대본 '전기가 새는 길'과 맞음).
  - c09: 흔들어 보고 → 아래로 버리고 → 새 멀티탭 들고 웃음. 프롬프트대로.
  - c10: 폰 → 동파 예방 보온재 감은 배관 들고 손 흔들기. 프롬프트대로.
  - c06, c08은 불이 겹치지 않게 아래 프롬프트에서 'no flames and no fire'를 넣어 바꿔 만듦(실제 사용한 문장은 맨 아래 '실제 사용 c06/c08').

# 39 final clip prompts (start frame = img_v3/sNN.jpg, Veo 3.1 Lite, 9:16)

## c01 (start: s01.jpg)

```
For the first three seconds the chibi engineer holds one more plug over the already-full power strip, looking for a free socket, while tiny sparks flicker at the crowded plugs; he tilts his head at the camera with a questioning face. Then he turns, points at the breaker panel on the wall behind him with a knowing grin, and looks back at the camera. Camera: slow push-in. Style: same bright Pixar-like 3D animation, colors and lighting as the start frame. Audio: none. No on-screen text, no letters, no numbers, no logos, no camera cuts.
```

## c02 (start: s02.jpg)

```
The chibi engineer wags his raised finger left and right with a playful 'no, no' smile and shakes his head behind the full power strip. Camera: static, slight push-in. Style: same bright Pixar-like 3D animation, colors and lighting as the start frame. Audio: none. No on-screen text, no letters, no numbers, no logos, no camera cuts.
```

## c03 (start: s03.jpg)

```
For the first three seconds the power strip slowly rotates so the small blank rating label turns to face the camera. Then a big magnifying glass slides in over the label and the label glows softly as the camera pushes in closer. No people appear. Camera: slow push-in. Style: same bright Pixar-like 3D animation, colors and lighting as the start frame. Audio: none. No on-screen text, no letters, no numbers, no logos, no camera cuts.
```

## c04 (start: s04.jpg)

```
One by one the kettle, the hair dryer and the heater switch on; with each one the power strip and its cord glow warmer, from soft orange to warning red, with faint heat shimmer above it. No people appear. Camera: slow push-in toward the glowing strip. Style: same bright Pixar-like 3D animation, colors and lighting as the start frame. Audio: none. No on-screen text, no letters, no numbers, no logos, no camera cuts.
```

## c05 (start: s05.jpg)

```
The chibi engineer pushes the heater's plug firmly into the wall outlet, the small heater beside him lights up with a warm orange glow, and he turns to the camera with a thumbs up; the unused power strip stays set aside on the floor. Camera: static medium shot. Style: same bright Pixar-like 3D animation, colors and lighting as the start frame. Audio: none. No on-screen text, no letters, no numbers, no logos, no camera cuts.
```

## c06 (start: s06.jpg)

```
The camera slowly tracks along the chain from the farthest power strip to the first one by the wall; the first strip's cord near the wall outlet glows brighter red hot, with heat shimmer, small flickering flames and a thin wisp of smoke rising from it. No people appear. Camera: slow tracking along the chain, then hold on the hot cord. Style: same bright Pixar-like 3D animation, colors and lighting as the start frame. Audio: none. No on-screen text, no letters, no numbers, no logos, no camera cuts.
```

## c07 (start: s07.jpg)

```
The chibi engineer's gloved finger presses the power strip's switch off, then his other gloved hand wipes the dust away with the dry cloth in a few quick strokes; little puffs of dust float up and the strip becomes clean and white. Only his two arms in cobalt-blue sleeves are visible. Camera: slow push-in. Style: same bright Pixar-like 3D animation, colors and lighting as the start frame. Audio: none. No on-screen text, no letters, no numbers, no logos, no camera cuts.
```

## c08 (start: s08.jpg)

```
A thin glowing orange path slowly creeps across the damp dust between the prongs, glowing brighter, until a small bright spark pops and a tiny flame flickers. No people appear. Camera: very slow push-in. Style: same bright Pixar-like 3D animation, colors and lighting as the start frame. Audio: none. No on-screen text, no letters, no numbers, no logos, no camera cuts.
```

## c09 (start: s09.jpg)

```
The chibi engineer shakes the old scorched power strip next to his ear as if hearing a rattle, frowns, drops it into a small bin, then picks up the brand-new power strip with a smile. Camera: static, slight push-in. Style: same bright Pixar-like 3D animation, colors and lighting as the start frame. Audio: none. No on-screen text, no letters, no numbers, no logos, no camera cuts.
```

## c10 (start: s10.jpg)

```
For the first three seconds the chibi engineer holds up the new power strip and gives a confident nod, then taps the blank phone screen as if sending a message. After that he puts the phone away, holds up a small water pipe wrapped in white insulation foam with frost on it, and waves goodbye at the camera with a teasing smile. Camera: slow push-in. Style: same bright Pixar-like 3D animation, colors and lighting as the start frame. Audio: none. No on-screen text, no letters, no numbers, no logos, no camera cuts.
```



## 실제 사용 c06/c08 (위 원래 프롬프트 대신)

### c06
```
The camera slowly tracks along the chain from the farthest power strip to the first one by the wall; the first strip's cord near the wall outlet glows brighter red hot with heat shimmer and a thin wisp of smoke rising from it, no flames and no fire. No people appear. Camera: slow tracking along the chain, then hold on the hot cord. Style: same bright Pixar-like 3D animation, colors and lighting as the start frame. Audio: none. No on-screen text, no letters, no numbers, no logos, no camera cuts.
```

### c08
```
A thin glowing orange path slowly creeps across the damp dust between the prongs, glowing brighter, until one small bright spark pops and fades, no flames and no fire. No people appear. Camera: very slow push-in. Style: same bright Pixar-like 3D animation, colors and lighting as the start frame. Audio: none. No on-screen text, no letters, no numbers, no logos, no camera cuts.
```
