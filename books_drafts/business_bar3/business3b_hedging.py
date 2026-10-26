"""Hedging (Manager, bar 3, part B): paying a known cost to reduce an unknown risk, in general terms."""
CODE = "business3b_hedging"
BOOK = {
    "title": "Hedging",
    "subtitle": "Paying a known cost to reduce an unknown risk",
    "chapters": [
        ("What a hedge is",
         "A hedge is a deal that reduces the damage from a risk you already face. You give up some possible gain, or pay a known cost, so that a bad move hurts less. A hedge does not remove the risk. It moves part of it to someone else, or changes its shape."),
        ("A farmer's example",
         "A farmer expects to harvest wheat in six months and fears the price will fall. She agrees today to sell at a fixed price for delivery at harvest. If prices fall, she is protected. If prices rise, she misses the extra gain."),
        ("A buyer's example",
         "A factory that uses large amounts of copper may agree a fixed price in advance. Its costs become predictable. If copper falls, the factory pays more than the market price, and that is the price of the certainty."),
        ("Every hedge has a cost",
         "A hedge always costs something: a fee, a premium, or a lost upside. The question is whether the protection is worth that cost. A hedge you cannot afford to keep does not protect you."),
        ("Match the real exposure",
         "Hedging works best when the risk is clear. You need to know how much you are exposed, for how long, and to what. A hedge that does not match the real risk can add risk instead of removing it."),
        ("Everyday hedges",
         "Hedges are common in daily life. A fixed-rate loan protects you from rises in the rate. Insurance is a kind of hedge, and so is a savings cushion for a sudden cost. Each one trades a small known cost for steadiness."),
    ],
    "test": [
        ("What does a hedge do?",
         [("a", "It removes every risk"), ("b", "It reduces the damage from a risk you already face"), ("c", "It guarantees a gain"), ("d", "It hides a loss from the books")], "b"),
        ("A farmer locks in a sale price before harvest. If prices rise, what does she give up?",
         [("a", "Her harvest"), ("b", "Her land"), ("c", "The extra gain above the locked price"), ("d", "Her right to sell")], "c"),
        ("What is always part of a hedge?",
         [("a", "A free guarantee"), ("b", "A loan from a bank"), ("c", "A promise from the government"), ("d", "A cost in exchange, such as a fee, a premium or a lost upside")], "d"),
        ("Which of these works as an everyday hedge?",
         [("a", "Spending every credit as it arrives"), ("b", "Carrying no savings at all"), ("c", "A fixed-rate loan, which protects against rises in the rate"), ("d", "Lending to the highest bidder")], "c"),
        ("Why must a hedge match the real exposure?",
         [("a", "So it can be sold at a profit"), ("b", "Because the law requires it"), ("c", "So the price never moves"), ("d", "Because a mismatched hedge can add risk instead of removing it")], "d"),
    ],
}
