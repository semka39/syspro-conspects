#!/usr/bin/env python3
"""
md2pdf.py — рекурсивно конвертирует .md в PDF (с формулами KaTeX) через установленный Chrome/Edge.

Из текущей папки берутся все .md в подпапках; файлы прямо в корне и README (любой регистр)
игнорируются. PDF всегда перезаписывается и кладётся рядом с исходным .md.

Зависимости:  pip install markdown-it-py mdit-py-plugins
              + установленный Chrome / Chromium / Edge (можно указать путь в переменной CHROME)

Запуск:       python md2pdf.py            (KaTeX берётся с CDN, нужен интернет)
              python md2pdf.py --offline  (KaTeX из локального `npm install katex`)
"""

from __future__ import annotations

import html
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from markdown_it import MarkdownIt
from mdit_py_plugins.dollarmath import dollarmath_plugin
from mdit_py_plugins.footnote import footnote_plugin
from mdit_py_plugins.tasklists import tasklists_plugin

KATEX_CDN = "https://cdn.jsdelivr.net/npm/katex@0.16.11/dist"
SKIP_DIRS = {".git", ".hg", ".svn", "node_modules", "venv", ".venv", "env", "__pycache__"}


# ---------------------------------------------------------------- Markdown -> HTML

def build_markdown() -> MarkdownIt:
    md = (
        MarkdownIt("commonmark", {"html": True, "breaks": True})
        .enable(["table", "strikethrough"])
        .use(dollarmath_plugin, allow_space=True, allow_digits=True, double_inline=True)
        .use(footnote_plugin)
        .use(tasklists_plugin)
    )
    inline = lambda self, t, i, o, e: f'<span class="math-inline">{html.escape(t[i].content)}</span>'
    block = lambda self, t, i, o, e: f'<div class="math-block">{html.escape(t[i].content)}</div>\n'
    md.add_render_rule("math_inline", inline)
    for rule in ("math_inline_double", "math_block", "math_block_label"):
        md.add_render_rule(rule, block)
    return md


CSS = r"""
* { box-sizing: border-box; }
html { font-size: 11.5pt; }
body { font-family: "Noto Serif","PT Serif",Georgia,"Times New Roman","DejaVu Serif",serif;
       line-height: 1.55; color: #1a1a1a; margin: 0; overflow-wrap: anywhere;
       -webkit-print-color-adjust: exact; print-color-adjust: exact; }
h1,h2,h3,h4,h5,h6 { font-family: "Noto Sans","PT Sans",Arial,"DejaVu Sans",sans-serif;
       line-height: 1.25; margin: 1.4em 0 .5em; break-after: avoid; }
h1 { font-size: 1.9rem; border-bottom: 2px solid #333; padding-bottom: .25em; margin-top: 0; }
h2 { font-size: 1.5rem; border-bottom: 1px solid #bbb; padding-bottom: .2em; }
h3 { font-size: 1.25rem; } h4 { font-size: 1.1rem; }
p { margin: .55em 0; text-align: justify; hyphens: auto; }
ul, ol { padding-left: 1.6em; margin: .4em 0; } li { margin: .25em 0; } li > p { margin: .25em 0; }
a { color: #0b57d0; text-decoration: none; }
img { max-width: 100%; height: auto; break-inside: avoid; }
blockquote { margin: .8em 0; padding: .2em 1em; border-left: 4px solid #c8c8c8;
             color: #444; background: #f7f7f7; break-inside: avoid; }
hr { border: 0; border-top: 1px solid #bbb; margin: 1.4em 0; }
table { border-collapse: collapse; margin: .8em 0; max-width: 100%; break-inside: avoid; }
th, td { border: 1px solid #aaa; padding: .3em .6em; } th { background: #eee; }
code, pre { font-family: "DejaVu Sans Mono",Consolas,monospace; font-size: .88em; }
code { background: #f1f1f1; padding: .08em .3em; border-radius: 3px; }
pre { background: #f6f8fa; padding: .7em .9em; border-radius: 5px; white-space: pre-wrap;
      word-break: break-word; break-inside: avoid; }
pre code { background: none; padding: 0; }
.math-block { margin: .8em 0; text-align: center; break-inside: avoid; }
.math-block .katex-display { margin: 0; }
.katex { font-size: 1.08em; }
.katex-display > .katex { white-space: normal; }
.footnotes { font-size: .9em; }
.task-list-item { list-style: none; margin-left: -1.2em; }
.math-error { color: #b00020; font-family: monospace; }
@page { size: A4; margin: 20mm 18mm;
        @bottom-center { content: counter(page) " / " counter(pages);
                         font: 9px sans-serif; color: #777; } }
"""

PAGE = """<!DOCTYPE html>
<html lang="ru"><head><meta charset="utf-8"><title>{title}</title>
<base href="{base}">
<link rel="stylesheet" href="{katex}/katex.min.css">
<style>{css}</style>
<script src="{katex}/katex.min.js"></script>
</head><body>
{body}
<script>
const macros = {{"\\\\R":"\\\\mathbb{{R}}","\\\\C":"\\\\mathbb{{C}}","\\\\N":"\\\\mathbb{{N}}",
                "\\\\Z":"\\\\mathbb{{Z}}","\\\\Q":"\\\\mathbb{{Q}}"}};
function render(el, display) {{
  try {{ katex.render(el.textContent, el, {{displayMode: display, throwOnError: false,
                                          strict: false, trust: true, macros}}); }}
  catch (e) {{ el.classList.add("math-error"); }}
}}
document.querySelectorAll(".math-inline").forEach(e => render(e, false));
document.querySelectorAll(".math-block").forEach(e => render(e, true));
</script>
</body></html>
"""


# ---------------------------------------------------------------- поиск файлов

def find_markdown_files(root: Path) -> list[Path]:
    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS and not d.startswith("."))
        if Path(dirpath) == root:
            continue  # файлы в корне пропускаем, но идём вглубь
        for name in sorted(filenames):
            p = Path(name)
            if p.suffix.lower() == ".md" and p.stem.lower() != "readme":
                found.append(Path(dirpath) / name)
    return found


# ---------------------------------------------------------------- браузер

def find_browser() -> str:
    env = os.environ.get("CHROME")
    if env and Path(env).exists():
        return env
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser",
                 "chrome", "microsoft-edge", "microsoft-edge-stable", "msedge"):
        if path := shutil.which(name):
            return path
    pf = [os.environ.get(k) for k in ("PROGRAMFILES", "PROGRAMFILES(X86)", "LOCALAPPDATA")]
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ]
    for base in filter(None, pf):
        candidates += [
            f"{base}/Google/Chrome/Application/chrome.exe",
            f"{base}/Microsoft/Edge/Application/msedge.exe",
            f"{base}/Chromium/Application/chrome.exe",
        ]
    for c in candidates:
        if Path(c).exists():
            return c
    sys.exit("Не найден Chrome/Chromium/Edge. Установите браузер или задайте путь в переменной CHROME.")


def resolve_katex(offline: bool) -> str:
    if not offline:
        return KATEX_CDN
    cands = [Path.cwd() / "node_modules/katex/dist", Path(__file__).parent / "node_modules/katex/dist"]
    cands += [p / "node_modules/katex/dist" for p in Path.cwd().parents]
    if shutil.which("npm"):
        root = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
        if root:
            cands.append(Path(root) / "katex/dist")
    for c in cands:
        if (c / "katex.min.js").exists():
            return c.resolve().as_uri()
    sys.exit("Локальный KaTeX не найден. Выполните: npm install katex")


def print_pdf(browser: str, html_file: Path, dst: Path, profile: Path) -> None:
    cmd = [
        browser, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
        "--allow-file-access-from-files", "--virtual-time-budget=20000",
        f"--user-data-dir={profile}", f"--print-to-pdf={dst}", html_file.as_uri(),
    ]
    if hasattr(os, "geteuid") and os.geteuid() == 0:
        cmd.insert(1, "--no-sandbox")
    if dst.exists():
        dst.unlink()
    subprocess.run(cmd, capture_output=True, timeout=180)
    if not dst.exists() or dst.stat().st_size == 0:
        raise RuntimeError("браузер не создал PDF")


# ---------------------------------------------------------------- main

def main() -> int:
    offline = "--offline" in sys.argv[1:]
    root = Path.cwd()
    files = find_markdown_files(root)
    if not files:
        print("Подходящих .md файлов не найдено.")
        return 0

    browser, katex, md = find_browser(), resolve_katex(offline), build_markdown()
    ok = failed = 0
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for i, src in enumerate(files, 1):
            rel = src.relative_to(root)
            try:
                page = PAGE.format(
                    title=html.escape(src.stem), base=src.parent.resolve().as_uri() + "/",
                    katex=katex, css=CSS, body=md.render(src.read_text(encoding="utf-8-sig")),
                )
                (tmp / "page.html").write_text(page, encoding="utf-8")
                print_pdf(browser, tmp / "page.html", src.with_suffix(".pdf"), tmp / "profile")
                print(f"[{i}/{len(files)}] ✓ {rel}")
                ok += 1
            except Exception as e:  # noqa: BLE001
                print(f"[{i}/{len(files)}] ✗ {rel}: {e}", file=sys.stderr)
                failed += 1
    print(f"\nГотово: {ok} ок, {failed} с ошибкой.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())