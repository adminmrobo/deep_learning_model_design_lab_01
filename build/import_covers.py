#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""받은 표지(cover_NN.png) 반영: 1600×900 WebP(220 KB 이하) · thumb 600×400 · og 1200×630
사용: python3 build/import_covers.py /받은/폴더"""
import os, sys, json
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = sys.argv[1]; OUT = os.path.join(ROOT, 'assets', 'img', 'covers')
done = []
for f in sorted(os.listdir(SRC)):
    if not (f.startswith('cover_') and f.lower().endswith(('.png', '.jpg', '.jpeg'))): continue
    n = f[6:8]; im = Image.open(os.path.join(SRC, f)).convert('RGB')
    w, h = im.size; th = round(w * 9 / 16)
    if h != th: t = (h - th) // 2; im = im.crop((0, t, w, t + th))
    big = im.resize((1600, 900), Image.LANCZOS)
    p = os.path.join(OUT, f'cover_{n}.webp')
    for q in (86, 80, 74, 68, 62):
        big.save(p, 'WEBP', quality=q, method=6)
        if os.path.getsize(p) <= 220 * 1024: break
    big.crop((125, 0, 1475, 900)).resize((420, 280), Image.LANCZOS).save(os.path.join(OUT, f'thumb_{n}.webp'), 'WEBP', quality=66, method=6)
    big.crop((0, 30, 1600, 870)).resize((1200, 630), Image.LANCZOS).save(os.path.join(OUT, f'og_{n}.jpg'), 'JPEG', quality=84, optimize=True)
    done.append(n); print(n, os.path.getsize(p) // 1024, 'KB')
m = os.path.join(ROOT, 'cover_manifest.json')
if os.path.exists(m):
    d = json.load(open(m, encoding='utf-8'))
    for it in d['items']:
        if it['id'][-2:] in done: it['status'] = 'ok'
    json.dump(d, open(m, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
