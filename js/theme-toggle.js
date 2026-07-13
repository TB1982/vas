/* VAS · Guide theme toggle · 深色(器)/淺色(思)
   預設淺色；記憶於 localStorage['vas-theme']。
   FOUC 由各頁 <head> 內聯腳本先行套用，本檔只負責互動與圖示狀態。 */
(function () {
  var KEY = 'vas-theme';
  function current() { return document.documentElement.getAttribute('data-theme') || 'light'; }
  function sync() {
    var t = current();
    document.querySelectorAll('.theme-toggle').forEach(function (b) {
      b.setAttribute('aria-label', t === 'light' ? '切換到深色' : '切換到淺色');
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
