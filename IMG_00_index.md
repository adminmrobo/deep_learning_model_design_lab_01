# 딥러닝 설계도면 연구실 01 — 이미지 제작 명세서 (IMG_00_index)

지금 페이지에 들어 있는 표지는 캐릭터 팩 픽셀아트를 모눈 바탕에 배치한 **대체 표지**입니다(`build/covers.py`). 아래 지시문으로 Genspark 등에서 표지를 받으면 `assets/img/covers/cover_NN.webp`(1600×900, 220 KB 이하)로 바꿔 넣고, `cover_manifest.json`의 status를 `ok`로 고칩니다.

## 공통 규칙
- 그림체: detailed 16-bit SNES-era pixel art, drawn natively at 1920×1080 with small dense pixels (fine detail on faces, hands, props)
- 배경: **white background** with a faint light-blue blueprint grid (연구실 스킬 흰 배경 지침)
- 그림 안 글자·숫자·로고 금지 (no text, no letters, no logos)
- 쓰지 않는 말: "작은 격자로 그린 뒤 4배 확대", "clearly visible square pixels"
- 얼굴·손은 가운데 80% 안전 영역 안
- 조수 하루·인턴 시아·인턴 모아는 좌우 뒤집기 금지

## DL-01 · FNN (피드포워드 신경망) — 작성 조수 하루
```
detailed 16-bit SNES-era pixel art, wide 16:9 cover illustration, white background with a faint light-blue blueprint grid. One author presenting a hand-drawn engineering blueprint: a large blueprint sheet showing three columns of square nodes joined by thin lines, flowing left to right. Character(s): girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans. Friendly, proud expression, holding the blueprint toward the viewer. Clean composition, characters on the right third, prop on the left two thirds. no text, no letters, no logos.
```

## DL-02 · CNN (합성곱 신경망) — 작성 조수 하루
```
detailed 16-bit SNES-era pixel art, wide 16:9 cover illustration, white background with a faint light-blue blueprint grid. One author presenting a hand-drawn engineering blueprint: a blueprint sheet with a small magnifying glass sliding over a pixel grid photo of a battery cell. Character(s): girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans. Friendly, proud expression, holding the blueprint toward the viewer. Clean composition, characters on the right third, prop on the left two thirds. no text, no letters, no logos.
```

## DL-03 · RNN (순환 신경망) — 작성 인턴 모아
```
detailed 16-bit SNES-era pixel art, wide 16:9 cover illustration, white background with a faint light-blue blueprint grid. One author presenting a hand-drawn engineering blueprint: a blueprint sheet with four identical green boxes in a row passing a small notebook from one to the next. Character(s): gentle girl maid intern, long ash-beige wavy hair, white frilled maid headband with a ribbon over the left ear, amber-brown eyes, red and navy plaid bow tie, camel knit cardigan, white frilled apron, black skirt. Friendly, proud expression, holding the blueprint toward the viewer. Clean composition, characters on the right third, prop on the left two thirds. no text, no letters, no logos.
```

## DL-04 · LSTM (장단기 기억 신경망) — 작성 인턴 모아
```
detailed 16-bit SNES-era pixel art, wide 16:9 cover illustration, white background with a faint light-blue blueprint grid. One author presenting a hand-drawn engineering blueprint: a blueprint sheet with a brass conveyor belt carrying memory cubes and three small gates with sliders. Character(s): gentle girl maid intern, long ash-beige wavy hair, white frilled maid headband with a ribbon over the left ear, amber-brown eyes, red and navy plaid bow tie, camel knit cardigan, white frilled apron, black skirt. Friendly, proud expression, holding the blueprint toward the viewer. Clean composition, characters on the right third, prop on the left two thirds. no text, no letters, no logos.
```

## DL-05 · GRU (게이트 순환 유닛) — 작성 인턴 모아
```
detailed 16-bit SNES-era pixel art, wide 16:9 cover illustration, white background with a faint light-blue blueprint grid. One author presenting a hand-drawn engineering blueprint: a blueprint sheet with a teapot and a mixing dial labeled only with colored marks, two small gates. Character(s): gentle girl maid intern, long ash-beige wavy hair, white frilled maid headband with a ribbon over the left ear, amber-brown eyes, red and navy plaid bow tie, camel knit cardigan, white frilled apron, black skirt. Friendly, proud expression, holding the blueprint toward the viewer. Clean composition, characters on the right third, prop on the left two thirds. no text, no letters, no logos.
```

## DL-06 · AE (오토인코더) — 작성 인턴 시아
```
detailed 16-bit SNES-era pixel art, wide 16:9 cover illustration, white background with a faint light-blue blueprint grid. One author presenting a hand-drawn engineering blueprint: a blueprint sheet shaped like an hourglass: wide on both sides, a narrow neck in the middle. Character(s): calm girl maid intern, long straight jet-black hair with side-swept bangs, no headdress, gray eyes, small silver drop earrings, charcoal-black long-sleeved maid dress, large gray bow, long white frilled apron. Friendly, proud expression, holding the blueprint toward the viewer. Clean composition, characters on the right third, prop on the left two thirds. no text, no letters, no logos.
```

## DL-07 · DBN (심층 신뢰 신경망) — 작성 인턴 시아
```
detailed 16-bit SNES-era pixel art, wide 16:9 cover illustration, white background with a faint light-blue blueprint grid. One author presenting a hand-drawn engineering blueprint: a blueprint sheet with stacked drawers, the lowest drawer neatly organized first, an old archive stamp. Character(s): calm girl maid intern, long straight jet-black hair with side-swept bangs, no headdress, gray eyes, small silver drop earrings, charcoal-black long-sleeved maid dress, large gray bow, long white frilled apron. Friendly, proud expression, holding the blueprint toward the viewer. Clean composition, characters on the right third, prop on the left two thirds. no text, no letters, no logos.
```

## DL-08 · GAN (적대적 생성 신경망) — 작성 인턴 시아
```
detailed 16-bit SNES-era pixel art, wide 16:9 cover illustration, white background with a faint light-blue blueprint grid. One author presenting a hand-drawn engineering blueprint: a blueprint sheet split in two: a forger desk with a stamp and an appraiser desk with a loupe. Character(s): calm girl maid intern, long straight jet-black hair with side-swept bangs, no headdress, gray eyes, small silver drop earrings, charcoal-black long-sleeved maid dress, large gray bow, long white frilled apron. Friendly, proud expression, holding the blueprint toward the viewer. Clean composition, characters on the right third, prop on the left two thirds. no text, no letters, no logos.
```

## DL-09 · Transformer (트랜스포머) — 작성 조수 하루
```
detailed 16-bit SNES-era pixel art, wide 16:9 cover illustration, white background with a faint light-blue blueprint grid. One author presenting a hand-drawn engineering blueprint: a blueprint sheet with many small word tiles connected by colored attention lines of varying thickness. Character(s): girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans. Friendly, proud expression, holding the blueprint toward the viewer. Clean composition, characters on the right third, prop on the left two thirds. no text, no letters, no logos.
```

## DL-10 · REVIEW (총괄 도면 감수) — 작성 감수 · 초파리 연구원 & 주판봇
```
detailed 16-bit SNES-era pixel art, wide 16:9 cover illustration, white background with a faint light-blue blueprint grid. Two reviewers presenting a hand-drawn engineering blueprint: nine small blueprint sheets pinned in a 3x3 grid on a white board, a red pen and a checklist clipboard. Character(s): anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus. Friendly, proud expression, holding the blueprint toward the viewer. Clean composition, characters on the right third, prop on the left two thirds. no text, no letters, no logos.
```

## INDEX (cover_00)
```
detailed 16-bit SNES-era pixel art, wide 16:9 group illustration, white background with a faint light-blue blueprint grid. Five lab members standing in a row, each holding a rolled blueprint: girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; gentle girl maid intern, long ash-beige wavy hair, white frilled maid headband with a ribbon over the left ear, amber-brown eyes, red and navy plaid bow tie, camel knit cardigan, white frilled apron, black skirt; calm girl maid intern, long straight jet-black hair with side-swept bangs, no headdress, gray eyes, small silver drop earrings, charcoal-black long-sleeved maid dress, large gray bow, long white frilled apron; anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus. The fruit fly and the robot hold a red pen and a checklist as reviewers. no text, no letters, no logos.
```
