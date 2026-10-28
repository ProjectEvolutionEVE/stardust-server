# Make Inara's voice script speakable (Eric 10-27)

Voice scripts are spoken words only: every number spelled out in words, and no quotation marks, brackets, colons,
semicolons, slashes, percent signs or other symbols (full-width ones too: 「」（）：；％). A voice model garbles them.

For each assigned file `/Users/ericwagoner/Desktop/stardust-godot-test/docs/inara-lines/<lang>.json` (a flat JSON
object, line ID -> text):
- Change ONLY the lines that contain a digit or one of those symbols. Leave every other line byte-for-byte alone.
- Spell numbers the way a native speaker says them aloud. Decimals: use the language's spoken "point" form
  (e.g. English "one point nine two", German "eins Komma neun zwei"); prefer whole units where exact (1.6 m = "one
  metre sixty"). Percent: the word ("sixty-five percent"). Japanese/Chinese: write numbers as spoken (kanji/hanzi or
  kana as natural), never Arabic digits.
- Brackets: fold the content into the sentence with commas. Colons/semicolons: a comma or full stop.
- The sample receipt code (WSC-7K3F-92QD): drop the example code, just say "a receipt with its own code".
- Keyboard keys W and S: say the letter names as spoken in that language.
- Keep the English button names (UNLOAD, SELL, Sell now, Exit Private Quarters, My items, COMMS, WARP...) and WSC/SET as
  they are. Keep the meaning exactly: add nothing, drop nothing else.
Write with Python: `json.dump(d, open(p, "w"), ensure_ascii=False, indent=1)`. Touch only your assigned files.
Then check: `re.search(r'[0-9%()\[\]{}"“”«»:;/×+=#@&*（）：；「」％]', text)` must find nothing in any line of your files.
Reply in at most 4 lines: per file, how many lines changed, and anything you were unsure of.
