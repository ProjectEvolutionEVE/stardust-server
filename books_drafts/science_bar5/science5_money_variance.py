"""Budget Variance and Cost Control in Projects: finding the gap between plan and spending, and bringing costs back under control."""
CODE = "science5_money_variance"
BOOK = {
    "title": "Budget Variance and Cost Control in Projects",
    "subtitle": "Variance types, root causes, corrective actions, forecast updates, spending authority and reporting",
    "chapters": [
        ("What variance means", "Budget variance is the difference between planned spending and actual spending. A positive or negative gap is only a signal. It tells you that something has changed, and that it is time to look more closely."),
        ("Types of variance", "Variance can be a price variance, when items cost more or less than planned, or a quantity variance, when more or less of an item is used. Timing variances show when money is spent earlier or later than planned. Naming the type helps find the cause."),
        ("Root causes", "A root cause is the underlying reason spending differed from plan. It may be a price rise, a change of scope, a delay or a poor estimate. Fixing the symptom alone usually lets the gap return."),
        ("Corrective actions", "A corrective action is a step taken to bring spending back under control. It might mean renegotiating a contract, cutting scope or changing the schedule. Each action should have an owner and a date."),
        ("Forecast updates", "A forecast update estimates the likely final cost, based on what is now known. Managers and funders need to see that forecast early, so they can decide what to do. Late forecasts leave less room for action."),
        ("Spending authority and reporting", "Spending authority sets the limit each person may approve. Keeping spending inside those limits keeps control with the right people. Regular reports show variances, causes and actions, so decisions are based on facts."),
    ],
    "test": [
        ("What is budget variance?",
         [("a", "The name of a budget document"), ("b", "A bank loan taken for a project"), ("c", "The difference between planned spending and actual spending"), ("d", "A rule about staff leave")], "c"),
        ("What is a root cause of a variance?",
         [("a", "The date the budget was printed"), ("b", "The office location of the team"), ("c", "The team's name"), ("d", "The underlying reason the spending differed from plan")], "d"),
        ("What is a corrective action?",
         [("a", "A step taken to bring spending back under control"), ("b", "A new coat of paint for the lab"), ("c", "A day off for the team"), ("d", "A renewal of a grant")], "a"),
        ("Why update the forecast?",
         [("a", "So that managers and funders can see the likely final cost"), ("b", "To hide overspending"), ("c", "Because forecasts never change"), ("d", "To stop reporting altogether")], "a"),
        ("What does spending authority mean?",
         [("a", "Permission to spend nothing at all"), ("b", "Ownership of a bank"), ("c", "The power to set salaries"), ("d", "The limit someone may approve, so spending stays with the right person")], "d"),
    ],
}
