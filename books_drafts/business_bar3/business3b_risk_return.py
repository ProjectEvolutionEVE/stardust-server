"""Risk and Return (Manager, bar 3, part B): why a higher hoped-for return comes with a higher chance of loss, and how to match risk to a goal."""
CODE = "business3b_risk_return"
BOOK = {
    "title": "Risk and Return",
    "subtitle": "Why a higher hoped-for return comes with a higher chance of loss",
    "chapters": [
        ("The trade-off",
         "In general, the more return you hope for, the more risk you must accept. Safer holdings pay less because they are less likely to lose value. Riskier holdings must offer more, because investors need a reason to take on the chance of a loss."),
        ("Expected return is an average",
         "An expected return is an average over many possible outcomes. It is not a promise. An item might gain 20% in one year and lose 15% in another. The average can look fine while the individual years are painful."),
        ("Volatility",
         "Volatility means how much a price swings up and down. Two holdings can have the same average return, yet one may swing far more than the other. Most people find big swings harder to hold through."),
        ("Why risk is real",
         "A loss becomes permanent if you sell after a fall. Time can help a price recover, but not always, and not before a deadline. Take only the risk you could carry through a bad year."),
        ("No free lunch",
         "A promise of high return with no risk is a warning sign. Over long periods, markets have rewarded risk-taking, but not every year. Be careful with any offer that claims otherwise."),
        ("Match risk to the goal",
         "A goal far away can carry more risk than a goal due next month, because you have time to recover from a fall. Match the risk to when you need the money, and to how much of a loss you could accept."),
    ],
    "test": [
        ("What is the usual trade-off between risk and return?",
         [("a", "A higher hoped-for return usually means higher risk"), ("b", "A higher return always comes with lower risk"), ("c", "Risk and return are unrelated"), ("d", "Only safe holdings give any return")], "a"),
        ("What is an expected return?",
         [("a", "A promise from the seller"), ("b", "A guaranteed profit"), ("c", "An average across possible outcomes, not a promise"), ("d", "The highest return ever seen")], "c"),
        ("What does volatility measure?",
         [("a", "How long an item is held"), ("b", "How much a price swings up and down"), ("c", "The size of a fee"), ("d", "The number of buyers")], "b"),
        ("Why should money needed next month carry less risk than money needed far in the future?",
         [("a", "Because short-term money earns more"), ("b", "Because prices never move in a month"), ("c", "Because you may need the money before a fall has time to recover"), ("d", "Because the bank requires it")], "c"),
        ("What is a warning sign in any offer?",
         [("a", "A clear fee list"), ("b", "A high return promised with no risk"), ("c", "A written contract"), ("d", "An honest answer to your questions")], "b"),
    ],
}
