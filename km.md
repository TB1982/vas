# KM — VAS 網站已知坑與解法

> 遇到坑才記，記了就不用再踩第二次。

---

## 1. 錨點捲動在手機版落點錯誤

**症狀**  
點選漢堡選單裡的錨點連結（如「起源」），頁面捲動到錯誤位置，停在目標區塊上方 100–300px 處。桌機版 pill 直接點擊正常。

**根本原因（三層疊加）**

| 層次 | 原因 | 影響 |
|------|------|------|
| 1 | 懶加載圖片缺少 `width`/`height` | 圖片載入前高度=0，錨點位置計算偏小 |
| 2 | `getBoundingClientRect()` 在 `close()` 之後、layout 穩定之前呼叫 | 選單收起動作尚未完成 layout pass，拿到舊值 |
| 3 | 偏移量 `+8px` 太小 | divider 貼著 header，上方沒有呼吸空間 |

**解法**

```html
<!-- 所有 loading="lazy" 的圖片必須加 width/height 屬性 -->
<img src="img/foo.webp" width="1920" height="1080" loading="lazy" ...>
```

```js
// 把 getBoundingClientRect 計算移進 requestAnimationFrame 裡
// close() 之後 browser 完成 layout 再取值
window.scrollTo({ top: window.pageYOffset, behavior: 'auto' });
requestAnimationFrame(() => {
    const destY = target.getBoundingClientRect().top + window.pageYOffset;
    const offset = (header ? header.offsetHeight : 64) + 40; // +40 = page-section padding-top
    window.scrollTo({ top: Math.max(0, destY - offset), behavior: 'smooth' });
});
```

**規則**  
- 懶加載圖片一律補 `width`/`height`（用 `python3` + `struct` 量 WebP 尺寸）
- 偏移量 = `header.offsetHeight + page-section padding-top`（目前均為 40px）
- 錨點位置計算必須在 rAF 內執行，不可在 click handler 頂部

---

## 2. 行動版 iOS Safari 捲動停在錯誤位置（mid-scroll 點擊）

**症狀**  
從功能→細節依序快點到起源時，頁面停在中間位置。

**原因**  
iOS Safari 不會取消進行中的 `smooth` scroll，兩段動畫疊加導致最終位置錯誤。

**解法**  
點擊前先用 `behavior: 'auto'` 釘住當前位置，再啟動新的 smooth scroll（已包含在上方 rAF 解法中）。

---

## 3. 首頁 VAS logo 重疊

**症狀**  
浮動 nav 與 sticky header 各有一個 VAS，捲動時兩個重疊。

**根本原因**  
設計層次過多：浮動 nav（z-60）＋ sticky header（z-50）各自渲染 VAS logo。

**解法**  
移除浮動 nav，將頁內錨點連結整合進 sticky header：
- 手機：hamburger 下拉選單（`sm:hidden`）
- 桌機：pill group（`hidden sm:flex`）

只剩一個 VAS，問題消失。

---

## 4. `getBoundingClientRect` vs `offsetTop` 的選擇

**結論：用 `getBoundingClientRect() + window.pageYOffset`，不用 `offsetTop` 遞迴加總。**

`offsetTop` 遞迴：在有 `position: relative` 祖先、margin collapsing 或 sticky 元素的情況下，容易算錯。  
`getBoundingClientRect() + pageYOffset`：瀏覽器直接給絕對座標，更可靠——但必須在 layout 穩定後呼叫（見坑 1）。

---

## 5. 圖片語言切換未更新 width/height 屬性

**症狀（潛在）**  
切換語言時 `switchLanguage()` 更換 `img.src`，但 HTML 上的 `width`/`height` 屬性仍是原始語言的尺寸，可能造成 CLS。

**現況**  
`vastoolbar`、`vasframe`、`sharesheet`、`fast` 四張圖有多語言版本（`-jp`、`-en`）。若各語言版本尺寸相同則無影響；若不同，需在 `switchLanguage` 裡一併更新屬性：

```js
img.src = '...';
img.width = 1920;   // 對應語言版本的實際尺寸
img.height = 1080;
```

**待確認**：各語言版本是否尺寸相同。
