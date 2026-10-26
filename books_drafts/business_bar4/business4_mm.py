"""The Modigliani-Miller Insight: why the way a firm is financed matters less than it seems."""
CODE = "business4_mm"
BOOK = {
    "title": "The Modigliani-Miller Insight",
    "subtitle": "Why the way a firm is financed matters less than it seems",
    "chapters": [
        ("A 1958 idea",
         "In 1958 Franco Modigliani and Merton Miller published a paper that changed corporate finance. Both later won the Nobel Prize in Economics. Their starting point was simple: in a perfect market, the way a firm splits its funding should not change its total value."),
        ("Value from assets, not packaging",
         "A firm's value comes from its assets and the cash they produce. Whether that cash is claimed by lenders or by shareholders only divides the same total. Slicing the same pie differently does not make it bigger."),
        ("The role of taxes",
         "Real tax systems often let interest be deducted from taxable profit, which makes debt cheaper than equity. Modigliani and Miller later accepted that this tax shield can add value. It is one of the main reasons firms borrow."),
        ("The cost of distress",
         "Too much debt raises the risk of failing to pay, and then lenders, staff and customers may react badly. The costs of financial distress are real. A firm must balance the tax benefit of debt against the risk of distress."),
        ("Real-world frictions",
         "Fees, gaps in information, conflicts between managers and owners, and rules about who may own what all break the perfect-market assumptions. These frictions explain why capital structure matters in practice, even though the core insight still holds."),
        ("What it teaches managers",
         "Look at the cash a project produces before worrying about how it is funded. Then weigh the tax benefit of debt against the risk of distress. The insight is a discipline: separate the value of the business from the way it is packaged."),
    ],
    "test": [
        ("When was the Modigliani-Miller proposition published?",
         [("a", "1908"), ("b", "1958"), ("c", "1985"), ("d", "2008")], "b"),
        ("In a perfect market, what does the funding mix do to total value?",
         [("a", "Greatly raises it"), ("b", "Greatly lowers it"), ("c", "Nothing, since it only divides the same cash"), ("d", "Makes it negative")], "c"),
        ("Why does debt get a tax benefit in many systems?",
         [("a", "Interest can be deducted from taxable profit"), ("b", "Lenders pay the tax"), ("c", "Debt is free of rules"), ("d", "Debt removes all risk")], "a"),
        ("What is the cost of distress?",
         [("a", "The cost of printing shares"), ("b", "The extra cost and damage from a high risk of failing to pay"), ("c", "A fee for buying gold"), ("d", "The payment of dividends")], "b"),
        ("What is the main lesson for managers?",
         [("a", "Ignore cash flows"), ("b", "Judge projects by their cash, then weigh debt's tax benefit against distress risk"), ("c", "Always borrow the maximum"), ("d", "Never borrow")], "b"),
    ],
}
