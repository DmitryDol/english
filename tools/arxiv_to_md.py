"""Скачивает HTML-версию статьи arXiv и конвертирует её в Markdown.

Использование:
    uv run python tools/arxiv_to_md.py 2403.14403v2 articles/article2_original.md
    uv run python tools/arxiv_to_md.py saved_page.html articles/article2_original.md

Указывай arXiv-номер с версией (v1, v2, ...), чтобы текст совпадал с PDF.
Нужен pandoc в PATH.
"""

import pathlib
import re
import subprocess
import sys
import urllib.request

LUA_FILTER = pathlib.Path(__file__).with_name("arxiv-html.lua")


def load_html(source: str) -> str:
    path = pathlib.Path(source)
    if path.suffix == ".html" and path.exists():
        return path.read_text(encoding="utf-8")
    with urllib.request.urlopen(f"https://arxiv.org/html/{source}") as response:
        return response.read().decode("utf-8")


def extract_article(html: str) -> str:
    # Pandoc отбрасывает тег <article>, поэтому меню и подвал arXiv отрезаем до конвертации.
    start = html.find("<article")
    end = html.rfind("</article>")
    if start == -1 or end == -1:
        sys.exit("На странице нет блока <article>: похоже, arXiv не смог собрать HTML для этой статьи.")
    return html[start : end + len("</article>")]


def unwrap_svg_text(html: str) -> str:
    # LaTeXML рисует часть текста как SVG с <foreignObject> внутри (токены Self-RAG, рамки с промптами),
    # а pandoc выбрасывает SVG целиком. Оставляем только текст из <foreignObject>.
    def replace(match: re.Match) -> str:
        parts = re.findall(r"<foreignObject\b[^>]*>(.*?)</foreignObject>", match.group(0), re.S)
        if not parts:
            return match.group(0)
        inner = " ".join(parts)
        tag = "div" if re.search(r"<(div|p)\b", inner) else "span"
        return f"<{tag}>{inner}</{tag}>"

    return re.sub(r"<svg\b.*?</svg>", replace, html, flags=re.S)


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    source, output = sys.argv[1], pathlib.Path(sys.argv[2])
    article = unwrap_svg_text(extract_article(load_html(source)))
    markdown = subprocess.run(
        # Таблицы с объединёнными ячейками в Markdown не помещаются: GFM оставляет их HTML-таблицами.
        ["pandoc", "-f", "html", "-t", "gfm", "--wrap=none", f"--lua-filter={LUA_FILTER}"],
        input=article,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    ).stdout
    # Невидимое умножение из MathML pandoc записывает как \hspace{0pt}: в формулах это только шум.
    markdown = markdown.replace("\\hspace{0pt}", "")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(markdown, encoding="utf-8")
    print(f"{output}: {len(''.join(markdown.split()))} chars without spaces")


if __name__ == "__main__":
    main()
