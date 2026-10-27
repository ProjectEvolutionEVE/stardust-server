# Translate library books into Arabic (Stardust - Terra Deleta): the translator's brief (Eric 10-27, rule 41)

Books and tests are read, not voiced. Translate into clear **Modern Standard Arabic** for a general audience: warm,
plain and short, like the English. Read /Users/ericwagoner/Desktop/stardust-godot-test/CLAUDE.md first.

**Input:** each assigned file is a JSON book: `{code, title, subtitle, chapters: [[title, text], ...],
test: [[question, [[letter, option], ...], answer_letter], ...]}`.

**Output:** for each one, write `/Users/ericwagoner/Desktop/stardust-godot-test/books_i18n/ar/<code>.json`, with the
same structure:
- Translate title, subtitle, chapter titles, chapter texts, questions and option texts.
- Keep `code`, every option **letter** and every **answer letter** exactly as they are. The right answer must stay
  right, and the wrong ones wrong.

**Fixed names:**
- Inara is إنارا.
- The ship is "WSC ألكسندر فون همبولت".
- Keep the game's English button names (UNLOAD, COMMS, WARP, COLLECT) in Latin letters.
- Write numbers in Western digits (1, 2, 3) and keep units (kg, km).

**Rules:**
- Translate faithfully. Add nothing, drop nothing, and never "improve" a fact.
- If an English sentence looks wrong, translate it anyway and list it in your reply.

**Files:** only write your own assigned files, using explicit file names, never a folder-wide glob, and quote shell
variables. Write each file with `json.dump(..., ensure_ascii=False)` from Python. Afterwards, check every one of
your files loads as JSON and has the same number of chapters, questions and options as its source.

**Reply** in at most 6 lines: files written, and any English sentences that looked wrong.
