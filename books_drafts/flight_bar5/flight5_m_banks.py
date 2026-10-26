"""How Banks Work: deposits, lending, reserves, runs, central banks and deposit insurance."""
CODE = "flight5_m_banks"
BOOK = {
    "title": "How Banks Work",
    "subtitle": "Deposits, loans, reserves and the safety net",
    "chapters": [
        ("Deposits",
         "A bank takes in deposits from savers and pays interest on some of them. The deposit is a debt the bank owes the saver. The bank must give the money back when it is asked for, under the terms of each account."),
        ("Lending",
         "A bank lends most of the money it holds to borrowers, such as homebuyers and businesses. It charges more interest on loans than it pays on deposits. That gap, the spread, is a large part of its income."),
        ("Reserves",
         "Banks keep some money in reserve, as cash or as deposits at the central bank, so they can meet withdrawals. A bank that lends out too much relative to its reserves is at risk if many savers want their money at once."),
        ("Runs",
         "If many savers fear the bank is in trouble, they may all withdraw at once. A bank that holds mostly loans cannot pay everyone straight away, so even a sound bank can be pushed to fail. This is why confidence matters."),
        ("Central banks",
         "A central bank oversees the banking system. It can lend to banks in trouble, set rules for reserves and act as a lender of last resort. Its support helps stop a run from spreading."),
        ("Deposit insurance",
         "Many countries insure bank deposits up to a set limit. If a bank fails, insured savers are paid back by the insurance scheme. This reduces the risk of runs, since savers have less reason to panic."),
    ],
    "test": [
        ("What is a deposit, from the bank's point of view?",
         [("a", "An asset the bank owns"), ("b", "A gift from the government"), ("c", "A debt the bank owes the saver"), ("d", "A tax paid to the state")], "c"),
        ("What is the spread in banking?",
         [("a", "The gap between the interest charged on loans and the interest paid on deposits"), ("b", "The number of branches"), ("c", "The size of a vault"), ("d", "A type of share")], "a"),
        ("Why do banks keep reserves?",
         [("a", "To avoid paying any interest"), ("b", "To lend nothing at all"), ("c", "To meet withdrawals"), ("d", "To avoid central bank rules")], "c"),
        ("What role does a central bank play in a crisis?",
         [("a", "It closes every bank"), ("b", "It acts as a lender of last resort to banks in trouble"), ("c", "It sets the price of shoes"), ("d", "It removes all deposits")], "b"),
        ("How does deposit insurance help prevent runs?",
         [("a", "It makes withdrawals illegal"), ("b", "It raises every loan rate"), ("c", "It ends saving"), ("d", "It gives savers less reason to panic, since insured deposits are paid back")], "d"),
    ],
}
