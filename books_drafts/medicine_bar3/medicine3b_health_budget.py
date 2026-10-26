"""Medicine, bar 3 (Senior Doctor), part B: Planning a Health Budget. Setting a yearly health budget, sinking funds for known costs, and comparing options by cost per crew-day."""
CODE = "medicine3b_health_budget"
BOOK = {
    "title": "Planning a Health Budget",
    "subtitle": "Setting a yearly health budget, sinking funds for known costs, and comparing options by the crew-day",
    "chapters": [
        ("Start with what you spend",
         "A health budget starts with a list of what health costs now. Include routine supplies, check-ups, replacement equipment and any regular costs. Writing it down shows where the money goes, and where it might go wrong."),
        ("Plan for the year",
         "Plan a year at a time, with an amount set aside each month for each cost. Some costs are regular and some are rare but large, so the plan has to cover both. Reviewing the budget every few months keeps it accurate."),
        ("Sinking funds",
         "A sinking fund saves a little each month toward a known future cost, such as replacing worn-out equipment or restocking a shelf. Saving steadily avoids a sudden large bill. If the savings earn interest, the fund grows a little faster."),
        ("Cost per crew-day",
         "Comparing options is easier with a common measure. Cost per crew-day shows what a supply or service costs for each person for each day. A cheap item that needs replacing often can cost more over a year than a dearer item that lasts."),
        ("Trade-offs and value",
         "Every spend is a choice. Spending on prevention and safety can cost less than treating problems later. Weigh the cost against the benefit, and remember that the cheapest option is not always the best value."),
        ("Money and care together",
         "A good health budget keeps money for emergencies and for planned care, and the people it covers can see it. Clear records of spending make next year's plan easier to set, and show that money is being used with care."),
    ],
    "test": [
        ("What does a health budget start with?",
         [("a", "A list of what health costs now"), ("b", "A holiday plan"), ("c", "A guess about the future"), ("d", "Ignoring the costs")], "a"),
        ("What is a sinking fund?",
         [("a", "A fund that loses money on purpose"), ("b", "A fund for holidays"), ("c", "Money saved a little at a time toward a known future cost"), ("d", "A loan with no interest")], "c"),
        ("What does cost per crew-day show?",
         [("a", "The speed of a ship"), ("b", "The number of crew"), ("c", "The length of a mission"), ("d", "The cost of a supply or service for each person for each day")], "d"),
        ("Why might a cheaper item cost more over a year?",
         [("a", "It never needs replacing"), ("b", "It needs replacing often, so the costs add up"), ("c", "It is always free"), ("d", "Its price never changes")], "b"),
        ("Why can spending on prevention be good value?",
         [("a", "It costs more than treating problems later"), ("b", "It removes the need for a budget"), ("c", "It may cost less than treating problems later"), ("d", "It is never worth it")], "c"),
    ],
}
