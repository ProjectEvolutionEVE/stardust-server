"""Actuarial science: mortality tables, the law of large numbers, Halley and Lloyd's, pricing risk, reserves and adverse selection."""
CODE = "business4_actuary"
BOOK = {
    "title": "Actuarial Science",
    "subtitle": "Pricing risk with mortality tables, large numbers and careful reserves",
    "chapters": [
        ("What actuaries do",
         "Actuaries measure risk using mathematics and data. They work mostly in insurance and pensions, estimating how likely events are and what they might cost."),
        ("Mortality tables",
         "A mortality table shows how many people of each age are likely to die within a year. Edmond Halley published one of the early tables in 1693, using records from the city of Breslau."),
        ("The law of large numbers",
         "The law of large numbers says that as a group grows, the average result tends to settle near the expected value. One person's life is uncertain, but a large group is far more predictable. This is what makes insurance possible."),
        ("Lloyd's of London",
         "Lloyd's began in a London coffee house in the late 1600s, where merchants and ship owners insured sea voyages. It became a major centre for marine insurance and still operates today."),
        ("Pricing and reserves",
         "An insurer sets a premium that covers expected claims, costs and a margin for profit. It also holds reserves, a store of money to pay future claims. Reserves protect the insurer if claims run higher than expected."),
        ("Adverse selection",
         "Adverse selection happens when people who expect to claim more are more likely to buy cover. Insurers manage this with careful underwriting, so that prices fit the real risk. An insurer that ignores it can lose money fast."),
    ],
    "test": [
        ("What is a mortality table?",
         [("a", "A table for dinner plans"), ("b", "A table showing how likely people of each age are to die within a year"), ("c", "A list of bus routes"), ("d", "A chart of stock colours")], "b"),
        ("Which scientist published an early mortality table in 1693?",
         [("a", "Galileo Galilei"), ("b", "Johannes Kepler"), ("c", "Edmond Halley"), ("d", "Blaise Pascal")], "c"),
        ("What does the law of large numbers say?",
         [("a", "Small groups always win"), ("b", "Numbers never repeat"), ("c", "Averages are always zero"), ("d", "Large groups have averages that settle near the expected value")], "d"),
        ("What is adverse selection?",
         [("a", "When people who expect to claim more are more likely to buy cover"), ("b", "When an insurer makes too many coffees"), ("c", "When a policy is printed in colour"), ("d", "When claims are paid too fast")], "a"),
        ("What is an insurer's reserve?",
         [("a", "A spare office chair"), ("b", "A store of money to pay future claims"), ("c", "A ticket for a boat"), ("d", "A type of bond with no interest")], "b"),
    ],
}
