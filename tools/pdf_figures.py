"""Вырезает рисунки из PDF статьи и вставляет их в Markdown-версию.

Использование (сначала tools/arxiv_to_md.py, потом этот скрипт):
    uv run --with pymupdf python tools/pdf_figures.py articles/article2_original.pdf articles/article2_original.md

Для каждой подписи «Figure N:» в PDF берёт область над ней, сохраняет её в
articles/article2_figures/figureN.png и вставляет картинку перед абзацем
«Figure N: ...» в Markdown. Границы рисунка ищутся эвристически, поэтому
каждую вырезку просмотри глазами.
"""

import pathlib
import re
import sys

import pymupdf

CAPTION = re.compile(r"\s*(Figure|Table)\s+\d+\s*:")
FIGURE_CAPTION = re.compile(r"\s*Figure\s+(\d+)\s*:")
GAP = 14  # больший вертикальный зазор между элементами считается границей рисунка
CAPTION_GAP = 24  # допустимый зазор между рисунком и его подписью
BODY_FONT = 9.5  # строки крупнее и шире 60% подписи считаются основным текстом


def page_items(page: pymupdf.Page) -> list[tuple[pymupdf.Rect, str, str, float]]:
    items = []
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            text = "".join(span["text"] for span in line["spans"]).strip()
            if text:
                size = max(span["size"] for span in line["spans"])
                items.append((pymupdf.Rect(line["bbox"]), "text", text, size))
    for drawing in page.get_drawings():
        # Линии таблиц имеют нулевую толщину, а пустые прямоугольники PyMuPDF не объединяет.
        items.append((drawing["rect"] + (-0.5, -0.5, 0.5, 0.5), "draw", "", 0.0))
    for image in page.get_image_info():
        items.append((pymupdf.Rect(image["bbox"]), "image", "", 0.0))
    return items


def figure_clip(page: pymupdf.Page, caption: pymupdf.Rect, items) -> pymupdf.Rect | None:
    def above_caption(rect: pymupdf.Rect) -> bool:
        return rect.x1 > caption.x0 - 2 and rect.x0 < caption.x1 + 2 and rect.y1 <= caption.y0 + 1 and not rect.intersects(caption)

    candidates = sorted((item for item in items if above_caption(item[0])), key=lambda item: item[0].y1, reverse=True)
    top, taken, stopped_at_table = caption.y0, [], False
    # Поднимаемся от подписи вверх, пока элементы идут без больших разрывов.
    for rect, kind, text, size in candidates:
        if rect.y1 < top - (GAP if taken else CAPTION_GAP):
            break
        if kind == "text" and (CAPTION.match(text) or (size >= BODY_FONT and rect.width >= 0.6 * caption.width)):
            stopped_at_table = text.startswith("Table")
            break
        taken.append((rect, kind))
        top = min(top, rect.y0)
    if stopped_at_table:
        # Над рисунком стоит таблица: рисунок начинается под её нижней линией.
        rules = [rect for rect, kind in taken if kind == "draw" and rect.height < 1.5 and rect.width >= 0.8 * caption.width]
        if rules:
            bottom = max(rule.y1 for rule in rules)
            taken = [(rect, kind) for rect, kind in taken if rect.y0 > bottom]
    if not taken:
        return None
    region = pymupdf.Rect(taken[0][0])
    for rect, _ in taken[1:]:
        region |= rect
    clip = pymupdf.Rect(min(region.x0, caption.x0) - 2, region.y0 - 2, max(region.x1, caption.x1) + 2, caption.y0 - 1)
    return clip & page.rect


def insert_images(markdown: str, figures: dict[int, str]) -> str:
    lines = markdown.split("\n")
    result = []
    for line in lines:
        match = FIGURE_CAPTION.match(line)
        if match and int(match.group(1)) in figures:
            image = f"![Figure {match.group(1)}]({figures[int(match.group(1))]})"
            previous = next((prev for prev in reversed(result) if prev.strip()), "")
            if previous != image:
                result += [image, ""]
        result.append(line)
    return "\n".join(result)


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    pdf_path, md_path = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    figures_dir = md_path.with_name(md_path.stem.removesuffix("_original") + "_figures")
    figures_dir.mkdir(exist_ok=True)
    figures = {}
    for page_number, page in enumerate(pymupdf.open(pdf_path), start=1):
        items = page_items(page)
        for block in page.get_text("blocks"):
            match = FIGURE_CAPTION.match(block[4])
            if not match:
                continue
            number = int(match.group(1))
            clip = figure_clip(page, pymupdf.Rect(block[:4]), items)
            if clip is None:
                print(f"Figure {number} (page {page_number}): area above the caption not found, crop it manually")
                continue
            image_path = figures_dir / f"figure{number}.png"
            page.get_pixmap(clip=clip, dpi=200).save(image_path)
            figures[number] = f"{figures_dir.name}/{image_path.name}"
            print(f"Figure {number} (page {page_number}) -> {image_path}")
    markdown = md_path.read_text(encoding="utf-8")
    md_path.write_text(insert_images(markdown, figures), encoding="utf-8")
    missing = sorted(set(figures) - {int(n) for n in re.findall(r"!\[Figure (\d+)\]", md_path.read_text(encoding="utf-8"))})
    if missing:
        print(f"No caption line in {md_path} for figures {missing}: insert them manually")


if __name__ == "__main__":
    main()
