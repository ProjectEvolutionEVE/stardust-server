"""Net Present Value for Software Projects: comparing money now with money later."""
CODE = "computing5_npv_software"
BOOK = {
    "title": "Net Present Value for Software Projects",
    "subtitle": "Comparing money now with money later",
    "chapters": [
        ("Discounting future cash",
         "Money paid later is worth less than money now, because money now can be invested and because later payments carry risk. Discounting converts future cash into today's value. The rate used is a judgment, so state it clearly."),
        ("Estimating benefits",
         "List the cash a project brings in or saves in each year, and be realistic about it. Benefits that depend on uncertain adoption should be counted cautiously. Write down the assumptions behind each figure."),
        ("Cost timelines",
         "Map the spending over time, including the running costs after launch. Many projects look cheap until the upkeep is counted. Include staff time as a real cost."),
        ("NPV and payback",
         "Net present value adds up each year's discounted cash, subtracting the cost. The formula divides each year's cash by one plus the rate, raised to the power of the year. Payback counts how long it takes to recover the cost, so the two measures can rank projects differently."),
        ("Sensitivity",
         "Sensitivity analysis tests how the answer changes if benefits fall or costs rise. A project that only works in the best case is risky. Check the range of likely outcomes, not one forecast."),
        ("Decision tests",
         "A project with a positive NPV at a sensible rate is worth considering. Weigh it alongside risk, strategy and the team's capacity. A good number does not replace judgment."),
    ],
    "test": [
        ("Why is money later worth less than money now?",
         [("a", "It can be invested and carries risk"), ("b", "It rusts"), ("c", "It is smaller by law"), ("d", "It is never paid")], "a"),
        ("What does NPV add up?",
         [("a", "Number of desks"), ("b", "Discounted cash flows"), ("c", "Team lunches"), ("d", "Bug counts")], "b"),
        ("What do cost timelines include?",
         [("a", "Only the launch cost"), ("b", "Nothing"), ("c", "Spending over time, including running costs after launch"), ("d", "Only lunch")], "c"),
        ("What is sensitivity analysis?",
         [("a", "Measuring feelings"), ("b", "Testing the office heating"), ("c", "Counting feedback"), ("d", "Testing how the answer changes if benefits fall or costs rise")], "d"),
        ("NPV and payback can disagree. Why?",
         [("a", "They measure different things: one discounts, the other counts time to recover cost"), ("b", "They always agree"), ("c", "One is a lie"), ("d", "Neither uses money")], "a"),
    ],
}
