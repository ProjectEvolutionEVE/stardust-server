"""Appraisal (10-20): judging what something is worth. Built on rules 12, 21, 23, 26, 27."""
CODE = "appraisal"
BOOK = {
    "title": "Appraisal",
    "subtitle": "Working out what something is really worth",
    "chapters": [
        ("What appraisal is",
         "Appraisal is working out what something is worth before you buy or sell it. A good appraiser asks: what is it, "
         "how much of it is there, what does it cost to make, and what are people paying for it now?"),
        ("What is it made of?",
         "Every ore piece is pure mineral, so its formula tells you exactly what's inside. Its metal share by weight is "
         "what smelting will give; the rest is slag. 100 kg of chalcopyrite holds 34.6 kg of copper. The library's Raw "
         "Materials Catalogue lists them all."),
        ("What is it trading for?",
         "The best guide to price is the market. At the Market terminal, look at the last price, the best bid and the "
         "best ask, and the chart. The bank's standing bid, 10% under the last price, is what you can always sell for "
         "right now."),
        ("The floor",
         "Every item has a floor price, and nothing trades below it. So the floor is the least anything can be worth on "
         "the market. Starting floors are half the starting prices."),
        ("Rare things",
         "One diamond in every 100,000 is near-flawless. It is not industrial diamond: it is a one-of-a-kind valuable, "
         "with its own starting price of 250,000 credits and a floor of 125,000. It isn't traded yet."),
        ("Is it genuine?",
         "Every approved blueprint design has a model code, and every printed copy has its own serial. A serial is "
         "genuine only if the server issued it, and anyone can check one. Receipt codes can be checked the same way. "
         "Always check before you trust."),
    ],
    "test": [
        ("What tells you exactly what an ore piece is made of?",
         [("a", "Its colour"), ("b", "Its formula"), ("c", "Its price"), ("d", "Its seller")], "b"),
        ("What can you always sell a lot for right now?",
         [("a", "The bank's standing bid"), ("b", "Double the last price"), ("c", "The reference price"), ("d", "Nothing")], "a"),
        ("What is the floor price?",
         [("a", "The most it can sell for"), ("b", "The least it can trade for"), ("c", "The bank's fee"), ("d", "The weight")], "b"),
        ("How often is a diamond near-flawless?",
         [("a", "1 in 100"), ("b", "1 in 1,000"), ("c", "1 in 100,000"), ("d", "Never")], "c"),
        ("When is a blueprint serial genuine?",
         [("a", "When it looks right"), ("b", "Only if the server issued it"), ("c", "When the seller says so"), ("d", "Always")], "b"),
    ],
}
