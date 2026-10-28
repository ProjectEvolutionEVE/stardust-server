"""Budget Governance and Capital Committees: budget cycles, approval limits, variance, reforecasts, committees and controls."""
CODE = 'mining5_budget_gov'
BOOK = {
    "title": "Budget Governance and Capital Committees",
    "subtitle": "Budget cycles, approval limits, variance and controls",
    "chapters": [
        ("Who decides how money is spent",
         "Budget governance sets who may spend what, and how the spending is checked. It keeps money tied to the plan. Good governance is quiet most of the time, and it matters most when a large sum is at stake."),
        ("The budget cycle",
         "A budget cycle is a repeated yearly process of planning, approving, spending and reviewing. Each stage feeds the next. Teams that skip the review repeat last year's mistakes."),
        ("Approval limits",
         "An approval limit is the largest amount a person may approve without a higher sign-off. Limits match responsibility to seniority. They should be published, and checked regularly."),
        ("Variance and reforecasts",
         "A variance is the gap between planned and actual spending. Small variances are normal; large or repeated ones need an explanation. A reforecast updates the year's expected results when the facts change."),
        ("Capital committees",
         "A capital committee decides on large investments, based on their business case and risk. It asks whether the return is real, and what happens if the plan goes wrong. Its decisions are recorded with reasons."),
        ("Controls",
         "Controls include sign-off above set limits, regular reviews and separation of duties. A control that is never tested is just a hope. Test the controls, and fix the weak ones first."),
    ],
    "test": [
        ("What is a budget cycle?",
         [("a", "A bicycle race"), ("b", "A type of machine"), ("c", "A repeated process of planning, approving, spending and reviewing"), ("d", "The time between two lunches")], "c"),
        ("What is an approval limit?",
         [("a", "The largest amount a person may approve without a higher sign-off"), ("b", "The longest meeting allowed"), ("c", "The minimum number of meetings"), ("d", "The colour of the signature")], "a"),
        ("What does a budget variance show?",
         [("a", "The weather"), ("b", "The gap between planned and actual spend"), ("c", "The staff pay"), ("d", "The number of invoices")], "b"),
        ("What does a capital committee decide?",
         [("a", "The menu for staff events"), ("b", "Staff holiday dates"), ("c", "Office colours"), ("d", "Large investments, based on their business case and risk")], "d"),
        ("Which is a budget control?",
         [("a", "Ignoring overspending"), ("b", "Letting each team spend freely"), ("c", "Requiring sign-off for spending above set limits"), ("d", "Removing all limits")], "c"),
    ],
}
