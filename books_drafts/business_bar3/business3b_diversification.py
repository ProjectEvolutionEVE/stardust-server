"""Diversification (Manager, bar 3, part B): spreading credits across holdings that do not all fall together, and rebalancing."""
CODE = "business3b_diversification"
BOOK = {
    "title": "Diversification",
    "subtitle": "Spreading your credits across holdings that do not all fall together",
    "chapters": [
        ("What diversification means",
         "Diversification means spreading your money across several holdings, so one bad result does not sink everything. It cannot prevent every loss, but it can make the losses less severe. It is one of the oldest ideas in money."),
        ("Correlation",
         "What matters is how the holdings move together. Two holdings that rise and fall in step give little protection. Holdings that move differently, or not closely together, soften the swings of the whole."),
        ("Count the real differences",
         "Ten items from the same mine or the same trade can fall together. Five items that depend on different things may hold up better. Ask what each holding depends on, not only how many you own."),
        ("Balance, and review",
         "Diversification works best when the mix stays in balance, so review it from time to time. A holding that grows fast can become too large a share of the whole. Rebalancing brings the mix back to your plan."),
        ("Its limits",
         "When a whole market falls, most holdings can fall together. Diversification softens that fall but does not stop it. Plan for the bad case in advance, with a cash reserve you can reach."),
        ("On the Starship",
         "The same idea applies to the Starship market. A set of different ores and goods is less exposed to one item's bad run than a stack of one item. The earlier book on risk makes the same point: do not put all your credits in one place."),
    ],
    "test": [
        ("What does diversification mean?",
         [("a", "Putting all your credits in one item"), ("b", "Borrowing to buy more"), ("c", "Selling everything at once"), ("d", "Spreading your money across several holdings")], "d"),
        ("When you judge two holdings for diversification, what matters most?",
         [("a", "Their colour"), ("b", "Their names"), ("c", "How they move together"), ("d", "How long they have been held")], "c"),
        ("Which mix is more diversified?",
         [("a", "Ten items that all depend on one mine"), ("b", "Five items that depend on different things"), ("c", "Two items from the same trade"), ("d", "One item bought ten times")], "b"),
        ("Can diversification stop all losses?",
         [("a", "Yes, always"), ("b", "Yes, if you hold ten items"), ("c", "No, it can soften losses but cannot stop them"), ("d", "Only in a rising market")], "c"),
        ("What is rebalancing?",
         [("a", "Bringing the mix back to your plan after holdings drift apart"), ("b", "Moving all your money into cash"), ("c", "Changing the rate on a loan"), ("d", "Doubling a holding that has fallen")], "a"),
    ],
}
