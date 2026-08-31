# VAS App — 全語 UI 用詞對照表

> **這是生成物，不要手改。** 重跑取最新：`node scripts/dump-i18n-table.mjs -o <檔名>`
> 正本＝`src/i18n/*.js`；語言名單正本＝`src/i18n.js` 的 `LANG_REGISTRY`（本表不手抄名單）。

## 這份表要怎麼用

官網若要與 app 用詞對齊，**以本表的值為準**——app 的字串是使用者實際看到的東西。
對不上時請回報，不要單方面改任一邊：兩邊都可能是對的，差異可能是刻意的（例如官網要完整句、app 受按鈕寬度限制）。

⚠️ **帶參數的訊息不列值**（值是函式、要代入參數才成形）——那類字串通常是 toast 與錯誤訊息，不是 UI 用詞，對官網文案影響小。

## 網站語言前綴（官網對接點）

| app 語言碼 | macOS bundle 碼 | 官網前綴 `sitePrefix` |
|---|---|---|
| `zh-CN` | `zh-Hans` | `cn/` |
| `zh` | `zh-Hant` | `` |
| `ja` | `ja` | `ja/` |
| `en` | `en` | `en/` |
| `es` | `es` | `es/` |

## 用詞對照

### `action`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `action_toast_dismiss` | 跳过 | 略過 | 閉じる | Dismiss | Descartar |

### `align`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `align_bottom_title` | 靠下 | 靠下 | 下揃え | Align Bottom | Alinear abajo |
| `align_btn_bottom` | 齐下 | 齊下 | ↓B | ↓B | ↓B |
| `align_btn_dist_h` | 水均 | 水均 | H= | H= | H= |
| `align_btn_dist_v` | 垂均 | 垂均 | V= | V= | V= |
| `align_btn_hcenter` | 水中 | 水中 | ↔C | ↔C | ↔C |
| `align_btn_left` | 齐左 | 齊左 | ←L | ←L | ←I |
| `align_btn_right` | 齐右 | 齊右 | R→ | R→ | D→ |
| `align_btn_top` | 齐上 | 齊上 | ↑T | ↑T | ↑A |
| `align_btn_vcenter` | 垂中 | 垂中 | ↕C | ↕C | ↕C |
| `align_center` | 中 | 中 | 中 | C | C |
| `align_dist_h_title` | 水平均分 | 水平均分 | 水平均等配置 | Distribute Horizontal | Distribuir en horizontal |
| `align_dist_v_title` | 垂直均分 | 垂直均分 | 垂直均等配置 | Distribute Vertical | Distribuir en vertical |
| `align_group_label` | 对齐 | 對齊 | 整列 | Align | Alinear |
| `align_hcenter_title` | 水平居中 | 水平置中 | 水平中央揃え | Center Horizontal | Centrar en horizontal |
| `align_left` | 左 | 左 | 左 | L | I |
| `align_left_title` | 靠左 | 靠左 | 左揃え | Align Left | Alinear a la izquierda |
| `align_right` | 右 | 右 | 右 | R | D |
| `align_right_title` | 靠右 | 靠右 | 右揃え | Align Right | Alinear a la derecha |
| `align_to_canvas` | 对齐中线 | 對齊中線 | 中央に揃える | Center | Centrar |
| `align_top_title` | 靠上 | 靠上 | 上揃え | Align Top | Alinear arriba |
| `align_vcenter_title` | 垂直居中 | 垂直置中 | 垂直中央揃え | Center Vertical | Centrar en vertical |

### `anno`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `anno_size_preset_title` | 快速选择大小 | 快速選擇大小 | サイズを選択 | Quick size selection | Elegir rápido el tamaño |

### `aria`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `aria_color_picker` | 选色面板 | 選色面板 | カラーピッカー | Color Picker | Selector de color |
| `aria_remove_file` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `aria_symbol_picker` | 符号选取面板 | 符號選取面板 | シンボル選択 | Symbol Picker | Selector de símbolos |
| `aria_template_panel` | 套版选择 | 套版選擇 | テンプレート | Template | Plantilla |

### `batch`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `batch` | 批量转 | 批次轉 | 一括変換 | Batch | Lote |
| `batch_add_more` | + 新增文件 | + 新增檔案 | + ファイルを追加 | + Add Files | + Añadir archivos |
| `batch_choose` | 选择… | 選擇… | 選択… | Choose… | Elegir… |
| `batch_convert_to` | 转换为 | 轉換為 | 変換形式 | Convert to | Convertir a |
| `batch_custom_dir` | 指定目录 | 指定目錄 | カスタムフォルダ | Custom directory | Carpeta personalizada |
| `batch_delete_orig` | 转换完成后删除原始文件 | 轉換完成後刪除原始檔 | 変換後に元ファイルを削除 | Delete originals after conversion | Eliminar los originales tras la conversión |
| `batch_drop_hint` | 拖拽图片至此，或 | 拖曳圖片至此，或 | ここに画像をドロップ、または | Drop images here, or | Suelta imágenes aquí, o |
| `batch_err_convert_failed` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `batch_err_dir_not_writable_custom` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `batch_err_dir_not_writable_same` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `batch_err_invalid_path` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `batch_err_mkdir_failed` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `batch_err_needs_permission` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `batch_err_open_failed` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `batch_err_outside_allowed` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `batch_err_outside_output` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `batch_err_save_failed` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `batch_err_svg_failed` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `batch_err_svg_pixmap_failed` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `batch_err_svg_too_large` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `batch_err_svg_zero_size` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `batch_err_svgz_unsupported` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `batch_err_too_large` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `batch_fix` | 固定 | 固定 | 固定 | Fix | Fijar |
| `batch_fix_pick_dir` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `batch_height` | 高度 | 高度 | 高さ | Height | Alto |
| `batch_limit_reached` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `batch_n_files` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `batch_not_selected` | 尚未选择 | 尚未選擇 | 未選択 | Not selected | Sin seleccionar |
| `batch_output` | 输出位置 | 輸出位置 | 出力先 | Output | Salida |
| `batch_overwrite_note` | 下列文件会被输出就地覆盖，原文件不保留： | 下列檔案會被輸出就地覆蓋，原檔不保留： | 以下のファイルは出力で上書きされ、元ファイルは残りません： | These files will be overwritten in place — the originals will not be kept: | Estos archivos se sobrescribirán en su sitio; no se conservarán los originales: |
| `batch_overwrite_suppress` | （已自动关闭「转换完成后删除原始文件」——覆盖本身就不保留原文件了） | （已自動關閉「轉換完成後刪除原始檔」——覆蓋本身就不保留原檔了） | （「変換後に元ファイルを削除」を自動でオフにしました — 上書きにより元ファイルは残りません） | (“Delete originals after conversion” turned off automatically — overwriting already replaces them) | («Eliminar los originales tras la conversión» se ha desactivado automáticamente: sobrescribir ya los reemplaza) |
| `batch_quality` | 质量 | 品質 | 品質 | Quality | Calidad |
| `batch_remove` | 从列表移除 | 從清單移除 | リストから削除 | Remove from list | Quitar de la lista |
| `batch_resize_all` | 统一调整尺寸 | 統一調整尺寸 | 一括リサイズ | Resize All | Redimensionar todo |
| `batch_resize_needs_value` | 请填入要缩放的尺寸 | 請填入要縮放的尺寸 | リサイズするサイズを入力してください | Enter a size to resize to | Introduce un tamaño para redimensionar |
| `batch_same_dir` | 同原始文件目录 | 同原始檔案目錄 | 元ファイルと同じ場所 | Same as source | La misma que el origen |
| `batch_same_format_hint` | 换个输出位置、调整尺寸或加上水印，就能转换这些文件。 | 換個輸出位置、調整尺寸或加上浮水印，就能轉換這些檔案。 | 出力先を変える・サイズを調整する・透かしを追加する — どれかを行えば変換できます。 | Change the output location, resize, or add a watermark to convert these files. | Cambia la carpeta de salida, ajusta el tamaño o añade una marca de agua para convertir estos archivos. |
| `batch_same_format_title` | 以下文件已是目标格式： | 以下檔案已是目標格式： | 以下のファイルはすでに対象形式です： | These files are already in target format: | Estos archivos ya están en el formato de destino: |
| `batch_select_btn` | 选取文件 | 選取檔案 | ファイルを選択 | Select Files | Seleccionar archivos |
| `batch_skip` | 跳过这些，继续转换 | 略過這些，繼續轉換 | スキップして続行 | Skip & continue | Omitir y continuar |
| `batch_start` | 开始转换 | 開始轉換 | 変換開始 | Start Convert | Iniciar conversión |
| `batch_svg_width` | SVG 输出宽度 | SVG 輸出寬度 | SVG 出力幅 | SVG Output Width | Ancho de salida SVG |
| `batch_title` | 批量格式转换 | 批次格式轉換 | 一括フォーマット変換 | Batch Format Convert | Conversión de formato por lotes |
| `batch_to` | 为 | 為 | へ | to | a |
| `batch_warn_svg_external_ref` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `batch_width` | 宽度 | 寬度 | 幅 | Width | Ancho |
| `batch_wm_choose_img` | 选取图片… | 選取圖片… | 画像を選択… | Choose image… | Elegir imagen… |
| `batch_wm_enable` | 加入水印 | 加入浮水印 | 透かしを追加 | Add Watermark | Añadir marca de agua |
| `batch_wm_img` | 图片（Logo） | 圖片（Logo） | 画像（ロゴ） | Image (Logo) | Imagen (logotipo) |
| `batch_wm_img_size` | 宽度占比 | 寬度佔比 | 幅の割合 | Width % | Ancho % |
| `batch_wm_margin` | 边距 | 邊距 | 余白 | Margin | Margen |
| `batch_wm_opacity` | 不透明 | 不透明 | 不透明度 | Opacity | Opacidad |
| `batch_wm_position` | 位置 | 位置 | 位置 | Position | Posición |
| `batch_wm_preview` | 预览图片 | 預覽圖片 | 画像プレビュー | Image Preview | Vista previa de la imagen |
| `batch_wm_size` | 字级 | 字級 | フォントサイズ | Font size | Tamaño de letra |
| `batch_wm_text` | 文字 | 文字 | テキスト | Text | Texto |
| `batch_wm_text_placeholder` | 输入水印文字 | 輸入浮水印文字 | 透かしテキストを入力 | Enter watermark text | Escribe el texto de la marca de agua |

### `border`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `border_thickness_title` | 外框粗细 px | 外框粗細 px | 枠線の太さ px | Border thickness px | Grosor del borde en px |

### `box`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `box_copy` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `box_drag` | 请拖拽选取区域 | 請拖曳選取區域 | 範囲をドラッグして選択 | Drag to select area | Arrastra para elegir un área |

### `btn`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `btn_clear` | 清除 | 清除 | クリア | Clear | Vaciar |
| `btn_close_title` | 关闭 | 關閉 | 閉じる | Close | Cerrar |
| `btn_copy` | 拷贝 | 複製 | コピー | Copy | Copiar |
| `btn_copy_title` | 拷贝最终图片到剪贴板 (⌘⇧C) | 複製最終圖片到剪貼簿 (⌘⇧C) | クリップボードにコピー (⌘⇧C) | Copy to Clipboard (⌘⇧C) | Copiar al portapapeles (⌘⇧C) |
| `btn_history` | 历史 | 歷史 | 履歴 | History | Historial |
| `btn_history_title` | 历史截图 | 歷史截圖 | スクリーンショット履歴 | Screenshot History | Historial de capturas |
| `btn_save` | 完成并保存 | 完成並儲存 | 保存 | Save | Guardar |

### `click`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `click_to_pick` | 点击选色 | 點擊選色 | クリックして色を選択 | Click to pick color | Haz clic para elegir un color |
| `click_to_pick_transparent` | 点击选色（透明=无外框） | 點擊選色（透明=無外框） | クリックして色を選択（透明＝枠なし） | Click to pick (transparent = no outline) | Haz clic para elegir (transparente = sin contorno) |

### `color`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `color` | 取色器 | 取色器 | カラーピッカー | Color Picker | Color |

### `cp`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `cp_copied` | 已复制 | 已複製 | コピーしました | Copied | Copiado |
| `cp_copy` | 拷贝色码 | 複製色碼 | コードをコピー | Copy code | Copiar código |

### `cpp`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `cpp_brand` | 品牌色库 | 品牌色庫 | ブランドカラー | Brand Colors | Colores de marca |
| `cpp_brand_add_title` | 将当前颜色加入品牌色库 | 將目前顏色加入品牌色庫 | 現在の色をブランドカラーに追加 | Add current color to brand library | Añadir el color actual a la biblioteca de marca |
| `cpp_brand_empty` | 尚未保存品牌色 | 尚未儲存品牌色 | ブランドカラーなし | No brand colors saved | No hay colores de marca guardados |
| `cpp_brand_remove` | 移除此品牌色 | 移除此品牌色 | ブランドカラーを削除 | Remove brand color | Quitar el color de marca |
| `cpp_eyedropper` | 吸管取色（从屏幕取色） | 滴管選色（從螢幕取色） | スポイト（画面から色を取得） | Eyedropper (pick from screen) | Cuentagotas (tomar de la pantalla) |
| `cpp_hex` | 色码（16 进制） | 色碼（16 進位） | 16進数カラーコード | Hex color code | Código de color hexadecimal |
| `cpp_recent` | 最近使用 | 最近使用 | 最近使用した色 | Recent | Recientes |
| `cpp_standard` | 标准色彩 | 標準色彩 | 標準カラー | Standard Colors | Colores estándar |

### `crop`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `crop_cancel` | 取消 | 取消 | キャンセル | Cancel | Cancelar |
| `crop_confirm` | 确认裁切 | 確認裁切 | トリミング確定 | Apply Crop | Aplicar recorte |
| `crop_dbl_hint` | 或双击 | 或雙擊 | またはダブルクリック | or double-click | o doble clic |
| `crop_drag` | 请拖拽选取范围 | 請拖曳選取範圍 | 範囲をドラッグして選択 | Drag to select crop area | Arrastra para elegir el área de recorte |

### `cs`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `cs_apply_hint` | 点一个样式，应用到选中的对象。 | 點一個樣式，套用到選取的物件。 | スタイルをタップして、選択中のオブジェクトに適用します。 | Tap a style to apply it to the selected object. | Toca un estilo para aplicarlo al objeto seleccionado. |
| `cs_apply_title` | 应用样式到对象 | 套用樣式到物件 | オブジェクトにスタイルを適用 | Apply Style to Object | Aplicar estilo al objeto |
| `cs_default_name` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `cs_delete` | 删除 | 刪除 | 削除 | Delete | Eliminar |
| `cs_delete_confirm_no` | 取消 | 取消 | キャンセル | Cancel | Cancelar |
| `cs_delete_confirm_yes` | 确定删除 | 確定刪除 | 削除を確定 | Confirm delete | Confirmar eliminación |
| `cs_edit_entry` | 编辑样式… | 編輯樣式… | スタイルを編集… | Edit Styles… | Editar estilos… |
| `cs_edit_title` | 编辑样式 | 編輯樣式 | スタイルを編集 | Edit Styles | Editar estilos |
| `cs_empty_hint` | 尚无自定义样式（右键对象可存） | 尚無自訂樣式（右鍵物件可存） | カスタムスタイルなし（オブジェクトを右クリックで保存） | No custom styles yet (right-click an object to save) | Aún no hay estilos propios (haz clic derecho en un objeto para guardarlo) |
| `cs_empty_toast` | 目前无自定义样式，请对编辑好的对象右键新增样式 | 目前無自訂樣式，請對編輯好的物件按右鍵新增樣式 | カスタムスタイルがありません。編集したオブジェクトを右クリックして追加してください | No custom styles yet — right-click a finished object to add one | Aún no hay estilos propios — haz clic derecho en un objeto terminado para añadir uno |
| `cs_label` | 自定义样式 | 自訂樣式 | カスタムスタイル | Custom Styles | Estilos propios |
| `cs_please_select` | 请选择 | 請選擇 | 選択してください | Please select | Selecciona uno |
| `cs_rename_hint` | 点一下改名 | 點一下改名 | クリックで名前変更 | Click to rename | Haz clic para renombrar |
| `cs_replace_hint` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `cs_replace_pick_hint` | 点一个样式，以当前对象的外观替换它。 | 點一個樣式，以目前物件的外觀取代它。 | スタイルをタップして、現在のオブジェクトの見た目で置き換えます。 | Tap a style to replace it with this object's appearance. | Toca un estilo para reemplazarlo con la apariencia de este objeto. |
| `cs_replace_pick_title` | 替换哪一个样式？ | 取代哪一個樣式？ | どのスタイルを置き換えますか？ | Replace which style? | ¿Qué estilo reemplazas? |
| `cs_replace_title` | 样式已满，替换哪一个？ | 樣式已滿，取代哪一個？ | スタイルが上限に達しました。どれを置き換えますか？ | Styles full — replace which one? | Estilos llenos — ¿cuál reemplazas? |
| `cs_toast_applied` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `cs_toast_save_fail` | 自定义样式保存失败 | 自訂樣式儲存失敗 | カスタムスタイルの保存に失敗しました | Failed to save custom style | No se pudo guardar el estilo propio |
| `cs_toast_saved` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |

### `ctx`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `ctx_apply_style` | 应用自定义样式 | 套用自訂樣式 | カスタムスタイルを適用 | Apply Custom Style | Aplicar estilo propio |
| `ctx_group` | 成为群组 | 成為群組 | グループ化 | Group | Agrupar |
| `ctx_move_down` | 下移一层 | 下移一層 | 一つ下へ | Move Down | Bajar |
| `ctx_move_up` | 上移一层 | 上移一層 | 一つ上へ | Move Up | Subir |
| `ctx_replace_style` | 替换现有样式 | 取代現有樣式 | 既存スタイルを置き換え | Replace a Custom Style | Reemplazar un estilo propio |
| `ctx_save_style` | 存为自定义样式 | 存為自訂樣式 | カスタムスタイルとして保存 | Save as Custom Style | Guardar como estilo propio |
| `ctx_to_bottom` | 移到最下层 | 移到最下層 | 最背面へ | Send to Back | Enviar al fondo |
| `ctx_to_top` | 移到最上层 | 移到最上層 | 最前面へ | Bring to Front | Traer al frente |
| `ctx_ungroup` | 解散群组 | 解散群組 | グループ解除 | Ungroup | Desagrupar |

### `cube`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `cube_light` | 光源 | 光源 | 光源 | Light | Luz |
| `cube_persp` | 透视 | 透視 | パース | Perspective | Perspectiva |

### `dash`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `dash_dash` | ╌╌╌╌ | ╌╌╌╌ | ╌╌╌╌ | ╌╌╌╌ | ╌╌╌╌ |
| `dash_dash-dot-dot` | ─··─·· | ─··─·· | ─··─·· | ─··─·· | ─··─·· |
| `dash_dash-lg` | ─ ─ ─ | ─ ─ ─ | ─ ─ ─ | ─ ─ ─ | ─ ─ ─ |
| `dash_dot` | ······ | ······ | ······ | ······ | ······ |
| `dash_dot-dash` | ·─·─ | ·─·─ | ·─·─ | ·─·─ | ·─·─ |
| `dash_solid` | ──── | ──── | ──── | ──── | ──── |

### `delay`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `delay` | 延迟 | 延遲 | 遅延 | Delay | Retardo |
| `delay_capture` | 延迟截图 | 延遲截圖 | 遅延キャプチャ | Delayed capture | Captura con retardo |

### `display`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `display_external` | 外接屏幕 | 外接螢幕 | 外部ディスプレイ | External Screen | Pantalla externa |
| `display_picker_title` | 选择屏幕 | 選擇螢幕 | 画面を選択 | Select Screen | Seleccionar pantalla |
| `display_primary` | 主屏幕 | 主螢幕 | メイン画面 | Primary Screen | Pantalla principal |

### `drop`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `drop_overlay_label` | 放开以导入图片 | 放開以匯入圖片 | ドロップして画像を読み込む | Drop to import image | Suelta para importar la imagen |

### `esc`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `esc_cancel` | Esc 取消 | Esc 取消 | Esc キャンセル | Esc cancel | Esc cancelar |

### `extend`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `extend_all` | 四边延伸 | 四邊延伸 | 四方に拡張 | Extend All | Ampliar en todo |
| `extend_cancel` | 取消 | 取消 | キャンセル | Cancel | Cancelar |
| `extend_confirm` | 确认延伸 | 確認延伸 | 確定 | Confirm | Confirmar |
| `extend_direction` | 延伸方向 | 延伸方向 | 方向 | Direction | Dirección |
| `extend_down` | 向下延伸 | 向下延伸 | 下に拡張 | Extend Down | Ampliar hacia abajo |
| `extend_left` | 向左延伸 | 向左延伸 | 左に拡張 | Extend Left | Ampliar a la izquierda |
| `extend_right` | 向右延伸 | 向右延伸 | 右に拡張 | Extend Right | Ampliar a la derecha |
| `extend_title` | 延伸画布 | 延伸畫布 | キャンバス拡張 | Extend Canvas | Ampliar lienzo |
| `extend_up` | 向上延伸 | 向上延伸 | 上に拡張 | Extend Up | Ampliar hacia arriba |

### `fill`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `fill_ellipse_title` | 椭圆色块 | 橢圓色塊 | 塗りつぶし楕円 | Fill Ellipse | Elipse rellena |
| `fill_rect_title` | 矩形色块 | 矩形色塊 | 塗りつぶし矩形 | Fill Rect | Rectángulo relleno |

### `float`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `float_drag_export_title` | 拖拽导出到 Line / Slack / Finder 等 | 拖曳匯出到 Line / Slack / Finder 等 | Line / Slack / Finder などにドラッグして書き出し | Drag to export to Line / Slack / Finder etc. | Arrastra para exportar a Line / Slack / Finder, etc. |
| `float_drag_label` | ⬆ 拖拽导出 | ⬆ 拖曳匯出 | ⬆ ドラッグして書き出し | ⬆ Drag Export | ⬆ Arrastrar |
| `float_drag_move_title` | 拖拽移动按钮位置 | 拖曳移動按鈕位置 | ドラッグしてボタン位置を変更 | Drag to reposition this button | Arrastra para recolocar este botón |
| `float_share_label` | 分享 | 分享 | 共有 | Share | Compartir |
| `float_share_title` | 通过 AirDrop / 消息 / 邮件等分享 | 透過 AirDrop / 訊息 / 郵件等分享 | AirDrop / メッセージ / メールなどで共有 | Share via AirDrop / Messages / Mail etc. | Compartir por AirDrop / Mensajes / Mail, etc. |

### `font`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `font_heiti` | 黑体 | 黑體-繁 | Heiti TC | Heiti TC | Heiti TC |
| `font_hiragino` | ヒラギノ角ゴ | ヒラギノ角ゴ | ヒラギノ角ゴ | Hiragino Kaku Gothic | Hiragino Kaku Gothic |
| `font_kaiti` | 楷体 | 楷體-繁 | Kaiti TC | Kaiti TC | Kaiti TC |
| `font_pingfang` | 苹方 | 蘋方-繁 | PingFang TC | PingFang TC | PingFang TC |
| `font_songti` | 宋体 | 宋體-繁 | Songti TC | Songti TC | Songti TC |

### `fullscreen`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `fullscreen` | 全屏 | 全螢幕 | 全画面 | Fullscreen | Pantalla completa |

### `grad`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `grad_angle` | 角度 | 角度 | 角度 | Angle | Ángulo |

### `help`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `help_arrow_keys` | 方向键 | 方向鍵 | 矢印キー | Arrow Keys | Teclas de flecha |
| `help_auto_hide` | 自动隐藏工具栏 | 自動隱藏工具列 | ツールバーを自動的に隠す | Auto-hide toolbar | Ocultar la barra automáticamente |
| `help_auto_hide_delay` | 显示时间 | 顯示時間 | 表示時間 | Show for | Mostrar durante |
| `help_auto_hide_hint` | 开启后工具栏会缩成呼吸灯，靠近点击即可展开。找不到的话按 Dock 图标召唤 XD | 開啟後工具列會縮成呼吸燈，靠近點擊即可展開。找不到的話按 Dock 圖示召喚 XD | ツールバーが呼吸ライトに縮小。近づいてクリックで展開。見失ったら Dock アイコンで召喚 XD | The toolbar collapses into a breathing light. Hover and click to expand. Lost it? Click the Dock icon XD | La barra se repliega en una luz que respira. Pasa el cursor y haz clic para desplegarla. ¿La perdiste? Haz clic en el icono del Dock XD |
| `help_canvas_nav` | 画布导航 | 畫布導航 | キャンバスナビ | Canvas Navigation | Navegación del lienzo |
| `help_colorblock` | 色块 | 色塊 | 塗りつぶし | Fill | Relleno |
| `help_colorpicker` | 取色器 | 取色器 | カラーピッカー | Color Picker | Selector de color |
| `help_copy` | 拷贝 | 複製 | コピー | Copy | Copiar |
| `help_copy_final` | 拷贝完成图 | 複製完成圖 | 完成画像をコピー | Copy Final Image | Copiar imagen final |
| `help_crop` | 裁切 | 裁切 | トリミング | Crop | Recortar |
| `help_delete` | 删除选取元素 | 刪除選取元素 | 選択を削除 | Delete Selected | Eliminar selección |
| `help_drag` | 拖拽 | 拖曳 | ドラッグ | Drag | Arrastrar |
| `help_editor` | 编辑器工具 | 編輯器工具 | エディタツール | Editor Tools | Herramientas del editor |
| `help_escape` | 取消 / 离开工具 | 取消 / 離開工具 | キャンセル / ツール終了 | Cancel / Exit Tool | Cancelar / Salir de la herramienta |
| `help_extend` | 延伸画布 | 延伸畫布 | キャンバス拡張 | Extend Canvas | Ampliar lienzo |
| `help_feedback_hint` | 写信给我们——会打开你的邮件 App | 寫信給我們——會開啟你的郵件 App | ご意見をお寄せください — メール App が開きます | Write to us — opens your mail app | Escríbenos — se abrirá tu app de correo |
| `help_feedback_link` | 💬 意见反馈 | 💬 意見回饋 | 💬 フィードバック | 💬 Send Feedback | 💬 Enviar comentarios |
| `help_fullscreen_capture` | 全屏截图 | 全螢幕截圖 | 全画面キャプチャ | Full Screen Capture | Captura de pantalla completa |
| `help_general` | 通用操作 | 通用操作 | 一般操作 | General | General |
| `help_global` | 全局快捷键 | 全域快捷鍵 | グローバルショートカット | Global Shortcuts | Atajos globales |
| `help_group` | 成为群组 | 成為群組 | グループ化 | Group | Agrupar |
| `help_line` | 线条 | 線條 | 線 | Line | Línea |
| `help_manual_link` | 📖 打开操作手册 | 📖 開啟操作手冊 | 📖 操作マニュアルを開く | 📖 Open User Guide | 📖 Abrir la guía de usuario |
| `help_marquee` | 框型选取 | 框型選取 | ボックス選択 | Box Select | Selección por marco |
| `help_mosaic` | 马赛克 / 模糊 | 馬賽克 / 模糊 | モザイク / ぼかし | Mosaic / Blur | Mosaico / Desenfoque |
| `help_nudge` | 微调 1px | 微調 1px | 1px 微調整 | Nudge 1px | Mover 1 px |
| `help_nudge10` | 微调 10px | 微調 10px | 10px 微調整 | Nudge 10px | Mover 10 px |
| `help_number` | 编号标记 | 編號標記 | 番号マーカー | Number Marker | Marcador numérico |
| `help_ocr` | OCR 文字识别 | OCR 文字辨識 | OCR テキスト認識 | OCR Text Recognition | Reconocimiento de texto (OCR) |
| `help_overlay` | 叠入图片 | 疊入圖片 | 画像オーバーレイ | Overlay Image | Superponer imagen |
| `help_pan` | 平移画布 | 平移畫布 | キャンバスパン | Pan Canvas | Desplazar el lienzo |
| `help_paste` | 粘贴 | 貼上 | 貼り付け | Paste | Pegar |
| `help_paste_image` | 粘入图片 | 貼入圖片 | 画像を貼り付け | Paste Image | Pegar imagen |
| `help_pencil` | 笔型 | 筆型 | ペン | Pen | Lápiz |
| `help_privacy` | 隐私遮蔽 | 隱私遮蔽 | プライバシーマスク | Privacy Mask | Máscara de privacidad |
| `help_rect` | 矩形框 | 矩形框 | 矩形 | Rectangle | Rectángulo |
| `help_redo` | 重做 | 重做 | やり直し | Redo | Rehacer |
| `help_region_capture` | 矩形选取截图 | 矩形選取截圖 | 矩形選択キャプチャ | Region Select | Selección de área |
| `help_resize` | 调整大小 | 調整大小 | サイズ変更 | Resize | Redimensionar |
| `help_ruler` | 尺标 | 尺標 | 定規 | Measure | Medir |
| `help_save` | 保存 | 儲存 | 保存 | Save | Guardar |
| `help_save_as` | 另存为 | 另存新檔 | 名前を付けて保存 | Save As | Guardar como |
| `help_scroll_capture` | 长截图 | 長截圖 | ロングスクリーンショット | Long screenshot | Captura larga |
| `help_select` | 选取 | 選取 | 選択 | Select | Seleccionar |
| `help_snap_toggle` | 智能导线开关 | 智慧導線開關 | スマートガイド切替 | Toggle Smart Guides | Alternar guías inteligentes |
| `help_symbol` | 符号印章 | 符號印章 | スタンプ | Stamp | Sello |
| `help_text` | 文字 | 文字 | テキスト | Text | Texto |
| `help_title` | 快捷键说明 | 快捷鍵說明 | キーボードショートカット | Keyboard Shortcuts | Atajos de teclado |
| `help_toolbar_settings` | 工具栏设置 | 工具列設定 | ツールバー設定 | Toolbar Settings | Ajustes de la barra |
| `help_undo` | 撤销 | 撤銷 | 元に戻す | Undo | Deshacer |
| `help_ungroup` | 解散群组 | 解散群組 | グループ解除 | Ungroup | Desagrupar |
| `help_window_capture` | 窗口截图 | 視窗截圖 | ウィンドウキャプチャ | Window Capture | Captura de ventana |
| `help_zoom_fit` | 适合窗口 | 適合視窗 | ウィンドウに合わせる | Fit to Window | Ajustar a la ventana |
| `help_zoom_in` | 放大 | 放大 | ズームイン | Zoom In | Acercar |
| `help_zoom_out` | 缩小 | 縮小 | ズームアウト | Zoom Out | Alejar |

### `history`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `history_copied_label` | 已复制 | 已複製 | コピー済み | Copied | Copiado |
| `history_empty` | 尚无记录 | 尚無紀錄 | 履歴なし | No history yet | Aún no hay historial |
| `history_file_not_found` | 文件已移动或删除 | 檔案已移動或刪除 | ファイルが移動または削除されました | File moved or deleted | El archivo se movió o se eliminó |
| `history_title` | 历史截图 | 歷史截圖 | スクリーンショット履歴 | Screenshot History | Historial de capturas |

### `longcap`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `longcap_enable_js` | 请先在 Chrome 勾选：显示方式 > 开发者选项 > 允许 Apple 事件的 JavaScript | 請先在 Chrome 勾選：顯示方式 > 開發人員選項 > 允許 Apple 事件的 JavaScript | Chrome で有効に：表示 > 開発 > Apple Events からの JavaScript を許可 | Enable in Chrome: View > Developer > Allow JavaScript from Apple Events | Actívalo en Chrome: Visualización > Desarrollo > Permitir JavaScript desde Apple Events |
| `longcap_no_browser` | 找不到浏览器窗口——请把要截的网页在桌面上的 Chrome 中打开，再按一次长截图 | 找不到瀏覽器視窗——請把要截的網頁開在桌面上的 Chrome，再按一次長截圖 | ブラウザのウィンドウが見つかりません——撮りたいページをデスクトップ上の Chrome で開いてから、もう一度長いスクリーンショットを押してください | No browser window found — open the page in Chrome on your desktop, then press Long screenshot again | No se encontró ninguna ventana de navegador — abre la página en Chrome en tu escritorio y pulsa Captura larga de nuevo |

### `measure`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `measure_hint` | 双击数字徽章可修改，其余数字自动等比换算 | 雙擊數字徽章可修改，其餘數字自動等比換算 | バッジをダブルクリックで数値を編集、他の数値は等比で自動換算 | Double-click a badge to edit; other values rescale proportionally | Haz doble clic en una etiqueta para editarla; los demás valores se reescalan proporcionalmente |
| `measure_hints` | 拖框量框　点两下量距（吸边·⌥暂停）　点选读数　⌫ 删除　⌘Z 撤销　Enter 导出　Esc 取消 | 拖框量框　點兩下量距（吸邊·⌥暫停）　點選讀數　⌫ 刪除　⌘Z 復原　Enter 輸出　Esc 取消 | ドラッグで枠計測　2点クリックで距離（吸着·⌥一時停止）　クリックで選択　⌫ 削除　⌘Z 取り消し　Enter 書き出し　Esc キャンセル | Drag = box　Click 2 pts = distance (snap·⌥ off)　Click to select　⌫ Delete　⌘Z Undo　Enter Export　Esc Cancel | Arrastrar = marco　2 clics = distancia (ajuste·⌥ desactiva)　Clic para seleccionar　⌫ Eliminar　⌘Z Deshacer　Intro Exportar　Esc Cancelar |
| `measure_reset` | 回实际测量值 | 回實際量測值 | 実測値に戻す | Reset to measured | Volver a lo medido |
| `measure_unit` | 单位 | 單位 | 単位 | Unit | Unidad |
| `measure_unit_none` | 无 | 無 | なし | None | Ninguna |

### `more`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `more` | 更多 | 更多 | その他 | More | Más |

### `mosaic`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `mosaic` | 马赛克 | 馬賽克 | モザイク | Mosaic | Mosaico |
| `mosaic_block` | 区块： | 區塊： | ブロック： | Block: | Bloque: |
| `mosaic_blur` | 模糊 | 模糊 | ぼかし | Blur | Desenfoque |
| `mosaic_intensity` | 强度： | 強度： | 強度： | Intensity: | Intensidad: |

### `nc`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `nc_a3_landscape` | A3 横（1191 × 842） | A3 橫（1191 × 842） | A3 横（1191 × 842） | A3 Landscape (1191 × 842) | A3 horizontal (1191 × 842) |
| `nc_a3_portrait` | A3 竖（842 × 1191） | A3 直（842 × 1191） | A3 縦（842 × 1191） | A3 Portrait (842 × 1191) | A3 vertical (842 × 1191) |
| `nc_a4_landscape` | A4 横（842 × 595） | A4 橫（842 × 595） | A4 横（842 × 595） | A4 Landscape (842 × 595) | A4 horizontal (842 × 595) |
| `nc_a4_portrait` | A4 竖（595 × 842） | A4 直（595 × 842） | A4 縦（595 × 842） | A4 Portrait (595 × 842) | A4 vertical (595 × 842) |
| `nc_facebook` | Facebook 帖子（1200 × 630） | Facebook 貼文（1200 × 630） | Facebook 投稿（1200 × 630） | Facebook Post (1200 × 630) | Publicación de Facebook (1200 × 630) |
| `nc_group_other` | 其他 | 其他 | その他 | Other | Otros |
| `nc_group_paper` | 纸张（72 dpi） | 紙張（72 dpi） | 用紙（72 dpi） | Paper (72 dpi) | Papel (72 ppp) |
| `nc_group_pixel` | 像素画 | 像素畫 | ドット絵 | Pixel Art | Pixel art |
| `nc_group_screen` | 屏幕 | 螢幕 | スクリーン | Screen | Pantalla |
| `nc_group_social` | 社交媒体（建议尺寸） | 社群媒體（建議尺寸） | ソーシャルメディア（推奨サイズ） | Social Media (recommended) | Redes sociales (recomendados) |
| `nc_ig_1_1` | IG 帖子 1:1（1080 × 1080） | IG 貼文 1:1（1080 × 1080） | IG 投稿 1:1（1080 × 1080） | IG Post 1:1 (1080 × 1080) | Publicación IG 1:1 (1080 × 1080) |
| `nc_ig_4_5` | IG 帖子 4:5（1080 × 1350） | IG 貼文 4:5（1080 × 1350） | IG 投稿 4:5（1080 × 1350） | IG Post 4:5 (1080 × 1350) | Publicación IG 4:5 (1080 × 1350) |
| `nc_ig_story` | IG / TikTok Story 9:16（1080 × 1920） | IG / TikTok Story 9:16（1080 × 1920） | IG / TikTok ストーリー 9:16（1080 × 1920） | IG / TikTok Story 9:16 (1080 × 1920) | Historia IG / TikTok 9:16 (1080 × 1920) |
| `nc_linkedin` | LinkedIn（1200 × 627） | LinkedIn（1200 × 627） | LinkedIn（1200 × 627） | LinkedIn (1200 × 627) | LinkedIn (1200 × 627) |
| `nc_px_20` | Clawdmeter（20 × 20 格） | Clawdmeter（20 × 20 格） | Clawdmeter（20 × 20 マス） | Clawdmeter (20 × 20 cells) | Clawdmeter (20 × 20 celdas) |
| `nc_px_40` | Clawdmeter（40 × 40 格） | Clawdmeter（40 × 40 格） | Clawdmeter（40 × 40 マス） | Clawdmeter (40 × 40 cells) | Clawdmeter (40 × 40 celdas) |
| `nc_px_60` | Clawdmeter（60 × 60 格） | Clawdmeter（60 × 60 格） | Clawdmeter（60 × 60 マス） | Clawdmeter (60 × 60 cells) | Clawdmeter (60 × 60 celdas) |
| `nc_px_free` | 自由像素图（自定义格数） | 自由像素圖（自訂格數） | フリーピクセル（マス数を自由に指定） | Free pixel art (custom size) | Píxel libre (tamaño personalizado) |
| `nc_size_invalid` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `nc_square` | 正方形（1000 × 1000） | 正方形（1000 × 1000） | 正方形（1000 × 1000） | Square (1000 × 1000) | Cuadrado (1000 × 1000) |
| `nc_twitter` | X / Twitter（1600 × 900） | X / Twitter（1600 × 900） | X / Twitter（1600 × 900） | X / Twitter (1600 × 900) | X / Twitter (1600 × 900) |
| `nc_youtube` | YouTube 缩略图（1280 × 720） | YouTube 縮圖（1280 × 720） | YouTube サムネイル（1280 × 720） | YouTube Thumbnail (1280 × 720) | Miniatura de YouTube (1280 × 720) |

### `newcanvas`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `newcanvas_bg` | 背景颜色 | 背景顏色 | 背景色 | Background | Fondo |
| `newcanvas_create` | 创建 | 建立 | 作成 | Create | Crear |
| `newcanvas_custom` | 自定义 | 自訂 | カスタム | Custom | Personalizado |
| `newcanvas_preset` | 预设尺寸 | 預設尺寸 | プリセット | Preset | Preajuste |
| `newcanvas_title` | 新建画布 | 新開畫布 | 新規キャンバス | New Canvas | Nuevo lienzo |
| `newcanvas_transparent` | 透明 | 透明 | 透明 | Transparent | Transparente |
| `newcanvas_unit_cell` | 格 | 格 | マス | cells | celdas |

### `num`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `num_size_title` | 编号大小（图像像素） | 編號大小（圖像像素） | 番号サイズ（画像ピクセル） | Number size (image pixels) | Tamaño del número (píxeles de la imagen) |
| `num_style_limit` | 上限：∞ | 上限：∞ | 上限：∞ | Max: ∞ | Máx.: ∞ |

### `ocr`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `ocr_copy` | 拷贝 | 複製 | コピー | Copy | Copiar |
| `ocr_copy_close` | 拷贝并关闭 | 複製並關閉 | コピーして閉じる | Copy & Close | Copiar y cerrar |
| `ocr_dl_body` | 首次使用 OCR 需下载语言数据： ⏎ 简体中文 (~18 MB) + 英文 (~4 MB) ⏎ 下载后可离线使用。 | 首次使用 OCR 需下載語言資料： ⏎ 繁體中文 (~18 MB) + 英文 (~4 MB) ⏎ 下載後離線即可使用，無需重複下載。 | 初回 OCR 使用時に言語データのダウンロードが必要です： ⏎ 繁体字中国語（〜18 MB）＋英語（〜4 MB） ⏎ ダウンロード後はオフラインで使用可能です。 | First-time OCR requires downloading language data: ⏎ Traditional Chinese (~18 MB) + English (~4 MB) ⏎ Works offline once downloaded. | El primer uso de OCR requiere descargar datos de idioma: ⏎ Chino tradicional (~18 MB) + Inglés (~4 MB) ⏎ Una vez descargados funciona sin conexión. |
| `ocr_dl_cancel` | 取消 | 取消 | キャンセル | Cancel | Cancelar |
| `ocr_dl_confirm` | 确认下载并识别 | 確認下載並辨識 | ダウンロードして認識 | Download & Recognize | Descargar y reconocer |
| `ocr_dl_title` | OCR 语言包 | OCR 語言包 | OCR 言語パック | OCR Language Pack | Paquete de idioma para OCR |
| `ocr_downloading` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `ocr_drag` | 请拖拽选取识别区域 | 請拖曳選取辨識區域 | OCR 範囲をドラッグして選択 | Drag to select OCR area | Arrastra para elegir el área de OCR |
| `ocr_fail_detail` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `ocr_initialized` | 初始化完成 | 初始化完成 | 初期化完了 | Initialized | Inicializado |
| `ocr_placeholder` | 识别结果将显示在此... | 辨識結果將顯示在此... | ここに結果が表示されます... | Results will appear here... | Los resultados aparecerán aquí... |
| `ocr_preparing` | 准备中... | 準備中... | 準備中... | Preparing... | Preparando... |
| `ocr_recognizing` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `ocr_recognizing_label` | 识别中... | 辨識中... | 認識中... | Recognizing... | Reconociendo... |
| `ocr_result_title` | OCR 识别结果 | OCR 辨識結果 | OCR 結果 | OCR Result | Resultado del OCR |

### `open`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `open` | 打开 | 開啟 | 開く | Open | Abrir |
| `open_menu_file` | 打开文件 | 開啟檔案 | ファイルを開く | Open File | Abrir archivo |
| `open_menu_new` | 新建画布 | 新開畫布 | 新規キャンバス | New Canvas | Nuevo lienzo |

### `opt`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `opt_align_center` | 居中对齐 | 置中對齊 | 中央揃え | Center | Centrado |
| `opt_align_left` | 左对齐 | 靠左對齊 | 左揃え | Left | Izquierda |
| `opt_align_right` | 右对齐 | 靠右對齊 | 右揃え | Right | Derecha |
| `opt_bold` | 粗体 | 粗體 | 太字 | Bold | Negrita |
| `opt_bold_title` | 粗体 | 粗體 | 太字 | Bold | Negrita |
| `opt_border` | 边框 | 邊框 | ボーダー | Border | Borde |
| `opt_color` | 颜色 | 顏色 | 色 | Color | Color |
| `opt_end` | 终点 | 終點 | 終点 | End | Fin |
| `opt_face_color` | 面色 | 面色 | 面 | Face | Cara |
| `opt_flip_h` | 水平镜像 | 水平鏡射 | 水平反転 | Flip Horizontal | Voltear en horizontal |
| `opt_flip_v` | 垂直镜像 | 垂直鏡射 | 垂直反転 | Flip Vertical | Voltear en vertical |
| `opt_font` | 字体 | 字體 | フォント | Font | Fuente |
| `opt_font_mono` | 等宽 Menlo | 等寬 Menlo | 等幅 Menlo | Menlo (Mono) | Menlo (mono) |
| `opt_font_system` | 系统默认 | 系統預設 | システムデフォルト | System | Sistema |
| `opt_gradient` | 渐变 | 漸層 | グラデーション | Gradient | Degradado |
| `opt_italic` | 斜体 | 斜體 | 斜体 | Italic | Cursiva |
| `opt_italic_title` | 斜体 | 斜體 | 斜体 | Italic | Cursiva |
| `opt_large` | 大 | 大 | 大 | L | G |
| `opt_limit` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `opt_line_color` | 线色 | 線色 | 線 | Line | Línea |
| `opt_line_style` | 线条 | 線條 | 線 | Line | Línea |
| `opt_medium` | 标准 | 標準 | 中 | M | M |
| `opt_next` | 下一个 | 下一個 | 次へ | Next | Siguiente |
| `opt_opacity` | 透明度 | 透明度 | 不透明度 | Opacity | Opacidad |
| `opt_orthogonal` | 折线 | 折線 | 折れ線 | Polyline | Polilínea |
| `opt_outline` | 外框 | 外框 | アウトライン | Outline | Contorno |
| `opt_radius` | 圆角 | 圓角 | 角丸 | Radius | Radio |
| `opt_reset` | 重置 | 重置 | リセット | Reset | Restablecer |
| `opt_shadow` | 阴影 | 陰影 | 影 | Shadow | Sombra |
| `opt_size` | 大小 | 大小 | サイズ | Size | Tamaño |
| `opt_small` | 小 | 小 | 小 | S | P |
| `opt_solid` | 实色 | 實色 | 単色 | Solid | Sólido |
| `opt_start` | 起点 | 起點 | 始点 | Start | Inicio |
| `opt_strikethrough` | 删除线 | 刪除線 | 取り消し線 | Strikethrough | Tachado |
| `opt_strikethrough_title` | 删除线 | 刪除線 | 取り消し線 | Strikethrough | Tachado |
| `opt_stroke` | 描边 | 描邊 | ストローク | Stroke | Trazo |
| `opt_stroke_opacity` | 不透明 | 不透明 | 不透明度 | Opacity | Opacidad |
| `opt_style` | 风格 | 風格 | スタイル | Style | Estilo |
| `opt_text_bg` | 背景 | 背景 | 背景 | Background | Fondo |
| `opt_text_stroke` | 描边 | 描邊 | ストローク | Stroke | Trazo |
| `opt_thickness` | 粗细 | 粗細 | 太さ | Width | Grosor |
| `opt_transparent` | 透明 | 透明 | 透明 | Transparent | Transparente |
| `opt_underline` | 下划线 | 底線 | 下線 | Underline | Subrayado |
| `opt_underline_title` | 下划线 | 底線 | 下線 | Underline | Subrayado |
| `opt_value` | 数值 | 數值 | 値 | Value | Valor |
| `opt_zoom` | 缩放比例 | 縮放比例 | ズーム | Zoom | Zoom |

### `perm`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `perm_modal_body` | VAS 截图需要「屏幕录制（截图）」与「辅助功能（滚动截图）」权限才能完成截图任务：请至 系统设置 > 隐私与安全性 > 屏幕与系统录音 / 辅助功能 > 开启 VAS，或点下方「＋」手动添加左侧「应用程序」中的 VAS 后，关闭 App 重新启动即可，谢谢您！ | VAS 截圖需要「螢幕錄製（截圖）」與「輔助使用（滾動截圖）」權限才能完成截圖任務：請至 系統設定 > 隱私權與安全性 > 螢幕與系統錄音 / 輔助使用 > 開啟 VAS，或按下方「＋」手動加入左側「應用程式」中的 VAS 後，關閉 App 重新啟動即可，謝謝您！ | VAS のスクリーンショットには「画面収録（撮影）」と「アクセシビリティ（スクロール撮影）」の権限が必要です：システム設定 > プライバシーとセキュリティ > 画面とシステムオーディオの収録 / アクセシビリティ で VAS をオンにするか、下の「＋」で左側の「アプリケーション」から VAS を追加してください。その後、App を終了して再起動すれば完了です。ありがとうございます！ | VAS needs Screen Recording (capture) and Accessibility (scrolling capture) permissions to take screenshots: go to System Settings > Privacy & Security > Screen & System Audio Recording / Accessibility and enable VAS, or use the “+” below to add VAS from the Applications folder on the left; then quit and relaunch the app. Thank you! | VAS necesita los permisos de Grabación de pantalla (captura) y Accesibilidad (captura con desplazamiento) para hacer capturas: ve a Ajustes del Sistema > Privacidad y seguridad > Grabación de pantalla y audio del sistema / Accesibilidad y activa VAS, o usa el “+” de abajo para añadir VAS desde la carpeta Aplicaciones de la izquierda; después sal de la app y vuelve a abrirla. ¡Gracias! |
| `perm_modal_title` | VAS 需要「屏幕录制」与「辅助功能」权限 | VAS 需要「螢幕錄製」與「輔助使用」權限 | VAS には「画面収録」と「アクセシビリティ」の権限が必要です | VAS needs Screen Recording & Accessibility permissions | VAS necesita permisos de Grabación de pantalla y Accesibilidad |

### `picker`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `picker_title` | 选择窗口 | 選擇視窗 | ウィンドウを選択 | Select Window | Seleccionar ventana |

### `pref`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `pref_click_to_record` | 点击录入… | 點擊錄入… | クリックして入力… | Click to record… | Haz clic para grabar… |
| `pref_colorpicker` | 取色器 | 取色器 | カラーピッカー | Color Picker | Selector de color |
| `pref_conflict_msg` | 已绑定到 | 已綁定到 | は既に割り当て済み： | is already assigned to | ya está asignado a |
| `pref_conflict_replace` | ，要替换吗？ | ，要取代嗎？ | 。置き換えますか？ | . Replace? | . ¿Reemplazar? |
| `pref_conflict_replaced` | 已替换 | 已取代 | 置き換え済み | Replaced | Reemplazado |
| `pref_fullscreen` | 全屏截图 | 全螢幕截圖 | 全画面キャプチャ | Full Screen Capture | Captura de pantalla completa |
| `pref_need_modifier` | 需要至少一个修饰键（⌘⌃⌥） | 需要至少一個修飾鍵（⌘⌃⌥） | 修飾キーが必要です（⌘⌃⌥） | Requires at least one modifier (⌘⌃⌥) | Requiere al menos un modificador (⌘⌃⌥) |
| `pref_paste` | 剪贴板截图 | 剪貼簿截圖 | クリップボードキャプチャ | Clipboard Capture | Captura del portapapeles |
| `pref_recording` | 请按下快捷键… | 請按下快捷鍵… | ショートカットを入力… | Press shortcut… | Pulsa el atajo… |
| `pref_rect` | 矩形截图 | 矩形截圖 | 矩形キャプチャ | Rectangle Capture | Captura de área |
| `pref_reserved` | 此为系统保留快捷键 | 此為系統保留快捷鍵 | システム予約済みのショートカットです | This shortcut is reserved by the system | Este atajo está reservado por el sistema |
| `pref_reset` | 还原默认值 | 還原預設值 | デフォルトに戻す | Restore Defaults | Restaurar valores por omisión |
| `pref_ruler` | 标尺 | 尺標 | 定規 | Ruler | Regla |
| `pref_scroll` | 长截图 | 長截圖 | ロングスクリーンショット | Long screenshot | Captura larga |
| `pref_shortcuts_title` | 快捷键设置 | 快捷鍵設定 | ショートカット設定 | Shortcut Settings | Ajustes de atajos |
| `pref_window` | 窗口截图 | 視窗截圖 | ウィンドウキャプチャ | Window Capture | Captura de ventana |

### `privacy`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `privacy_hint` | K = 全图扫描　拖拽 = 指定区域 | K = 全圖掃描　拖曳 = 指定區域 | K = 全体スキャン　ドラッグ = 範囲指定 | K = full scan   drag = region scan | K = análisis completo   arrastrar = análisis del área |
| `privacy_mode_label` | 遮蔽方式： | 遮蔽方式： | マスクモード： | Mask mode: | Modo de máscara: |

### `px`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `px_acts` | 选区变换 | 選區變換 | 選択範囲の変換 | Selection transforms | Transformaciones de la selección |
| `px_add_col` | 加一栏 | 加一欄 | 列を追加 | Add column | Añadir columna |
| `px_add_color` | 新增颜色 | 新增顏色 | 色を追加 | Add colour | Añadir color |
| `px_add_row` | 加一行 | 加一列 | 行を追加 | Add row | Añadir fila |
| `px_bad_hex` | 色码格式要像 #RRGGBB | 色碼格式要像 #RRGGBB | カラーコードは #RRGGBB の形式です | Colour code should look like #RRGGBB | El código de color debe tener la forma #RRGGBB |
| `px_bg_over_palette` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `px_blocked_here` | 像素格子画布不支持这个功能 | 像素格子畫布不支援這個功能 | ドット絵キャンバスでは使えません | Not available on a pixel-grid canvas | No disponible en un lienzo de cuadrícula de píxeles |
| `px_bright_hint` | ⚠️ 颜色要亮 — 设备面板是纯黑，暗色在上面等于隐形 | ⚠️ 顏色要亮 — 裝置面板是純黑，暗色在上面等於隱形 | ⚠️ 明るい色で — デバイスの画面は真っ黒、暗い色は見えません | ⚠️ Keep colours bright — the device panel is pure black, dark colours vanish | ⚠️ Usa colores vivos — el panel del dispositivo es negro puro y los colores oscuros desaparecen |
| `px_cannot_replace_transparent` | 0 号是透明，不能换成颜色 | 0 號是透明，不能換成顏色 | 0 番は透明なので色にはできません | Index 0 is transparent and cannot become a colour | El índice 0 es transparente y no puede convertirse en un color |
| `px_category` | 分类 | 分類 | カテゴリ | Category | Categoría |
| `px_cell_pos` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `px_chart_cells` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `px_chart_col_code` | 色号 | 色號 | コード | Code | Código |
| `px_chart_col_color` | 色票 | 色票 | 色 | Color | Color |
| `px_chart_col_count` | 数量 | 數量 | 個数 | Count | Cantidad |
| `px_chart_colors` | 颜色 | 顏色 | 色数 | Colors | Colores |
| `px_chart_grid` | 格数 | 格數 | グリッド | Grid | Cuadrícula |
| `px_chart_materials` | 材料 | 材料 | 材料 | Materials | Materiales |
| `px_copied` | 已复制 JSON | 已複製 JSON | JSON をコピーしました | JSON copied | JSON copiado |
| `px_copy_json` | 拷贝 JSON | 複製 JSON | JSON をコピー | Copy JSON | Copiar JSON |
| `px_copy_short` | 拷贝 | 複製 | コピー | Copy | Copiar |
| `px_del_col` | 减一栏（删最右栏，⌘Z 可复原） | 減一欄（刪最右欄，⌘Z 可復原） | 右端の列を削除（⌘Z で戻せます） | Remove column (rightmost; ⌘Z undoes) | Quitar columna (la última; ⌘Z deshace) |
| `px_del_row` | 减一行（删最下行，⌘Z 可复原） | 減一列（刪最下列，⌘Z 可復原） | 下端の行を削除（⌘Z で戻せます） | Remove row (bottom; ⌘Z undoes) | Quitar fila (la última; ⌘Z deshace) |
| `px_export_failed` | 导出检查未过： | 匯出檢查未過： | 書き出しチェック失敗： | Export check failed:  | Falló la comprobación de exportación:  |
| `px_flip_h` | 左右翻 — 把选区内容水平镜射（没有选区时翻整张） | 左右翻 — 把選區內容水平鏡射（沒有選區時翻整張） | 左右反転 — 選択範囲を水平ミラー（未選択なら全体） | Flip horizontally — mirrors the selection (whole canvas if nothing is selected) | Voltear en horizontal — refleja la selección (todo el lienzo si no hay nada seleccionado) |
| `px_flip_v` | 上下翻 — 把选区内容垂直镜射（没有选区时翻整张） | 上下翻 — 把選區內容垂直鏡射（沒有選區時翻整張） | 上下反転 — 選択範囲を垂直ミラー（未選択なら全体） | Flip vertically — mirrors the selection (whole canvas if nothing is selected) | Voltear en vertical — refleja la selección (todo el lienzo si no hay nada seleccionado) |
| `px_frame_add` | ＋ | ＋ | ＋ | ＋ | ＋ |
| `px_frame_add_title` | 在当前格之后插入一张空白格 | 在目前格之後插入一張空白格 | 現在のコマの後ろに空白コマを挿入 | Insert a blank frame after this one | Insertar un fotograma en blanco después de este |
| `px_frame_back` | → | → | → | → | → |
| `px_frame_back_title` | 后移——与后一格交换位置 | 後移——與後一格交換位置 | 後ろへ移動 — 次のコマと入れ替え | Move frame later — swap with the next frame | Retrasar el fotograma — intercambiarlo con el siguiente |
| `px_frame_del` | 🗑 | 🗑 | 🗑 | 🗑 | 🗑 |
| `px_frame_del_title` | 删除当前格（只剩一格时停用） | 刪除目前格（只剩一格時停用） | 現在のコマを削除（残り1コマでは無効） | Delete this frame (disabled at one frame) | Eliminar este fotograma (desactivado si solo queda uno) |
| `px_frame_dup` | ⧉ | ⧉ | ⧉ | ⧉ | ⧉ |
| `px_frame_dup_title` | 在当前格之后插入一份副本 | 在目前格之後插入一份複本 | 現在のコマの複製を後ろに挿入 | Insert a copy of this frame after it | Insertar una copia de este fotograma después de él |
| `px_frame_fwd` | ← | ← | ← | ← | ← |
| `px_frame_fwd_title` | 前移——与前一格交换位置 | 前移——與前一格交換位置 | 前へ移動 — 前のコマと入れ替え | Move frame earlier — swap with the previous frame | Adelantar el fotograma — intercambiarlo con el anterior |
| `px_frames` | 帧 | 影格 | フレーム | Frames | Fotogramas |
| `px_gif_custom` | 自定义… | 自訂… | カスタム… | Custom… | Personalizado… |
| `px_gif_flatten_go` | 照样导出 | 照樣匯出 | このまま書き出す | Export anyway | Exportar de todos modos |
| `px_gif_hold_flatten` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `px_gif_size` | 输出尺寸 | 輸出尺寸 | 出力サイズ | Output size | Tamaño de salida |
| `px_gif_size_hint` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `px_gradient_hint` | 色盘不够用时，点渐层取自己的颜色 | 色盤不夠用時，點漸層取自己的顏色 | パレットに欲しい色がないときは、グラデーションをクリックして取得 | Need a colour the swatches lack? Click the gradient to sample one | ¿Falta un color? Haz clic en el degradado para tomarlo |
| `px_hex_add` | 加入 | 加入 | 追加 | Add | Añadir |
| `px_hex_replace` | 取代 | 取代 | 置換 | Replace | Reemplazar |
| `px_hex_replace_title` | 替换颜色——框里有新色就先按我再点旧色；框空着就先选旧色票再按我 | 取代顏色——框裡有新色就先按我再點舊色；框空著就先選舊色票再按我 | 色を置き換え——枠に新色があればまず押してから旧色をクリック；枠が空なら旧色スウォッチを選んでから押す | Replace a colour — with a new colour in the box, press me then click the old one; with the box empty, select the old swatch first | Reemplazar un color: con un color nuevo en el cuadro, púlsame y elige el viejo; con el cuadro vacío, selecciona antes la muestra vieja |
| `px_hold` | 停留 | 停留 | 表示時間 | Hold | Duración |
| `px_hold_bad_fraction` | 停留时间不能有小数点 | 停留時間不能有小數點 | 表示時間に小数は使えません | Hold time cannot have decimals | La duración no puede tener decimales |
| `px_hold_bad_max` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `px_hold_bad_min` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `px_hold_bad_nan` | 停留时间请输入数字 | 停留時間請輸入數字 | 表示時間は数値で入力してください | Hold time must be a number | La duración debe ser un número |
| `px_hold_bad_step` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `px_hold_down` | 停留 −20 ms | 停留 −20 ms | 表示時間 −20 ms | Hold −20 ms | Duración −20 ms |
| `px_hold_up` | 停留 +20 ms | 停留 +20 ms | 表示時間 +20 ms | Hold +20 ms | Duración +20 ms |
| `px_import_do` | 导入 | 匯入 | 読み込み | Import | Importar |
| `px_import_hint` | 在 Clawdmeter 编辑器点「复制到剪贴板」，然后在这里粘贴（⌘V） | 在 Clawdmeter 編輯器按「複製到剪貼簿」，然後在這裡貼上（⌘V） | Clawdmeter エディタで「クリップボードにコピー」を押し、ここに貼り付け（⌘V） | Hit “Copy to clipboard” in the Clawdmeter editor, then paste here (⌘V) | Pulsa «Copiar al portapapeles» en el editor de Clawdmeter y pégalo aquí (⌘V) |
| `px_import_json` | 粘贴 JSON | 貼上 JSON | JSON を貼り付け | Paste JSON | Pegar JSON |
| `px_import_kind_claw_in_free` | 这是 Clawdmeter 动画文件——请先开一张 Clawdmeter 像素画布再导入 | 這是 Clawdmeter 動畫檔——請開一張 Clawdmeter 像素畫布再匯入 | これは Clawdmeter アニメのファイルです——Clawdmeter キャンバスを開いてから読み込んでください | This is a Clawdmeter animation file — open a Clawdmeter canvas to import it | Este es un archivo de animación Clawdmeter: abre un lienzo Clawdmeter para importarlo |
| `px_import_kind_free_in_claw` | 这是自由像素图文件——请先开一张自由像素画布再导入 | 這是自由像素圖檔——請開一張自由像素畫布再匯入 | これはフリーピクセルのファイルです——フリーピクセルキャンバスを開いてから読み込んでください | This is a free pixel art file — open a free pixel canvas to import it | Este es un archivo de píxel libre: abre un lienzo de píxel libre para importarlo |
| `px_import_ph` | { "name": …, "frames": […] } | { "name": …, "frames": […] } | { "name": …, "frames": […] } | { "name": …, "frames": […] } | { "name": …, "frames": […] } |
| `px_import_title` | 粘贴动画 JSON | 貼上動畫 JSON | アニメーション JSON を貼り付け | Paste animation JSON | Pegar el JSON de la animación |
| `px_imported` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `px_io_hd` | JSON 档处理 | JSON 檔處理 | JSONファイル | JSON file | Archivo JSON |
| `px_name` | 动画名称 | 動畫名稱 | アニメ名 | Animation name | Nombre de la animación |
| `px_name_hint` | 名称要唯一，之后要填进 splash.cpp 才会显示 | 名稱要唯一，之後要填進 splash.cpp 才會顯示 | 名前は一意に。splash.cpp に追加しないと表示されません | Must be unique — also needs adding to splash.cpp to show up | Debe ser único — además hay que añadirlo a splash.cpp para que aparezca |
| `px_name_required` | 请先填动画名称——设备那边要靠名字才找得到这支动画 | 請先填動畫名稱——裝置那邊要靠名字才找得到這支動畫 | まずアニメ名を入力してください。デバイスは名前で参照します | Name the animation first — the device finds it by name | Ponle nombre a la animación — el dispositivo la busca por su nombre |
| `px_onion_title` | 洋葱皮——前一格垫底显示（第一格垫最后一格） | 洋蔥皮——前一格墊底顯示（第一格墊最後一格） | オニオンスキン — 前のコマを下に表示（最初のコマは最後のコマ） | Onion skin — previous frame shown underneath (first frame shows the last) | Papel cebolla — muestra debajo el fotograma anterior (el primero muestra el último) |
| `px_painted` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `px_palette` | 这支动画的颜色 | 這支動畫的顏色 | このアニメの色 | Colours in this animation | Colores de esta animación |
| `px_palette_free` | 这张图的颜色 | 這張圖的顏色 | この絵の色 | Colours in this image | Colores de esta imagen |
| `px_palette_full` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `px_paste_short` | 粘贴 | 貼上 | 貼り付け | Paste | Pegar |
| `px_pick` | 选色 | 選色 | 色を選ぶ | Pick a colour | Elige un color |
| `px_pick_hint` | 点一下就加进这支动画的颜色并选取。已经在用的会直接选取。 | 點一下就加進這支動畫的顏色並選取。已經在用的會直接選取。 | クリックで「このアニメの色」に追加＋選択。使用中の色はそのまま選択されます。 | Click to add it to this animation’s colours and select it. Colours already in use get selected. | Haz clic para añadirlo a los colores de esta animación y seleccionarlo. Los colores ya usados quedan seleccionados. |
| `px_play` | ▶ 播放 | ▶ 播放 | ▶ 再生 | ▶ Play | ▶ Reproducir |
| `px_preview` | 实机预览 | 實機預覽 | 実機プレビュー | Device preview | Vista previa del dispositivo |
| `px_pv_badge` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `px_pv_splash` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `px_replace_cancelled` | 已取消替换 | 已取消取代 | 置き換えをキャンセルしました | Replace cancelled | Reemplazo cancelado |
| `px_replace_pick_new` | 点一个新颜色——色盘、渐层或直接输入色码（Esc 取消） | 點一個新顏色——色盤、漸層或直接輸入色碼（Esc 取消） | 新しい色をクリック——色盤・グラデーション・カラーコード入力のいずれでも（Esc でキャンセル） | Click a new colour — the swatch board, the gradient, or type a hex code (Esc to cancel) | Haz clic en un color nuevo: el muestrario, el degradado o escribe un código hex (Esc para cancelar) |
| `px_replace_pick_old` | 点一下要被换掉的颜色——画布上的格子或色票列皆可（Esc 取消） | 點一下要被換掉的顏色——畫布上的格子或色票列皆可（Esc 取消） | 置き換えたい色をクリック——キャンバスのマスでもパレット列でも OK（Esc でキャンセル） | Click the colour to replace — a canvas cell or a swatch in the palette row (Esc to cancel) | Haz clic en el color a reemplazar: una celda del lienzo o una muestra de la paleta (Esc para cancelar) |
| `px_resize_max` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `px_save_json` | 存档 JSON… | 存檔 JSON… | JSON を保存… | Save JSON… | Guardar JSON… |
| `px_save_short` | 存档 | 存檔 | 保存 | Save | Guardar |
| `px_saved` | 已存档 | 已存檔 | 保存しました | Saved | Guardado |
| `px_sec_info` | 动画信息 | 動畫資訊 | アニメ情報 | Animation info | Información de la animación |
| `px_sel_clipped` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `px_sel_empty` | 选区里没有东西可以翻 | 選區裡沒有東西可以翻 | 選択範囲に反転できるものがありません | Nothing in the selection to flip | No hay nada en la selección que voltear |
| `px_slot_clean` | ✓ 刚好在插槽边界结束 | ✓ 剛好在插槽邊界結束 | ✓ スロットの境界でちょうど終わる | ✓ Lands on the slot boundary | ✓ Encaja justo en el intervalo |
| `px_slot_cut` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `px_slot_fix` | 调成 | 調成 | 候補 | Try | Probar |
| `px_slot_sum` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `px_stop` | ■ 停止 | ■ 停止 | ■ 停止 | ■ Stop | ■ Detener |
| `px_tool_eraser` | 橡皮擦 — 把格子清成透明（0 号） | 橡皮擦 — 把格子清成透明（0 號） | 消しゴム — マスを透明（0 番）に戻す | Eraser — clear cells to transparent (index 0) | Goma — deja las celdas transparentes (índice 0) |
| `px_tool_pen` | 画笔 — 用选中的颜色填格 | 畫筆 — 用選中的顏色填格 | ペン — 選択中の色でマスを塗る | Pen — fill cells with the selected colour | Lápiz — rellena celdas con el color elegido |
| `px_tool_picker` | 滴管 — 点一格取它的色号（空格＝取到透明） | 滴管 — 點一格取它的色號（空格＝取到透明） | スポイト — マスをクリックして色番号を取得（空マス＝透明） | Eyedropper — click a cell to pick its colour index (empty = transparent) | Cuentagotas — haz clic en una celda para tomar su índice de color (vacía = transparente) |
| `px_tool_select` | 选取 — 框住一块，可拖曳／方向键搬移、⌘C 复制、⌘V 贴原位 | 選取 — 框住一塊，可拖曳／方向鍵搬移、⌘C 複製、⌘V 貼原位 | 選択 — 範囲を囲んでドラッグ／矢印キーで移動、⌘C でコピー、⌘V で同じ位置に貼り付け | Select — box a region, then drag or arrow-key it; ⌘C copies, ⌘V pastes in place | Seleccionar — enmarca una zona y arrástrala o muévela con las flechas; ⌘C copia, ⌘V pega en el sitio |
| `px_tools` | 像素工具 | 像素工具 | ピクセルツール | Pixel tools | Herramientas de píxeles |
| `px_transparent` | 透明（0 号） | 透明（0 號） | 透明（0 番） | Transparent (index 0) | Transparente (índice 0) |
| `px_zoom_per_cell` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |

### `qr`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `qr_toast_copied` | QR Code 内容已复制到剪贴板 | QR Code 內容已複製到剪貼簿 | QR コードの内容をクリップボードにコピーしました | QR Code content copied to clipboard | Contenido del código QR copiado al portapapeles |
| `qr_toast_msg` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `qr_toast_open` | 打开 | 開啟 | 開く | Open | Abrir |
| `qr_toast_url_copied` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |

### `region`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `region` | 矩形 | 矩形 | 矩形 | Region | Área |

### `resize`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `resize_apply` | 应用 | 套用 | 適用 | Apply | Aplicar |
| `resize_cancel` | 取消 | 取消 | キャンセル | Cancel | Cancelar |
| `resize_height` | 高度 | 高度 | 高さ | Height | Alto |
| `resize_height_hint` | px（等比例自动计算） | px（等比例自動計算） | px（縦横比固定） | px (proportional) | px (proporcional) |
| `resize_lock_title` | 锁定等比例 | 鎖定等比例 | 縦横比を固定 | Lock aspect ratio | Bloquear la proporción |
| `resize_title` | 调整尺寸 | 調整尺寸 | サイズ変更 | Resize | Redimensionar |
| `resize_width` | 宽度 | 寬度 | 幅 | Width | Ancho |

### `ruler`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `ruler` | 标尺 | 尺標 | 定規 | Ruler | Regla |

### `save`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `save_bmp_desc` | 点阵图，无压缩 | 點陣圖，無壓縮 | ビットマップ、非圧縮 | Bitmap, uncompressed | Mapa de bits, sin comprimir |
| `save_cancel` | 取消 | 取消 | キャンセル | Cancel | Cancelar |
| `save_confirm` | 保存 | 儲存 | 保存 | Save | Guardar |
| `save_gif_desc` | 单帧图片，256 色 | 單幀圖片，256 色 | 単一フレーム、256色 | Single frame, 256 colors | Un solo fotograma, 256 colores |
| `save_gif_desc_anim` | 整支动画，256 色 | 整支動畫，256 色 | アニメーション全体、256色 | Whole animation, 256 colors | La animación completa, 256 colores |
| `save_gif_desc_free` | 单帧图片——无格线与数字带 | 單幀圖片——無格線與數字帶 | 単一フレーム——グリッド線・番号帯なし | Single frame — no gridlines or number bands | Fotograma único: sin cuadrícula ni bandas de números |
| `save_jpg_desc` | 有损压缩，文件较小 | 有損壓縮，檔案較小 | 非可逆圧縮、ファイルサイズ小 | Lossy, smaller file size | Con pérdida, archivo más pequeño |
| `save_json_desc` | Clawdmeter 动画数据（机器读） | Clawdmeter 動畫資料（機器讀） | Clawdmeter アニメデータ（機械可読） | Clawdmeter animation data (machine-readable) | Datos de animación de Clawdmeter (legibles por máquina) |
| `save_json_desc_free` | 自由像素图数据（VAS 可重新打开编辑） | 自由像素圖資料（VAS 可重新開啟編輯） | 自由ピクセルアートのデータ（VAS で再編集できます） | Free pixel-art data (reopens in VAS for editing) | Datos de píxel libre (se puede reabrir y editar en VAS) |
| `save_pdf_desc` | 文档格式，适合打印 | 文件格式，適合列印 | ドキュメント形式、印刷に最適 | Document format, ideal for printing | Formato de documento, ideal para imprimir |
| `save_png_desc` | 无损，支持透明背景 | 無損，支援透明背景 | 可逆圧縮、透明背景対応 | Lossless, supports transparency | Sin pérdida, admite transparencia |
| `save_pxchart` | 图表 | 圖表 | 図案 | Chart | Diagrama |
| `save_pxchart_desc` | 可打印的拼豆／织图图表（格线＋色号＋数量） | 可列印的拼豆／織圖圖表（格線＋色號＋數量） | 印刷用ビーズ／クロスステッチ図案（グリッド＋色番号＋数量） | Printable bead / stitch chart (grid, color codes, counts) | Diagrama imprimible para hama / punto de cruz (cuadrícula, códigos y cantidades) |
| `save_tiff_desc` | 印刷级质量，支持透明 | 印刷級品質，支援透明 | 印刷品質、透明背景対応 | Print-quality, supports transparency | Calidad de imprenta, admite transparencia |
| `save_title` | 保存格式 | 儲存格式 | 保存形式 | Save Format | Formato de guardado |
| `save_webp_desc` | 现代格式，支持透明 | 現代格式，支援透明 | モダン形式、透明背景対応 | Modern format, supports transparency | Formato moderno, admite transparencia |

### `screen`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `screen_select_click` | 点击截取此屏幕 | 點擊截取此螢幕 | クリックしてこの画面をキャプチャ | Click to capture this screen | Haz clic para capturar esta pantalla |
| `screen_select_display` | 屏幕 | 螢幕 | ディスプレイ | Display | Pantalla |
| `screen_select_hints_multi` | Enter — 截取全部屏幕并合并　　Esc — 取消 | Enter — 截取全部螢幕並合併　　Esc — 取消 | Enter — 全画面を結合キャプチャ　　Esc — キャンセル | Enter — Capture all screens merged　　Esc — Cancel | Intro — Capturar todas las pantallas unidas　　Esc — Cancelar |
| `screen_select_hints_single` | Esc — 取消 | Esc — 取消 | Esc — キャンセル | Esc — Cancel | Esc — Cancelar |

### `scroll`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `scroll_capture` | 长截图 | 長截圖 | ロングスクリーンショット | Long screenshot | Captura larga |
| `scroll_hints_auto` | 自动滚动截取中…　Enter 提前完成　Esc 取消 | 自動捲動擷取中…　Enter 提前完成　Esc 取消 | 自動スクロール撮影中…　Enter 早めに完了　Esc キャンセル | Auto-scrolling capture…　Enter Finish early　Esc Cancel | Capturando con desplazamiento automático…　Intro Terminar antes　Esc Cancelar |
| `scroll_hints_capture` | 慢慢滚动页面　Enter 完成拼接　Esc 取消 | 慢慢捲動頁面　Enter 完成拼接　Esc 取消 | ゆっくりスクロール　Enter つなぎ合わせ完了　Esc キャンセル | Scroll slowly　Enter Finish stitching　Esc Cancel | Desplázate despacio　Intro Terminar la unión　Esc Cancelar |
| `scroll_hints_frame` | 拖框圈住要滚动的内容　空格键＝自动框住光标下窗口　Esc 取消 | 拖框圈住要捲動的內容　空白鍵＝自動框住游標下視窗　Esc 取消 | スクロールする範囲をドラッグで囲む　スペース＝カーソル下のウィンドウを自動枠取り　Esc キャンセル | Drag around the scrolling content　Space = auto-frame window under cursor　Esc Cancel | Arrastra alrededor del contenido desplazable　Espacio = encuadrar la ventana bajo el cursor　Esc Cancelar |

### `shape`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `shape_ellipse_title` | 椭圆框 | 橢圓框 | 楕円 | Ellipse | Elipse |
| `shape_rect_title` | 矩形框 | 矩形框 | 矩形 | Rectangle | Rectángulo |

### `snap`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `snap_toggle_title` | 智能导线（\ 开关 ／ ⌥ 暂停吸附） | 智慧導線（\ 開關 ／ ⌥ 暫停吸附） | スマートガイド（\ トグル ／ ⌥ でスナップ一時停止） | Smart Guides (\ toggle / ⌥ pause snap) | Guías inteligentes (\ alternar / ⌥ pausar el ajuste) |

### `stroke`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `stroke_color_title` | 描边颜色 | 描邊顏色 | ストロークカラー | Stroke color | Color del trazo |
| `stroke_width_preset_title` | 快速选择粗细 | 快速選擇粗細 | 線幅をすばやく選択 | Quick-select stroke width | Elegir rápido el grosor del trazo |

### `style`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `style_circle` | 空心圆圈① | 空心圓圈① | 丸囲み① | Circle ① | Círculo ① |
| `style_circle_fill` | 实心圆圈➊ | 實心圓圈➊ | 塗り丸➊ | Filled circle ➊ | Círculo relleno ➊ |
| `style_cjk_circle` | 中文圆圈㊀ | 中文圓圈㊀ | 漢数字丸囲㊀ | CJK circle ㊀ | Círculo CJK ㊀ |
| `style_cjk_paren` | 中文括号㈠ | 中文括號㈠ | 漢数字括弧㈠ | CJK paren ㈠ | Paréntesis CJK ㈠ |
| `style_dot` | 实心圆点 | 實心圓點 | 塗りつぶし点 | Filled dot | Punto relleno |
| `style_roman` | 罗马数字Ⅰ | 羅馬數字Ⅰ | ローマ数字Ⅰ | Roman Ⅰ | Romano Ⅰ |

### `sym`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `sym_arrow` | 箭头 | 箭頭 | 矢印 | Arrows | Flechas |
| `sym_cat_arrow_basic` | 一般 | 一般 | 一般 | Basic | Básicas |
| `sym_cat_arrow_double` | 双线 | 雙線 | 二重線 | Double | Dobles |
| `sym_cat_arrow_triangle` | 三角 | 三角 | 三角 | Triangle | Triangulares |
| `sym_cat_letter_bold` | 粗体 | 粗體 | ボールド | Bold | Negrita |
| `sym_cat_letter_bold_italic` | 粗斜 | 粗斜 | 太字斜体 | Bold Italic | Negrita cursiva |
| `sym_cat_letter_circle` | 圆框 | 圓框 | 丸囲み | Circled | En círculo |
| `sym_cat_letter_full` | 全角 | 全形 | 全角 | Full-width | Ancho completo |
| `sym_cat_letter_script` | 草书 | 草書 | 筆記体 | Script | Manuscrita |
| `sym_cat_misc_currency` | 货币 | 貨幣 | 通貨 | Currency | Moneda |
| `sym_cat_misc_mark` | 标记 | 標記 | マーク | Marks | Marcas |
| `sym_cat_misc_math` | 数学 | 數學 | 数学 | Math | Matemáticas |
| `sym_cat_misc_tech` | 技术 | 技術 | テック | Tech | Técnicos |
| `sym_cat_shape_deco` | 装饰 | 裝飾 | 装飾 | Decorative | Decorativas |
| `sym_cat_shape_geom` | 几何 | 幾何 | 幾何 | Geometric | Geométricas |
| `sym_gradient_empty` | 渐变模式不支持此分类的符号 | 漸層模式不支援此分類的符號 | グラデーションモードはこのカテゴリの記号に対応していません | Gradient mode does not support symbols in this category | El modo degradado no admite símbolos de esta categoría |
| `sym_letter` | 字母 | 字母 | 文字 | Letters | Letras |
| `sym_misc` | 其他 | 其他 | その他 | Misc | Varios |
| `sym_shape` | 形状 | 形狀 | 図形 | Shapes | Formas |

### `symbol`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `symbol_reopen_title` | 点击重开面板 | 點擊重開面板 | クリックしてパネルを再表示 | Click to reopen panel | Haz clic para volver a abrir el panel |
| `symbol_size_title` | 符号大小（图像像素） | 符號大小（圖像像素） | シンボルサイズ（画像ピクセル） | Symbol size (image pixels) | Tamaño del símbolo (píxeles de la imagen) |

### `text`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `text_stroke_preset_title` | 快速选择描边粗细 | 快速選擇描邊粗細 | ストローク幅をすばやく選択 | Quick-select stroke width | Elegir rápido el grosor del trazo |
| `text_stroke_width_title` | 描边粗细（0 = 无） | 描邊粗細（0 = 無） | ストローク幅（0＝なし） | Stroke width (0 = none) | Grosor del trazo (0 = ninguno) |

### `thickness`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `thickness_line` | 粗细 | 粗細 | 太さ | Width | Grosor |
| `thickness_stroke` | 描边 | 描邊 | ストローク | Stroke | Trazo |

### `tip`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `tip_end_cap` | 终点样式 | 終點樣式 | 終点スタイル | End cap style | Estilo del extremo final |
| `tip_font_size_preset` | 快速选择大小 | 快速選擇大小 | クイックサイズ | Quick size picker | Selector rápido de tamaño |
| `tip_letterbox` | 等比留白，不限制比例 | 等比留白，不限制比例 | レターボックス（比率ロックなし） | Letterbox (no aspect ratio lock) | Bandas negras (sin bloqueo de proporción) |
| `tip_line_ortho` | 折线绘制（按 Shift 锁水平/垂直） | 折線繪製（按 Shift 鎖水平/垂直） | 折れ線（Shift で水平/垂直にスナップ） | Polyline (hold Shift to lock horizontal/vertical) | Polilínea (mantén Mayús para fijarla en horizontal/vertical) |
| `tip_start_cap` | 起点样式 | 起點樣式 | 始点スタイル | Start cap style | Estilo del extremo inicial |

### `toast`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `toast_box_copied` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `toast_capture_fail` | 截图失败 | 截圖失敗 | キャプチャに失敗しました | Capture failed | Falló la captura |
| `toast_clipboard_empty` | 剪贴板没有图片 | 剪貼簿沒有圖片 | クリップボードに画像がありません | No image in clipboard | No hay ninguna imagen en el portapapeles |
| `toast_clipboard_paste` | 粘贴图片 | 貼上圖片 | 画像を貼り付け | Paste Image | Pegar imagen |
| `toast_converted` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `toast_copied` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `toast_crop_first` | 请先拖拽选取裁切范围 | 請先拖曳選取裁切範圍 | トリミング範囲をドラッグして選択してください | Drag to select a crop area first | Primero arrastra para elegir un área de recorte |
| `toast_crop_oob` | 裁切范围超出图片边界 | 裁切範圍超出圖片邊界 | トリミング範囲が画像の境界を超えています | Crop area exceeds image bounds | El área de recorte se sale de la imagen |
| `toast_cropped` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `toast_done` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `toast_drop_images` | 仅支持 PNG / JPG / WebP / GIF / BMP / TIFF / SVG 格式 | 僅支援 PNG / JPG / WebP / GIF / BMP / TIFF / SVG 格式 | PNG / JPG / WebP / GIF / BMP / TIFF / SVG のみ対応 | Only PNG / JPG / WebP / GIF / BMP / TIFF / SVG supported | Solo se admiten PNG / JPG / WebP / GIF / BMP / TIFF / SVG |
| `toast_drop_mismatch` | 无法导入这个文件——扩展名与实际内容不符 | 無法匯入這個檔案——副檔名與實際內容不符 | このファイルは読み込めません——拡張子と実際の内容が一致しません | Cannot import this file — its extension doesn't match its actual content | No se puede importar: la extensión no coincide con el contenido real |
| `toast_drop_svgz` | 这是 gzip 压缩的 SVG（.svgz），请先解压缩再导入 | 這是 gzip 壓縮的 SVG（.svgz），請先解壓縮再匯入 | gzip 圧縮された SVG（.svgz）です。展開してから読み込んでください | This is a gzip-compressed SVG (.svgz) — decompress it first | Es un SVG comprimido con gzip (.svgz): descomprímelo primero |
| `toast_export_render_fail` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `toast_extended` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `toast_feedback_manual` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `toast_image_read_fail` | 无法读取这个图片（过大／格式不符／文件夹不允许） | 無法讀取這個圖片（過大／格式不符／資料夾不允許） | この画像を読み込めません（サイズ／形式／フォルダ） | Can't read this image (too large / wrong format / folder) | No se puede leer esta imagen (tamaño / formato / carpeta) |
| `toast_img_copied` | 图片已复制到剪贴板 | 圖片已複製到剪貼簿 | 画像をクリップボードにコピーしました | Image copied to clipboard | Imagen copiada al portapapeles |
| `toast_import_too_large` | 图片超过 20MB 上限，无法导入 | 圖片超過 20MB 上限，無法匯入 | 画像が 20MB の上限を超えています | Image exceeds the 20 MB limit | La imagen supera el límite de 20 MB |
| `toast_imported` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `toast_load_image_first` | 请先载入图片 | 請先載入圖片 | 先に画像を読み込んでください | Please load an image first | Primero carga una imagen |
| `toast_new_canvas` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `toast_no_files` | 没有可转换的文件 | 沒有可轉換的檔案 | 変換するファイルがありません | No files to convert | No hay archivos que convertir |
| `toast_no_image` | 尚未载入图片 | 尚未載入圖片 | 画像が読み込まれていません | No image loaded | No hay ninguna imagen cargada |
| `toast_no_windows` | 未找到可截图的窗口 | 未找到可截圖的視窗 | キャプチャできるウィンドウが見つかりません | No capturable windows found | No se encontró ninguna ventana capturable |
| `toast_num_limit` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `toast_num_reset` | 编号已重置，下一个从 1 开始 | 編號已重置，下一個從 1 開始 | カウンターを 1 にリセットしました | Counter reset to 1 | Contador reiniciado a 1 |
| `toast_ocr_copied` | OCR 文字已复制到剪贴板 | OCR 文字已複製到剪貼簿 | OCR テキストをクリップボードにコピーしました | OCR text copied to clipboard | Texto del OCR copiado al portapapeles |
| `toast_ocr_fail` | OCR 识别失败 | OCR 辨識失敗 | OCR に失敗しました | OCR failed | Falló el OCR |
| `toast_ocr_no_text` | OCR 未识别到文字，请尝试更清晰的区域 | OCR 未辨識到文字，請嘗試更清晰的區域 | テキストが検出されませんでした。より鮮明な範囲を試してください | No text detected — try a clearer area | No se detectó texto — prueba con un área más nítida |
| `toast_open_settings` | 打开系统设置 | 開啟系統設定 | システム設定を開く | Open System Settings | Abrir Ajustes del Sistema |
| `toast_overlay_exists` | 请先删除现有叠入图（Delete 键），再插入新图 | 請先刪除現有疊入圖（Delete 鍵），再插入新圖 | 既存のオーバーレイを削除（Delete キー）してから新しい画像を挿入してください | Delete the existing overlay (Delete key) before inserting a new one | Elimina la superposición existente (tecla Delete) antes de insertar otra |
| `toast_overlay_inserted` | 叠入图片已插入，拖动可移动，拖角落可等比缩放 | 疊入圖片已插入，拖動可移動，拖角落可等比縮放 | オーバーレイを挿入しました。ドラッグで移動、コーナーをドラッグで拡縮 | Overlay inserted — drag to move, drag corner to scale | Superposición insertada — arrastra para moverla, arrastra una esquina para escalarla |
| `toast_permission` | 需要「屏幕录制」权限   | 需要「螢幕錄製」權限   | 「画面収録」の権限が必要です   | Screen Recording permission required   | Se necesita permiso de Grabación de pantalla   |
| `toast_privacy_done` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `toast_privacy_fail` | 检测失败 | 偵測失敗 | 検出に失敗しました | Detection failed | Falló la detección |
| `toast_privacy_none` | 未检测到敏感信息 | 未偵測到敏感資訊 | 機微情報は検出されませんでした | No sensitive info detected | No se detectó información sensible |
| `toast_privacy_scanning` | 检测敏感信息中… | 偵測敏感資訊中… | 機微情報を検出中… | Detecting sensitive info… | Detectando información sensible… |
| `toast_qr_opened` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `toast_qr_scheme_copied` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `toast_resize_invalid` | 请输入有效的宽度与高度 | 請輸入有效的寬度與高度 | 有効な幅と高さを入力してください | Please enter valid width and height | Escribe un ancho y un alto válidos |
| `toast_resize_max` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `toast_resize_min` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `toast_resized` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `toast_save_fail` | 保存失败 | 儲存失敗 | 保存に失敗しました | Save failed | Falló el guardado |
| `toast_save_fail_detail` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `toast_saved` | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ | _（帶參數的訊息·值需代入參數才成形）_ |
| `toast_select_dir` | 请先选择输出目录 | 請先選擇輸出目錄 | 出力フォルダを選択してください | Please select an output directory | Selecciona una carpeta de salida |
| `toast_select_files` | 请先选取要转换的文件 | 請先選取要轉換的檔案 | 変換するファイルを選択してください | Please select files to convert | Selecciona los archivos que quieres convertir |
| `toast_template_applied` | 套版已应用 | 套版已套用 | テンプレートを適用しました | Template applied | Plantilla aplicada |
| `toast_text_copied` | 文字已复制到剪贴板 | 文字已複製到剪貼簿 | テキストをクリップボードにコピーしました | Text copied to clipboard | Texto copiado al portapapeles |
| `toast_wm_conflict` | 文字与图片水印位置相同，请各自选择不同位置 | 文字與圖片浮水印位置相同，請各自選擇不同位置 | テキストと画像の透かし位置が同じです。それぞれ異なる位置を選択してください | Text and image watermarks overlap — choose different positions | Las dos marcas de agua se solapan — elige posiciones distintas |
| `toast_wm_img_missing` | 已勾选图片水印，但尚未选取图片 | 已勾選圖片浮水印，但尚未選取圖片 | 画像透かしが有効ですが、画像が選択されていません | Image watermark is enabled but no image has been selected | La marca de agua de imagen está activada pero no has elegido ninguna imagen |
| `toast_wm_text_empty` | 已勾选文字水印，但尚未输入文字 | 已勾選文字浮水印，但尚未輸入文字 | テキスト透かしが有効ですが、テキストが入力されていません | Text watermark is enabled but no text has been entered | La marca de agua de texto está activada pero no has escrito ningún texto |

### `tool`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `tool_boxselect` | 框型选取 (M) | 框型選取 (M) | ボックス選択 (M) | Box Select (M) | Selección por marco (M) |
| `tool_callout` | 对话气泡 (Q) | 對話氣泡 (Q) | 吹き出し (Q) | Callout Bubble (Q) | Globo de texto (Q) |
| `tool_crop` | 裁切 (C) | 裁切 (C) | トリミング (C) | Crop (C) | Recortar (C) |
| `tool_cube` | 立方体 | 立方體 | 立方体 | Cube | Cubo |
| `tool_extend` | 延伸画布 (E) | 延伸畫布 (E) | キャンバス拡張 (E) | Extend Canvas (E) | Ampliar lienzo (E) |
| `tool_fillrect` | 色块 (B) | 色塊 (B) | 塗りつぶし (B) | Fill (B) | Relleno (B) |
| `tool_fit` | 适合窗口 (⌘0) | 適合視窗 (⌘0) | ウィンドウに合わせる (⌘0) | Fit to Window (⌘0) | Ajustar a la ventana (⌘0) |
| `tool_line` | 线条 (L) | 線條 (L) | 線 (L) | Line (L) | Línea (L) |
| `tool_magnify` | 放大镜标注 (Y) | 放大鏡標註 (Y) | 拡大鏡注釈 (Y) | Magnify Annotation (Y) | Anotación de lupa (Y) |
| `tool_measure` | 尺标 (D) | 尺標 (D) | 定規 (D) | Measure (D) | Medir (D) |
| `tool_mosaic` | 马赛克/模糊 (X) | 馬賽克/模糊 (X) | モザイク/ぼかし (X) | Mosaic/Blur (X) | Mosaico/Desenfoque (X) |
| `tool_number` | 编号 (N) | 編號 (N) | 番号 (N) | Number (N) | Número (N) |
| `tool_ocr` | OCR 文字识别 (G) | OCR 文字辨識 (G) | OCR (G) | OCR (G) | OCR (G) |
| `tool_open_menu` | 打开 / 新画布 | 開啟 / 新畫布 | 開く / 新規キャンバス | Open / New Canvas | Abrir / Nuevo lienzo |
| `tool_overlay` | 叠入图片 (O) | 疊入圖片 (O) | 画像オーバーレイ (O) | Overlay Image (O) | Superponer imagen (O) |
| `tool_pen` | 笔型 (P) | 筆型 (P) | ペン (P) | Pen (P) | Lápiz (P) |
| `tool_privacymask` | 隐私遮蔽 (K) | 隱私遮蔽 (K) | プライバシーマスク (K) | Privacy Mask (K) | Máscara de privacidad (K) |
| `tool_rect` | 矩形框 (R) | 矩形框 (R) | 矩形 (R) | Rectangle (R) | Rectángulo (R) |
| `tool_redo` | 重做 (⌘⇧Z) | 重做 (⌘⇧Z) | やり直し (⌘⇧Z) | Redo (⌘⇧Z) | Rehacer (⌘⇧Z) |
| `tool_resize` | 调整大小 (S) | 調整大小 (S) | サイズ変更 (S) | Resize (S) | Redimensionar (S) |
| `tool_select` | 选取 (V) | 選取 (V) | 選択 (V) | Select (V) | Seleccionar (V) |
| `tool_solid` | 立体标注 | 立體標註 | 立体オブジェクト | 3D Object | Objeto 3D |
| `tool_solid_fill` | 填色 | 填色 | 塗りつぶし | Filled | Relleno |
| `tool_solid_wire` | 框线 | 框線 | ワイヤー | Wireframe | Alambre |
| `tool_sphere` | 球体 | 球體 | 球体 | Sphere | Esfera |
| `tool_symbol` | 符号印章 (U) | 符號印章 (U) | スタンプ (U) | Stamp (U) | Sello (U) |
| `tool_template` | 一键套版 | 一鍵套版 | テンプレート | Template | Plantilla |
| `tool_text` | 文字 (T) | 文字 (T) | テキスト (T) | Text (T) | Texto (T) |
| `tool_text_pro` | 去背（Pro 版功能） | 去背（Pro 版功能） | 背景除去（Pro 版） | Remove BG (Pro) | Quitar fondo (Pro) |
| `tool_undo` | 撤销 (⌘Z) | 撤銷 (⌘Z) | 元に戻す (⌘Z) | Undo (⌘Z) | Deshacer (⌘Z) |
| `tool_zoom_in` | 放大 (⌘=) | 放大 (⌘=) | 拡大 (⌘=) | Zoom In (⌘=) | Acercar (⌘=) |
| `tool_zoom_out` | 缩小 (⌘-) | 縮小 (⌘-) | 縮小 (⌘-) | Zoom Out (⌘-) | Alejar (⌘-) |

### `tpl`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `tpl_adjust` | 调整 | 調整 | 調整 | Adjust | Ajustar |
| `tpl_apple_blue` | Apple 蓝 | Apple 藍 | Apple ブルー | Apple Blue | Azul Apple |
| `tpl_apple_green` | Apple 绿 | Apple 綠 | Apple グリーン | Apple Green | Verde Apple |
| `tpl_apple_orange` | Apple 橙 | Apple 橙 | Apple オレンジ | Apple Orange | Naranja Apple |
| `tpl_apple_purple` | Apple 紫 | Apple 紫 | Apple パープル | Apple Purple | Morado Apple |
| `tpl_apple_red` | Apple 红 | Apple 紅 | Apple レッド | Apple Red | Rojo Apple |
| `tpl_apple_yellow` | Apple 黄 | Apple 黃 | Apple イエロー | Apple Yellow | Amarillo Apple |
| `tpl_background` | 背景 | 背景 | 背景 | Background | Fondo |
| `tpl_padding` | 留白 | 留白 | 余白 | Padding | Margen interior |
| `tpl_radius` | 圆角 | 圓角 | 角丸 | Radius | Radio |
| `tpl_shadow` | 外框 | 外框 | シャドウ | Shadow | Sombra |
| `tpl_social` | 社群尺寸（可选） | 社群尺寸（選用） | SNS サイズ（任意） | Social Sizes (optional) | Tamaños para redes (opcional) |
| `tpl_title` | 一键套版 | 一鍵套版 | テンプレート | Template | Plantilla |

### `tray`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `tray_new_canvas` | 新建空白画布 | 新增空白畫布 | 新規空白キャンバス | New Blank Canvas | Nuevo lienzo en blanco |
| `tray_open_file` | 打开图片… | 開啟圖片… | 画像を開く… | Open Image… | Abrir imagen… |
| `tray_quit` | 退出 VAS | 結束 VAS | VAS を終了 | Quit VAS | Salir de VAS |

### `whiteboard`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `whiteboard` | 白板 | 白板 | キャンバス | Canvas | Lienzo |

### `window`

| key | zh-CN（zh-Hans） | zh（zh-Hant） | ja（ja） | en（en） | es（es） |
|---|---|---|---|---|---|
| `window` | 窗口 | 視窗 | ウィンドウ | Window | Ventana |
