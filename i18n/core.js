// i18n/core.js — VAS 導覽核心：手機版頁內 nav 下拉選單
// 註：本站為 static-per-locale，每個語系是獨立檔案（zh 根目錄 / en/ ja/ cn/）。
// 早期的執行期 i18n（applyLang + data-lang-key + i18n/<lang>.js 語言包）已於 2026-06 全數拆除——
// 它從未被實際呼叫，是會誤導人的死碼。語系切換一律靠頁面導覽，不靠執行期換字。
(function () {

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
    initNavDropdown: initNavDropdown
  };

})();
