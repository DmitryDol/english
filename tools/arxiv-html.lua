-- Pandoc-фильтр для HTML-статей arXiv (LaTeXML). Подключается из tools/arxiv_to_md.py.
-- Работает в два прохода: сначала сноски, потом очистка разметки (иначе сноски теряют структуру).

local function is_blank(item)
  return item.t == 'Space' or item.t == 'SoftBreak' or item.t == 'LineBreak'
end

-- Проход 1: сноски LaTeXML превращаем в обычные сноски Markdown.
local notes = {
  Span = function(el)
    if not el.classes:includes('ltx_note') then
      return nil
    end
    local content
    el:walk({
      Span = function(s)
        if not content and s.classes:includes('ltx_note_content') then
          content = s.content
        end
      end,
    })
    if not content then
      return nil
    end
    local text = pandoc.Inlines({})
    for _, item in ipairs(content) do
      local is_mark = item.t == 'Superscript'
        or (item.t == 'Span' and (item.classes:includes('ltx_tag_note') or item.classes:includes('ltx_note_type')))
      if not is_mark and not (#text == 0 and is_blank(item)) then
        text:insert(item)
      end
    end
    return pandoc.Note({ pandoc.Plain(text) })
  end,
}

-- Проход 2: снимаем HTML-обёртки, чтобы в Markdown остался только текст.
local cleanup = {
  -- Ссылки внутри страницы (на литературу, рисунки, разделы) и пустые mailto заменяем их текстом.
  -- У внешних ссылок убираем классы, иначе GFM выводит их HTML-тегом <a>.
  Link = function(el)
    if el.target:sub(1, 1) == '#' or el.target == 'mailto:' then
      return el.content
    end
    el.attr = pandoc.Attr()
    return el
  end,

  -- Картинки локально недоступны, подписи к рисункам остаются в тексте.
  Image = function()
    return {}
  end,

  -- Маркеры «•» у пунктов списков и пустые якоря удаляем, остальные <span> раскрываем.
  Span = function(el)
    if el.classes:includes('ltx_tag_item') then
      return {}
    end
    return el.content
  end,

  -- После удаления маркера «•» у пункта списка остаётся пустая строка: убираем её.
  Plain = function(el)
    for _, item in ipairs(el.content) do
      if not is_blank(item) then
        return nil
      end
    end
    return {}
  end,

  Div = function(el)
    return el.content
  end,

  -- Рисунок или таблицу с подписью разворачиваем в обычные блоки; подпись таблицы ставим над ней.
  Figure = function(el)
    local blocks = pandoc.Blocks({})
    if el.classes:includes('ltx_table') then
      blocks:extend(el.caption.long)
      blocks:extend(el.content)
    else
      blocks:extend(el.content)
      blocks:extend(el.caption.long)
    end
    return blocks
  end,
}

return { notes, cleanup }
