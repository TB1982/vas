// version.js — VAS 版本號單一來源
// 所有頁面的版本號從這裡讀取，更新時只需改這一個檔案。
//
// 使用方式：
//   <script src="version.js"></script>
//   然後在 JS 裡用 window.VAS_VERSION（完整版本號）
//   或 window.VAS_VERSION_SHORT（不含 patch，如 "3.44"）
//
// 下載連結範例：
//   'https://github.com/TB1982/pm/releases/download/v' + VAS_VERSION + '/VAS-' + VAS_VERSION + '-arm64.dmg'

(function () {
  var VERSION = '3.44.0';
  window.VAS_VERSION = VERSION;
  window.VAS_VERSION_SHORT = VERSION.split('.').slice(0, 2).join('.');
}());
