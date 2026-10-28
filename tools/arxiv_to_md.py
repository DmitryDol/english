r"""Скачивает HTML-версию статьи arXiv и конвертирует её в Markdown.

Использование:
    uv run python tools/arxiv_to_md.py 2403.14403v2 articles/article2_original.md --acl-citations
    uv run python tools/arxiv_to_md.py saved_page.html articles/article2_original.md

Указывай arXiv-номер с версией (v1, v2, ...), чтобы текст совпадал с PDF.
--acl-citations нужен для статей в стиле ACL (ACL, NAACL, EMNLP): там \cite даёт
ссылку в скобках «(Brown et al., 2020)», а arXiv выводит её как «Brown et al. (2020)».
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


def parenthesize_citations(html: str) -> str:
    # В стиле ACL \cite — ссылка в скобках: «Brown et al. (2020); OpenAI (2023)» → «(Brown et al., 2020; OpenAI, 2023)».
    def fix_link(match: re.Match) -> str:
        return re.sub(r"(\S) \(([^()]+)\)(</a>)$", r"\1, \2\3", match.group(0))

    def replace(match: re.Match) -> str:
        body = re.sub(r"<a\b[^>]*>[^<]*</a>", fix_link, match.group(2))
        return f"{match.group(1)}({body})</cite>"

    return re.sub(r'(<cite class="ltx_cite ltx_citemacro_cite">)(.*?)</cite>', replace, html, flags=re.S)


def main() -> None:
    args = [arg for arg in sys.argv[1:] if arg != "--acl-citations"]
    if len(args) != 2:
        sys.exit(__doc__)
    source, output = args[0], pathlib.Path(args[1])
    article = unwrap_svg_text(extract_article(load_html(source)))
    if "--acl-citations" in sys.argv:
        article = parenthesize_citations(article)
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
    # Неразрывные и широкие пробелы («et al.» и др.) заменяем обычными, иначе цитату не найти поиском.
    markdown = re.sub("[      ]", " ", markdown)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(markdown, encoding="utf-8")
    print(f"{output}: {len(''.join(markdown.split()))} chars without spaces")


if __name__ == "__main__":
    main()
