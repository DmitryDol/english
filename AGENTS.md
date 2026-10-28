# AGENTS.md — Руководство для AI-агентов

Документ определяет контекст, правила работы, требования к качеству и алгоритмы выполнения задач для интеллектуальных агентов (Antigravity, Cursor, Copilot, Claude Code и др.) в рамках данного репозитория.

---

## 1. Контекст проекта

- **Предмет:** Иностранный язык в профессиональной деятельности (English for Professional Purposes).
- **Учебное заведение:** Самарский университет (СГАУ), магистратура.
- **Студент:** Должиков Д. П.
- **Профиль подготовки:** Информационные технологии, программная инженерия, искусственный интеллект, распределенные и граничные вычисления (Edge AI / IoT).
- **Итоговый контроль:** Зачет.

### Ключевые файлы:
- [English for Professional Purposes.pdf](file:///C:/projects/ssau/english/English%20for%20Professional%20Purposes.pdf) — оригинальный документ с методическими указаниями и заданиями.
- [english_for_professional_purposes.md](file:///C:/projects/ssau/english/english_for_professional_purposes.md) — оцифрованный текст методички с шаблонами клише и исходным текстом предложенной статьи.
- [README.md](file:///C:/projects/ssau/english/README.md) — главный семестровый трекер задач и чек-лист.
- [ДолжиковДП_Англ1.md](file:///C:/projects/ssau/english/ДолжиковДП_Англ1.md) — исходный текст работы по предложенной статье.
- [ДолжиковДП_Англ1.docx](file:///C:/projects/ssau/english/ДолжиковДП_Англ1.docx) — скомпилированный файл для сдачи преподавателю.

---

## 2. Текущее состояние и невыполненные задачи

### Что уже сделано:
1. **Предложенная статья (`ДолжиковДП_Англ1.md` / `ДолжиковДП_Англ1.docx`) полностью завершена (100%):**
   - Выполнен полный академический перевод статьи (*Chen et al., 2025: Latency reduction in IoT networks through edge AI deployment*) на русский язык.
   - Составлен словарь из 30 терминов с переводом и оригинальными цитатами.
   - Выполнен **TASK 1** (Step 1: выходные данные; Step 2: жанр и аудитория; Step 3: детальные ответы на вопросы a–e).
   - Выполнен **TASK 2** (Аннотация на английском языке с использованием регламентированных клише).
   - Выполнен **TASK 3** (Сценарий устной презентации на ~750 слов / 5–7 минут с таймингом и речевыми оборотами методички).
   - Скомпилирован итоговый файл `ДолжиковДП_Англ1.docx` через Pandoc.

### Что осталось выполнить (Чек-лист задач):

> [!NOTE]
> Основной интерактивный чек-лист ведется в [README.md](file:///C:/projects/ssau/english/README.md). Ниже приведена сводка задач, ожидающих выполнения.

1. **Предложенная статья (`ДолжиковДП_Англ1.md`):**
   - [x] **TASK 1, TASK 2, TASK 3 и экспорт в DOCX завершены.**

2. **Статья по специальности №1 (`ДолжиковДП_Англ2.md`):**
   - Выбрана статья: Jeong et al. (2024), *Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity*, NAACL 2024, pp. 7036–7050 — [arXiv:2403.14403](https://arxiv.org/abs/2403.14403).
   - Оригинал: `articles/article2_original.pdf` и `.md`; основной текст — 41 556 знаков без пробелов.
   - [x] Выбор профильной англоязычной статьи ($\ge 10\,000$ знаков без пробелов).
   - [ ] Полный перевод статьи на русский язык.
   - [ ] Список из не менее 30 терминов/выражений с контекстом.
   - [ ] TASK 1 (Step 1, Step 2, Step 3 a–e).
   - [ ] TASK 2 (Аннотация с клише).
   - [ ] TASK 3 (Скрипт доклада на 5–7 мин).
   - [ ] Компиляция в `ДолжиковДП_Англ2.docx`.

3. **Статья по специальности №2 (`ДолжиковДП_Англ3.md`):**
   - Выбрана статья: Asai et al. (2024), *Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection*, ICLR 2024 — [arXiv:2310.11511](https://arxiv.org/abs/2310.11511).
   - Оригинал: `articles/article3_original.pdf` и `.md`; основной текст — 38 648 знаков без пробелов.
   - [ ] Выбор статьи ($\ge 10\,000$ знаков без пробелов), перевод, 30 терминов, TASK 1, TASK 2, TASK 3, компиляция в `ДолжиковДП_Англ3.docx`.

4. **Статья по специальности №3 (`ДолжиковДП_Англ4.md`):**
   - Выбрана статья: Yan et al. (2024), *Corrective Retrieval Augmented Generation*, препринт [arXiv:2401.15884](https://arxiv.org/abs/2401.15884) (рецензируемая публикация не найдена).
   - Оригинал: `articles/article4_original.pdf` и `.md`; основной текст — 33 604 знака без пробелов.
   - [ ] Выбор статьи ($\ge 10\,000$ знаков без пробелов), перевод, 30 терминов, TASK 1, TASK 2, TASK 3, компиляция в `ДолжиковДП_Англ4.docx`.

---

## 3. Стандарты качества и правила генерации для Агента

При выполнении заданий агент обязан следовать установленным стандартам:

### А. Правила перевода на русский язык
- Стиль: строгий научно-технический стиль русской академической литературы.
- Избегать калькирования английских синтаксических конструкций; адаптировать порядок слов под нормы русского научного языка.
- Терминология должна быть консистентной на протяжении всего документа (например: *inference* — «инференс / логический вывод нейросети», *edge computing* — «периферийные вычисления», *testbed* — «испытательный стенд / экспериментальная платформа», *quantization* — «квантование», *trade-off* — «компромиссное решение / компромисс»).
- Сохранять формулы, математические обозначения ($p < 0.05$, $SD = 4.1$, проценты, размерности).

### Б. Требования к словарю (30 терминов)
- Ровно 30 или более пунктов.
- Формат каждого пункта:
  ```markdown
  N. **English Term**: русский эквивалент (*"Контекстная цитата из текста статьи"*).
  ```
- Выбирать специфические профессиональные термины, коллокации и устойчивые академические обороты (не общеупотребительные простые слова).

### В. Требования к TASK 1
- **Step 1 (Publication Details):** Journal name, Volume, Issue, Year, Pages, Article Title, Authors (Surnames and initials).
- **Step 2 (Genre, Audience, Purpose):**
  - Определение типа статьи (Research article, Review article или Theoretical paper) с обоснованием.
  - Определение целевой аудитории (уровень подготовки, специализация, международная аудитория).
  - Ответы на 3 вопроса по заголовку: Why has it been written? What is the object? What does it review / investigate?
- **Step 3 (Detailed Study):**
  - Четкие развернутые ответы на английском языке на вопросы **a** (Background & Aim), **b** (Methods/What was done), **c** (Findings), **d** (Meaning of Results), **e** (References to literature).

### Г. Требования к TASK 2 (Аннотация / Annotation)
- Пишется на **английском языке**.
- Объем: 200–350 слов.
- Обязательно используются стандартизированные вводные фразы из [english_for_professional_purposes.md](file:///C:/projects/ssau/english/english_for_professional_purposes.md#L90-L133):
  1. *Вступление:* `The article I'm going to give a review of is taken from...`, `The headline of the article is...`, `The author of the article is...` / `It is written by...`
  2. *Тема и структура:* `The topic of the article is...`, `The key issue of the article is...`, `The article under discussion is devoted to the problem of...`, `The article under discussion may be divided into several logically connected parts which are...`
  3. *Краткое содержание и выводы:* `The author starts by telling the reader that...`, `At the beginning of the article the author describes...`, `Then / After that the author touches upon / explains / points out...`, `In conclusion the author says / makes it clear that...`, `The author concludes by saying that...`

### Д. Требования к TASK 3 (Устная презентация / Oral Presentation)
- Пишется на **английском языке**.
- Рассчитана на **5–7 минут непрерывной устной речи** (~650–850 слов при темпе 120–140 слов/мин).
- Должна содержать явные тайминговые отметки и четкое деление на разделы:
  1. **1. Opening (~1.0–1.5 мин):**
     - Greeting & gratitude (*"Good afternoon, ladies and gentlemen...", "Thank you all for coming today..."*).
     - Introduction of speaker & purpose (*"My name is Dmitry Dolzhikov. Today I am going to talk about..."*).
     - Route map (*"To start with, I'll describe... Then I'll mention... Next, I'll discuss... Finally, I'll summarize..."*).
  2. **2. Body (~3.5–4.5 мин):**
     - Плавные связки (*"Let's begin by...", "Well, I've told you about...", "Now we'll move on to...", "Let me turn now to..."*).
     - Анализ фактов и цифр (*"Where does that lead us?", "Let's consider this in more detail", "What does this mean for...?"*).
     - Примеры и иллюстрации (*"To give you an example...", "A good example of this is..."*).
     - **Без интерактивных отступлений:** текст должен быть чистым связным монологом без моделирования вопросов из зала или ремарок вроде `*(Noticing a question...)*`.
  3. **3. Closing (~1.0 мин):**
     - Краткое резюме (*"In conclusion, let me sum up the main findings..."*).
     - Практический вывод / мысль на будущее (Wisdom / Action / Emotion: *"If you take just one thing from this talk, take this..."*).
     - Благодарность (*"Many thanks for your attention"*).
     - Переход к Q&A (*"Now I'll be glad to answer any questions you may have"*).

---

## 4. Рабочие процессы и инструменты (Tooling)

### Проверка объема статьи ($\ge 10\,000$ знаков без пробелов)
Для подсчета количества символов в тексте статьи без пробелов используйте команду Python:
```powershell
python -c "import pathlib; text = pathlib.Path('article_text.txt').read_text(encoding='utf-8'); non_space = len(''.join(text.split())); print(f'Chars without spaces: {non_space}')"
```

### Сборка DOCX через Pandoc
Все отчеты оформляются в Markdown и компилируются в DOCX:
```powershell
pandoc ДолжиковДП_Англ1.md -o ДолжиковДП_Англ1.docx
pandoc ДолжиковДП_Англ2.md -o ДолжиковДП_Англ2.docx
pandoc ДолжиковДП_Англ3.md -o ДолжиковДП_Англ3.docx
pandoc ДолжиковДП_Англ4.md -o ДолжиковДП_Англ4.docx
```

### Соглашение об именовании файлов
- `ДолжиковДП_Англ1.md` / `.docx` — Предложенная статья (Sample Article).
- `ДолжиковДП_Англ2.md` / `.docx` — Статья по специальности №1.
- `ДолжиковДП_Англ3.md` / `.docx` — Статья по специальности №2.
- `ДолжиковДП_Англ4.md` / `.docx` — Статья по специальности №3.
- При сохранении исходных текстов статей на английском языке рекомендуется складывать их в каталог `articles/` (например, `articles/article1_original.txt` или `.pdf`).
- Статьи с arXiv конвертируются в Markdown скриптом `tools/arxiv_to_md.py` (HTML-версия arXiv → pandoc). Для PDF в две колонки pdfplumber не подходит: склеивает слова и перемешивает строки колонок.
