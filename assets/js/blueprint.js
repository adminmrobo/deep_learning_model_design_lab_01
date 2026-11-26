/* 딥러닝 설계도면 연구실 01 — 공용 동작 (외부 라이브러리 없음) */
var BP = (function () {
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function fmt(x, d) { d = d == null ? 3 : d; var v = Number(x).toFixed(d); return v === '-0.' + '0'.repeat(d) ? (0).toFixed(d) : v; }
  function sig(x) { return 1 / (1 + Math.exp(-x)); }
  function tanh(x) { var a = Math.exp(x), b = Math.exp(-x); return (a - b) / (a + b); }

  /* 선택형 문제: <div class="choices" data-answer="b"> <button data-k="a">…</button> … </div><p class="feedback" data-ok=".." data-no=".."></p> */
  function choices() {
    $$('.choices').forEach(function (box) {
      var ans = box.getAttribute('data-answer');
      var fb = box.nextElementSibling;
      $$('button', box).forEach(function (b) {
        b.type = 'button';
        b.addEventListener('click', function () {
          $$('button', box).forEach(function (x) { x.classList.remove('right', 'wrong'); });
          var ok = b.getAttribute('data-k') === ans;
          b.classList.add(ok ? 'right' : 'wrong');
          if (fb && fb.classList.contains('feedback')) {
            fb.innerHTML = ok ? ('⭕ ' + (fb.getAttribute('data-ok') || '맞았어요.')) : ('다시 보기 · ' + (b.getAttribute('data-why') || fb.getAttribute('data-no') || '다른 답을 골라 보세요.'));
          }
        });
      });
    });
  }

  /* 슬라이더 값 표시: <input type=range id=x> 와 <span class="val" data-for="x"> */
  function bindVals(root) {
    $$('.val[data-for]', root).forEach(function (s) {
      var i = document.getElementById(s.getAttribute('data-for'));
      var d = +(s.getAttribute('data-d') || 2);
      var up = function () { s.textContent = fmt(i.value, d); };
      i.addEventListener('input', up); up();
    });
  }

  function svg(tag, attrs, text) {
    var e = document.createElementNS('http://www.w3.org/2000/svg', tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text != null) e.textContent = text;
    return e;
  }

  document.addEventListener('DOMContentLoaded', function () { choices(); bindVals(); });
  return { $: $, $$: $$, fmt: fmt, sig: sig, tanh: tanh, svg: svg, bindVals: bindVals };
})();
