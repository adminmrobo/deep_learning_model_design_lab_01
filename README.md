# 딥러닝 설계도면 연구실 01 (DL BLUEPRINT)

조수 **하루**, 인턴 **모아**·**시아**가 대표 딥러닝 모델 9종을 한 장씩 "설계도면"으로 직접 그려 전달하고, **초파리 연구원**과 **주판봇**이 아홉 장을 한 장에 모아 감수하는 연구실 해설 시리즈입니다. 형식은 [LLM의 마법 주문서](https://adminmrobo.github.io/Automate_prompt_lab/)(터미널 머리 · 픽셀 글꼴 · 흰 배경)를 따릅니다.

- 사이트: https://adminmrobo.github.io/deep_learning_model_design_lab_01/
- 독자: AI를 처음 접하는 직장인·학생 (코드·수식을 몰라도 읽히게)

## 도면 목록

| 번호 | 도면 | 계열 | 작성 |
|---|---|---|---|
| — | [INDEX](index.html) | 목차 · 도면 읽는 법 | — |
| DL-01 | [FNN · 피드포워드 신경망](01_fnn.html) | 기본 구조 | 조수 하루 |
| DL-02 | [CNN · 합성곱 신경망](02_cnn.html) | 기본 구조 | 조수 하루 |
| DL-03 | [RNN · 순환 신경망](03_rnn.html) | 순서·기억 | 인턴 모아 |
| DL-04 | [LSTM · 장단기 기억](04_lstm.html) | 순서·기억 | 인턴 모아 |
| DL-05 | [GRU · 게이트 순환 유닛](05_gru.html) | 순서·기억 | 인턴 모아 |
| DL-06 | [오토인코더](06_autoencoder.html) | 압축·생성 | 인턴 시아 |
| DL-07 | [DBN · 심층 신뢰 신경망](07_dbn.html) | 압축·생성 | 인턴 시아 |
| DL-08 | [GAN · 적대적 생성 신경망](08_gan.html) | 압축·생성 | 인턴 시아 |
| DL-09 | [트랜스포머](09_transformer.html) | 기본 구조 | 조수 하루 |
| DL-10 | [총괄 도면 감수](10_review.html) | 감수 | 초파리 연구원 · 주판봇 |
| 마지막 장 | [실전 연습장 · 설계 의뢰 접수처](practice/index.html) | 연습 | 판정 · 박사 |

도면 한 장의 순서: 3줄 요약 → 등장인물 → 전체 구조도(모눈 SVG) → 부품 명세 → 왜 이 설계 | 수식은 동료가 대신 질문(손계산) → 일상·현장 → 실험대 → AI 판단 코너 → 한계 → 확인 퀴즈 → 감수 메모 → 지식 색인·온톨로지 꾸러미.

## 감수 결과 요약

참고 자료(「9 Deep Learning Algorithms Every Engineer Should Know」 인포그래픽 10장, 작성자 표기 없음)에서 **고침 7건 · 보충 4건**을 반영했습니다. 그림은 모두 새로 그렸습니다. 자세한 내용은 [10 감수 의견서](10_review.html#errata).

## 폴더

```
index.html, 01_fnn.html … 10_review.html, practice/index.html   만든 페이지 (직접 고치지 말고 build/src를 고친 뒤 조립)
build/src/NN.html        도면 본문 원본
build/pages.py           페이지 머리 정보 · 지식 색인 원본 · 참고문헌
build/build.py           조립 (머리 틀 + 본문 + 지식 색인·꾸러미)
build/import_covers.py   받은 표지 반영 (python3 build/import_covers.py 받은폴더)
build/covers.py          대체 표지 만들기 (받은 표지가 있으면 건너뜀)
assets/css, assets/js    공용 스타일·동작 (외부 라이브러리 없음)
assets/img/chars         캐릭터 팩 픽셀아트 (fruitfly-lab-expressions)
assets/img/covers        표지 · 목차 썸네일 · 공유 미리보기
kg/                      지식 색인·꾸러미 모듈 (kgx.js, retrofit.py)
GENSPARK_covers.md       Genspark 표지 요청문 (대화 5개, 저장 이름 체크리스트) · build/genspark.py로 생성
cover_manifest.json      표지 현황판용 목록
```

다시 조립: `python3 build/build.py` (일부만: `python3 build/build.py 03 04`)

## 만든 사람

글 · 안상선 (https://adminmrobo.github.io/who_am_i/who_am_i.html) · (주)M-Robo 대표

캐릭터 설정·그림은 저작권자 허락 없이 사용할 수 없습니다.
