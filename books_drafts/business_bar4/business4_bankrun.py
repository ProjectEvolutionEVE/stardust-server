"""Bank runs and deposit insurance: why banks are fragile, how panic spreads, and how a guarantee calms it."""
CODE = "business4_bankrun"
BOOK = {
    "title": "Bank Runs and Deposit Insurance",
    "subtitle": "Why banks are fragile, how panic spreads and how a guarantee calms it",
    "chapters": [
        ("What a bank does",
         "A bank takes deposits and lends most of that money out to people and firms. Only a small part sits in cash at any one time. This is useful, because loans power the economy, but it also makes the bank fragile."),
        ("The bank run",
         "If many depositors want their money back at once, the bank cannot pay everyone straight away. A rumour can start a rush. Economists Douglas Diamond and Philip Dybvig described this in a famous 1983 paper: waiting can become a self-fulfilling fear."),
        ("A film example",
         "In the classic film It's a Wonderful Life, from 1946, townspeople rush to the bank to withdraw their savings. The film is fiction, but it shows the scene well. Real runs have happened many times, including at Northern Rock in Britain in 2007."),
        ("Deposit insurance",
         "In the United States, the FDIC was created in 1933 after many bank failures. It insures deposits up to a set limit, so ordinary savers do not lose their money if their bank fails. Most countries now have a similar scheme."),
        ("Other tools",
         "Central banks can lend to banks in trouble, and regulators can require banks to hold more capital and cash. These tools reduce the risk of a run, though they never remove it entirely."),
        ("What to remember",
         "A bank depends on trust. When trust is strong, the system works quietly. When trust breaks, a sound bank can still be hurt. Knowing how deposit insurance works is a sensible part of managing your own savings."),
    ],
    "test": [
        ("What is a bank run?",
         [("a", "Many depositors trying to withdraw their money at once"), ("b", "A race between two banks"), ("c", "A bank opening a new branch"), ("d", "A loan that is repaid early")], "a"),
        ("Why can a bank be fragile even when it is sound?",
         [("a", "It keeps all its money in a safe"), ("b", "It lends most deposits out, so it cannot pay everyone at once"), ("c", "It never lends money"), ("d", "It pays no interest")], "b"),
        ("What is the main purpose of deposit insurance?",
         [("a", "It stops banks from ever failing"), ("b", "It pays higher interest"), ("c", "It guarantees that savers keep their deposits up to a set limit"), ("d", "It forces people to borrow")], "c"),
        ("When was the FDIC created in the United States?",
         [("a", "1946"), ("b", "1983"), ("c", "2007"), ("d", "1933")], "d"),
        ("Which economic idea did Diamond and Dybvig describe?",
         [("a", "A bank run as a self-fulfilling fear"), ("b", "The best rate for a home loan"), ("c", "How to value a stock"), ("d", "The cost of a passport")], "a"),
    ],
}
