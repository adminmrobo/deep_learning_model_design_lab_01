#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""대체 표지 만들기 (Genspark 표지가 오기 전까지 쓰는 픽셀 대체 표지).

모눈 바탕 + 캐릭터 팩 픽셀아트(정수배 확대) + Galmuri 글자.
cover_NN.webp 1600×900 · thumb_NN.webp 600×400 · og_NN.jpg 1200×630
필요: Pillow, Galmuri11 글꼴 (npm pack galmuri → package/dist/Galmuri11.ttf)
사용: python3 build/covers.py /경로/Galmuri11.ttf
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from pages import P, WHO  # noqa
FONT = sys.argv[1] if len(sys.argv) > 1 else '/tmp/package/dist/Galmuri11.ttf'
BOLD = FONT.replace('Galmuri11.ttf', 'Galmuri11-Bold.ttf')
OUT = os.path.join(ROOT, 'assets', 'img', 'covers'); os.makedirs(OUT, exist_ok=True)
CH = os.path.join(ROOT, 'assets', 'img', 'chars')
NAVY = (30, 47, 92); GRID = (230, 238, 249); GRID2 = (211, 225, 244); MUTE = (107, 107, 122)
ACC = {'asst': (217, 112, 126), 'moa': (180, 123, 50), 'sia': (110, 91, 168), 'review': (217, 68, 58)}
W, H = 1600, 900


def grid(im):
    d = ImageDraw.Draw(im)
    for x in range(0, W, 20): d.line([(x, 0), (x, H)], fill=GRID2 if x % 100 == 0 else GRID)
    for y in range(0, H, 20): d.line([(0, y), (W, y)], fill=GRID2 if y % 100 == 0 else GRID)
    d.rectangle([24, 24, W - 25, H - 25], outline=NAVY, width=6)


def sprite(who, e, k):
    s = Image.open(os.path.join(CH, f'{who}_e{e}.webp')).convert('RGBA')
    return s.resize((s.width * k, s.height * k), Image.NEAREST)


def blocks(d, x0, y0, cell, pattern, color):
    """픽셀 소품: 문자열 격자를 네모로 찍는다."""
    for r, row in enumerate(pattern):
        for c, v in enumerate(row):
            if v != '.':
                d.rectangle([x0 + c * cell, y0 + r * cell, x0 + (c + 1) * cell - 1, y0 + (r + 1) * cell - 1], fill=color if v == '#' else NAVY)


PROP = {  # 모델마다 작은 픽셀 소품 (16×10)
    'FNN': ['#...#...#.......', '.@.@.@.@.@......', '#...#...#.......', '.@.@.@.@.@......', '#...#...#.......'],
    'CNN': ['########........', '#@@@####........', '#@@@####........', '#@@@####........', '########........'],
    'RNN': ['.###..###..###..', '.#@#>.#@#>.#@#..', '.###..###..###..', '..^....^....^...'],
    'LSTM': ['################', '..@....@....@...', '.###..###..###..', '.#@#..#@#..#@#..', '.###..###..###..'],
    'GRU': ['########........', '..@.....@.......', '.###...###......', '.#@#...#@#......', '.###...###......'],
    'AE': ['####......####..', '.###..##..###...', '..##..##..##....', '.###..##..###...', '####......####..'],
    'DBN': ['@@@@@@@@........', '########........', '@@@@@@@@........', '########........', '@@@@@@@@........'],
    'GAN': ['###....@@@......', '#@#.>..@#@......', '###....@@@......'],
    'Transformer': ['@#@#@#@#........', '################', '#@@@@@@@@@@@@@@#', '################', '@#@#@#@#........'],
    'REVIEW': ['#.#.#...........', '@@@@@@@@@@@.....', '#.#.#...........', '@@@@@@@@@.......', '#.#.#...........'],
}


def text(d, xy, s, size, fill, bold=False):
    f = ImageFont.truetype(BOLD if bold and os.path.exists(BOLD) else FONT, size)
    d.text(xy, s, font=f, fill=fill)
    return d.textbbox(xy, s, font=f)


def make(n, code, abbr, ko, who, title_line):
    im = Image.new('RGB', (W, H), 'white'); grid(im); d = ImageDraw.Draw(im)
    acc = ACC[who]
    text(d, (90, 90), code, 54, acc)
    big = 150 if len(abbr) <= 4 else (110 if len(abbr) <= 6 else 96)
    b = text(d, (84, 160), abbr, big, NAVY, True)
    b2 = text(d, (90, b[3] + 26), ko, 56, NAVY)
    text(d, (90, b2[3] + 22), title_line, 34, MUTE)
    text(d, (90, H - 120), '딥러닝 설계도면 연구실 01', 30, MUTE)
    # 소품
    blocks(d, 90, H - 260, 16, PROP.get(abbr, PROP['FNN']), acc)
    # 캐릭터
    if who == 'review':
        a = sprite('fly', '10', 3); im.paste(a, (W - 2 * 576 + 140, H - 576 - 60), a)
        b_ = sprite('robo', '10', 3); im.paste(b_, (W - 576 - 70, H - 576 - 60), b_)
    else:
        s = sprite(who, '07', 3); im.paste(s, (W - 576 - 110, H - 576 - 60), s)
    return im


def save(im, n):
    out = os.path.join(OUT, f'cover_{n}.webp')
    im.save(out, 'WEBP', lossless=True, method=6)          # 픽셀 표지는 무손실이 더 작고 선명하다
    if os.path.getsize(out) > 150 * 1024:                   # 넘치면 손실 압축으로
        im.save(out, 'WEBP', quality=90, method=6)
    t = im.crop((0, 0, 1350, 900)).resize((600, 400), Image.LANCZOS); t.save(os.path.join(OUT, f'thumb_{n}.webp'), 'WEBP', quality=88, method=6)
    og = im.crop((0, 30, 1600, 870)).resize((1200, 630), Image.LANCZOS); og.save(os.path.join(OUT, f'og_{n}.jpg'), 'JPEG', quality=86)


for p in P:
    w = WHO[p['who']]
    line = ('작성 · ' + w['full']) if p['who'] != 'review' else '감수 · 초파리 연구원 & 주판봇'
    save(make(p['n'], p['code'], p['abbr'], p['ko'], p['who'], line), p['n'])

# 목차 표지: 다섯 식구
im = Image.new('RGB', (W, H), 'white'); grid(im); d = ImageDraw.Draw(im)
text(d, (90, 90), 'INDEX', 54, ACC['asst'])
b = text(d, (84, 160), 'DL BLUEPRINT', 110, NAVY, True)
b2 = text(d, (90, b[3] + 26), '딥러닝 설계도면 연구실 01', 56, NAVY)
text(d, (90, b2[3] + 22), '하루 · 모아 · 시아가 그리고, 초파리 · 주판봇이 감수한다', 34, MUTE)
x = 40
for who, e in (('asst', '07'), ('moa', '13'), ('sia', '13'), ('fly', '10'), ('robo', '16')):
    s = sprite(who, e, 2); im.paste(s, (x, H - 384 - 50), s); x += 292
save(im, '00')
print('표지 완료:', len(P) + 1)
