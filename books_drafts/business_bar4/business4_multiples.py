"""Valuation Multiples: quick comparisons, and where they mislead."""
CODE = "business4_multiples"
BOOK = {
    "title": "Valuation Multiples",
    "subtitle": "Quick comparisons, and where they mislead",
    "chapters": [
        ("A quick ratio",
         "A multiple divides a company's price by a measure of its results. Price to earnings divides the share price by earnings per share. It is quick to calculate and easy to compare across similar firms."),
        ("Price to sales",
         "Price to sales divides market value by revenue. It can be useful for young firms that do not yet make a profit. It says little, however, about whether that revenue will ever turn into profit."),
        ("Enterprise value",
         "Enterprise value adds debt to a company's market value and subtracts its cash. It is a fairer base when firms carry different amounts of debt. Ratios built on it, such as enterprise value to operating earnings, are common in deals."),
        ("Comparable firms",
         "To use a multiple, find firms that are truly similar in size, growth, risk and industry. Compare their multiples, then apply a typical figure to the company being valued. The quality of the comparison decides the quality of the answer."),
        ("Why multiples differ",
         "A firm that grows fast, has steady cash flow, or carries less risk usually earns a higher multiple. Accounting rules, one-off items and the stage of the economic cycle also shift the numbers. The reason a multiple is high often matters more than the number itself."),
        ("The traps of a single number",
         "A single multiple hides debt, growth and the quality of earnings. A low multiple can be a warning, not a bargain. Use several measures together, and check them against a fuller model such as discounted cash flow."),
    ],
    "test": [
        ("What does price to earnings divide?",
         [("a", "Share price by earnings per share"), ("b", "Revenue by debt"), ("c", "Staff by cost"), ("d", "Cash by age")], "a"),
        ("Which measure suits a young firm that has no profit yet?",
         [("a", "Price to earnings"), ("b", "Price to sales"), ("c", "Dividend yield"), ("d", "The number of shares")], "b"),
        ("What does enterprise value add to market value?",
         [("a", "Only profits"), ("b", "Taxes paid"), ("c", "Debt, minus cash"), ("d", "Staff numbers")], "c"),
        ("What makes a comparison of multiples useful?",
         [("a", "Picking any firm at all"), ("b", "Firms truly similar in size, growth, risk and industry"), ("c", "Using only the largest firm"), ("d", "Ignoring growth")], "b"),
        ("Why is a single multiple risky to rely on?",
         [("a", "It always lies"), ("b", "It hides debt, growth and the quality of earnings"), ("c", "It is used only in banking"), ("d", "It is set by law")], "b"),
    ],
}
