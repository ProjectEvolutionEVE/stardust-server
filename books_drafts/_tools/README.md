# Writing bars 4 and 5 for one career (the method Eric approved, 10-26)

1. Covered list: `python3 books_drafts/_tools/titles.py <career> > <scratch>/<career>-covered.txt`
2. One Haiku planner (Eric 10-27: cheapest model): follow plan-brief.md, writing <scratch>/<career>-plan45.md (120 bar-4 + 325 bar-5 lines).
3. Split the plan into slices of about 40 lines; mkdir books_drafts/<career>_bar4 and _bar5.
4. About 11 Haiku writers, one slice each, following write-brief-lean.md (only their own files!).
5. About 6 Haiku checkers, each given 70-80 of the new books, following verify-brief.md: answer keys, facts, rules. The lead
   session settles every flag (Eric 10-27). Check the facts the writers flagged; `python3 books_drafts/_tools/check45.py "books_drafts/<career>_bar[45]/*.py"`;
   remove __pycache__; run test_server.py on the test database; commit; push.
Pacing (Eric 10-27): before each batch check usage. Wait for the reset if the 5-hour window is past about 55%; stop for
the week past 90% weekly. Measured on the Max plan: about 25% of a 5-hour window and 3.5-4% weekly per career.
Done: Flight, Business, Mining, Engineering, Computing (10-27). Left: Medicine, Navigation, Science.
Tests: the test environment lives in ~/.local/share/stardust-test/ (venv + Postgres on port 5544, database dfgtest),
not in a scratch folder (macOS cleans /private/tmp).
