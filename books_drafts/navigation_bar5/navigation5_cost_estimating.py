"""Cost-Estimating Relationships for Spacecraft: mass-based estimates, learning effects, analogies, uncertainty, reviews and budgets."""
CODE = "navigation5_cost_estimating"
BOOK = {
    "title": "Cost-Estimating Relationships for Spacecraft",
    "subtitle": "Estimating what a spacecraft will cost before it is built",
    "chapters": [
        ("Mass-based estimates",
         "A common shortcut estimates cost from a spacecraft's mass. Heavier craft often cost more. The relationship is a rough guide, not a precise law."),
        ("Learning effects",
         "Teams get better with repeated builds, so later units often cost less than the first. Learning effects are included in estimates for production runs. They vary from team to team and from design to design."),
        ("Analogies",
         "An analogy compares a new craft with a similar past one. Adjustments are made for differences in size and technology. Analogies are useful when data is limited."),
        ("Uncertainty",
         "Early estimates are uncertain, sometimes by a large margin. Estimators give ranges rather than single numbers. The uncertainty should be stated clearly."),
        ("Reviews",
         "Independent reviews check estimates for errors and hidden assumptions. A review adds confidence before a budget is set. Reviews catch problems early, when they are cheapest to fix."),
        ("Budgets",
         "A budget sets money aside for the work. Good budgets include reserves for risk. An estimate becomes a budget only after review and approval."),
    ],
    "test": [
        ("What is a common quick estimate of spacecraft cost based on?",
         [("a", "Mass"), ("b", "The colour of the paint"), ("c", "The name of the team"), ("d", "The shape of the logo")], "a"),
        ("What do learning effects usually do to later units?",
         [("a", "Raise cost a lot"), ("b", "Double the cost"), ("c", "Lower the cost"), ("d", "Have no effect at all")], "c"),
        ("What is an analogy in cost estimating?",
         [("a", "A riddle"), ("b", "Comparing a new craft with a similar past one"), ("c", "A poem"), ("d", "A spare part")], "b"),
        ("What should estimators state about their figures?",
         [("a", "One exact number, always"), ("b", "Nothing, it is a secret"), ("c", "Only the name of the team"), ("d", "Ranges, with the uncertainty stated clearly")], "d"),
        ("What does an independent review do?",
         [("a", "Adds costs"), ("b", "Checks for errors and hidden assumptions"), ("c", "Cancels the project"), ("d", "Paints the craft")], "b"),
    ],
}
