// i18n/core.js — VAS 語系核心：動態載入 + dropdown 邏輯
// 無翻譯資料。新增語系只需加 i18n/<lang>.js，無需改此檔。
(function () {

  var labelMap = { zh: '中', en: 'EN', ja: '日', cn: '简' };
  var loaded   = {};

  // ── 動態載入語言包 ───────────────────────────────────────────
  function loadLang(lang, cb) {
    if (window.VASI18n && window.VASI18n[lang]) {
      cb(window.VASI18n[lang]);
      return;
    }
    var s    = document.createElement('script');
    s.src    = 'i18n/' + lang + '.js';
    s.onload = function () { cb(window.VASI18n[lang]); };
    s.onerror = function () { console.warn('[VASCore] failed to load i18n/' + lang + '.js'); };
    document.head.appendChild(s);
  }

  // ── 語言下拉選單 UI 更新 ─────────────────────────────────────
  function updateDropdown(lang) {
    var label = document.getElementById('langDropdownLabel');
    if (label) label.textContent = labelMap[lang] || lang;
    document.querySelectorAll('.lang-opt').forEach(function (btn) {
      btn.classList.toggle('active', btn.dataset.lang === lang);
    });
  }

  // ── 下拉選單事件綁定 + 語言恢復 ─────────────────────────────
  function initDropdown(applyFn) {
    var btn  = document.getElementById('langDropdownBtn');
    var menu = document.getElementById('langDropdownMenu');
    if (!btn || !menu) return;

    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var willOpen = !menu.classList.contains('open');
      menu.classList.toggle('open', willOpen);
      btn.setAttribute('aria-expanded', String(willOpen));
    });

    document.querySelectorAll('.lang-opt').forEach(function (opt) {
      opt.addEventListener('click', function () {
        applyFn(opt.dataset.lang);
        menu.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
      });
    });

    document.addEventListener('click', function () {
      if (menu.classList.contains('open')) {
        menu.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
      }
    });

    // 恢復上次語言，或依瀏覽器語言自動偵測
    try {
      var saved = localStorage.getItem('vasLang');
      if (saved && labelMap[saved]) { applyFn(saved); return; }
    } catch (e) {}
    var bl   = (navigator.language || '').toLowerCase();
    var auto = (bl === 'zh-cn' || bl.startsWith('zh-hans') || bl === 'zh-sg') ? 'cn'
             : bl.startsWith('zh') ? 'zh'
             : bl.startsWith('ja') ? 'ja'
             : 'en';
    applyFn(auto);
  }

  // ── 手機版頁內 nav 下拉選單 ──────────────────────────────────
  function initNavDropdown() {
    var btn     = document.getElementById('navMobileBtn');
    var menu    = document.getElementById('navMobileMenu');
    var chevron = document.getElementById('navMobileChevron');
    if (!btn || !menu) return;
    var open = false;

    function close() {
      open = false;
      menu.style.display = 'none';
      if (chevron) chevron.style.transform = '';
      btn.setAttribute('aria-expanded', 'false');
    }
    function toggle(e) {
      e.stopPropagation();
      if (open) { close(); return; }
      open = true;
      menu.style.display = 'flex';
      if (chevron) chevron.style.transform = 'rotate(180deg)';
      btn.setAttribute('aria-expanded', 'true');
    }

    btn.addEventListener('click', toggle);
    menu.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', close); });
    document.addEventListener('click', close);
  }

  window.VASCore = {
    loadLang:        loadLang,
    updateDropdown:  updateDropdown,
    initDropdown:    initDropdown,
    initNavDropdown: initNavDropdown
  };

})();
