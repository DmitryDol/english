"""Выделяет термины словаря полужирным в оригинале статьи и проверяет цитаты.

Использование:
    uv run python tools/mark_terms.py ДолжиковДП_Англ2.md articles/article2_original.md

Берёт из словаря строки вида «N. **Term**: перевод (*"цитата"*).», находит каждую
цитату в оригинале и выделяет термин полужирным внутри неё (методичка требует
отметить термины в тексте статьи). Повторный запуск ничего не дублирует.
Если цитаты нет в оригинале дословно или в ней нет термина, скрипт сообщает
об этом и завершается с ошибкой, ничего не меняя.
"""

import pathlib
import re
import sys

GLOSSARY_ITEM = re.compile(r'^\d+\.\s+\*\*(?P<term>.+?)\*\*:.*\(\*"(?P<quote>.+)"\*\)\.?\s*$')


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    work_path, original_path = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    items = [m.groupdict() for line in work_path.read_text(encoding="utf-8").splitlines() if (m := GLOSSARY_ITEM.match(line))]
    if not items:
        sys.exit(f"{work_path}: glossary items not found")
    text = original_path.read_text(encoding="utf-8")
    errors, marked = [], 0
    for item in items:
        term, quote = item["term"], item["quote"]
        found = re.search(re.escape(term), quote, re.IGNORECASE)
        if not found:
            errors.append(f"term {term!r} is not in its quote {quote!r}")
            continue
        bolded = f"{quote[:found.start()]}**{found.group(0)}**{quote[found.end():]}"
        if bolded in text:
            continue
        if quote not in text:
            errors.append(f"quote for {term!r} is not in the original: {quote!r}")
            continue
        text = text.replace(quote, bolded, 1)
        marked += 1
    if errors:
        sys.exit("\n".join(errors))
    original_path.write_text(text, encoding="utf-8")
    print(f"{len(items)} glossary items, {marked} newly marked in {original_path}")


if __name__ == "__main__":
    main()
