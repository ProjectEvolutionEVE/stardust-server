"""Reconciling Your Books (Broker, bar 2): matching records, explaining every difference, and correcting without erasing."""
CODE = "business2_reconcile"
BOOK = {
    "title": "Reconciling Your Books",
    "subtitle": "Matching records, explaining every difference, and correcting without erasing",
    "chapters": [
        ("Match, then explain",
         "When two records disagree, do not guess. Match each line of one record to a line of the other, then list whatever is left over. Every leftover needs a reason, such as a fee you forgot, a rounding, or a mistake."),
        ("Fees and rounding",
         "Fees are sometimes rounded, so the number on a receipt can be a credit more than you worked out. The auction fee is 2.5% of the bid, rounded up to whole credits. On a bid of 350 credits, the fee is 8.75, which rounds up to 9."),
        ("Correct, do not erase",
         "If a line is wrong, do not rub it out. Add a new line that corrects it, with the date and a short reason. Then the first line and the fix both stay on the record, so anyone can follow what happened."),
        ("Period reviews",
         "Look over your books at the end of each period you choose, such as a day, a week or a run of trades. Check the totals, the open orders and the set-aside credits. Then write a one-line summary of where you stand."),
        ("An audit trail",
         "An audit trail is the chain of records that lets someone follow a deal from start to finish. Every receipt has a code, and anyone can check a code. A trail built from codes can therefore be checked by anyone who needs to."),
        ("Records as a habit",
         "Good records are a habit more than a talent. A few minutes at the end of each session, spent matching and noting, saves hours later. Accountants on Earth have worked this way for centuries."),
    ],
    "test": [
        ("What does reconciling mean?",
         [("a", "Checking two records until they agree"), ("b", "Deleting old records"), ("c", "Raising a floor"), ("d", "Sending receipts to the bank")], "a"),
        ("A bid is 350 credits. What is the Starship fee on it?",
         [("a", "8 credits"), ("b", "8.75 credits"), ("c", "9 credits"), ("d", "35 credits")], "c"),
        ("A line in your books is wrong. What is the right fix?",
         [("a", "Rub it out"), ("b", "Delete the whole log"), ("c", "Add a correcting line with the date and a reason"), ("d", "Ask the bank to change it")], "c"),
        ("What is an audit trail?",
         [("a", "A list of players"), ("b", "The chain of records that lets someone follow a deal from start to finish"), ("c", "A map of the cargo hold"), ("d", "The bank's list of floors")], "b"),
        ("After you match two records, a difference is left over. What should you do?",
         [("a", "Ignore it"), ("b", "Find a reason for it"), ("c", "Round it to zero"), ("d", "Sell the goods")], "b"),
    ],
}
