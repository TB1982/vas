// i18n-privacy.js — VAS 隱私權政策頁翻譯
// 依賴：i18n-shared.js 必須先載入
(function () {
  var pageT = {
    zh: {
      pageLabel: 'Legal',
      appName: 'VAS 隱私權政策',
      updatedDate: '最後更新：2026-04-03'
    },
    en: {
      pageLabel: 'Legal',
      appName: 'VAS Privacy Policy',
      updatedDate: 'Last updated: 2026-04-03'
    },
    ja: {
      pageLabel: 'Legal',
      appName: 'VAS プライバシーポリシー',
      updatedDate: '最終更新：2026-04-03'
    }
  };

  // sharedT 已包含 footer，合併進來
  ['zh', 'en', 'ja'].forEach(function (l) {
    Object.assign(pageT[l], window.VASShared.sharedT[l]);
  });

  window.VASPrivacyT = pageT;
}());
