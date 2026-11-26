# -*- coding: utf-8 -*-
"""시리즈 목록과 페이지별 머리 정보, 지식 색인(노드·관계) 원본."""

SERIES = '딥러닝 설계도면 연구실 01'
SITE = 'https://adminmrobo.github.io/deep_learning_model_design_lab_01/'
REPO = 'https://github.com/adminmrobo/deep_learning_model_design_lab_01'
DATE = '2026-11-26'
VERSION = '1.0'

WHO = {
    'asst': {'ko': '하루', 'full': '조수 하루', 'cls': 'by-haru', 'shell': 'haru@lab'},
    'moa': {'ko': '모아', 'full': '인턴 모아', 'cls': 'by-moa', 'shell': 'moa@lab'},
    'sia': {'ko': '시아', 'full': '인턴 시아', 'cls': 'by-sia', 'shell': 'sia@lab'},
    'review': {'ko': '초파리·주판봇', 'full': '감수 · 초파리 연구원 & 주판봇', 'cls': 'by-review', 'shell': 'fly+robo@lab'},
}
NAME = {'asst': '하루', 'moa': '모아', 'sia': '시아', 'fly': '초파리', 'robo': '주판봇', 'doc': '박사'}

# 수식 상자에서 대신 물어 주는 동료(작성자와 다른 사람)
ASKER = {'asst': 'moa', 'moa': 'asst', 'sia': 'asst'}

FAMILY = {
    'base': '기본 구조 계열 (하루 담당)',
    'seq': '순서·기억 계열 (모아 담당)',
    'gen': '압축·생성 계열 (시아 담당)',
    'rev': '감수',
}

P = [
    dict(n='01', file='01_fnn.html', code='DL-01', abbr='FNN', ko='피드포워드 신경망', en='Feedforward Neural Network',
         who='asst', fam='base', h1='FNN', sub='앞으로만 흐르는 기본 설계도',
         desc='입력에서 출력으로 한 방향으로만 흐르는, 모든 신경망의 기본 부품. 가중합과 활성화 함수 두 가지만 알면 읽힌다.',
         motto='부품은 두 개 — 더하기, 그리고 구부리기.'),
    dict(n='02', file='02_cnn.html', code='DL-02', abbr='CNN', ko='합성곱 신경망', en='Convolutional Neural Network',
         who='asst', fam='base', h1='CNN', sub='작은 돋보기로 그림을 훑는 설계도',
         desc='작은 필터 하나를 그림 위로 밀며 같은 무늬를 어디서든 찾는다. 사진 판정의 기본 설계.',
         motto='돋보기 하나를 어디에나 똑같이.'),
    dict(n='03', file='03_rnn.html', code='DL-03', abbr='RNN', ko='순환 신경망', en='Recurrent Neural Network',
         who='moa', fam='seq', h1='RNN', sub='메모를 들고 다음 순서로 넘기는 설계도',
         desc='한 번에 하나씩 읽으며 앞에서 읽은 것을 메모(은닉 상태)로 넘긴다. 순서가 있는 데이터의 기본 설계.',
         motto='읽은 것은 메모에 모아서 다음으로.'),
    dict(n='04', file='04_lstm.html', code='DL-04', abbr='LSTM', ko='장단기 기억 신경망', en='Long Short-Term Memory',
         who='moa', fam='seq', h1='LSTM', sub='문 세 개로 기억을 지키는 설계도',
         desc='잊을 것·적을 것·꺼낼 것을 문(게이트) 세 개가 정하고, 긴 기억은 컨베이어처럼 흘러간다.',
         motto='버릴지, 적을지, 보여 줄지 — 문이 정한다.'),
    dict(n='05', file='05_gru.html', code='DL-05', abbr='GRU', ko='게이트 순환 유닛', en='Gated Recurrent Unit',
         who='moa', fam='seq', h1='GRU', sub='문을 두 개로 줄인 가벼운 설계도',
         desc='LSTM의 문 세 개를 두 개로 줄여 부품 수를 줄였다. 많은 일에서 비슷하게 잘한다.',
         motto='섞는 비율 하나로 옛 메모와 새 메모를.'),
    dict(n='06', file='06_autoencoder.html', code='DL-06', abbr='AE', ko='오토인코더', en='Autoencoder',
         who='sia', fam='gen', h1='AUTOENCODER', sub='좁은 목을 지나 다시 그려 내는 설계도',
         desc='입력을 작은 요약으로 줄였다가 다시 펼쳐 원래대로 되살린다. 정답표 없이 배운다.',
         motto='줄여 보면 중요한 것만 남는다.'),
    dict(n='07', file='07_dbn.html', code='DL-07', abbr='DBN', ko='심층 신뢰 신경망', en='Deep Belief Network',
         who='sia', fam='gen', h1='DBN', sub='한 층씩 쌓아 올린 옛 설계도',
         desc='작은 확률 부품(RBM)을 한 층씩 미리 학습해 쌓고, 마지막에 정답표로 다듬는다. 깊은 학습을 다시 가능하게 한 역사적 설계.',
         motto='한 번에 한 층씩, 차곡차곡.'),
    dict(n='08', file='08_gan.html', code='DL-08', abbr='GAN', ko='적대적 생성 신경망', en='Generative Adversarial Network',
         who='sia', fam='gen', h1='GAN', sub='위조범과 감정사가 겨루는 설계도',
         desc='만드는 쪽(생성자)과 가려내는 쪽(판별자)이 겨루며 둘 다 실력이 는다. 진짜 같은 데이터를 만든다.',
         motto='속이려는 쪽이 있어야 보는 눈이 는다.'),
    dict(n='09', file='09_transformer.html', code='DL-09', abbr='Transformer', ko='트랜스포머', en='Transformer',
         who='asst', fam='base', h1='TRANSFORMER', sub='모든 단어가 서로를 한꺼번에 보는 설계도',
         desc='순서대로 읽지 않고, 모든 단어가 서로에게 얼마나 주목할지(어텐션)를 한꺼번에 계산한다. 요즘 AI의 기본 설계.',
         motto='누구를 얼마나 볼지, 점수로 정한다.'),
    dict(n='10', file='10_review.html', code='DL-10', abbr='REVIEW', ko='총괄 도면 감수', en='Design review of 9 models',
         who='review', fam='rev', h1='REVIEW', sub='초파리와 주판봇이 9장을 한 장에 놓고 감수하다',
         desc='아홉 도면을 한 장에 모은 총괄 도면을 초파리·주판봇이 감수한다. 참고 자료에서 찾은 틀린 곳과 고친 곳을 빨간 펜으로 남긴다.',
         motto='큰 것은 의심하고, 숫자는 세어 본다.'),
]
BY_N = {p['n']: p for p in P}
for i, p in enumerate(P):
    p['prev'] = P[i - 1] if i > 0 else None
    p['next'] = P[i + 1] if i + 1 < len(P) else None

# ---------------------------------------------------------------- 지식 색인 원본
# (id, type, ko, en, 정의, 앵커, level, coverage)
def node(i, t, ko, en, d, a='#dwg', lv=2, cov='explained', dom=('ai',)):
    return dict(id=i, type=t, label=dict(ko=ko, en=en), anchor=a, level=lv, status='known',
                confidence='high', coverage=cov, domain=list(dom), match=[], definition=dict(ko=d))

def edge(s, p, o, a='#dwg'):
    return dict(s=s, p='lab:' + p, o=o, anchor=a, confidence='high')

T = 'lab:topic/'
KG = {}
KG['01'] = ([
    node('lab:method/fnn', 'Method', '피드포워드 신경망', 'Feedforward neural network', '입력에서 출력으로 한 방향으로만 신호가 흐르는 신경망. 순환이 없다.'),
    node('lab:concept/weighted-sum', 'Concept', '가중합', 'Weighted sum', '입력마다 중요도(가중치)를 곱해 더하고 편향을 더한 값 z = Σwx + b.', '#math', 1),
    node('lab:concept/activation', 'Concept', '활성화 함수', 'Activation function', '가중합을 구부려 비선형성을 더하는 함수. ReLU, 시그모이드, tanh 등.', '#math', 1),
    node('lab:concept/loss', 'Concept', '손실', 'Loss', '예측과 정답의 차이를 평균한 값. 학습은 이 값을 줄이는 방향으로 가중치를 고친다.', '#spec', 1),
    node('lab:limit/fnn-no-memory', 'Limitation', '앞의 입력을 기억하지 못함', 'No memory of previous inputs', '입력 하나를 따로 본다. 순서가 있는 데이터에는 RNN 계열이 필요해진다.', '#limit', 2),
], [
    edge('lab:method/fnn', 'broader', T + 'mlp'), edge('lab:method/fnn', 'uses', 'lab:concept/weighted-sum'),
    edge('lab:method/fnn', 'uses', 'lab:concept/activation'), edge('lab:concept/activation', 'broader', T + 'activation-function'),
    edge('lab:concept/loss', 'broader', T + 'loss-function'), edge('lab:method/fnn', 'hasLimitation', 'lab:limit/fnn-no-memory'),
    edge('lab:method/fnn', 'prerequisiteOf', 'lab:method/cnn'), edge('lab:method/fnn', 'prerequisiteOf', 'lab:method/rnn'),
])
KG['02'] = ([
    node('lab:method/cnn', 'Method', '합성곱 신경망', 'Convolutional neural network', '작은 필터를 그림 위로 밀어 가며 같은 무늬를 찾는 신경망.'),
    node('lab:concept/filter', 'Concept', '필터(커널)', 'Filter (kernel)', '3×3 같은 작은 숫자 판. 그림 위를 밀며 곱해 더한다.', '#math', 1),
    node('lab:concept/feature-map', 'Concept', '특징 지도', 'Feature map', '필터가 무늬를 얼마나 강하게 찾았는지 위치별로 적은 표.', '#lab', 1),
    node('lab:concept/pooling', 'Concept', '풀링', 'Pooling', '작은 구역의 대표값(최댓값·평균)만 남겨 크기를 줄인다.', '#spec', 1),
    node('lab:concept/weight-sharing', 'Concept', '가중치 공유', 'Parameter sharing', '같은 필터를 모든 위치에 다시 써서 부품 수를 줄인다.', '#why', 2),
], [
    edge('lab:method/cnn', 'broader', T + 'convolution'), edge('lab:method/cnn', 'uses', 'lab:concept/filter'),
    edge('lab:method/cnn', 'uses', 'lab:concept/pooling'), edge('lab:concept/pooling', 'broader', T + 'pooling'),
    edge('lab:concept/filter', 'relatedTo', 'lab:concept/feature-map'), edge('lab:method/cnn', 'uses', 'lab:concept/weight-sharing'),
    edge('lab:method/fnn', 'prerequisiteOf', 'lab:method/cnn'),
])
KG['03'] = ([
    node('lab:method/rnn', 'Method', '순환 신경망', 'Recurrent neural network', '순서대로 하나씩 읽으며 은닉 상태를 다음 시점으로 넘기는 신경망.'),
    node('lab:concept/hidden-state', 'Concept', '은닉 상태', 'Hidden state', '지금까지 읽은 내용을 요약한 숫자 묶음(메모). h_t로 쓴다.', '#math', 1),
    node('lab:concept/shared-weights-time', 'Concept', '시점 간 가중치 공유', 'Weights shared across time', '모든 시점에 같은 가중치를 쓴다. 길이가 달라도 같은 부품으로 읽는다.', '#spec', 2),
    node('lab:limit/vanishing-gradient', 'Limitation', '기울기 소실', 'Vanishing gradient', '먼 과거의 영향이 곱셈을 거듭하며 0에 가까워져 학습이 안 되는 문제.', '#lab', 2),
], [
    edge('lab:method/rnn', 'broader', T + 'rnn'), edge('lab:method/rnn', 'uses', 'lab:concept/hidden-state'),
    edge('lab:method/rnn', 'uses', 'lab:concept/shared-weights-time'), edge('lab:method/rnn', 'hasLimitation', 'lab:limit/vanishing-gradient'),
    edge('lab:limit/vanishing-gradient', 'addressedBy', 'lab:method/lstm'), edge('lab:method/fnn', 'prerequisiteOf', 'lab:method/rnn'),
])
KG['04'] = ([
    node('lab:method/lstm', 'Method', 'LSTM', 'Long short-term memory', '셀 상태와 문 세 개(망각·입력·출력)로 긴 기억을 지키는 RNN 변형.'),
    node('lab:concept/cell-state', 'Concept', '셀 상태', 'Cell state', '시점을 따라 흐르는 긴 기억. 곱하기(망각)와 더하기(새 내용)로만 바뀐다.', '#math', 2),
    node('lab:concept/gate', 'Concept', '게이트', 'Gate', '0~1 사이 값(시그모이드)으로 정보를 얼마나 통과시킬지 정하는 문.', '#spec', 2),
    node('lab:concept/forget-gate', 'Concept', '망각 게이트', 'Forget gate', '옛 기억을 얼마나 남길지 정하는 문. 1에 가까우면 유지.', '#spec', 2),
], [
    edge('lab:method/lstm', 'broader', T + 'lstm-gru'), edge('lab:method/lstm', 'specialCaseOf', 'lab:method/rnn'),
    edge('lab:method/lstm', 'uses', 'lab:concept/cell-state'), edge('lab:method/lstm', 'uses', 'lab:concept/gate'),
    edge('lab:concept/forget-gate', 'broader', 'lab:concept/gate'), edge('lab:limit/vanishing-gradient', 'addressedBy', 'lab:method/lstm'),
])
KG['05'] = ([
    node('lab:method/gru', 'Method', 'GRU', 'Gated recurrent unit', '리셋·업데이트 문 두 개만 쓰는 가벼운 RNN 변형. 셀 상태 없이 은닉 상태 하나로 기억한다.'),
    node('lab:concept/update-gate', 'Concept', '업데이트 게이트', 'Update gate', '옛 메모와 새 후보를 섞는 비율 z_t.', '#math', 2),
    node('lab:concept/reset-gate', 'Concept', '리셋 게이트', 'Reset gate', '새 후보를 만들 때 옛 메모를 얼마나 참고할지 정하는 r_t.', '#spec', 2),
    node('lab:concept/param-count', 'Metric', '부품 수(파라미터 수)', 'Parameter count', '학습으로 정하는 숫자의 개수. 많을수록 무겁다.', '#lab', 1),
], [
    edge('lab:method/gru', 'broader', T + 'lstm-gru'), edge('lab:method/gru', 'specialCaseOf', 'lab:method/rnn'),
    edge('lab:method/gru', 'uses', 'lab:concept/update-gate'), edge('lab:method/gru', 'uses', 'lab:concept/reset-gate'),
    edge('lab:method/gru', 'relatedTo', 'lab:method/lstm'), edge('lab:concept/update-gate', 'broader', 'lab:concept/gate'),
])
KG['06'] = ([
    node('lab:method/autoencoder', 'Method', '오토인코더', 'Autoencoder', '입력을 작은 잠재 표현으로 줄였다가(인코더) 다시 되살리는(디코더) 신경망.'),
    node('lab:concept/latent', 'Concept', '잠재 표현(병목)', 'Latent representation (bottleneck)', '입력을 줄여 만든 작은 숫자 묶음 z. 중요한 것만 남게 한다.', '#math', 2),
    node('lab:concept/recon-error', 'Metric', '재구성 오차', 'Reconstruction error', '입력 x와 되살린 x̂의 차이. 이상 탐지의 점수로도 쓴다.', '#lab', 1),
    node('lab:method/pca', 'Method', '주성분 분석(PCA)', 'Principal component analysis', '데이터를 가장 많이 퍼진 방향으로 줄이는 선형 방법. 선형 오토인코더와 같은 공간을 찾는다.', '#why', 2, 'mentioned'),
], [
    edge('lab:method/autoencoder', 'broader', T + 'autoencoder'), edge('lab:method/autoencoder', 'uses', 'lab:concept/latent'),
    edge('lab:method/autoencoder', 'uses', 'lab:concept/recon-error'), edge('lab:method/pca', 'relatedTo', 'lab:method/autoencoder'),
    edge('lab:method/autoencoder', 'broader', T + 'unsupervised-learning'),
])
KG['07'] = ([
    node('lab:method/dbn', 'Method', '심층 신뢰 신경망', 'Deep belief network', 'RBM을 한 층씩 비지도 사전학습으로 쌓고, 정답표로 미세조정하는 생성 모델.'),
    node('lab:method/rbm', 'Method', '제한 볼츠만 머신', 'Restricted Boltzmann machine', '보이는 층과 숨은 층 두 층만 서로 이어진 확률 모델. 같은 층끼리는 잇지 않는다.', '#math', 2),
    node('lab:concept/pretraining', 'Concept', '층별 사전학습', 'Greedy layer-wise pretraining', '아래층부터 하나씩 따로 학습해 좋은 출발점을 만드는 방법.', '#spec', 2),
    node('lab:concept/cd', 'Method', '대조 발산', 'Contrastive divergence', 'RBM을 빠르게 학습시키는 근사 방법.', '#spec', 3, 'mentioned'),
], [
    edge('lab:method/dbn', 'broader', T + 'unsupervised-learning'), edge('lab:method/dbn', 'uses', 'lab:method/rbm'),
    edge('lab:method/dbn', 'uses', 'lab:concept/pretraining'), edge('lab:method/rbm', 'uses', 'lab:concept/cd'),
    edge('lab:concept/pretraining', 'relatedTo', T + 'transfer-learning'),
])
KG['08'] = ([
    node('lab:method/gan', 'Method', '적대적 생성 신경망', 'Generative adversarial network', '생성자와 판별자가 겨루며 학습하는 생성 모델.'),
    node('lab:concept/generator', 'Concept', '생성자', 'Generator', '무작위 잡음을 받아 진짜 같은 데이터를 만드는 쪽 G.', '#spec', 1),
    node('lab:concept/discriminator', 'Concept', '판별자', 'Discriminator', '진짜와 가짜를 받아 진짜일 확률을 내는 쪽 D.', '#spec', 1),
    node('lab:concept/minimax', 'Concept', '최소최대 게임', 'Minimax game', 'D는 맞히는 확률을 키우고 G는 들키는 확률을 줄이는 겨루기.', '#math', 2),
    node('lab:limit/mode-collapse', 'Limitation', '모드 붕괴', 'Mode collapse', '생성자가 몇 가지 결과만 되풀이해 다양성이 사라지는 문제.', '#limit', 2),
], [
    edge('lab:method/gan', 'broader', T + 'gan'), edge('lab:method/gan', 'uses', 'lab:concept/generator'),
    edge('lab:method/gan', 'uses', 'lab:concept/discriminator'), edge('lab:method/gan', 'uses', 'lab:concept/minimax'),
    edge('lab:method/gan', 'hasLimitation', 'lab:limit/mode-collapse'),
])
KG['09'] = ([
    node('lab:method/transformer', 'Method', '트랜스포머', 'Transformer', '순환·합성곱 없이 어텐션만으로 순서 데이터를 처리하는 구조.'),
    node('lab:concept/self-attention', 'Concept', '셀프 어텐션', 'Self-attention', '한 문장 안의 모든 토큰이 서로에게 얼마나 주목할지 점수를 매겨 섞는 계산.', '#math', 2),
    node('lab:concept/qkv', 'Concept', '쿼리·키·밸류', 'Query, key, value', '찾는 질문(Q), 각 토큰의 꼬리표(K), 실제 내용(V).', '#math', 2),
    node('lab:concept/positional-encoding', 'Concept', '위치 인코딩', 'Positional encoding', '한꺼번에 보느라 잃는 순서 정보를 숫자로 더해 주는 장치.', '#spec', 2),
    node('lab:concept/softmax', 'Concept', '소프트맥스', 'Softmax', '점수들을 합이 1인 비율로 바꾸는 함수.', '#math', 1),
], [
    edge('lab:method/transformer', 'broader', T + 'transformer'), edge('lab:concept/self-attention', 'broader', T + 'self-attention'),
    edge('lab:method/transformer', 'uses', 'lab:concept/self-attention'), edge('lab:concept/self-attention', 'uses', 'lab:concept/qkv'),
    edge('lab:concept/self-attention', 'uses', 'lab:concept/softmax'), edge('lab:method/transformer', 'uses', 'lab:concept/positional-encoding'),
    edge('lab:concept/positional-encoding', 'broader', T + 'positional-encoding'),
])
KG['10'] = ([
    node('lab:method/' + k, 'Method', ko, en, d, '#overview', 2, 'mentioned') for k, ko, en, d in [
        ('fnn', '피드포워드 신경망', 'Feedforward neural network', '한 방향으로만 흐르는 기본 신경망.'),
        ('cnn', '합성곱 신경망', 'Convolutional neural network', '필터로 공간 무늬를 찾는 신경망.'),
        ('rnn', '순환 신경망', 'Recurrent neural network', '은닉 상태로 순서를 기억하는 신경망.'),
        ('lstm', 'LSTM', 'Long short-term memory', '문 세 개로 긴 기억을 지키는 RNN.'),
        ('gru', 'GRU', 'Gated recurrent unit', '문 두 개의 가벼운 RNN.'),
        ('autoencoder', '오토인코더', 'Autoencoder', '줄였다 되살리며 표현을 배우는 신경망.'),
        ('dbn', '심층 신뢰 신경망', 'Deep belief network', 'RBM을 층별로 쌓는 생성 모델.'),
        ('gan', '적대적 생성 신경망', 'Generative adversarial network', '생성자와 판별자의 겨루기.'),
        ('transformer', '트랜스포머', 'Transformer', '어텐션만으로 만든 구조.')]
] + [
    node('lab:claim/review-errata', 'Claim', '참고 인포그래픽에 고칠 곳이 있다', 'The reference infographics contain errors',
         'RNN 예시의 번호 오류, DBN 비교표의 어긋난 열과 깨진 글자, GAN 설명의 오타, FNN 요약의 과장 문구를 감수에서 확인했다.', '#errata', 2),
    node('lab:question/which-model', 'Question', '내 데이터에는 어느 설계도가 맞나', 'Which blueprint fits my data?',
         '데이터 모양(표·그림·순서)과 목적(판정·예측·생성)으로 먼저 좁히고, 데이터 양과 계산 자원으로 고른다.', '#choose', 2),
], [
    edge('lab:method/fnn', 'prerequisiteOf', 'lab:method/cnn', '#overview'), edge('lab:method/fnn', 'prerequisiteOf', 'lab:method/rnn', '#overview'),
    edge('lab:method/lstm', 'specialCaseOf', 'lab:method/rnn', '#overview'), edge('lab:method/gru', 'specialCaseOf', 'lab:method/rnn', '#overview'),
    edge('lab:method/gru', 'relatedTo', 'lab:method/lstm', '#overview'), edge('lab:method/dbn', 'relatedTo', 'lab:method/autoencoder', '#overview'),
    edge('lab:method/gan', 'relatedTo', 'lab:method/autoencoder', '#overview'), edge('lab:method/rnn', 'prerequisiteOf', 'lab:method/transformer', '#overview'),
    edge('lab:claim/review-errata', 'relatedTo', 'lab:method/dbn', '#errata'),
])
KG['00'] = ([
    node('lab:area/dl-blueprints', 'Topic', '딥러닝 설계도면 9종', 'Nine deep learning blueprints', '기본 구조 · 순서·기억 · 압축·생성 세 계열로 묶은 9개 모델.', '#map', 1),
    node('lab:method/fnn', 'Method', '피드포워드 신경망', 'Feedforward neural network', '01 도면.', '#list', 1, 'mentioned'),
    node('lab:method/rnn', 'Method', '순환 신경망', 'Recurrent neural network', '03 도면.', '#list', 1, 'mentioned'),
    node('lab:method/autoencoder', 'Method', '오토인코더', 'Autoencoder', '06 도면.', '#list', 1, 'mentioned'),
    node('lab:method/transformer', 'Method', '트랜스포머', 'Transformer', '09 도면.', '#list', 1, 'mentioned'),
], [
    edge('lab:method/fnn', 'broader', 'lab:area/dl-blueprints', '#map'), edge('lab:method/rnn', 'broader', 'lab:area/dl-blueprints', '#map'),
    edge('lab:method/autoencoder', 'broader', 'lab:area/dl-blueprints', '#map'), edge('lab:method/transformer', 'broader', 'lab:area/dl-blueprints', '#map'),
    edge('lab:area/dl-blueprints', 'broader', 'lab:area/nn-basics', '#map'),
])

REFS_COMMON = [
    {"id": "ref-infographic", "type": "graphic", "title": "9 Deep Learning Algorithms Every Engineer Should Know (인포그래픽 10장)",
     "note": "작성자 표기 없음. 이 시리즈는 내용만 참고하고 그림은 새로 그렸다."},
]
REFS = {
    '01': [{"id": "rumelhart1986", "type": "article-journal", "title": "Learning representations by back-propagating errors",
            "author": [{"family": "Rumelhart", "given": "David E."}, {"family": "Hinton", "given": "Geoffrey E."}, {"family": "Williams", "given": "Ronald J."}],
            "container-title": "Nature", "volume": "323", "page": "533-536", "issued": {"date-parts": [[1986]]}, "DOI": "10.1038/323533a0"}],
    '02': [{"id": "lecun1998", "type": "article-journal", "title": "Gradient-based learning applied to document recognition",
            "author": [{"family": "LeCun", "given": "Yann"}, {"family": "Bottou", "given": "Léon"}, {"family": "Bengio", "given": "Yoshua"}, {"family": "Haffner", "given": "Patrick"}],
            "container-title": "Proceedings of the IEEE", "volume": "86", "issue": "11", "page": "2278-2324", "issued": {"date-parts": [[1998]]}, "DOI": "10.1109/5.726791"}],
    '03': [{"id": "elman1990", "type": "article-journal", "title": "Finding structure in time", "author": [{"family": "Elman", "given": "Jeffrey L."}],
            "container-title": "Cognitive Science", "volume": "14", "issue": "2", "page": "179-211", "issued": {"date-parts": [[1990]]}, "DOI": "10.1207/s15516709cog1402_1"}],
    '04': [{"id": "hochreiter1997", "type": "article-journal", "title": "Long short-term memory",
            "author": [{"family": "Hochreiter", "given": "Sepp"}, {"family": "Schmidhuber", "given": "Jürgen"}],
            "container-title": "Neural Computation", "volume": "9", "issue": "8", "page": "1735-1780", "issued": {"date-parts": [[1997]]}, "DOI": "10.1162/neco.1997.9.8.1735"}],
    '05': [{"id": "cho2014", "type": "paper-conference", "title": "Learning phrase representations using RNN encoder–decoder for statistical machine translation",
            "author": [{"family": "Cho", "given": "Kyunghyun"}, {"literal": "외"}], "container-title": "Proceedings of EMNLP 2014", "page": "1724-1734",
            "issued": {"date-parts": [[2014]]}, "DOI": "10.3115/v1/D14-1179"}],
    '06': [{"id": "hinton2006science", "type": "article-journal", "title": "Reducing the dimensionality of data with neural networks",
            "author": [{"family": "Hinton", "given": "Geoffrey E."}, {"family": "Salakhutdinov", "given": "Ruslan R."}],
            "container-title": "Science", "volume": "313", "issue": "5786", "page": "504-507", "issued": {"date-parts": [[2006]]}, "DOI": "10.1126/science.1127647"}],
    '07': [{"id": "hinton2006nc", "type": "article-journal", "title": "A fast learning algorithm for deep belief nets",
            "author": [{"family": "Hinton", "given": "Geoffrey E."}, {"family": "Osindero", "given": "Simon"}, {"family": "Teh", "given": "Yee-Whye"}],
            "container-title": "Neural Computation", "volume": "18", "issue": "7", "page": "1527-1554", "issued": {"date-parts": [[2006]]}, "DOI": "10.1162/neco.2006.18.7.1527"}],
    '08': [{"id": "goodfellow2014", "type": "paper-conference", "title": "Generative adversarial nets",
            "author": [{"family": "Goodfellow", "given": "Ian J."}, {"literal": "외"}], "container-title": "Advances in Neural Information Processing Systems 27",
            "issued": {"date-parts": [[2014]]}, "URL": "https://arxiv.org/abs/1406.2661"}],
    '09': [{"id": "vaswani2017", "type": "paper-conference", "title": "Attention is all you need",
            "author": [{"family": "Vaswani", "given": "Ashish"}, {"literal": "외"}], "container-title": "Advances in Neural Information Processing Systems 30",
            "issued": {"date-parts": [[2017]]}, "URL": "https://arxiv.org/abs/1706.03762"}],
}
