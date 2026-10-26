# Write library books from a plan (Stardust - Terra Deleta) — lean brief

Write DRAFTS only, in the folder named in your task: never touch any other file, never commit, never run the server.
OTHER WRITERS SHARE YOUR FOLDER. Any script, sed or glob you run must list YOUR file codes explicitly (from your plan
lines); never use a folder-wide glob like *.py, and never modify, reformat or rebalance a file you did not write.

1. Read /Users/ericwagoner/Desktop/stardust-godot-test/CLAUDE.md (settled rules) and ONE sample book for the shape:
   /Users/ericwagoner/Desktop/stardust-godot-test/books_drafts/flight_bar1/flight1_controls.py. Do NOT read other books;
   the plan already avoids repeats.
2. Write one file per plan line assigned to you: <folder>/<file code>.py with a module docstring, CODE = "<file code>",
   BOOK = {"title", "subtitle", "chapters": 6 (title, 2-4 sentences each), "test": exactly 5 questions, each
   (question, [("a",..),("b",..),("c",..),("d",..)], correct letter)}. Follow the plan's title and scope.
3. Several books per file write is fine; write them steadily without re-reading what you wrote. After all are written,
   check them all in ONE command: for f in <your files>; do python3 -c "import ast,sys; ast.parse(open(sys.argv[1]).read())" $f || echo BAD $f; done
4. Rules: well-established real-world facts or facts stated in CLAUDE.md only; never invent game features, numbers or
   story; leave out any fact you are not sure of. Bar 4/5 books go deeper than earlier bars but stay plain, warm, short
   sentences for a general audience; one clearly right answer, three plausible wrong ones; the five right answers use at
   least three different letters. Never children or ages, player chat, any secret booklet/gift/Easter egg; Inara is
   never an AI. No dosing instructions in any medical text.
5. Reply briefly: how many files written, and one line only for each fact you were unsure of (skip books with none).
