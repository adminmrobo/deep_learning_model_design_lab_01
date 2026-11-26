#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""딥러닝 설계도면 연구실 01 — 조립 스크립트

build/src/NN.html (본문 조각) + 머리 틀 → 저장소 맨 위 NN_xxx.html
그다음 kg/retrofit.py로 지식 색인(#kg)·꾸러미(#export)를 덧붙인다.

사용: python3 build/build.py          (저장소 맨 위에서)
"""
import html, json, os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from pages import P, BY_N, WHO, NAME, FAMILY, SERIES, SITE, REPO, DATE, VERSION, KG, REFS, REFS_COMMON  # noqa

PXFIX = ('<!-- px-fix v1 --><style id="px-fix">img{image-rendering:auto!important}</style><script id="px-fix-js">(function(){var R=window.ResizeObserver;function f(i){var n=i.naturalWidth,w=i.getBoundingClientRect().width;if(!n||!w)return;var s=w*(window.devicePixelRatio||1)/n;i.style.setProperty("image-rendering",s>=1.95?"pixelated":"auto","important")}var ro=R?new R(function(es){es.forEach(function(e){f(e.target)})}):null;function a(i){if(i.__px)return;i.__px=1;i.addEventListener("load",function(){f(i)});if(ro)ro.observe(i);f(i)}function all(r){(r||document).querySelectorAll&&(r||document).querySelectorAll("img").forEach(a)}function go(){all();if(window.MutationObserver)new MutationObserver(function(ms){ms.forEach(function(m){m.addedNodes.forEach(function(n){if(n.nodeType!==1)return;if(n.tagName==="IMG")a(n);else all(n)})})}).observe(document.documentElement,{childList:true,subtree:true});window.addEventListener("resize",function(){document.querySelectorAll("img").forEach(f)})}if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",go);else go()})();</script><!-- /px-fix -->')

E = html.escape


def ch(who, e, base=''):
    return f'{base}assets/img/chars/{who}_e{e}.webp'


def head(title, desc, og, base=''):
    return f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta property="og:type" content="article">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:image" content="{SITE}{og}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{base}assets/img/chars/asst_e13.webp">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/galmuri@latest/dist/galmuri.css">
<link rel="stylesheet" href="{base}assets/css/blueprint.css">
<script src="{base}assets/js/blueprint.js"></script>
{PXFIX}
</head>
'''


def topnav(cur, base=''):
    links = [f'<a class="home" href="{base}index.html">DL 설계도면 연구실</a>']
    for p in P:
        c = ' class="here" aria-current="page"' if p['n'] == cur else ''
        links.append(f'<a href="{base}{p["file"]}"{c}>{p["n"]} {E(p["abbr"] if p["abbr"] != "REVIEW" else "감수")}</a>')
    c = ' class="here" aria-current="page"' if cur == 'practice' else ''
    links.append(f'<a href="{base}practice/index.html"{c}>실전 연습장</a>')
    return '<nav class="topnav" aria-label="도면 목록"><div class="wrap">' + ''.join(links) + '</div></nav>\n'


def footer(base='', extra=''):
    return f'''<footer>
  <div class="wrap">
    <p>글 · 안상선 (<a href="https://adminmrobo.github.io/who_am_i/who_am_i.html">https://adminmrobo.github.io/who_am_i/who_am_i.html</a>) · (주)M-Robo 대표</p>
    <p>캐릭터: 조수 하루 · 인턴 모아 · 인턴 시아 · 초파리 연구원 · 주판봇 · 박사 — <a href="https://github.com/adminmrobo/fruitfly-lab-expressions">fruitfly-lab-expressions</a> 픽셀아트 캐릭터 팩. 도면 그림은 이 저장소에서 새로 그렸습니다.</p>
    <p>참고 자료: 「9 Deep Learning Algorithms Every Engineer Should Know」 인포그래픽 10장(작성자 표기 없음). 내용만 참고했고, 그림과 문장은 새로 만들었으며 틀린 곳은 고쳤습니다(<a href="{base}10_review.html#errata">감수 의견서</a>).{extra}</p>
    <p>저장소: <a href="{REPO}">adminmrobo/deep_learning_model_design_lab_01</a> · <a href="https://www.ahnboat.xyz">ahnboat.xyz</a></p>
  </div>
</footer>
'''


def hero(p):
    w = WHO[p['who']]
    if p['who'] == 'review':
        who = (f'<div class="who two"><img src="{ch("fly","10")}" alt="클립보드를 든 초파리 연구원" width="192" height="192">'
               f'<img src="{ch("robo","10")}" alt="체크 표시를 하는 주판봇" width="192" height="192"></div>')
        writer = '아홉 도면 작성: 조수 하루 · 인턴 모아 · 인턴 시아'
        reviewer = '초파리 연구원 · 주판봇'
    else:
        who = f'<div class="who"><img src="{ch(p["who"],"07")}" alt="{E(w["full"])} 픽셀아트 초상, 검지를 세워 설명하는 모습" width="192" height="192"></div>'
        writer = w['full']
        reviewer = '초파리 연구원 · 주판봇 (<a href="10_review.html">10 감수 도면</a>)'
    return f'''<div class="wrap">
  <div class="term">
    <div class="bar"><span class="dot" style="background:var(--pink)"></span><span class="dot" style="background:var(--lav)"></span><span class="dot" style="background:var(--navy)"></span><span class="t mono">blueprint · {p["code"]}_{E(p["abbr"])}.dwg</span></div>
    <div class="term-body">
      <p class="prompt mono"><b>{w["shell"]}</b>:~$ open {p["code"]}_{E(p["abbr"])}.blueprint</p>
      <div class="hero">
        {who}
        <div>
          <h1>{E(p["h1"])}</h1>
          <div class="sub">{E(p["sub"])}</div>
          <p class="by">{p["code"]} · {E(p["ko"])} ({E(p["en"])}) · {E(w["full"])} 작성</p>
          <span class="motto pix">{E(p["motto"])}</span>
        </div>
      </div>
      <table class="titleblock" aria-label="도면 표제란">
        <tr><th>도면 번호</th><td>{p["code"]}</td><th>계열</th><td>{E(FAMILY[p["fam"]])}</td></tr>
        <tr><th>작성</th><td>{writer}</td><th>감수</th><td>{reviewer}</td></tr>
        <tr><th>모델</th><td>{E(p["abbr"] if p["abbr"]!="REVIEW" else "9종 총괄")} · {E(p["ko"])}</td><th>날짜 · 판</th><td>{DATE} · v{VERSION}</td></tr>
      </table>
    </div>
  </div>
</div>
'''


def pnav(p):
    pr, nx = p['prev'], p['next']
    a = (f'<a href="{pr["file"]}"><small>← 앞 도면 {pr["code"]}</small>{E(pr["abbr"])} · {E(pr["ko"])}</a>' if pr
         else '<a href="index.html"><small>← 처음으로</small>INDEX · 도면 목록</a>')
    b = (f'<a class="nx" href="{nx["file"]}"><small>다음 도면 {nx["code"]} →</small>{E(nx["abbr"] if nx["abbr"]!="REVIEW" else "감수")} · {E(nx["ko"])}</a>' if nx
         else '<a class="nx" href="practice/index.html"><small>마지막 장 →</small>실전 연습장 · 설계 의뢰 접수처</a>')
    return f'''<section id="next"><div class="wrap">
  <h2><span class="no">▣</span>다른 도면 펼치기</h2>
  <div class="pnav">{a}<a class="ix" href="index.html">INDEX</a>{b}</div>
</div></section>
'''


def build_part(p):
    src = open(os.path.join(HERE, 'src', p['n'] + '.html'), encoding='utf-8').read()
    w = WHO[p['who']]
    title = f'{p["code"]} {p["abbr"] if p["abbr"]!="REVIEW" else "감수"} — {p["ko"]} 설계도면 | {SERIES}'
    cover = (f'<header class="cover" id="cover" data-img="cover_{p["n"]}"><picture><img src="assets/img/covers/cover_{p["n"]}.webp" width="1600" height="900" '
             f'alt="{E(p["code"])} {E(p["abbr"])} 설계도면 표지: 모눈 바탕 위의 {E(w["full"])} 픽셀아트" fetchpriority="high" decoding="async"></picture>'
             f'<span class="cover-chip">{SERIES} · {p["code"]}</span></header>\n')
    out = (head(title, p['desc'], f'assets/img/covers/og_{p["n"]}.jpg') +
           f'<body class="{w["cls"]}">\n<a class="skip" href="#main">본문으로 건너뛰기</a>\n' + topnav(p['n']) + cover + hero(p) +
           '<main id="main">\n' + src + '\n</main>\n' + pnav(p) + footer() + '</body>\n</html>\n')
    return out


def kg_for(n, page_file, title, number):
    nodes, edges = KG[n]
    nodes = [dict(x, page=page_file.replace('.html', '')) for x in nodes]
    have = {x['id'] for x in nodes}
    for e in edges:
        for k in ('s', 'o'):
            i = e[k]
            if i not in have and not i.startswith(('lab:topic/', 'lab:area/')):
                ko = {x['id']: x for n_ in KG.values() for x in n_[0]}.get(i)
                lab = ko['label'] if ko else {'ko': i.split('/')[-1], 'en': i.split('/')[-1]}
                nodes.append(dict(id=i, type=(ko or {}).get('type', 'Method'), label=lab, page=page_file.replace('.html', ''), anchor='#limit',
                                  level=2, status='known', confidence='high', coverage='mentioned', domain=['ai'], match=[],
                                  definition=(ko or {}).get('definition', {'ko': ''})))
                have.add(i)
    kg = {'version': '1.0', 'page': page_file.replace('.html', ''), 'nodes': nodes, 'edges': edges}
    refs = [dict(r, lab={'verified': {k: True for k in ('title', 'author', 'issued', 'container-title', 'DOI', 'URL') if k in r}}) for r in REFS.get(n, []) + REFS_COMMON]
    meta = {'title': title, 'number': number, 'series': SERIES, 'date': DATE, 'version': VERSION,
            'creator': [{'name': '안상선', 'role': 'author'}], 'contributor': [{'name': 'AI 보조 제작', 'role': 'assistant'}],
            'about': [nodes[0]['id']], 'basedOn': [r['id'] for r in refs] + ['ref-infographic'], 'educationalLevel': '입문',
            'license': '', 'url': SITE + page_file, 'registry': 'KG_00_registry 0.3', 'seeAlso': SITE + 'index.html',
            'suggestedCitation': f'안상선 ({DATE[:4]}). {title}. {SERIES} v{VERSION}.'}
    return kg, refs, meta


def retrofit(path, n, title, number, js):
    kg, refs, meta = kg_for(n, os.path.relpath(path, ROOT), title, number)
    tmp = tempfile.mkdtemp()
    files = {}
    for k, o in (('kg', kg), ('refs', refs), ('meta', meta)):
        files[k] = os.path.join(tmp, k + '.json')
        json.dump(o, open(files[k], 'w', encoding='utf-8'), ensure_ascii=False)
    subprocess.check_call([sys.executable, os.path.join(ROOT, 'kg', 'retrofit.py'), path, '--kg', files['kg'], '--refs', files['refs'],
                           '--meta', files['meta'], '--js', js, '-o', path], stdout=subprocess.DEVNULL)


def make_cards():
    """목차의 도면 카드 묶음을 만든다 (build/src/_cards.html)."""
    fam = {'base': ('기본 구조 계열 · 하루', 'haru'), 'seq': ('순서·기억 계열 · 모아', 'moa'), 'gen': ('압축·생성 계열 · 시아', 'sia'), 'rev': ('감수 · 초파리 & 주판봇', 'review')}
    order = [('base', ['01', '02', '09']), ('seq', ['03', '04', '05']), ('gen', ['06', '07', '08']), ('rev', ['10'])]
    out = []
    for f, ns in order:
        t, cls = fam[f]
        out.append(f'<h3>{t}</h3>\n<div class="cards">')
        for n in ns:
            p = BY_N[n]; w = WHO[p['who']]
            au = ('<img src="assets/img/chars/fly_e10.webp" alt="" width="28" height="28"><img src="assets/img/chars/robo_e10.webp" alt="" width="28" height="28">감수 · 초파리 연구원 &amp; 주판봇'
                  if p['who'] == 'review' else f'<img src="assets/img/chars/{p["who"]}_e13.webp" alt="" width="28" height="28">작성 · {w["full"]}')
            name = p['abbr'] if p['abbr'] != 'REVIEW' else '감수 도면'
            out.append(f'  <a class="card fam-{cls}" href="{p["file"]}"><img class="th" src="assets/img/covers/thumb_{n}.webp" alt="{p["code"]} 표지" width="600" height="400" loading="lazy">'
                       f'<span class="no">{p["code"]}</span><b>{name} · {E(p["ko"])}</b><span class="d">{E(p["desc"])}</span><span class="au">{au}</span></a>')
        if f == 'rev':
            out.append('  <a class="card fam-review" href="practice/index.html"><img class="th" src="assets/img/covers/thumb_00.webp" alt="실전 연습장 표지" width="600" height="400" loading="lazy">'
                       '<span class="no">마지막 장</span><b>실전 연습장 · 설계 의뢰 접수처</b><span class="d">현장 의뢰서 네 장을 받아 아홉 설계도 중 하나를 고르고 조건을 바꿔 보며, 감수자의 판정을 받는 연습장.</span>'
                       '<span class="au"><img src="assets/img/chars/doc_e08.webp" alt="" width="28" height="28">판정 · 박사</span></a>')
        out.append('</div>')
    open(os.path.join(HERE, 'src', '_cards.html'), 'w', encoding='utf-8').write('\n'.join(out))


def main():
    only = sys.argv[1:]
    make_cards()
    for p in P:
        if only and p['n'] not in only:
            continue
        if not os.path.exists(os.path.join(HERE, 'src', p['n'] + '.html')):
            print('건너뜀(본문 없음):', p['n']); continue
        out = os.path.join(ROOT, p['file'])
        open(out, 'w', encoding='utf-8').write(build_part(p))
        retrofit(out, p['n'], f'{p["code"]} {p["ko"]} 설계도면', p['n'], 'kg/kgx.js')
        print('만듦:', p['file'])
    # 목차
    if (not only or '00' in only) and os.path.exists(os.path.join(HERE, 'src', 'index.html')):
        src = open(os.path.join(HERE, 'src', 'index.html'), encoding='utf-8').read()
        src = src.replace('{{CARDS}}', open(os.path.join(HERE, 'src', '_cards.html'), encoding='utf-8').read())
        title = f'{SERIES} — 하루·모아·시아가 직접 그린 딥러닝 설계도면 9장 + 감수'
        desc = '조수 하루, 인턴 모아·시아가 딥러닝 모델 9종을 한 장씩 설계도면으로 그려 전달하고, 초파리와 주판봇이 총괄 도면을 감수한다.'
        out = os.path.join(ROOT, 'index.html')
        html_ = (head(title, desc, 'assets/img/covers/og_00.jpg') + '<body class="by-haru">\n<a class="skip" href="#main">본문으로 건너뛰기</a>\n' +
                 topnav('00') + src + footer() + '</body>\n</html>\n')
        open(out, 'w', encoding='utf-8').write(html_)
        retrofit(out, '00', title, '00', 'kg/kgx.js')
        print('만듦: index.html')
    if (not only or 'practice' in only) and os.path.exists(os.path.join(HERE, 'src', 'practice.html')):
        src = open(os.path.join(HERE, 'src', 'practice.html'), encoding='utf-8').read()
        title = f'실전 연습장 — 설계 의뢰 접수처 | {SERIES}'
        desc = '현장 의뢰서를 받고 아홉 설계도 중 하나를 골라 조건을 맞춰 보는 연습장.'
        html_ = (head(title, desc, 'assets/img/covers/og_00.jpg', '../') + '<body class="by-review">\n<a class="skip" href="#main">본문으로 건너뛰기</a>\n' +
                 topnav('practice', '../') + src + footer('../') + '</body>\n</html>\n')
        open(os.path.join(ROOT, 'practice', 'index.html'), 'w', encoding='utf-8').write(html_)
        print('만듦: practice/index.html')


if __name__ == '__main__':
    main()
