#!/usr/bin/env python3
"""VAS 發版數字 —— 版號／日期／大小只寫在 tools/release-facts.json 一處，頁面上的每個現況欄位由本工具對齊。

用法（在 repo 根目錄）：
    python3 tools/release_facts.py              # 檢查（CI 用；有任何不一致回傳非 0，並列出哪頁哪個值）
    python3 tools/release_facts.py --fix        # 改完 release-facts.json 後跑：各頁舊值一次換成新值
    python3 tools/release_facts.py --register   # 重建欄位登記表（新增／刪除了某個現況欄位之後才需要）

發版流程：①（更新日誌的新一行／新一卷照常手寫）② 改 release-facts.json ③ --fix ④ 檢查全綠。
Sprint 數與 Electron 版本數不用填：由更新日誌的實際行數推導。

歷史紀錄不連動：更新日誌的 arc-line 與 arc-divider 先遮掉再比對，舊版號的那一行不會被 --fix 改到。
唯一例外是免費版那組的標題「v3.45 → vX.YY」——它是現況。里程碑頁（milestone）整頁是歷史，不登記。
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FACTS = os.path.join(ROOT, "tools", "release-facts.json")
REGISTRY = os.path.join(ROOT, "tools", "release-slots.json")
LOCALES = ["", "en/", "ja/", "cn/", "es/"]
PAGES = ["index.html", "instrument.html", "changelog.html", "faq.html"]
FILES = [l + p for l in LOCALES for p in PAGES]
# 頁面上合法、但不是發版數字的大小（Snagit 450 MB、歷史圖匣單張 4.4 MB、批次單檔上限 20 MB）
MB_ALLOW = {"450", "4.4", "20"}

MONTH_EN = "January February March April May June July August September October November December".split()
MONTH_ES = "enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split()

# 與 matrix_audit.py 的 HIST 同範圍，但保留 AI CONTEXT 註解（那是現況宣稱）與免費版的組標題
HIST = re.compile(r'<div class="arc-line">.*?</div>'
                  r'|<summary class="arc-divider">(?:(?!</summary>|v3\.45 → ).)*</summary>'
                  r'|<div class="edensity-cap">.*?</div>')


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def live_spans(text):
    """遮掉歷史區塊之後剩下的區段 [(start, end), ...]。"""
    spans, pos = [], 0
    for m in HIST.finditer(text):
        spans.append((pos, m.start()))
        pos = m.end()
    spans.append((pos, len(text)))
    return spans


def live_text(text):
    return "\0".join(text[a:b] for a, b in live_spans(text))


def derive():
    """從各語系更新日誌推導 Sprint 數與 Electron 版本數；五語不一致即報錯。"""
    sprints, versions = set(), set()
    for l in LOCALES:
        t = read(l + "changelog.html")
        # era-label 前綴隨語系（es 是 PISTA），只認「· 軌名」
        at = {m.group(1): m.start() for m in re.finditer(r'class="era-label">[^<]*· (\w+)<', t)}
        tauri = t[at["TAURI"]:at["ELECTRON"]]
        electron = t[at["ELECTRON"]:at.get("WEBSITE", len(t))]
        sprints.add(max(int(n) for n in re.findall(r'<span class="arc-date">Sprint (\d+)</span>', tauri)))
        versions.add(electron.count('<div class="arc-line">'))
    if len(sprints) != 1 or len(versions) != 1:
        sys.exit(f"五語更新日誌不一致：Sprint 數 {sorted(sprints)}、Electron 行數 {sorted(versions)}")
    return str(sprints.pop()), str(versions.pop())


def expand(facts):
    """facts → {key: (value, kind)}；日期展開成頁面上出現的四種寫法。"""
    def dates(prefix, iso):
        y, m, d = (int(x) for x in iso.split("-"))
        return {f"{prefix}@iso": (iso, "lit"),
                f"{prefix}@cjk": (f"{y} 年 {m} 月 {d} 日", "lit"),
                f"{prefix}@en": (f"{d} {MONTH_EN[m - 1]} {y}", "lit"),
                f"{prefix}@es": (f"{d} de {MONTH_ES[m - 1]} de {y}", "lit")}
    t, e = facts["tauri"], facts["electron"]
    sprints, versions = derive()
    out = {"tauri.version": (t["version"], "ver"),
           "tauri.download_mb": (t["download_mb"], "mb"),
           "tauri.install_mb": (t["install_mb"], "mb"),
           "tauri.sprints": (sprints, "sprints"),
           "electron.version": (e["version"], "ver"),
           "electron.short": (".".join(e["version"].split(".")[:2]), "ver"),
           "electron.download_mb": (e["download_mb"], "mb"),
           "electron.install_mb": (e["install_mb"], "mb"),
           "electron.versions": (versions, "versions")}
    out.update(dates("tauri.approved", t["approved"]))
    out.update(dates("electron.released", e["released"]))
    return out


def pattern(value, kind):
    v = re.escape(value)
    if kind == "ver":
        return rf"(?<![\d.]){v}(?![\d]|\.\d)"  # 句尾句號可以，接 .0 的完整版號不行
    if kind == "mb":
        return rf"(?<![\d.]){v}(?= ?MB)"
    if kind == "sprints":
        return rf"(?<![\d.–-]){v}(?=[ -]?(?:個の ?|個 ?|个 ?)?Sprints?\b)|(?<=Sprint ){v}(?![\d–-])"
    if kind == "versions":
        return rf"(?<![\d.]){v}(?= ?(?:個の ?|個 ?|个 ?)?(?:版本|versions|versiones|バージョン))"
    return rf"(?<!\d){v}(?!\d)"


def counts(values):
    reg = {}
    for f in FILES:
        lt = live_text(read(f))
        c = {k: len(re.findall(pattern(v, kind), lt)) for k, (v, kind) in values.items()}
        c = {k: n for k, n in c.items() if n}
        if c:
            reg[f] = c
    return reg


def save_registry(values, reg):
    data = {"_generated": "由 tools/release_facts.py --register／--fix 產生，勿手改",
            "values": {k: v for k, (v, _) in values.items()},
            "slots": reg}
    with open(REGISTRY, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def load_facts():
    with open(FACTS, encoding="utf-8") as f:
        return json.load(f)


def load_registry():
    with open(REGISTRY, encoding="utf-8") as f:
        return json.load(f)


def sweep(values, errors):
    """不靠登記表的廣掃：全站（archive 除外）凡是「現況型」寫法，值都要等於事實。"""
    cur = {k: v for k, (v, _) in values.items()}
    rules = [(r"download\.yoursvas\.app/VAS-([\d.]+)-arm64\.dmg", cur["electron.version"]),
             (r'"softwareVersion": "([^"]+)"', cur["tauri.version"]),
             (r"v(\d+\.\d+\.\d+) · Mac App Store", cur["tauri.version"]),
             (r"v(\d+\.\d+) · DMG", cur["electron.short"])]
    mb_ok = {cur[k] for k in values if k.endswith("_mb")} | MB_ALLOW
    for dirpath, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in (".git", "archive", "node_modules")]
        for name in files:
            if not name.endswith(".html"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, name), ROOT)
            lt = live_text(read(rel))
            for rx, want in rules:
                for got in re.findall(rx, lt):
                    if got != want:
                        errors.append(f"{rel}: 「{rx}」讀到 {got}，事實是 {want}")
            if rel in FILES:
                for got in re.findall(r"(?<![\d.])(\d+(?:\.\d+)?) ?MB", lt):
                    if got not in mb_ok:
                        errors.append(f"{rel}: 出現 {got} MB，不在 release-facts.json 也不在允許清單")


def check():
    values = expand(load_facts())
    reg = load_registry()
    errors = []
    stale = {k: (reg["values"].get(k), v) for k, (v, _) in values.items() if reg["values"].get(k) != v}
    for k, (old, new) in stale.items():
        errors.append(f"{k}：頁面登記的是 {old}，事實是 {new} —— 跑 python3 tools/release_facts.py --fix")
    if not stale:
        now = counts(values)
        for f in sorted(set(reg["slots"]) | set(now)):
            want, got = reg["slots"].get(f, {}), now.get(f, {})
            for k in sorted(set(want) | set(got)):
                if want.get(k, 0) != got.get(k, 0):
                    errors.append(f"{f}: {k}＝{values[k][0]} 應出現 {want.get(k, 0)} 處，實際 {got.get(k, 0)} 處")
    sweep(values, errors)
    if errors:
        print("發版數字不一致：")
        for e in errors:
            print("  ✗", e)
        sys.exit(1)
    print(f"發版數字一致（{len(reg['slots'])} 檔 · {sum(map(len, reg['slots'].values()))} 組欄位）")


def fix():
    values = expand(load_facts())
    reg = load_registry()
    old = reg["values"]
    changed = {k: (old[k], v, kind) for k, (v, kind) in values.items() if old.get(k) != v}
    if not changed:
        print("release-facts.json 與頁面登記一致，沒有要改的")
        return
    by_kind = {}
    for k, (o, _, kind) in changed.items():
        if (o, kind) in by_kind:
            sys.exit(f"中止：{k} 與 {by_kind[(o, kind)]} 的舊值都是 {o}，無法分辨該換哪一個")
        by_kind[(o, kind)] = k
    out = {}
    for f, slots in reg["slots"].items():
        text = read(f)
        spans = live_spans(text)
        new_text, pos = [], 0
        hits = {k: 0 for k in changed}
        for a, b in spans:
            new_text.append(text[pos:a])
            seg = text[a:b]
            for i, (k, (o, _, kind)) in enumerate(changed.items()):
                seg, n = re.subn(pattern(o, kind), f"\x01{i}\x02", seg)
                hits[k] += n
            new_text.append(seg)
            pos = b
        new_text.append(text[pos:])
        joined = "".join(new_text)
        for k, n in hits.items():
            if n != slots.get(k, 0):
                sys.exit(f"中止（未寫入任何檔）：{f} 的 {k}＝{changed[k][0]} 登記 {slots.get(k, 0)} 處，找到 {n} 處\n"
                         "  頁面被手改過：把它改回舊值再跑 --fix；或把全部頁面手動改好後跑 --register")
        for i, (k, (_, nv, _)) in enumerate(changed.items()):
            joined = joined.replace(f"\x01{i}\x02", nv)
        if joined != text:
            out[f] = joined
    for f, t in out.items():
        with open(os.path.join(ROOT, f), "w", encoding="utf-8") as fh:
            fh.write(t)
    save_registry(values, counts(values))
    for k, (o, nv, _) in changed.items():
        print(f"  {k}: {o} → {nv}")
    print(f"已改 {len(out)} 個檔；請接著跑 python3 tools/gen_sitemap.py 與檢查")


def register():
    values = expand(load_facts())
    reg = counts(values)
    save_registry(values, reg)
    for f, c in reg.items():
        print(f, c)


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    {"--fix": fix, "--register": register, "": check}.get(arg, lambda: sys.exit(__doc__))()
