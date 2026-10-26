"""Hedging: forward contracts, options in words, the cost of cover, basis risk, examples and the limits of hedging."""
CODE = "flight5_m_hedging"
BOOK = {
    "title": "Hedging",
    "subtitle": "Locking in part of a price, and what it costs",
    "chapters": [
        ("What hedging means",
         "Hedging means taking a second position that is meant to offset a risk you already carry. A farmer who sells next season's crop in advance is hedging against a fall in price. A hedge does not make money by itself; it reduces the swings."),
        ("Forward contracts",
         "A forward contract is a private deal to buy or sell at a set price on a set date. It removes uncertainty about that price. The downside is that you give up any gain if the market moves in your favour."),
        ("Options in words",
         "An option gives its holder the right, but not the duty, to buy or sell at a set price before a set date. A holder pays a premium for this right. If the market moves against the holder, the option can limit the loss to the premium."),
        ("The cost of cover",
         "Every hedge has a cost. A forward gives up upside, and an option costs its premium. Compare the cost of cover with the size of the risk. Some risks are not worth covering at all."),
        ("Basis risk",
         "Basis risk is the danger that the hedge does not move exactly with the thing you are protecting. A fuel hedge bought in one grade of oil may not track the fuel you actually use. Gaps like this leave some risk unhedged."),
        ("Limits",
         "Hedging can fail to protect you, can cost more than it saves, and can create new risks if the contracts are not managed carefully. Use it to reduce risk you cannot bear, not to chase profit."),
    ],
    "test": [
        ("What is hedging?",
         [("a", "Borrowing as much as possible"), ("b", "Selling everything at once"), ("c", "Raising prices"), ("d", "Taking a position to offset a risk you already carry")], "d"),
        ("What does a forward contract do?",
         [("a", "Guarantees a profit"), ("b", "Pays a monthly pension"), ("c", "Removes uncertainty about a price by fixing it in advance"), ("d", "Lowers taxes")], "c"),
        ("What does an option give its holder?",
         [("a", "The right, but not the duty, to buy or sell at a set price"), ("b", "A duty to buy or sell"), ("c", "A fixed salary"), ("d", "A guaranteed loan")], "a"),
        ("What is basis risk?",
         [("a", "The risk of a bank closing"), ("b", "The risk of tax rises"), ("c", "The risk that a hedge does not move exactly with the thing it protects"), ("d", "The risk of a missed meal")], "c"),
        ("What is a real cost of hedging?",
         [("a", "It always adds to profit"), ("b", "It gives up some upside, and an option costs a premium"), ("c", "It removes all risk"), ("d", "It has no cost")], "b"),
    ],
}
