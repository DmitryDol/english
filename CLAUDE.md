# CLAUDE.md

Инструкции для Claude Code в этом репозитории. Это не программный, а учебный проект: здесь готовятся письменные работы по дисциплине «Иностранный язык в профессиональной деятельности» (English for Professional Purposes). Результат работы — Markdown-файлы `ДолжиковДП_АнглN.md` и собранные из них через Pandoc файлы `.docx`, которые сдаются преподавателю.

С пользователем общайся на русском языке.

## Контекст

- Вуз: Самарский университет (СГАУ), магистратура. Итоговый контроль — зачёт.
- Студент: Должиков Д. П. (в англоязычных текстах — Dmitry Dolzhikov).
- Профиль подготовки: информационные технологии, программная инженерия, искусственный интеллект, распределённые и граничные вычисления (Edge AI / IoT).
- Для зачёта нужно 4 комплекта: предложенная статья и 3 статьи по специальности, каждая объёмом не меньше 10 000 знаков без пробелов.
- Комплект по каждой статье: полный перевод на русский, словарь из 30+ терминов, TASK 1 (анализ структуры), TASK 2 (аннотация), TASK 3 (устная презентация на 5–7 минут).

## Карта репозитория

- `English for Professional Purposes.pdf` — оригинал методички, первоисточник требований.
- `english_for_professional_purposes.md` — оцифрованная методичка. Нужные фрагменты читай по строкам, а не целиком:
  - строки 17–88: TASK 1 (структура IMRaD, Step 1–3);
  - строки 90–133: TASK 2 (клише аннотации);
  - строки 135–261: TASK 3 (фразы для Opening / Body / Closing);
  - строки 263–297: текст предложенной статьи Chen et al. (2025).
- `README.md` — семестровый трекер с чек-листами, главный источник информации о прогрессе.
- `AGENTS.md` — те же правила для других агентов (Cursor, Copilot и др.).
- `ДолжиковДП_Англ1.md` / `.docx` — предложенная статья, выполнена полностью. Образец структуры и стиля.
- `ДолжиковДП_Англ1_humanized.md` / `.docx` — вариант с более естественным языком в TASK 2 и TASK 3 (см. раздел «Humanized-версии»).
- `ДолжиковДП_Англ2.md` … `ДолжиковДП_Англ4.md` — статьи по специальности №1–3, пока не созданы.
- `articles/` — оригиналы выбранных статей (`articleN_original.pdf` и извлечённый текст `articleN_original.txt`). Каталога пока нет: создай его, когда возьмёшься за первую статью.
- `pyproject.toml`, `uv.lock`, `.python-version` — окружение uv на Python 3.14. Единственная зависимость — `pdfplumber` для извлечения текста из PDF. `src/english/` пока заглушка.

Ссылки вида `file:///C:/projects/ssau/english/...` в `AGENTS.md` и `README.md` — локальные пути Windows. В новых текстах ссылайся на файлы относительными путями.

## Текущее состояние

- Англ1 (предложенная статья): готово всё — перевод, 30 терминов, TASK 1–3, DOCX, а также humanized-версия.
- Англ2, Англ3, Англ4: не начаты.

Когда этап готов, отметь чек-боксы в `README.md`, обнови сводку в разделе 2 файла `AGENTS.md` и этот раздел, чтобы файлы не расходились.

## Структура файла `ДолжиковДП_АнглN.md`

Повторяй структуру `ДолжиковДП_Англ1.md`. В новых файлах не ставь `**` внутри заголовков.

```markdown
### Перевод статьи
**<Название статьи на русском>**
***Авторы**: …*
***Журнал:** …, том …, вып. …, с. …*
<разделы оригинала в том же порядке: **Аннотация**, **Ключевые слова**, **Введение (Introduction)**, **Методы (Methods)**, …>

### 30 слов и выражений из текста статьи

### TASK 1
#### Step 1: Navigating and positioning a text using publication details
#### Step 2: Genre, audience, and purpose
##### 1. What type of article is this?
##### 2. Who do you think it is written for?
##### 3. Questions based on the title:
#### Step 3: Study the whole text and answer the questions
##### a. What is the background and aim of the investigation?
##### b. What was done in the investigation?
##### c. What was found/discovered?
##### d. What do the Results mean?
##### e. What literature sources are referenced in the paper?

### TASK 2: Annotation

### TASK 3: Oral Presentation
#### 1. Opening (~1.5 minutes)
#### 2. Body (~4.0 minutes)
#### 3. Closing (~1.0 minute)
```

Перевод пишется на русском, TASK 1–3 — на английском, в словаре — английский термин, русский эквивалент и цитата из оригинала.

Структуру бери из Англ1, но объёмы всегда проверяй скриптом. В Англ1 аннотация длиннее лимита (около 380 слов), а в блоке Timing Overview указано 760 слов при фактических ~670.

## Правила выполнения

### Достоверность — главное правило

- Работай только с реальной статьёй, полный текст которой лежит в `articles/` или прислан пользователем. Не выдумывай библиографические данные, цифры, цитаты и источники: всё в словаре и TASK 1–3 должно проверяться по оригиналу.
- Если полный текст недоступен (paywall, нет сети), остановись и попроси пользователя положить PDF в `articles/`.

### Выбор статьи

- Тематика — профиль магистратуры: AI/ML, Edge AI, IoT, распределённые системы, программная инженерия.
- Источник — рецензируемое профильное издание (IEEE, ACM, ScienceDirect, Springer и т. п.).
- Предпочтительна research article в формате IMRaD: вопросы Step 3 рассчитаны именно на неё.
- Объём полного текста — не меньше 10 000 знаков без пробелов (команда в разделе «Команды»). Если результат близок к порогу, пересчитай без списка литературы.
- Статьи в разных комплектах не должны повторяться.
- До начала перевода согласуй выбор с пользователем: покажи выходные данные, тип статьи и объём.

### Перевод на русский

- Строгий научно-технический стиль русской академической литературы. Не калькируй английский синтаксис: порядок слов — по нормам русского научного текста.
- Переводи весь текст статьи: заголовок, аннотацию, ключевые слова и все разделы. Названия разделов — по-русски, с оригиналом в скобках: **Введение (Introduction)**.
- Терминология должна быть единой во всём документе:
  - edge computing — периферийные вычисления; edge — периферийный (не смешивай с «граничный» в одном документе);
  - inference — инференс (логический вывод нейросети);
  - latency — задержка; end-to-end latency — сквозная задержка;
  - testbed — испытательный стенд / экспериментальная платформа;
  - quantization — квантование;
  - trade-off — компромисс / компромиссное решение;
  - offload — делегировать (выгружать) вычисления.
- Формулы и обозначения сохраняй ($p < 0,05$, $SD = 4,1$, проценты, размерности). В русском тексте используй десятичную запятую и русские единицы (187,6 мс, 12,3 мДж), в английских разделах — точку (187.6 ms).
- Длинную статью переводи по разделам и дописывай файл частями — так проще сверять с оригиналом.

### Словарь (30+ терминов)

- Не меньше 30 пунктов, нумерованный список в формате:
  ```markdown
  N. **English Term**: русский эквивалент (*"Дословная цитата из текста статьи"*).
  ```
- Выбирай профессиональные термины, коллокации и устойчивые академические обороты, а не общеупотребительные слова. Переводы терминов должны совпадать с теми, что использованы в переводе статьи.
- Каждая цитата — дословный фрагмент оригинала; проверь её поиском по `articles/articleN_original.txt`.
- Методичка требует ещё и «отметить термины в тексте статьи». В Англ1 это никак не отражено, поэтому форму (например, выделение терминов в оригинале в `articles/`) уточни у пользователя.

### TASK 1 (на английском)

- **Step 1:** Journal name, Volume, Issue, Year, first and last pages, Article title, Authors (surnames and initials) — строго по оригиналу.
- **Step 2:** тип статьи (research article, review article или другой тип, например theoretical paper) с обоснованием. Аудитория — по вариантам методички: students / researchers, lecturers, professors; novices / experts; national / international audience. Ответы на три вопроса по заголовку: Why has the article been written? What is the object of the article? What does the article review / investigate?
- **Step 3:** развёрнутые ответы на вопросы a–e:
  - a — background и aim;
  - b — что сделано: методы, данные, экспериментальная установка;
  - c — результаты с конкретными цифрами;
  - d — смысл результатов: интерпретация, ограничения, future work;
  - e — источники литературы: основные группы работ и их роль в статье.

### TASK 2: Annotation (на английском)

- Объём 200–350 слов (считай скриптом, а не на глаз). Три абзаца: вступление → тема и части статьи → краткое содержание и выводы.
- Обязательные клише — дословно и в этом порядке:
  1. Вступление: `The article I'm going to give a review of is taken from...`, `The headline of the article is...`, `The author of the article is...` / `It is written by...`
  2. Тема и структура: `The topic of the article is...`, `The key issue of the article is...`, `The article under discussion is devoted to the problem of...`, `The article under discussion may be divided into several logically connected parts which are...`
  3. Содержание и выводы: `The author starts by telling the reader that...`, `At the beginning of the article the author describes...`, `Then / After that the author touches upon / explains / points out...`, `In conclusion the author says / makes it clear that...`, `The author concludes by saying that...`
- Полный список допустимых глаголов и фраз — в `english_for_professional_purposes.md`, строки 90–133.

### TASK 3: Oral Presentation (на английском)

- Шапка: `**Speaker:** Dmitry Dolzhikov`, `**Topic:** ...`, `**Estimated Speech Duration:** ...`, затем блок `Timing Overview` с числом слов по разделам. Числа бери из подсчёта скриптом.
- Длительность 5–7 минут непрерывной речи: 650–850 слов при темпе 120–140 слов в минуту.
- **1. Opening (~1.0–1.5 мин):**
  - приветствие и благодарность: *Good afternoon, ladies and gentlemen... Thank you all for coming today...*;
  - представление и цель: *My name is Dmitry Dolzhikov. Today I am going to talk about...*;
  - route map: *To start with, I'll describe... Then I'll mention... Next, I'll discuss... Finally, I'll summarize...*
- **2. Body (~3.5–4.5 мин):**
  - связки: *Let's begin by... / Well, I've told you about... / Now we'll move on to... / Let me turn now to...*;
  - анализ: *Where does that lead us? / Let's consider this in more detail / What does this mean for...?*;
  - примеры: *To give you an example... / A good example of this is...*
- **3. Closing (~1.0 мин):**
  - резюме: *In conclusion, let me sum up the main findings...*;
  - финальная мысль в технике Wisdom / Action / Emotion: *If you take just one thing from this talk, take this...*;
  - благодарность: *Many thanks for your attention*;
  - переход к вопросам: *Now I'll be glad to answer any questions you may have.*
- Только связный монолог: никаких смоделированных вопросов из зала и ремарок вроде `*(Noticing a question...)*`.
- Текст пишется для произнесения вслух: цифры и статистику записывай так, как их говорят (*87 percent*, *p below 0.001*), а не формулами LaTeX.

### Стиль английских текстов

- Академично, но без штампов, по которым узнаётся сгенерированный текст: hype-слов (*unprecedented, revolutionary, impressive, slashing, game-changer*), обилия длинных тире, конструкций вида *"it is not X; it is Y"*, цепочек из трёх эпитетов подряд.
- Клише методички — не штампы, а обязательный элемент задания: сохраняй их дословно.

### Humanized-версии

- `ДолжиковДП_АнглN_humanized.md` / `.docx` создаются только по просьбе пользователя. Это копия основного файла, в которой TASK 2 и TASK 3 переписаны проще и естественнее, а к их заголовкам добавлена пометка `(Humanized / De-AI Version)`.
- Перевод, словарь и TASK 1 в обеих версиях одинаковы: правишь одну — синхронизируй вторую.
- «Очеловечивание» касается текста вокруг речевых формул. Клише TASK 2 и обязательные фразы TASK 3 остаются; структура, тайминг и объём тоже.

## Алгоритм для новой статьи (N = 2, 3, 4)

1. Подбери 1–3 кандидатов и согласуй выбор с пользователем.
2. Сохрани оригинал в `articles/articleN_original.pdf`, извлеки текст в `articles/articleN_original.txt` и проверь объём.
3. Создай `ДолжиковДП_АнглN.md` по структуре выше и выполни полный перевод.
4. Составь словарь из 30+ терминов.
5. Выполни TASK 1, TASK 2 и TASK 3.
6. Пройди чек-лист готовности (ниже).
7. Собери DOCX.
8. Обнови `README.md` и раздел 2 в `AGENTS.md`, закоммить `.md` и `.docx` вместе.

## Команды

Команды запускаются из корня репозитория и работают и в bash, и в PowerShell. Если uv недоступен, замени `uv run python` на `python`: pdfplumber нужен только для извлечения текста из PDF.

Подготовить окружение (один раз):
```bash
uv sync
```

Извлечь текст из PDF:
```bash
uv run python -c "import sys, pdfplumber; pdf = pdfplumber.open(sys.argv[1]); open(sys.argv[2], 'w', encoding='utf-8').write('\n\n'.join(p.extract_text() or '' for p in pdf.pages))" articles/article2_original.pdf articles/article2_original.txt
```

Подсчитать знаки без пробелов (требуется не меньше 10 000):
```bash
uv run python -c "import sys, pathlib; text = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'); print('Chars without spaces:', len(''.join(text.split())))" articles/article2_original.txt
```

Подсчитать слова во фрагменте от маркера START до маркера END. Строки-заголовки не учитываются; без END счёт идёт до конца файла.
```bash
# Аннотация (200–350 слов): START = "The article I", END = "### TASK 3"
uv run python -c "import sys, pathlib; t = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'); s = t[t.index(sys.argv[2]):]; s = s.split(sys.argv[3], 1)[0] if len(sys.argv) > 3 else s; body = ' '.join(l for l in s.splitlines() if not l.startswith('#')); print(sum(1 for w in body.split() if any(c.isalnum() for c in w)), 'words')" ДолжиковДП_Англ2.md "The article I" "### TASK 3"
# Речь целиком (650–850 слов): START = "#### 1. Opening", без END.
# По разделам: "#### 1. Opening" → "#### 2. Body" → "#### 3. Closing" → конец файла.
uv run python -c "import sys, pathlib; t = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'); s = t[t.index(sys.argv[2]):]; s = s.split(sys.argv[3], 1)[0] if len(sys.argv) > 3 else s; body = ' '.join(l for l in s.splitlines() if not l.startswith('#')); print(sum(1 for w in body.split() if any(c.isalnum() for c in w)), 'words')" ДолжиковДП_Англ2.md "#### 1. Opening"
```

Подсчитать пункты словаря (требуется не меньше 30):
```bash
uv run python -c "import re, sys, pathlib; t = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'); s = t.split('### 30', 1)[1].split('### TASK 1', 1)[0]; print(len(re.findall(r'^\d+\.\s', s, re.M)), 'terms')" ДолжиковДП_Англ2.md
```

Проверить наличие обязательных клише аннотации (пустой вывод — всё на месте):
```bash
uv run python -c "import sys, pathlib; t = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'); [print('MISSING:', p) for p in ['give a review of is taken from', 'The headline of the article is', 'written by', 'The topic of the article is', 'The key issue of the article is', 'is devoted to the problem', 'may be divided into several logically connected parts', 'The author starts by telling the reader', 'At the beginning of the article the author', 'In conclusion the author', 'The author concludes by saying'] if p not in t]" ДолжиковДП_Англ2.md
```

Собрать DOCX и проверить результат (DOCX вручную не правь — только пересобирай из `.md`):
```bash
pandoc ДолжиковДП_Англ2.md -o ДолжиковДП_Англ2.docx
pandoc ДолжиковДП_Англ2.docx -t plain | head -40
```

## Чек-лист готовности

- Объём оригинала — не меньше 10 000 знаков без пробелов, текст сохранён в `articles/`.
- Перевод покрывает всю статью, терминология единая.
- В словаре не меньше 30 пунктов, цитаты дословные.
- Данные Step 1 сверены с оригиналом, цифры в TASK 1–3 совпадают со статьёй.
- TASK 2: 200–350 слов, все клише на месте.
- TASK 3: 650–850 слов, числа в Timing Overview совпадают с фактическим подсчётом, нет интерактивных ремарок.
- DOCX пересобран из актуального `.md` и читается через `pandoc -t plain`.
- `README.md` и `AGENTS.md` обновлены.

## Git

- Коммить `.md` и соответствующий `.docx` вместе, чтобы они не расходились.
- Не меняй готовые файлы Англ1 без прямой просьбы пользователя.
- `.venv/` и кэши Python уже в `.gitignore`. Не коммить временные файлы.
