"""Inflation-Protected Bonds: how TIPS and I bonds adjust for inflation, real yields, breakeven inflation, and where these bonds fit in a plan."""
CODE = "business5_tips"
BOOK = {
    "title": "Inflation-Protected Bonds",
    "subtitle": "Bonds that adjust to rising prices, and what they can and cannot do",
    "chapters": [
        ("Bonds and inflation",
         "A normal bond pays a fixed amount of interest and returns a fixed sum at the end. If prices rise, the fixed payments buy less. Inflation-protected bonds are designed to reduce that risk."),
        ("TIPS",
         "TIPS, or Treasury Inflation-Protected Securities, are US government bonds whose principal rises with the consumer price index and falls with deflation. Interest is paid on the adjusted amount. They are issued by the US Treasury and are widely held as a hedge against inflation."),
        ("Real yields",
         "A real yield is the return after allowing for inflation. It shows how much the investment grows in purchasing power, not just in cash. Comparing real yields with nominal yields shows how much inflation is expected to cost."),
        ("Breakeven inflation",
         "Breakeven inflation is the rate of inflation that would make a normal bond and an inflation-protected bond of the same term perform equally well. It is estimated from the gap between their yields. It is a market estimate, not a forecast anyone can rely on."),
        ("I bonds",
         "I bonds are US savings bonds whose interest rate combines a fixed rate with a rate that changes with inflation. They have purchase limits per person each year. They cannot be cashed in during the first twelve months, and cashing in early loses some interest."),
        ("Where they fit",
         "Inflation-protected bonds can be one part of a diversified plan, especially for money needed in the future. They are not a guaranteed route to wealth. Compare them with other holdings, and check their tax treatment before deciding."),
    ],
    "test": [
        ("What does TIPS stand for?",
         [("a", "Treasury Inflation-Protected Securities"), ("b", "Taxed Interest Payment System"), ("c", "Tax Income Pay Scheme"), ("d", "Tokens in Pounds Sterling")], "a"),
        ("What happens to a TIPS principal when inflation rises?",
         [("a", "It falls to zero"), ("b", "It is paid out in gold"), ("c", "It adjusts upward"), ("d", "It is fixed forever")], "c"),
        ("What is a real yield?",
         [("a", "A bond's name"), ("b", "A type of salary"), ("c", "A return before tax"), ("d", "A return after allowing for inflation")], "d"),
        ("What does breakeven inflation estimate?",
         [("a", "The inflation rate markets expect, from the gap between normal and inflation-protected yields"), ("b", "The tax on bonds"), ("c", "The bank's fees"), ("d", "The price of a sandwich")], "a"),
        ("Which is a rule for US I bonds?",
         [("a", "They can be cashed in at any moment with no loss"), ("b", "They must be held at least a year before they can be cashed in"), ("c", "They are issued by shops"), ("d", "They never earn interest")], "b"),
    ],
}
