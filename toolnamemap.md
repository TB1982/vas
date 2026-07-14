# Guide 工具名四語對照（取自 app src/i18n/*.js，key parity 有 CI 守）

> 來源：Code宰相/Nova 提供的 app localization（zh / en / ja / zh-CN）。
> 用法：翻 guide 時工具名一律照此，不重譯。app key 附上供追溯。

## 截圖 / 工具列
| 繁中 | app key | English | 日本語 | 简体 |
|------|---------|---------|--------|------|
| 全螢幕 | fullscreen | Fullscreen | 全画面 | 全屏 |
| 視窗 | window | Window | ウィンドウ | 窗口 |
| 矩形 / 區域 | region | Region | 矩形 | 矩形 |
| 長截圖 | scroll_capture | Long screenshot | ロングスクリーンショット | 长截图 |
| 延遲 | delay | Delay | 遅延 | 延迟 |
| 取色器 | color | Color Picker | カラーピッカー | 取色器 |
| 尺標 | ruler | Ruler | 定規 | 标尺 |
| 呼吸燈 | （非 key）| breathing light | ⚠ 見下方討論 | 呼吸灯 |

## 選取工具
| 繁中 | key | English | 日本語 | 简体 |
|------|-----|---------|--------|------|
| 選取 | tool_select | Select | 選択 | 选取 |
| 框型選取 | tool_boxselect | Box Select | ボックス選択 | 框型选取 |

## 標註工具（12）
| 繁中 | key | English | 日本語 | 简体 |
|------|-----|---------|--------|------|
| 筆型 | tool_pen | Pen | ペン | 笔型 |
| 線條 | tool_line | Line | 線 | 线条 |
| 矩形框 | tool_rect | Rectangle | 矩形 | 矩形框 |
| 色塊 | tool_fillrect | Fill ⚠ | 塗りつぶし | 色块 |
| 文字 | tool_text | Text | テキスト | 文字 |
| 編號 | tool_number | Number | 番号 | 编号 |
| 符號印章 | tool_symbol | Stamp | スタンプ | 符号印章 |
| 馬賽克 / 模糊 | tool_mosaic | Mosaic/Blur | モザイク/ぼかし | 马赛克/模糊 |
| 放大鏡 | tool_magnify | Magnify Annotation | 拡大鏡注釈 | 放大镜标注 |
| 對話氣泡 | tool_callout | Callout Bubble | 吹き出し | 对话气泡 |
| OCR 文字辨識 | tool_ocr / help_ocr | OCR Text Recognition | OCR テキスト認識 | OCR 文字识别 |
| 隱私遮蔽 | tool_privacymask | Privacy Mask | プライバシーマスク | 隐私遮蔽 |

## 檢視工具（3）
| 繁中 | key | English | 日本語 | 简体 |
|------|-----|---------|--------|------|
| 放大 | tool_zoom_in | Zoom In | 拡大 | 放大 |
| 縮小 | tool_zoom_out | Zoom Out | 縮小 | 缩小 |
| 適合視窗 | tool_fit | Fit to Window | ウィンドウに合わせる | 适合窗口 |

## 畫布操作（3）
| 繁中 | key | English | 日本語 | 简体 |
|------|-----|---------|--------|------|
| 裁切 | tool_crop | Crop | トリミング | 裁切 |
| 調整大小 | tool_resize | Resize | サイズ変更 | 调整大小 |
| 延伸畫布 | tool_extend | Extend Canvas | キャンバス拡張 | 延伸画布 |

## 匯入・套版（2）
| 繁中 | key | English | 日本語 | 简体 |
|------|-----|---------|--------|------|
| 疊入圖片 | tool_overlay | Overlay Image | 画像オーバーレイ | 叠入图片 |
| 一鍵套版 | tool_template / tpl_title | Template ⚠ | テンプレート | 一键套版 |

## 往返操作（1）
| 繁中 | key | English | 日本語 | 简体 |
|------|-----|---------|--------|------|
| 撤銷 | tool_undo | Undo | 元に戻す | 撤销 |
| 重做 | tool_redo | Redo | やり直し | 重做 |

## OCR 三功能（頁面 h2；部分為 guide 自撰標題）
| 繁中 | 來源 | English | 日本語 | 简体 |
|------|------|---------|--------|------|
| 文字辨識 | help_ocr | Text Recognition (OCR) | OCR テキスト認識 | 文字识别 |
| 自動隱私遮蔽特化 | guide 自撰 | Auto Privacy Masking | 自動プライバシーマスク | 自动隐私遮蔽 |
| QR Code 掃描 | qr_toast | QR Code Scan | QR コードスキャン | QR Code 扫描 |

## 分類標籤（guide 自撰分組，非 app UI 字串；下為我建議，待 Nova 確認）
| 繁中 | English | 日本語 | 简体 |
|------|---------|--------|------|
| 選取工具 | Select | 選択 | 选取工具 |
| 標註工具 | Annotate | 注釈 | 标注工具 |
| 檢視工具 | View | 表示 | 检视工具 |
| 畫布操作 | Canvas | キャンバス | 画布操作 |
| 匯入・套版 | Import & Template | 読み込み・テンプレート | 导入・套版 |
| 往返操作 | History | 履歴 | 往返操作 |

