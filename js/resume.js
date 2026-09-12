/* VAS · 數位履歷 · 頁面互動（QR 彈窗 · 右側點點目錄）
   中英兩版共用。本檔不含任何需在地化的字串——按鈕文字都在各自的 HTML 裡。 */
(function(){
  var url = location.href.split('#')[0];
  function draw(el, cell){
    var q = qrcode(0,'M'); q.addData(url); q.make();
    el.innerHTML = q.createSvgTag({cellSize:cell, margin:0, scalable:true});
    var svg = el.querySelector('svg');
    if(svg){ svg.removeAttribute('width'); svg.removeAttribute('height'); svg.style.width='100%'; svg.style.height='auto'; }
  }
  var big = document.getElementById('qrBig');
  if(window.qrcode){ draw(big,8); }
  else {
    // CDN 讀不到時（會場網路擋外連）不留空白框，改顯示網址讓對方手打
    big.innerHTML = '<div style="color:#0e0b1a;font-family:var(--vas-mono);font-size:11px;'
                  + 'letter-spacing:.06em;word-break:break-all;line-height:1.7">' + url + '</div>';
  }
  document.getElementById('qrUrl').textContent = url;
  var m = document.getElementById('qrModal');
  document.getElementById('qrFab').onclick = function(){ m.classList.add('open'); };
  document.getElementById('qrClose').onclick = function(){ m.classList.remove('open'); };
  m.onclick = function(e){ if(e.target === m) m.classList.remove('open'); };
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape') m.classList.remove('open'); });

  // ── 點點目錄：捲動時標出目前章節 ──
  var items = [].slice.call(document.querySelectorAll('.dn-item'));
  var targets = items.map(function(a){ return document.getElementById(a.getAttribute('href').slice(1)); });
  function mark(){
    var line = window.scrollY + window.innerHeight * 0.32, cur = 0;
    targets.forEach(function(t, i){ if(t && t.offsetTop <= line) cur = i; });
    // 捲到底時最後一節可能永遠追不到偵測線，直接判定為最後一項
    if(window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 4) cur = items.length - 1;
    items.forEach(function(a, i){
      a.classList.toggle('is-current', i === cur);
      a.classList.toggle('is-visited', i < cur);
    });
  }
  mark();
  addEventListener('scroll', function(){ requestAnimationFrame(mark); }, {passive:true});
  addEventListener('resize', mark);
})();
