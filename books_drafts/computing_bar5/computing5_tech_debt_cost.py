"""The Financial Cost of Technical Debt: how shortcuts in code slow delivery, raise incident costs and need budget to fix."""
CODE = "computing5_tech_debt_cost"
BOOK = {
    "title": "The Financial Cost of Technical Debt",
    "subtitle": "How shortcuts in code become a running cost, and how to pay them down",
    "chapters": [
        ("Interest on debt",
         "Technical debt is the future cost of a shortcut taken in code or systems. Like financial debt, it charges interest: every new feature takes longer while the shortcut stays in place. The longer it waits, the more it costs."),
        ("Slowed delivery",
         "Messy code makes each change slower to make and safer to test. Teams spend more hours on tasks that should take less time. Measure the time each change takes, to see the cost of the debt."),
        ("Incident costs",
         "Fragile systems fail more often, and each failure costs staff time, lost service and sometimes customers. Track incidents linked to old shortcuts. Their total cost often makes the case for repair."),
        ("Estimating debt",
         "Estimate debt by listing the areas that slow the team most, then the hours each one costs in a year. Multiply by the hourly cost of the people involved. The result is rough but useful for making decisions."),
        ("Paying it down",
         "Paying down debt means rewriting or simplifying the worst parts. Work on the areas that cost the most each month first. Small, steady repairs are often safer than one large rewrite."),
        ("Budget allocation",
         "Set aside a fixed share of each budget for repair work, so it does not lose every argument to new features. Review that share each year. A visible budget keeps the debt from quietly growing."),
    ],
    "test": [
        ("What is technical debt in financial terms?",
         [("a", "A loan from a bank for hardware"), ("b", "The future cost of a shortcut taken in code or systems"), ("c", "A tax on software sales"), ("d", "The price of a licence")], "b"),
        ("How does technical debt slow a team?",
         [("a", "It makes the office quieter"), ("b", "It removes the need for testing"), ("c", "It makes meetings shorter"), ("d", "Every change takes longer and is harder to test")], "d"),
        ("What makes a good first step in paying down debt?",
         [("a", "Work first on the areas that cost the most each month"), ("b", "Start with a full rewrite of everything"), ("c", "Ignore the problem until it fails"), ("d", "Delete all the code at once")], "a"),
        ("Why set a fixed share of the budget for repair?",
         [("a", "So the budget can be spent in one month"), ("b", "So no one checks the costs"), ("c", "So repair work is not always pushed aside by new features"), ("d", "So features are never built")], "c"),
        ("How can incident costs help make the case for repair?",
         [("a", "They prove that nothing is wrong"), ("b", "They show the total cost of failures linked to old shortcuts"), ("c", "They remove the need for staff"), ("d", "They reduce the number of customers")], "b"),
    ],
}
