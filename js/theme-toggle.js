/* VAS · Guide theme toggle · 深色(器)/淺色(思)
   預設淺色；記憶於 localStorage['vas-theme']。
   FOUC 由各頁 <head> 內聯腳本先行套用，本檔只負責互動與圖示狀態。 */
(function () {
  var KEY = 'vas-theme';
  function current() { return document.documentElement.getAttribute('data-theme') || 'light'; }
  // aria-label 依 <html lang> 在地化；繁中維持原字串（向後相容）。
  var LABELS = {
    'zh-Hant': ['切換到深色', '切換到淺色'],
    'en':      ['Switch to dark', 'Switch to light'],
    'ja':      ['ダークに切り替え', 'ライトに切り替え'],
    'zh-Hans': ['切换到深色', '切换到浅色']
  };
  function labels() {
    return LABELS[document.documentElement.getAttribute('lang')] || LABELS['zh-Hant'];
  }
  function sync() {
    var t = current(), lab = labels();
    document.querySelectorAll('.theme-toggle').forEach(function (b) {
      b.setAttribute('aria-label', t === 'light' ? lab[0] : lab[1]);
      b.setAttribute('aria-pressed', t === 'dark' ? 'true' : 'false');
    });
  }
  function apply(t) {
    document.documentElement.setAttribute('data-theme', t);
    try { localStorage.setItem(KEY, t); } catch (e) {}
    sync();
  }
  function toggle() { apply(current() === 'light' ? 'dark' : 'light'); }
  function init() {
    document.querySelectorAll('.theme-toggle').forEach(function (b) {
      b.addEventListener('click', toggle);
    });
    sync();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
}());
