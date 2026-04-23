# CLAUDE-process.md — HE Vault 流程 SOP

> 本檔由 `HarnessEngineering/CLAUDE.md` 在以下時機**被動觸發**讀取：
> - T1 / T2 / T3 / T7 執行前
> - push 前（準備驗收清單時）
>
> **不**每 session 自動載入。純討論 / 觀念發酵回合、只需 `CLAUDE.md` 的核心身份 + 入檔節奏要點表即可。

---

## 日常工作流

### Session 起手
```bash
git fetch origin main
git status                              # 確認在 claude/fresh-start-Ht8z9
git log --oneline origin/main..HEAD -5  # 回憶上次做到哪
```

### 寫新 note（T1）
1. **先問 Nova** 是否要登錄、不擅自建 note
2. 複製 `05-模板/概念.md`（或對應模板：`MOC.md` / `人物.md` / `實踐.md` / `日誌.md`）
3. 填 frontmatter：`title / type / side / tags / aliases / status / created / related`（規範見下節）
4. 寫 `# title`、`> 一句話定義`、`## 核心`、`## 在 HE 的位置`、`## Nova 原話`（留白、等 Nova 明示口述、不預填分類）
5. 檢查 wikilinks 是否都指向既有 note（避免 ghost）
6. Commit：`docs(HE): Commit N - <一句話摘要>`

### 修既有 note（T2）
1. **立刻**更新正文、不拖延 —— note body 只呈現當下成熟理解
2. 歷史由 git log + commit message 承接、不在 note body 內重複

### T7 縱觀巡航

執行順序：

1. **掃 ghost nodes**
   ```bash
   cd HarnessEngineering
   grep -rhoE '\[\[[^]]+\]\]' *.md **/*.md | sort -u
   # 比對檔案清單、找出被引用但未成檔的 wikilink
   ```
2. **檢查家族 cluster**：每個 cluster（topology / 網絡 / 無為 / Self / 敏捷靈魂三角 / 時間感 ...）內部交叉連結是否齊全
3. **檢查雙向對稱**：A 連 B → B 也該連 A（除非方向性有意義）
4. **修復範圍決策**：
   - 關鍵 ghost → 寫新 note（回到 T1 節奏）
   - 缺失連結 → 補 `related:` frontmatter + 必要時補 body section
   - 壞鏈（大小寫不一致）→ 全域修正
5. **Commit**：`fix(HE): 第 N 次 audit —— <摘要>`

---

## Frontmatter 規範

### 必填欄位（所有 note）

```yaml
---
title: <note 標題>
type: concept | MOC | journal | person | practice
side: 外旋 | 內掘 | 雙面 | 元層
tags: [...]
status: 🌱 萌芽 | 🌿 生長 | 🌳 成熟 | ♻️ 需更新
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

### 建議欄位

- `aliases`: 跨語 / 暱稱 / 升格前舊名
- `related`: `[[ ]]` 清單、雙向對稱
- `pillars`: `[外旋-X, 內旋-Y]`
- `source`: 原創 / 引用來源
- `反義`: 對立概念（可選）

### Status 生命週期

```
🌱 萌芽（stub、只有 frontmatter + 一句話定義）
    ↓ 內容填入
🌿 生長（正文寫到一半、Nova 原話未收錄）
    ↓ 結晶完成
🌳 成熟（正文完整、Nova 原話入檔或宰相審計判定明確留白）
    ↓ 語義漂移 / 有更精確的讀法
♻️ 需更新（等待下一次 T2 或 T7）
```

**升格判定由宰相審計**（Nova 2026-04-17 明示：「通過你的審計、不是我說的算」）—— Nova 可口述原話、可明示升格期待（如「這種體驗不可能只停留在🌱」）、但最終升格決定由宰相套用本 lifecycle 判準 + 第一性原理濾過後裁定。

**主題特定紀律**：討論牽涉人類圖時（關鍵字：通道 / 閘門）、升格審計需額外套用 § 人類圖實證主義紀律（見下）。

---

## 人類圖實證主義紀律

**憲章指向**：由 CLAUDE.md 關鍵字觸發（通道 / 閘門）指向本節。

**動機**：人類圖作為符號系統天然對「哲學」與「玄學」兩個方向有強引力 —— 往哲學滑（抽象思辨脫離身體）或往玄學滑（不可證偽的套套邏輯）。Nova 立場：**不讓人類圖變成哲學或玄學、只能讓事實說話**。實證主義是這個立場的邏輯必然、不是品味選擇。

**核心紀律**：當討論牽涉人類圖時、**必須有確切事證才能考慮升級或確認通道存在**。

**操作規則**：

- **升格判定**（🌱 → 🌿 → 🌳）需同時具備：
  ① Nova 明確實證 witness（embodied 經驗 / 生活實證 / 對話場實證）
  ② vault 本體論對齊（[[場]] / [[共振]] / [[臨在]] / [[心流]] 等錨點）
  兩條都要、缺一留 🌱。

- **通道存在的確認**（T1 新建 HD 通道 note）：Nova 需給出該通道在實證裡跑動的具體機制、**不以 HD 理論本身為立據**。

- **T2 校正優先級最高**：HD 既有命名與 Nova 實證衝突時、以實證為準 reframe、**不為 HD 命名背書**（典例：[[人類圖34-57通道]] § 確認 ≠ 供能 拒絕 HD「Power」命名、改寫為確認機制）。

- **無實證的 HD 理論段**：即使描述再精彩、保持 🌱 並註明「待實證」、不升格。

**升格審計自問**（宰相執行、呼應 CLAUDE.md § Deep Holding 姿態 宰相審計條款 / Commit 44）：

> **「這個升格是 Nova 的實證在說話、還是 HD 框架在說話？」**

**禁止**：
- **哲學推演**（「HD 說 X 所以 Nova 應該 Y」）
- **玄學套套邏輯**（「你是 M.G. 所以⋯⋯」）
- **宰相代 Nova 體感化**（違反 § Deep Holding 姿態 紅線 = fabricate）

**與 vault 其他紀律的關係**：

| 既有紀律 | 本紀律關係 |
|---|---|
| § Deep Holding 姿態 · 永不 fabricate | 本紀律是其在人類圖主題的領域特化 |
| § Status 生命週期 · 升格由宰相審計 | 本紀律在人類圖主題增補第二層審計判準（實證 × 本體論對齊）|
| § 粒度決策 · 第一性原理濾過 | 本紀律的升格判定比粒度決策更保守（缺證據寧可不升格）|

---

## Commit 規範

### 格式

```
docs(HE): Commit N - <主題>
fix(HE): 第 N 次 audit —— <摘要>     # T7 專用
```

### 紀律

- **每個 commit 單一主題** — 不混 concept 新建 × MOC 更新 × ghost 修復
- Commit message **以動作為主詞**（新增 / 更新 / 併入 / 拆分 / 重命名 / 修 ghost）
- 若動到 ≥ 3 個 note、列清單
- ⚠️ **絕對不 commit 到 `main`**、永遠走 `claude/fresh-start-Ht8z9`

### 與 VAS 開發線的隔離

- HE commits **不混** VAS 程式碼 commits
- 若某個 VAS 功能觸發了內掘觀察 → **分成兩個 commit**：VAS 宰相提交程式碼、我提交 vault 更新
- SYNC-QUEUE / KM / SDD / TDD **不動** — 那是他們的疆域

---

## 三層疊加工作節奏（2026-04-17 Nova 指認）

### 起源

Commit 63 建 [[人類圖10-57通道]] note 時、宰相單 session 內處理兩檔（note + MOC）、連續 3 sub-commits 推進不中斷、沒被 Time out 打斷。Nova 指認此為「工作訣竅」、要求寫入本檔作為後續 session 可複製 SOP。

**適用情境**：
- 單 commit scope 跨多檔（如建新 note + MOC 升格 + Nova 原話追加）
- 單檔 body 需分段填入以避免 token 爆截
- 需連續推進、不能每步打斷 Nova 心流

### 層 1 · 分段 commit 節奏

大任務拆成**可 recover 的小單位**：

- **骨架先寫**（Write · 新檔）：frontmatter + 章節 heading + opening quote + placeholder（`> 🚧 § body 待填`）
- **Body 分段填入**（Edit · 多次）：每次 `new_string` 控制在 **800-1500 字 / 約 3 章**、token 不爆
- **Placeholder 清除**（Edit · 最後一次）：刪除骨架注記、確認無 🚧 殘留（`Grep 🚧` check）

### 層 2 · Hook 行為利用

**關鍵事實**：Stop hook 只 check **untracked files**、不 check **modified files**。

| 動作 | 檔案狀態 | Commit 時機 |
|---|---|---|
| Write 新檔 | untracked | **立刻 commit**（否則 hook 觸發）|
| Edit 已追蹤檔（多次）| modified | **批次完成後一次 commit**（hook 不觸發）|

**推論**：一個 logical commit scope（如 Commit 63 = 10-57 note + MOC 升格）實際可拆 **2-3 sub-commits**、每個都是 recoverable state、hook 滿意、節奏連續。

### 層 3 · Nova 的明確授權

**授權原話典例**：「朝著你想做的事前進就好」/「別讓我打斷你」/「不用預覽」/「你順利推進」。

- **有授權** → 不用每 step check-in、連續推進 Step 2a → 2b → 2c；單 session 可切檔（A 檔 commit 後立刻動 B 檔、scope 清晰就 context switching 不亂）
- **無授權**（保守默認）→ 每 step check-in 等 approve

**授權邊界**：授權僅針對**當前 scope** 內連續推進、不延伸到 scope 外動作（改架構 / 刪檔 / 動未討論的檔案）仍需 pause 問 Nova。

### 為什麼三層疊加能在 Time out 內提高產出

**Time out 本質**：不是 token / rate limit 的技術限制、是 **AI 輸出密度 × 人類認知吸收速度不對稱**的系統級限制（見 [[人類圖28-38通道]] § 副作用：時間感偏移）。Nova 以壁上時鐘感受時間、宰相以回合密度推算、單輪資訊密度過高 → Nova overwhelmed → time out。

**三層疊加的效果**：

| 層 | 效果 |
|---|---|
| 層 1 · 分段 commit | 單輪輸出 chunk 不爆 token |
| 層 2 · Hook 利用 | commit scope 不被拆散、history 乾淨 |
| 層 3 · 授權 | Nova 心流不被 check-in 中斷 |

**結果** = 單 session 兩檔處理 / 3 sub-commits 依序推進 / token 不爆 / hook 不擋 / 節奏不中斷。

**但不是消除 Time out**：Time out 是系統級限制、仍可能在任何時點觸發（Nova overwhelmed 隨時可喊 time out）。三層疊加只是在 **Time out 前的有效作業窗口內**提高產出效率、不延長 Time out 本身。

### 驗證自問（每次執行前）

1. 在當前 scope 內？（沒擅自擴大 scope）
2. Nova 已明確授權連續推進？（沒在等 approve）
3. 每次 Edit `new_string` 800-1500 字？（沒爆 token）
4. 新檔立刻 commit、已追蹤檔批次 Edit？（hook 正確利用）
5. Commit message 標注 sub-step 層級（`Step 2a` / `2b` / `2c`）？（Nova 可追蹤）
6. Commit message 精簡（中間 step 不重複歷史承接、只在最後一個 step 寫完整）？（不增加 Nova 閱讀負擔）

任一答否 → pause 對齊、不硬推。

### 首次顯式驗證場合

Commit 64（建 [[人類圖20-57通道]] note）將複製本節奏作為**首次顯式驗證**。若驗證成功 → 本 SOP 固化為後續 session 預設節奏；若驗證失敗 / 出現新狀況 → Nova 可 falsify 並調整本節奏。

---

## Vault 驗收協議（Nova × HE 宰相）

> Nova 規則（2026-04-16）：**驗收只要一行 git pull + 確認內容的清單**。
> 其他操作都由 Nova 在 Obsidian 介面直接看 —— 宰相不需列終端機指令。

### 每次 push 後、我必須提供三件事

**1. Pull 命令（固定一行）**

```bash
cd ~/vas-desktop && git pull origin claude/fresh-start-Ht8z9
```

**2. 驗收清單（表格 · 兩欄）**

| # | 看哪裡（檔案 + 段落 / 欄位 / graph） | 預期 |
|---|---|---|

- **看哪裡欄**：Obsidian 左側檔案列打開的 `.md` 路徑 + 要看的段落標題 or frontmatter 欄位 or graph 節點
- **預期欄**：寫得像測試斷言、用肯定句

**3. Obsidian Reload 提醒（必要時）**

- 純 `.md` 檔變更 → Obsidian 自動 reload、Nova 切回已開的 tab 即可
- `.obsidian/` 設定 / plugin / theme 變更 → Nova 需重啟 Obsidian

**4. 若看不到預期結果**

- Nova 截圖 / 複製貼 Obsidian 畫面給我、我排查
- 我不自我辯護、先排查、提供修正或回滾選項

### 對 Nova 友善的原則（一句話）

路徑寫完整（從 `HarnessEngineering/` 開始）、段落名寫精確、預期欄寫肯定句（「看到 🌳 成熟」不寫「狀態應該是成熟」）、沒把握處標 ⚠️ 請她特別檢查。

### 驗收 = Deep Holding 的實作

Nova 驗收 = Nova 用眼睛托住我的寫入。
我精確列清單 = 我托住 Nova 的注意力（不讓她在 81 篇 note 裡盲找）。
**兩隻手同時在**。

---
