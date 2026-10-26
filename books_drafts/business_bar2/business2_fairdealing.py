"""Ethics and Fair Dealing (Broker, bar 2): telling the truth, keeping your word, and never rigging a price."""
CODE = "business2_fairdealing"
BOOK = {
    "title": "Ethics and Fair Dealing",
    "subtitle": "Telling the truth, keeping your word, and never rigging a price",
    "chapters": [
        ("Fair dealing",
         "Fair dealing means telling the truth about what you are selling, and paying what you agreed. It is the rule that keeps a market worth trading in. Once people think a market is rigged, they stop trading in it, and everyone loses."),
        ("Describe what you sell",
         "A blueprint says what it does and what it needs. Describe it exactly as it is. A design that promises more than it delivers harms the buyer, and it harms your name too."),
        ("Forgeries and copies",
         "The serial system exists to stop forgeries and theft of designs. A serial is genuine only when the server issued it, and only a serialed copy of that exact design counts. Do not try to pass off a copy as the original. A copy you bought can never be resold, and getting around that is not fair dealing."),
        ("Do not move prices by pretending",
         "Posting bids you never mean to fill, in order to push a price, is called manipulation. Trades you make with yourself, to make a price look busy, are the same kind of wrong. In most real markets these acts are against the law."),
        ("Use only what everyone can see",
         "Trading on information the public does not have is called insider trading, and real markets punish it. On the Starship, the book shows everyone the same prices and trades. Use what the book shows, and nothing else."),
        ("Fair even when it costs you",
         "A fair trader keeps the promise even when it costs money. Name your floor honestly, pay the fee you agreed, and say so when you have made a mistake. A good name takes years to build and a moment to lose."),
    ],
    "test": [
        ("What does fair dealing mean?",
         [("a", "Charging the most you can"), ("b", "Telling the truth about what you sell, and paying what you agreed"), ("c", "Never trading with anyone"), ("d", "Keeping prices secret")], "b"),
        ("What does a serial prove?",
         [("a", "That the item is old"), ("b", "That the owner is famous"), ("c", "That the server issued it, so a serialed copy of that exact design is genuine"), ("d", "That the floor is low")], "c"),
        ("What is it called when someone posts bids they never mean to fill, to push a price?",
         [("a", "Insider trading"), ("b", "Manipulation"), ("c", "Drafting"), ("d", "Setting a floor")], "b"),
        ("What is insider trading?",
         [("a", "Trading on information the public does not have"), ("b", "Trading inside the cargo hold"), ("c", "Trading at night"), ("d", "Trading only with the bank")], "a"),
        ("Can a copy you bought at auction be resold?",
         [("a", "Yes, at auction"), ("b", "Yes, on the order book"), ("c", "Only to the bank"), ("d", "No, never")], "d"),
    ],
}
