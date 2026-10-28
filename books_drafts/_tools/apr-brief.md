# Bank rates are now APRs (Eric 10-27): update the money books

The Starship Bank now works like a real bank. Rewrite every sentence, example and test question in your files that
states the old weekly rates (0.5% a week savings, 1-1.5% a week term deposits, 6-12% a week loans, "8% a week" etc.)
so it matches these facts exactly. Change nothing else.

**The facts (server: lending.py, settled by Eric):**
- Every rate is an **APR**, a year's rate. Each week the Bank charges or pays **the APR divided by 52** on the balance.
- Savings account: **4% APR**, take money out any time. Term deposits: **5% APR for 2 weeks, 6% for 4, 7% for 8**; the
  interest is paid at the end, and closing early gives it up.
- Loans: only the Bank lends, and only to a player **wearing the Business uniform** (put on in the Closet). **No Business
  bar, no loan.** The APR falls with the bars on that uniform: **1 bar 16%, 2 bars 14%, 3 bars 12%, 4 bars 10%, 5 bars 8%.**
- **Down payment:** if the top Business bar is **silver**, the Bank lends only 80% of what is asked; the borrower pays
  the other **20% down** from their own credits, as banks expect. A **gold** top bar (an exceptional record) waives it.
- Unchanged: interest only on what is still owed; paying early saves interest (payoff = what's left plus interest up
  to today); a missed payment brings a late fee and lowers the credit standing; the Bank still weighs the record and
  income to decide how much it will lend.

**Exact worked numbers (from the server's own formula; use only these, do not compute new ones):**
- 1,000 credits at 8% APR over 8 weeks: 126 a week, 1,007 in all, so 7 credits of interest.
- 1,000 at 16% APR over 8 weeks: 127 a week, 1,014 in all, 14 of interest.
- 1,000 at 12% APR over 8 weeks: 127 a week, 1,010 in all, 10 of interest.
- 2,000 at 8% APR over 5 weeks: 402 a week, 2,009 in all, 9 of interest. At 16%: 404 a week, 2,018 in all, 18.
- 10,000 at 16% APR over 8 weeks: 1,268 a week, 10,139 in all, 139 of interest. At 8%: 1,259 a week, 10,070 in all, 70.
- For contrast, a real-world payday-style loan at 400% APR: 1,000 over 8 weeks is 172 a week, 1,376 in all, 376 of interest.
- 10,000 credits in savings at 4% APR earns about 7.69 credits a week (about 400 in a year).
A good lesson line where it fits: at a fair APR a short loan costs little; the danger is a high APR, like a payday loan.

**Rules:** keep each test five questions, same option letters, the right answer still right and the wrong ones still
wrong (rewrite a question and its options if the numbers change). Keep the house style: plain, warm, short. Never
call Inara an AI. Edit only your assigned files, by explicit name. For a `books_i18n/ar/<code>.json` file, make the
same change in Modern Standard Arabic, matching the English (write it with
`json.dump(d, open(p, "w"), ensure_ascii=False, indent=1)` if that's how it is formatted; check first). Afterwards check
each .py file still imports and each .json loads. Reply in at most 5 lines: files changed, anything you were unsure of.
