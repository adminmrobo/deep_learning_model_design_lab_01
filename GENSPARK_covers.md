# 딥러닝 설계도면 연구실 01 — Genspark 표지 요청문

연구실 스킬 18-14-4 틀. **요청문 하나 = Genspark 대화 하나**로 붙여 넣습니다. 같은 비율(16:9)끼리 3장 이하로 묶었어요.

## 진행 순서

1. **대화 1(목차 표지)을 먼저** 받아 그림체·캐릭터 외형을 확인합니다.
2. 마음에 들면 그 목차 표지를 **참고 그림으로 함께 올려** 대화 2~5를 진행합니다 (첨부 목록에 `cover_00`이라고 적어 둔 곳).
3. 받은 그림은 아래 저장 이름으로 저장해 보내 주시면, 1600×900 WebP(220 KB 이하)로 바꿔 넣고 목차 썸네일·공유 미리보기도 다시 자릅니다.

## 참고 이미지 (꾸러미 `refs/` 폴더)

| 파일 | 캐릭터 |
|---|---|
| `refs/ref_01_doc.png` | 박사 |
| `refs/ref_02_haru.png` | 조수 하루 |
| `refs/ref_03_fly.png` | 초파리 연구원 |
| `refs/ref_04_jupanbot.png` | 주판봇 |
| `refs/ref_05_moa.png` | 인턴 모아 |
| `refs/ref_06_sia.png` | 인턴 시아 |

## 저장 이름 체크리스트

| 대화 | 저장 이름 | 도면 | 받음 |
|---|---|---|---|
| 대화 1 | `cover_00.png` | INDEX · 딥러닝 설계도면 연구실 01 | ☐ |
| 대화 2 | `cover_01.png` | DL-01 FNN · 피드포워드 신경망 (작성 하루) | ☐ |
| 대화 2 | `cover_02.png` | DL-02 CNN · 합성곱 신경망 (작성 하루) | ☐ |
| 대화 2 | `cover_09.png` | DL-09 TRANSFORMER · 트랜스포머 (작성 하루) | ☐ |
| 대화 3 | `cover_03.png` | DL-03 RNN · 순환 신경망 (작성 모아) | ☐ |
| 대화 3 | `cover_04.png` | DL-04 LSTM · 장단기 기억 (작성 모아) | ☐ |
| 대화 3 | `cover_05.png` | DL-05 GRU · 게이트 순환 유닛 (작성 모아) | ☐ |
| 대화 4 | `cover_06.png` | DL-06 AUTOENCODER · 오토인코더 (작성 시아) | ☐ |
| 대화 4 | `cover_07.png` | DL-07 DBN · 심층 신뢰 신경망 (작성 시아) | ☐ |
| 대화 4 | `cover_08.png` | DL-08 GAN · 적대적 생성 신경망 (작성 시아) | ☐ |
| 대화 5 | `cover_10.png` | DL-10 REVIEW · 총괄 도면 감수 (초파리 · 주판봇) | ☐ |

---

## 대화 1 · 목차 표지 (먼저 받아 그림체 확인)

**첨부:** `ref_02_haru.png`, `ref_05_moa.png`, `ref_06_sia.png`, `ref_01_doc.png`, `ref_03_fly.png`, `ref_04_jupanbot.png`

### cover_00 — INDEX · 딥러닝 설계도면 연구실 01

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_00 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 장소 | 흰 제도실, 옅은 하늘색 모눈 |
| 주제 은유 | 아홉 장의 둘둘 만 설계도(분홍·카멜·보라 통)와 벽의 빈 도면 아홉 장 |
| 캐릭터 포즈 | 하루·모아·시아가 앞줄에서 각자 둘둘 만 설계도 통을 들고 / 박사는 가운데 뒤에서 벽의 3×3 도면판을 가리킴 / 초파리는 왼쪽에서 클립보드 / 주판봇은 오른쪽에서 주판 |
| 대체 글 (alt) | 모눈 바탕의 하얀 제도실에서 하루, 모아, 시아가 설계도 통을 들고 서 있고, 뒤에서 박사가 아홉 장짜리 도면판을 가리키며 초파리 연구원과 주판봇이 양옆에서 지켜보는 픽셀아트 |
| 앞 표지와 다른 점 | 시리즈 첫 표지 — 여섯 캐릭터 모두, 도면판 전경 |

**Genspark에 붙여 넣기 ↓**

```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘. 한 장씩 따로, 아래 순서대로.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (가로 1600 이상에서 그린 작고 촘촘한 픽셀로 세밀하게 — 작은 그림을 확대한 큰 네모 블록 금지, 매끈한 일러스트·벡터·수채화·3D 금지)
- 배경은 밝은 흰색 제도실, 벽과 바닥에 옅은 하늘색 모눈
- 첨부한 참고 이미지의 캐릭터를 같은 외형으로 그릴 것 (조수 하루·인턴 시아·인턴 모아는 좌우 뒤집기 금지)
- 그림 안에 글자·숫자·로고를 넣지 말 것 (설계도에는 선과 도형만)
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
각 장은 아래 영어 프롬프트를 그대로 써 줘.

[1장] cover_00 — INDEX · 딥러닝 설계도면 연구실 01
Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art rendered natively at high resolution with small, dense pixels (each art pixel about 2 screen pixels at 1600 px width — NOT a small image blown up into big square blocks), rich detail in faces, hair, hands, clothes and props, bold dark outline, 2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
Scene: a bright white drafting studio with a faint light-blue blueprint grid on the walls and floor, large drafting tables, rolled blueprint tubes, soft daylight.
Characters (6):
  girl researcher Haru, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, front center-left, hugging a pink rolled blueprint tube, cheerful;
  gentle girl maid intern Moa, long ash-beige wavy hair, white frilled maid headband with a ribbon over the left ear, amber-brown eyes, red and navy plaid bow tie, camel knit cardigan, white frilled apron, black skirt, front center, holding a caramel-colored rolled blueprint tube with both hands, gentle smile;
  calm girl maid intern Sia, long straight jet-black hair with side-swept bangs, no headdress, gray eyes, small silver drop earrings, charcoal-black long-sleeved maid dress, large gray bow, long white frilled apron, front center-right, holding a violet rolled blueprint tube upright, calm and composed;
  chibi scientist professor, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center back, pointing a long pointer at a wall board with nine blank blueprint sheets pinned in a 3x3 grid;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, holding a clipboard checklist and a red pen, curious;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left, holding a wooden abacus, excited;
Visual metaphor of the topic: nine blank blueprint sheets pinned in a 3x3 grid, color-coded corners (pink, caramel, violet), and three rolled blueprint tubes in the same colors.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the 3x3 board of blueprint sheets.
Mood: proud, welcoming, a team about to present their work.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands. Blueprint sheets show only lines and shapes, never writing.

```

---

## 대화 2 · 하루 도면 3장

**첨부:** `ref_02_haru.png`, `ref_01_doc.png`, `ref_03_fly.png`, `ref_04_jupanbot.png`, `cover_00` (받은 목차 표지)

### cover_01 — DL-01 FNN · 피드포워드 신경망 (작성 하루)

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_01 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 장소 | 흰 제도실, 옅은 하늘색 모눈 |
| 주제 은유 | 왼쪽→오른쪽으로만 흐르는 세 줄의 네모 노드 설계도 |
| 캐릭터 포즈 | 하루가 제도대에 큰 설계도를 펼침 / 박사는 뒤에서 T자를 들고 / 초파리는 왼쪽에서 돋보기 / 주판봇은 오른쪽에서 주판 |
| 대체 글 (alt) | 하루가 제도대 위에 왼쪽에서 오른쪽으로만 선이 이어진 신경망 설계도를 펼치고, 박사와 초파리 연구원, 주판봇이 들여다보는 픽셀아트 |
| 앞 표지와 다른 점 | INDEX의 도면판과 달리 제도대 위 한 장, 펼치는 동작 |

### cover_02 — DL-02 CNN · 합성곱 신경망 (작성 하루)

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_02 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 장소 | 흰 제도실, 옅은 하늘색 모눈 |
| 주제 은유 | 큰 픽셀 격자 사진 위를 미끄러지는 작은 빛나는 네모 창(필터) |
| 캐릭터 포즈 | 하루가 라이트 테이블의 큰 격자 사진 위로 작은 네모 창을 밀고 있음 / 박사는 뒤에서 팔짱 / 초파리는 왼쪽에서 쪼그려 앉아 관찰 / 주판봇은 오른쪽에서 사진 더미를 들고 |
| 대체 글 (alt) | 하루가 라이트 테이블 위 배터리 셀 픽셀 사진 위로 작은 빛나는 네모 창을 밀고, 박사와 초파리 연구원, 주판봇이 지켜보는 픽셀아트 |
| 앞 표지와 다른 점 | 01의 펼친 설계도 대신 라이트 테이블과 미끄러지는 작은 창 |

### cover_09 — DL-09 TRANSFORMER · 트랜스포머 (작성 하루)

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_09 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 장소 | 흰 제도실, 옅은 하늘색 모눈 |
| 주제 은유 | 빈 단어 카드들을 굵기가 다른 색실이 서로 잇는 코르크판(어텐션) |
| 캐릭터 포즈 | 하루가 코르크판 앞에서 카드 하나를 가리키고 색실이 다른 카드로 뻗음 / 박사는 뒤에서 실타래를 건넴 / 초파리는 왼쪽에서 가는 실을 확인 / 주판봇은 오른쪽에서 실타래를 잔뜩 안음 |
| 대체 글 (alt) | 하루가 빈 카드들이 굵기가 다른 색실로 서로 이어진 코르크판 앞에서 카드 하나를 가리키고, 박사와 초파리 연구원, 주판봇이 함께 보는 픽셀아트 |
| 앞 표지와 다른 점 | 제도대·라이트 테이블이 아닌 벽면 코르크판과 색실 |

**Genspark에 붙여 넣기 ↓**

```
웹페이지 맨 위에 거는 표지 그림 3장을 만들어 줘. 한 장씩 따로, 아래 순서대로.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (가로 1600 이상에서 그린 작고 촘촘한 픽셀로 세밀하게 — 작은 그림을 확대한 큰 네모 블록 금지, 매끈한 일러스트·벡터·수채화·3D 금지)
- 배경은 밝은 흰색 제도실, 벽과 바닥에 옅은 하늘색 모눈
- 첨부한 참고 이미지의 캐릭터를 같은 외형으로 그릴 것 (조수 하루·인턴 시아·인턴 모아는 좌우 뒤집기 금지)
- 그림 안에 글자·숫자·로고를 넣지 말 것 (설계도에는 선과 도형만)
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
각 장은 아래 영어 프롬프트를 그대로 써 줘.

[1장] cover_01 — DL-01 FNN · 피드포워드 신경망 (작성 하루)
Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art rendered natively at high resolution with small, dense pixels (each art pixel about 2 screen pixels at 1600 px width — NOT a small image blown up into big square blocks), rich detail in faces, hair, hands, clothes and props, bold dark outline, 2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
Scene: a bright white drafting studio with a faint light-blue blueprint grid on the walls and floor, large drafting tables, rolled blueprint tubes, soft daylight.
Characters (4):
  girl researcher Haru, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, center front, unrolling a large blueprint across a drafting table with both hands;
  chibi scientist professor, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center back, holding a T-square, nodding;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, leaning in with a magnifying glass;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left, holding a wooden abacus up high;
Visual metaphor of the topic: a large blueprint showing three columns of small square nodes (green, yellow, pink) joined by thin lines that flow only from left to right, with small arrowheads pointing right.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the unrolled blueprint with left-to-right lines.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands. Blueprint sheets show only lines and shapes, never writing.

[2장] cover_02 — DL-02 CNN · 합성곱 신경망 (작성 하루)
Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art rendered natively at high resolution with small, dense pixels (each art pixel about 2 screen pixels at 1600 px width — NOT a small image blown up into big square blocks), rich detail in faces, hair, hands, clothes and props, bold dark outline, 2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
Scene: a bright white drafting studio with a faint light-blue blueprint grid on the walls and floor, large drafting tables, rolled blueprint tubes, soft daylight.
Characters (4):
  girl researcher Haru, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, center front, sliding a small glowing square frame across a large pixel-grid photo on a light table;
  chibi scientist professor, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center back, arms crossed, watching closely;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, crouching at table height, observing;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left, carrying a tall stack of photo cards;
Visual metaphor of the topic: a large pixel-grid photo of a cylindrical battery cell on a glowing light table, and a small bright square window sliding over it leaving a faint trail of highlighted squares.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the small glowing square window on the pixel grid.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands. Blueprint sheets show only lines and shapes, never writing.

[3장] cover_09 — DL-09 TRANSFORMER · 트랜스포머 (작성 하루)
Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art rendered natively at high resolution with small, dense pixels (each art pixel about 2 screen pixels at 1600 px width — NOT a small image blown up into big square blocks), rich detail in faces, hair, hands, clothes and props, bold dark outline, 2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
Scene: a bright white drafting studio with a faint light-blue blueprint grid on the walls and floor, large drafting tables, rolled blueprint tubes, soft daylight.
Characters (4):
  girl researcher Haru, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, center front, pointing at one card on the board while colored threads spread from it to all other cards;
  chibi scientist professor, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center back, handing over a spool of colored thread;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, inspecting a very thin thread closely;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left, arms full of many thread spools;
Visual metaphor of the topic: a corkboard with a row of blank word cards; every card is connected to every other card by colored threads of different thickness, the thickest threads glowing.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the glowing thick threads between the cards.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands. Blueprint sheets show only lines and shapes, never writing.

```

---

## 대화 3 · 모아 도면 3장

**첨부:** `ref_05_moa.png`, `ref_01_doc.png`, `ref_03_fly.png`, `ref_04_jupanbot.png`, `cover_00` (받은 목차 표지)

### cover_03 — DL-03 RNN · 순환 신경망 (작성 모아)

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_03 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 장소 | 흰 제도실, 옅은 하늘색 모눈 |
| 주제 은유 | 똑같은 초록 상자 넷이 한 줄로 서서 수첩(메모)을 다음으로 넘김 |
| 캐릭터 포즈 | 모아가 줄지은 초록 상자 넷 사이로 작은 수첩을 다음 상자로 건넴 / 박사는 뒤에서 차를 들고 / 초파리는 왼쪽 첫 상자 옆에서 흐려지는 글씨 없는 수첩을 들여다봄 / 주판봇은 오른쪽 끝 상자 옆 |
| 대체 글 (alt) | 모아가 한 줄로 놓인 똑같은 초록 상자 넷 사이로 작은 수첩을 다음 상자로 건네고, 박사와 초파리 연구원, 주판봇이 보는 픽셀아트 |
| 앞 표지와 다른 점 | 하루 표지들과 다른 주인공(모아), 수첩을 건네는 동작, 화분과 찻잔 |

### cover_04 — DL-04 LSTM · 장단기 기억 (작성 모아)

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_04 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 장소 | 흰 제도실, 옅은 하늘색 모눈 |
| 주제 은유 | 작은 기억 상자를 싣고 흐르는 황동 컨베이어와 레버 달린 작은 문 세 개 |
| 캐릭터 포즈 | 모아가 컨베이어 옆 세 레버 중 하나를 당김 / 박사는 뒤에서 기름통 / 초파리는 왼쪽에서 문 하나를 살핌 / 주판봇은 오른쪽에서 컨베이어 끝 상자를 받음 |
| 대체 글 (alt) | 모아가 작은 기억 상자를 싣고 흐르는 황동 컨베이어 옆에서 작은 문 세 개의 레버를 조절하고, 박사와 초파리 연구원, 주판봇이 보는 픽셀아트 |
| 앞 표지와 다른 점 | 03의 상자 줄 대신 길게 흐르는 컨베이어와 문 세 개 |

### cover_05 — DL-05 GRU · 게이트 순환 유닛 (작성 모아)

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_05 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 장소 | 흰 제도실, 옅은 하늘색 모눈 |
| 주제 은유 | 두 색 다이얼이 달린 찻주전자로 옛 차와 새 차를 섞음(문 두 개) |
| 캐릭터 포즈 | 모아가 두 색 다이얼 달린 찻주전자로 찻잔에 따름 / 박사는 뒤에서 찻잔을 받침 / 초파리는 왼쪽에서 레버 두 개를 셈 / 주판봇은 오른쪽에서 커다란 주전자를 들고 옴 |
| 대체 글 (alt) | 모아가 두 색 다이얼이 달린 찻주전자로 차를 섞어 따르고, 박사와 초파리 연구원, 주판봇이 보는 픽셀아트 |
| 앞 표지와 다른 점 | 04의 기계 컨베이어 대신 차 탁자, 레버 두 개만 |

**Genspark에 붙여 넣기 ↓**

```
웹페이지 맨 위에 거는 표지 그림 3장을 만들어 줘. 한 장씩 따로, 아래 순서대로.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (가로 1600 이상에서 그린 작고 촘촘한 픽셀로 세밀하게 — 작은 그림을 확대한 큰 네모 블록 금지, 매끈한 일러스트·벡터·수채화·3D 금지)
- 배경은 밝은 흰색 제도실, 벽과 바닥에 옅은 하늘색 모눈
- 첨부한 참고 이미지의 캐릭터를 같은 외형으로 그릴 것 (조수 하루·인턴 시아·인턴 모아는 좌우 뒤집기 금지)
- 그림 안에 글자·숫자·로고를 넣지 말 것 (설계도에는 선과 도형만)
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
각 장은 아래 영어 프롬프트를 그대로 써 줘.

[1장] cover_03 — DL-03 RNN · 순환 신경망 (작성 모아)
Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art rendered natively at high resolution with small, dense pixels (each art pixel about 2 screen pixels at 1600 px width — NOT a small image blown up into big square blocks), rich detail in faces, hair, hands, clothes and props, bold dark outline, 2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
Scene: a bright white drafting studio with a faint light-blue blueprint grid on the walls and floor, large drafting tables, rolled blueprint tubes, soft daylight.
Characters (4):
  gentle girl maid intern Moa, long ash-beige wavy hair, white frilled maid headband with a ribbon over the left ear, amber-brown eyes, red and navy plaid bow tie, camel knit cardigan, white frilled apron, black skirt, center front, gently handing a small notebook from one green box to the next, a potted plant beside her;
  chibi scientist professor, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center back, holding a teacup, smiling;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, next to the first box, peering at a faded notebook;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left, next to the last box, waving;
Visual metaphor of the topic: four identical green boxes in a row on a long table; a small notebook is being passed from box to box, the notebooks getting paler toward the right.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the notebook being handed between the boxes.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands. Blueprint sheets show only lines and shapes, never writing.

[2장] cover_04 — DL-04 LSTM · 장단기 기억 (작성 모아)
Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art rendered natively at high resolution with small, dense pixels (each art pixel about 2 screen pixels at 1600 px width — NOT a small image blown up into big square blocks), rich detail in faces, hair, hands, clothes and props, bold dark outline, 2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
Scene: a bright white drafting studio with a faint light-blue blueprint grid on the walls and floor, large drafting tables, rolled blueprint tubes, soft daylight.
Characters (4):
  gentle girl maid intern Moa, long ash-beige wavy hair, white frilled maid headband with a ribbon over the left ear, amber-brown eyes, red and navy plaid bow tie, camel knit cardigan, white frilled apron, black skirt, center front, pulling one of three small levers beside the conveyor;
  chibi scientist professor, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center back, holding a small oil can;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, inspecting one of the little gates;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left, receiving cubes at the end of the conveyor;
Visual metaphor of the topic: a long brass conveyor belt running across the room carrying small glowing memory cubes, passing three small sluice gates with levers (one red, one blue, one yellow).
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the glowing cubes on the conveyor.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands. Blueprint sheets show only lines and shapes, never writing.

[3장] cover_05 — DL-05 GRU · 게이트 순환 유닛 (작성 모아)
Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art rendered natively at high resolution with small, dense pixels (each art pixel about 2 screen pixels at 1600 px width — NOT a small image blown up into big square blocks), rich detail in faces, hair, hands, clothes and props, bold dark outline, 2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
Scene: a bright white drafting studio with a faint light-blue blueprint grid on the walls and floor, large drafting tables, rolled blueprint tubes, soft daylight.
Characters (4):
  gentle girl maid intern Moa, long ash-beige wavy hair, white frilled maid headband with a ribbon over the left ear, amber-brown eyes, red and navy plaid bow tie, camel knit cardigan, white frilled apron, black skirt, center front, pouring tea from a teapot that has a two-color mixing dial;
  chibi scientist professor, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center back, holding out a teacup on a saucer;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, counting two small levers on the teapot;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left, proudly carrying an oversized teapot;
Visual metaphor of the topic: a teapot with a round two-color dial (half amber, half light blue) and two small levers, pouring a stream that blends both colors into one cup.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the two-color dial and the blended tea stream.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands. Blueprint sheets show only lines and shapes, never writing.

```

---

## 대화 4 · 시아 도면 3장

**첨부:** `ref_06_sia.png`, `ref_01_doc.png`, `ref_03_fly.png`, `ref_04_jupanbot.png`, `cover_00` (받은 목차 표지)

### cover_06 — DL-06 AUTOENCODER · 오토인코더 (작성 시아)

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_06 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 장소 | 흰 제도실, 옅은 하늘색 모눈 |
| 주제 은유 | 넓게 시작해 가운데가 아주 좁았다가 다시 넓어지는 모래시계 모양 유리 장치 |
| 캐릭터 포즈 | 시아가 모래시계 장치의 좁은 목을 가리킴 / 박사는 뒤에서 유리판을 닦음 / 초파리는 왼쪽에서 걸러지지 않는 빨간 구슬 하나를 집음 / 주판봇은 오른쪽에서 구슬을 잔뜩 부으려 함 |
| 대체 글 (alt) | 시아가 가운데가 아주 좁은 모래시계 모양 유리 장치의 목을 가리키고, 박사와 초파리 연구원, 주판봇이 보는 픽셀아트 |
| 앞 표지와 다른 점 | 모아 표지들의 따뜻한 소품과 달리 차분한 유리 장치, 주인공 시아 |

### cover_07 — DL-07 DBN · 심층 신뢰 신경망 (작성 시아)

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_07 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 장소 | 흰 제도실, 옅은 하늘색 모눈 |
| 주제 은유 | 맨 아래부터 한 층씩 정리된 서랍장과 오래된 설계도(역사 자료실) |
| 캐릭터 포즈 | 시아가 서랍장 맨 아래 서랍을 정돈 / 박사는 뒤에서 오래된 설계도 두루마리를 펼침 / 초파리는 왼쪽에서 먼지를 털며 살핌 / 주판봇은 오른쪽에서 맨 위 서랍을 먼저 열려 함 |
| 대체 글 (alt) | 시아가 역사 자료실의 서랍장을 맨 아래 서랍부터 정리하고, 박사가 오래된 설계도를 펼치며 초파리 연구원과 주판봇이 지켜보는 픽셀아트 |
| 앞 표지와 다른 점 | 새 장비가 아닌 오래된 자료실, 세피아 빛이 살짝 도는 서랍장 |

### cover_08 — DL-08 GAN · 적대적 생성 신경망 (작성 시아)

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_08 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 장소 | 흰 제도실, 옅은 하늘색 모눈 |
| 주제 은유 | 위조범 책상(주판봇이 그림 복제)과 감정사 책상(시아의 루페)이 마주 봄 |
| 캐릭터 포즈 | 시아가 감정사 책상에서 루페로 그림을 봄 / 박사는 가운데 뒤에서 심판처럼 서 있음 / 초파리는 왼쪽에서 진짜·가짜 두 그림을 나란히 듦 / 주판봇은 오른쪽 위조범 책상에서 붓으로 복제 중 |
| 대체 글 (alt) | 시아가 감정사 책상에서 루페로 그림을 살피고, 맞은편 책상에서 주판봇이 픽셀 그림을 따라 그리며, 박사와 초파리 연구원이 지켜보는 픽셀아트 |
| 앞 표지와 다른 점 | 시아 표지 중 유일하게 두 책상이 마주 보는 겨루기 구도 |

**Genspark에 붙여 넣기 ↓**

```
웹페이지 맨 위에 거는 표지 그림 3장을 만들어 줘. 한 장씩 따로, 아래 순서대로.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (가로 1600 이상에서 그린 작고 촘촘한 픽셀로 세밀하게 — 작은 그림을 확대한 큰 네모 블록 금지, 매끈한 일러스트·벡터·수채화·3D 금지)
- 배경은 밝은 흰색 제도실, 벽과 바닥에 옅은 하늘색 모눈
- 첨부한 참고 이미지의 캐릭터를 같은 외형으로 그릴 것 (조수 하루·인턴 시아·인턴 모아는 좌우 뒤집기 금지)
- 그림 안에 글자·숫자·로고를 넣지 말 것 (설계도에는 선과 도형만)
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
각 장은 아래 영어 프롬프트를 그대로 써 줘.

[1장] cover_06 — DL-06 AUTOENCODER · 오토인코더 (작성 시아)
Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art rendered natively at high resolution with small, dense pixels (each art pixel about 2 screen pixels at 1600 px width — NOT a small image blown up into big square blocks), rich detail in faces, hair, hands, clothes and props, bold dark outline, 2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
Scene: a bright white drafting studio with a faint light-blue blueprint grid on the walls and floor, large drafting tables, rolled blueprint tubes, soft daylight.
Characters (4):
  calm girl maid intern Sia, long straight jet-black hair with side-swept bangs, no headdress, gray eyes, small silver drop earrings, charcoal-black long-sleeved maid dress, large gray bow, long white frilled apron, center front, calmly pointing at the narrow neck of the apparatus;
  chibi scientist professor, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center back, polishing a glass panel;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, holding up one odd red bead;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left, about to pour a big bucket of beads;
Visual metaphor of the topic: a tall hourglass-shaped glass apparatus lying sideways: wide on the left, a very narrow neck in the middle, wide again on the right; blue beads flow through and come out in the same pattern, one red bead stuck at the neck.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the narrow neck of the hourglass apparatus.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands. Blueprint sheets show only lines and shapes, never writing.

[2장] cover_07 — DL-07 DBN · 심층 신뢰 신경망 (작성 시아)
Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art rendered natively at high resolution with small, dense pixels (each art pixel about 2 screen pixels at 1600 px width — NOT a small image blown up into big square blocks), rich detail in faces, hair, hands, clothes and props, bold dark outline, 2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
Scene: a bright white drafting studio with a faint light-blue blueprint grid on the walls and floor, large drafting tables, rolled blueprint tubes, soft daylight.
Characters (4):
  calm girl maid intern Sia, long straight jet-black hair with side-swept bangs, no headdress, gray eyes, small silver drop earrings, charcoal-black long-sleeved maid dress, large gray bow, long white frilled apron, center front, neatly arranging the bottom drawer of a tall cabinet;
  chibi scientist professor, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center back, unrolling an old yellowed blueprint scroll;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, dusting a drawer with a tiny brush;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left, reaching up eagerly toward the top drawer;
Visual metaphor of the topic: a tall wooden cabinet of stacked drawers; the bottom drawers are already neatly organized and glowing softly, the upper ones still closed; old archive atmosphere with a slight sepia tint, still a bright white room.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the neatly organized bottom drawers.
Mood: curious, nostalgic, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands. Blueprint sheets show only lines and shapes, never writing.

[3장] cover_08 — DL-08 GAN · 적대적 생성 신경망 (작성 시아)
Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art rendered natively at high resolution with small, dense pixels (each art pixel about 2 screen pixels at 1600 px width — NOT a small image blown up into big square blocks), rich detail in faces, hair, hands, clothes and props, bold dark outline, 2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
Scene: a bright white drafting studio with a faint light-blue blueprint grid on the walls and floor, large drafting tables, rolled blueprint tubes, soft daylight.
Characters (4):
  calm girl maid intern Sia, long straight jet-black hair with side-swept bangs, no headdress, gray eyes, small silver drop earrings, charcoal-black long-sleeved maid dress, large gray bow, long white frilled apron, center front-left at an appraiser desk, examining a small pixel painting through a jeweler loupe;
  chibi scientist professor, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center back, standing like a referee between the two desks;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, holding two nearly identical small paintings side by side;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left at a forger desk, carefully copying a pixel painting with a tiny brush;
Visual metaphor of the topic: two desks facing each other: an appraiser desk with a loupe and a lamp, and a forger desk with brushes and a half-finished copy of a small landscape pixel painting.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the two nearly identical paintings.
Mood: playful rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands. Blueprint sheets show only lines and shapes, never writing.

```

---

## 대화 5 · 감수 도면 1장

**첨부:** `ref_03_fly.png`, `ref_04_jupanbot.png`, `ref_01_doc.png`, `ref_02_haru.png`, `ref_05_moa.png`, `ref_06_sia.png`, `cover_00` (받은 목차 표지)

### cover_10 — DL-10 REVIEW · 총괄 도면 감수 (초파리 · 주판봇)

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_10 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 장소 | 흰 제도실, 옅은 하늘색 모눈 |
| 주제 은유 | 3×3으로 붙인 작은 설계도 아홉 장과 빨간 펜·체크리스트 |
| 캐릭터 포즈 | 초파리가 왼쪽 앞에서 빨간 펜으로 한 장에 동그라미 / 주판봇이 오른쪽 앞에서 주판을 튕기며 체크리스트 / 박사는 가운데 뒤에서 찍지 않은 승인 도장을 듦 / 하루·모아·시아는 뒤에서 긴장하며 지켜봄 |
| 대체 글 (alt) | 초파리 연구원이 빨간 펜으로 아홉 장짜리 도면판의 한 곳에 동그라미를 치고, 주판봇이 주판과 체크리스트로 세어 보며, 박사와 하루·모아·시아가 뒤에서 지켜보는 픽셀아트 |
| 앞 표지와 다른 점 | 주인공이 감수자 둘, 여섯 캐릭터 모두, 빨간 펜과 승인 도장 |

**Genspark에 붙여 넣기 ↓**

```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘. 한 장씩 따로, 아래 순서대로.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (가로 1600 이상에서 그린 작고 촘촘한 픽셀로 세밀하게 — 작은 그림을 확대한 큰 네모 블록 금지, 매끈한 일러스트·벡터·수채화·3D 금지)
- 배경은 밝은 흰색 제도실, 벽과 바닥에 옅은 하늘색 모눈
- 첨부한 참고 이미지의 캐릭터를 같은 외형으로 그릴 것 (조수 하루·인턴 시아·인턴 모아는 좌우 뒤집기 금지)
- 그림 안에 글자·숫자·로고를 넣지 말 것 (설계도에는 선과 도형만)
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
각 장은 아래 영어 프롬프트를 그대로 써 줘.

[1장] cover_10 — DL-10 REVIEW · 총괄 도면 감수 (초파리 · 주판봇)
Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art rendered natively at high resolution with small, dense pixels (each art pixel about 2 screen pixels at 1600 px width — NOT a small image blown up into big square blocks), rich detail in faces, hair, hands, clothes and props, bold dark outline, 2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
Scene: a bright white drafting studio with a faint light-blue blueprint grid on the walls and floor, large drafting tables, rolled blueprint tubes, soft daylight.
Characters (6):
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, front left facing right, circling a spot on one blueprint sheet with a red pen;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, front right facing left, flicking beads on a wooden abacus, a checklist clipped to his arm;
  chibi scientist professor, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, center back, holding an approval stamp that has not been stamped yet;
  girl researcher Haru, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, back left, watching nervously with hands clasped;
  gentle girl maid intern Moa, long ash-beige wavy hair, white frilled maid headband with a ribbon over the left ear, amber-brown eyes, red and navy plaid bow tie, camel knit cardigan, white frilled apron, black skirt, back center, holding a teacup, hopeful;
  calm girl maid intern Sia, long straight jet-black hair with side-swept bangs, no headdress, gray eyes, small silver drop earrings, charcoal-black long-sleeved maid dress, large gray bow, long white frilled apron, back right, calm, arms folded;
Visual metaphor of the topic: a large white board with nine small blueprint sheets pinned in a 3x3 grid (corners pink, caramel and violet), one small red circle drawn on one sheet.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner plain, bright and simple; the light falls on the 3x3 board and the red pen.
Mood: focused, careful, the moment before approval.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands. Blueprint sheets show only lines and shapes, never writing.

```

---

## 고칠 때 (같은 대화에서)

```
Same characters, same 16-bit pixel-art style and composition. Change only: {고칠 점}. Still pixel art, still no text.
```

자주 쓰는 고칠 점: `make the pixels smaller and denser, more detail on faces and hands` · `remove all writing from the blueprint sheets` · `Haru must have pink hair with two round buns and a navy streak` · `the robot must keep the beige CRT box body and tank treads`
