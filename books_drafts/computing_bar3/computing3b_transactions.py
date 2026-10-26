"""Transactions in Depth: commit and roll back, the four promises of a transaction, and how the game's credit transfers use one."""
CODE = "computing3b_transactions"
BOOK = {
    "title": "Transactions in Depth",
    "subtitle": "Commit, roll back, and what a failed step leaves behind",
    "chapters": [
        ("Begin, then commit or roll back",
         "A transaction starts, collects its changes, and then either commits them all or rolls them back. A commit makes every change permanent together. A rollback undoes the changes, as if none of them had been made."),
        ("What a failed step does",
         "If any step in a transaction fails, the program should roll back, and the database returns to how it was before the start. Half-finished work is the danger. A transfer that takes credits from one account but never adds them to the other is exactly what a transaction prevents."),
        ("The four promises",
         "Database people describe transactions with four letters. Atomic means all or nothing. Consistent means the rules still hold afterwards. Isolated means one transaction cannot see another's half-done work. Durable means a committed change survives a crash."),
        ("Keep the work short",
         "A transaction holds its locks until it ends, so a long one makes other work wait. Do the slow thinking before the transaction begins, and keep the changes inside it quick and tidy."),
        ("The game's credit transfers",
         "The game's credit transfer locks both accounts in the same order, changes both balances, and writes the paper-trail row. The caller wraps it in a transaction, so the balance changes and the record happen together, or not at all."),
        ("Retries and money",
         "When a request fails in the middle, the program may not know whether the change was committed. Good designs give each request a unique reference, so a retried request is recognised and does not pay or change things twice."),
    ],
    "test": [
        ("What does a rollback do?",
         [("a", "Makes the changes permanent"), ("b", "Undoes the changes in the transaction, as if none had been made"), ("c", "Doubles every balance"), ("d", "Sends the receipt to the player")], "b"),
        ("What does the A in ACID stand for?",
         [("a", "Atomic, meaning all or nothing"), ("b", "Automatic"), ("c", "Accurate"), ("d", "Account")], "a"),
        ("What is the main danger that a transaction prevents?",
         [("a", "Slow screens"), ("b", "Long names for accounts"), ("c", "Half-finished work, such as one account debited and the other never credited"), ("d", "Too many players")], "c"),
        ("Why should a transaction be kept short?",
         [("a", "Because it holds its locks until it ends, and other work may wait"), ("b", "Because the database forgets it after a while"), ("c", "Because longer transactions cost nothing"), ("d", "Because a transaction must always be one minute long")], "a"),
        ("Why give each request a unique reference when a retry is possible?",
         [("a", "So a retried request is recognised and does not pay or change things twice"), ("b", "So the request is printed on the screen"), ("c", "So the server runs more slowly"), ("d", "So the request expires after a day")], "a"),
    ],
}
