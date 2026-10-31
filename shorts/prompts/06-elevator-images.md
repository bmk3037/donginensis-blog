# 06편 장면 이미지 프롬프트 (ChatGPT용)

06편 「엘리베이터가 고장 나기 전에 수리 기사가 먼저 오는 곳이 있습니다」의 장면 이미지를 ChatGPT로 만들 때 씁니다. 이미지에는 움직임, 붉은 전류선, 숫자, 자막을 넣지 않습니다. 그건 합성 단계에서 얹습니다.

## 쓰는 법

1. ChatGPT 새 대화를 열고 아래 **공통 스타일**을 먼저 붙여 넣습니다.
2. 이어서 장면 프롬프트를 하나씩 붙여 넣어 이미지를 만듭니다. 마음에 들 때까지 다시 만들어도 됩니다.
3. 내려받은 이미지를 아래 파일 이름으로 저장해서 보내 주세요. 예: `06_s1_lobby.png`
4. 글자, 숫자, 로고가 이미지에 들어가면 "remove all text and logos"라고 다시 요청합니다.

## 공통 스타일 (먼저 붙여 넣기)

```
I will ask you for several images for one vertical short video. Keep the same look for all of them:
- Vertical 9:16 portrait image, 1024x1792 or the closest you support.
- Photorealistic 3D render, calm engineering-documentary mood, cinematic but not dramatic.
- Cool blue-grey palette with soft warm interior light. Clean, uncluttered composition.
- Korean apartment and Korean industrial settings, modern and realistic.
- Keep the bottom 30% of the frame calm and simple (dark floor or shadow), because subtitles go there.
- Absolutely no text, letters, numbers, signs with writing, logos, brand marks or watermarks anywhere.
- No visible faces. People only as back views or silhouettes.
Reply "ready" and wait for my first scene.
```

## 장면 프롬프트

| 파일 이름 | 비트 | 쓰는 시간 |
|---|---|---|
| `06_s1_lobby.png` | 1. 장면 열기 | 0–10초 |
| `06_s2_shaft.png` | 2. 균열 | 10–20초 |
| `06_s3_stuck.png` | 3. 딜레마 | 20–34초 |
| `06_s4_door.png` | 4. 발상 전환 | 34–52초 |
| `06_s5_night.png` | 5. 숫자 | 52–62초 |
| `06_s6_factory.png` | 6. 지금 여기로 (앞) | 62–69초 |
| `06_s7_open.png` | 6. 지금 여기로 (끝) | 69–77초 |

### 1. `06_s1_lobby.png` — 출근길 엘리베이터 앞

```
Scene 1. Morning in a Korean apartment elevator lobby. Brushed stainless-steel elevator doors are closed. In front of the doors stands a plain yellow A-frame caution stand with a completely blank face (no text, no symbols). A person in office clothes is seen from behind on the right, about to walk in and stopping. Soft daylight from the side, polished floor with faint reflections. Camera at eye level, slightly wide.
```

### 2. `06_s2_shaft.png` — 멀쩡한데 기사가 온다

```
Scene 2. Cutaway cross-section of a mid-rise Korean apartment building showing the elevator shaft in the center: the elevator car is halfway up the shaft, steel ropes rise to a small machine room at the top. The floors on both sides are dimly visible as clean architectural sections. At ground level on the right, a maintenance technician in work clothes with a toolbox walks toward the building, seen from behind. Precise, technical, documentary cutaway style.
```

### 3. `06_s3_stuck.png` — 층 사이에 멈춘 엘리베이터

```
Scene 3. The same cutaway elevator shaft, closer. The elevator car is stopped between two floors, its interior light slightly dimmer, a single passenger silhouette standing inside, seen from behind. The shaft walls, guide rails and landing doors above and below are visible. Tense but calm mood, subtle red-tinted emergency light inside the car.
```

### 4. `06_s4_door.png` — 문 장치와 센서

```
Scene 4. Close-up of the top of an elevator car door: the door operator unit with a small electric motor, belt and door hangers above two stainless-steel sliding door panels that are half open. A small sensor module is attached next to the motor. Clean technical close-up, shallow depth of field, cool light. Leave empty dark space on the right side of the frame for graphics.
```

### 5. `06_s5_night.png` — 밤의 아파트 단지

```
Scene 5. Night view of a large Korean apartment complex: several tall residential towers, many windows softly lit. Each tower shows a thin vertical glowing line along its elevator core, as if the elevator shafts were faintly visible. Wide shot from a slightly elevated angle, deep blue night sky, calm atmosphere. Leave the top 20% of the frame as empty sky for numbers.
```

### 6. `06_s6_factory.png` — 공장 모터와 제어반

```
Scene 6. Inside a clean Korean factory: a row of industrial electric motors and pumps connected by pipes in the foreground, and a grey industrial control cabinet with its door open in the background, neat wiring and a small blank display screen inside. Cool industrial lighting, documentary realism, no people.
```

### 7. `06_s7_open.png` — 다시 엘리베이터 앞, 문이 열린다

```
Scene 7. The same Korean apartment elevator lobby as scene 1, now with no caution stand. The elevator doors are open, warm light coming from inside the car, the floor reflecting the light. Hopeful, calm morning mood. No people.
```

## 합성 단계에서 얹는 것

- 느린 확대·이동(돌리 인)과 장면 전환
- 붉은 전류선(`#D4362A`): 기계실에서 퍼지는 신호(2번), 센서에서 이어지는 선(4번), 모터에서 제어반으로 가는 선(6번)
- 문 닫힘 시간 막대와 경고 표시(4번), "80만 대+"와 "−43%" 숫자(5번), 제어반 그래프(6번)
- '점검 중' 글자(1번 안내판), 한글 자막, 내레이션 음성
