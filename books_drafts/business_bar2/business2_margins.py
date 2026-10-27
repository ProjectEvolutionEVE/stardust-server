"""Pricing and Margins (Broker, bar 2): margin, markup, break-even, and the floor as a cost check."""
CODE = "business2_margins"
BOOK = {
    "title": "Pricing and Margins",
    "subtitle": "Margin, markup, break-even and the floor",
    "chapters": [
        ("Margin and markup",
         "The margin is the share of the sale price that is profit: the price minus the cost, divided by the price. The markup is the profit as a share of the cost: the price minus the cost, divided by the cost. The two are different, and mixing them up is a classic mistake."),
        ("A worked example",
         "Say a copy costs 14 credits and sells for 20. The profit is 6 credits. The margin is 6 out of 20, which is 30%. The markup is 6 out of 14, which is about 43%. The same profit gives two different percentages, so always say which one you mean."),
        ("The floor is a cost check",
         "In a blueprint auction, the floor is the lowest price you set for your copies, the least a bid can be. It is not the market floor of an item. Before you set one, compare it with the cost per copy. A floor under your cost means a sale would lose money."),
        ("Break-even",
         "The break-even price is the price at which you get back exactly what you spent. For a copy, that is its cost per copy. Every credit above it is profit, and every credit below it is a loss."),
        ("Selling below cost",
         "The auction lets a designer set a floor below cost, but only after ticking a box that confirms they know copies will sell below what they cost. This can be a reasonable choice, but it is always a choice to make on purpose, with the numbers in front of you."),
        ("Set the price after the cost",
         "A floor that is too high may stop every bid, and the auction then holds. A floor that is too low gives away profit. Work out your cost first, then set the price, and watch what the first copies do before you change it."),
    ],
    "test": [
        ("What is a margin?",
         [("a", "Profit divided by cost"), ("b", "The price divided by the cost"), ("c", "Profit as a share of the sale price"), ("d", "The floor price")], "c"),
        ("A copy costs 14 credits and sells for 20. What is its margin?",
         [("a", "43%"), ("b", "14%"), ("c", "30%"), ("d", "6%")], "c"),
        ("What is the markup on that same copy?",
         [("a", "30%"), ("b", "6%"), ("c", "20%"), ("d", "About 43%")], "d"),
        ("What is the break-even price for one copy?",
         [("a", "Its cost per copy"), ("b", "Its floor"), ("c", "Twice its cost"), ("d", "The auction fee")], "a"),
        ("When can a designer set a floor below the cost of a copy?",
         [("a", "At any time"), ("b", "Never"), ("c", "Only after ticking a box that confirms they know the copies will sell below cost"), ("d", "Only on the first run")], "c"),
    ],
}
