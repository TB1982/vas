// i18n-shared.js — VAS 系列頁面共用翻譯 + 下拉選單邏輯
// 載入順序：此檔必須在各頁的 i18n-xxx.js 之前載入

window.VASShared = (function () {

  // ── 共用翻譯資料 ─────────────────────────────────────────────
  var sharedT = {
    zh: {
      footer: '由 GitHub 部署　｜　Claude Code 傾力打造　｜　<a href="mailto:babelon1882@gmail.com" class="hover:text-white/50 transition-colors">Nova</a> 最後更新於 2026',
      privacyLink: '隱私權政策', pmLink: '深握計畫',
      navGuide: '操作手冊', navGuideShort: '操作',
      navInsight: '設計洞察', navInsightShort: '設計',
      navMilestone: '里程碑',  navMilestoneShort: '里程碑',
      navCollab: '協作筆記',   navCollabShort: '協作',
      navHarness: '系統建構裏話', navHarnessShort: '系統'
    },
    en: {
      footer: 'Deployed via GitHub　｜　Built with Claude Code　｜　Last updated 2026 by <a href="mailto:babelon1882@gmail.com" class="hover:text-white/50 transition-colors">Nova</a>',
      privacyLink: 'Privacy Policy', pmLink: 'Deep Holding Project',
      navGuide: 'User Guide',      navGuideShort: 'Guide',
      navInsight: 'Design Insights', navInsightShort: 'Insights',
      navMilestone: 'Milestones',  navMilestoneShort: 'Milestone',
      navCollab: 'Collab Notes',   navCollabShort: 'Collab',
      navHarness: 'System Thinking', navHarnessShort: 'System'
    },
    ja: {
      footer: 'GitHub でデプロイ　｜　Claude Code で構築　｜　2026年 <a href="mailto:babelon1882@gmail.com" class="hover:text-white/50 transition-colors">Nova</a> 最終更新',
      privacyLink: 'プライバシーポリシー', pmLink: 'ディープホールディング計画',
      navGuide: '操作マニュアル', navGuideShort: '操作',
      navInsight: 'デザインの洞察', navInsightShort: '洞察',
      navMilestone: 'マイルストーン', navMilestoneShort: 'マイル',
      navCollab: '協作ノート',     navCollabShort: '協作',
      navHarness: 'システム構築の裏話', navHarnessShort: 'システム'
    }
  };

  var labelMap = { zh: '中', en: 'EN', ja: '日' };

  // ── 下拉選單 UI 更新 ─────────────────────────────────────────
  function updateDropdown(lang) {
    var label = document.getElementById('langDropdownLabel');
    if (label) label.textContent = labelMap[lang] || lang;
    document.querySelectorAll('.lang-opt').forEach(function (btn) {
      btn.classList.toggle('active', btn.dataset.lang === lang);
    });
  }

  // ── 下拉選單事件綁定 + 語言恢復 ─────────────────────────────
  // applyFn(lang) 由各頁自行提供
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

    // 恢復上次語言選擇
    try {
      var saved = localStorage.getItem('vasLang');
      if (saved && labelMap[saved]) applyFn(saved);
    } catch (e) {}
  }

  // ── 手機版頁內/頁間 nav 下拉選單 ────────────────────────────
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
    menu.querySelectorAll('a').forEach(function(a) { a.addEventListener('click', close); });
    document.addEventListener('click', close);
  }

  return { sharedT: sharedT, initDropdown: initDropdown, updateDropdown: updateDropdown, initNavDropdown: initNavDropdown };

})();
