"""Return on Investment (Manager, bar 3, part A): what you gained from a purchase, as a share of what it cost."""
CODE = "business3a_roi"
BOOK = {
    "title": "Return on Investment",
    "subtitle": "What you gained from a purchase, as a share of what it cost",
    "chapters": [
        ("What ROI measures",
         "Return on investment, or ROI, compares what you gained from a purchase with what it cost. It turns the answer into a percentage, so two different purchases can be compared fairly, even when their costs differ."),
        ("The formula",
         "ROI equals the gain minus the cost, divided by the cost, then multiplied by 100. The gain is the total money the purchase brought back. The cost is what you paid to get it."),
        ("A worked example",
         "Suppose you spend 500 credits on a bigger hold, and over the period it brings in 650 credits of extra income. The gain is 150. Divide 150 by 500 to get 0.3, so the ROI is 30%."),
        ("Compare like with like",
         "ROI is most useful when the periods are the same. A purchase that returns 30% in one week is far better than one that returns 30% over five years. Always note the time as well as the percentage."),
        ("Count the full cost",
         "Include everything you paid to get the purchase working: its price, any fees, the upkeep you must pay and the interest on any loan. A purchase that looks good before those costs may look very different after them."),
        ("Not the whole story",
         "ROI does not show when the money comes back, or how safe the return is. Use it together with the payback period, and with an honest look at the risks."),
    ],
    "test": [
        ("What does return on investment compare?",
         [("a", "The price of an item with its weight"), ("b", "The gain from a purchase with what it cost"), ("c", "The number of players with the number of units"), ("d", "The loan with the savings rate")], "b"),
        ("A purchase costs 500 and returns a gain of 150. What is its ROI?",
         [("a", "150%"), ("b", "500%"), ("c", "3%"), ("d", "30%")], "d"),
        ("Why must loan interest and upkeep be counted in the cost?",
         [("a", "Because they are part of what the purchase really cost"), ("b", "Because they are always zero"), ("c", "Because the Bank asks for them each week"), ("d", "Because they are never paid")], "a"),
        ("Two purchases both return 30%. What else must you check before you compare them?",
         [("a", "Their colours"), ("b", "Whether both are in the cargo hold"), ("c", "The time over which each return is earned"), ("d", "Their names")], "c"),
        ("What does ROI not show?",
         [("a", "The size of the return as a percentage"), ("b", "When the money comes back, and how safe the return is"), ("c", "The cost you paid"), ("d", "The formula used to work it out")], "b"),
    ],
}
