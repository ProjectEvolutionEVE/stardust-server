"""Compound Growth (Manager, bar 3, part B): interest on interest, the rule of 72, why time matters most, and how debt compounds too."""
CODE = "business3b_compound_growth"
BOOK = {
    "title": "Compound Growth",
    "subtitle": "Interest on interest, the rule of 72, and why starting early matters most",
    "chapters": [
        ("Simple versus compound",
         "Simple growth adds the same amount each period, based on the original sum. Compound growth adds each period's gain to the total, so the next gain is earned on a bigger base. Over long periods the difference becomes large."),
        ("A worked example",
         "Suppose 100 credits grows by 10% a year. After one year it is 110. After two years, 10% of 110 is 11, so the total is 121, not 120. That extra credit is interest earned on interest."),
        ("The rule of 72",
         "To estimate how many years money takes to double, divide 72 by the yearly rate. At 6% a year, money roughly doubles in 12 years. At 9%, it takes about 8 years. The rule is a quick estimate, not an exact figure."),
        ("Time is a big lever",
         "For most savers, time matters as much as the rate. At 7% a year, money left alone for 30 years grows to about 7.6 times its start. Left for 15 years, the same money grows to about 2.8 times."),
        ("Save on a schedule",
         "Adding a fixed amount each period speeds up growth, because every new addition also earns a return. Regular saving usually beats one large attempt to pick the perfect moment."),
        ("Debt compounds too",
         "Unpaid interest on a loan is added to what you owe, and then it earns more interest in turn. The same arithmetic that builds savings can build a debt. Paying down debt early stops that growth."),
    ],
    "test": [
        ("What is compound growth?",
         [("a", "Each period's gain is added to the total, so later gains earn too"), ("b", "Gains are kept in a separate box"), ("c", "A fixed sum of interest every year"), ("d", "The bank's fee for an account")], "a"),
        ("100 credits grows by 10% a year for two years. How much is it at the end?",
         [("a", "120 credits"), ("b", "110 credits"), ("c", "121 credits"), ("d", "200 credits")], "c"),
        ("By the rule of 72, about how long does money take to double at 6% a year?",
         [("a", "6 years"), ("b", "72 years"), ("c", "8 years"), ("d", "12 years")], "d"),
        ("Why does starting early help a saver?",
         [("a", "The bank pays a bonus to early starters"), ("b", "Each gain has more years to earn its own gain"), ("c", "Early savers pay less tax"), ("d", "Prices fall in the first years")], "b"),
        ("How can debt grow in the same way?",
         [("a", "Unpaid interest is added to what you owe and then earns more interest"), ("b", "Debt shrinks with time"), ("c", "Debt never grows"), ("d", "Only the bank's fee grows")], "a"),
    ],
}
