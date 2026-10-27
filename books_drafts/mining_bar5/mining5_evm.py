"""Earned Value Management: planned value, earned value, cost and schedule indices, forecasts, controls and limits."""
CODE = 'mining5_evm'
BOOK = {
    "title": "Earned Value Management",
    "subtitle": "Planned value, earned value, cost and schedule indices and forecasts",
    "chapters": [
        ("Measuring progress in money",
         "Earned value management compares the work planned, the work done and the money spent. It turns progress into numbers that can be checked. Project teams use it to see trouble early, while there is still time to act."),
        ("Planned value",
         "Planned value is the budgeted value of the work scheduled to be finished by a given date. It is the plan, written in money. Planned value does not change just because the work is late."),
        ("Earned value",
         "Earned value is the budgeted value of the work actually completed. If a task was budgeted at 100 thousand and is half done, its earned value is 50 thousand. Earned value measures progress, not spending."),
        ("Cost and schedule indices",
         "The cost performance index divides earned value by actual cost. A value below 1 means the work costs more than budgeted. The schedule performance index divides earned value by planned value, and shows whether work is ahead of or behind plan."),
        ("Forecasts",
         "Using the indices, a team can forecast the final cost and the finish date. The forecast assumes today's performance continues, so it is only as good as the data. Forecasts should be updated regularly."),
        ("Controls and limits",
         "Controls act on the numbers: re-plan the work, change the scope, or bring in help. EVM has limits. It depends on honest estimates of progress, and it can hide problems in work that is hard to measure."),
    ],
    "test": [
        ("What does planned value measure?",
         [("a", "The budgeted value of work scheduled to be finished by this date"), ("b", "The money the company has in the bank"), ("c", "The number of workers on site"), ("d", "The value of the finished asset")], "a"),
        ("What is earned value?",
         [("a", "The cost of the tools used this month"), ("b", "The price paid to suppliers"), ("c", "The budgeted value of the work actually completed"), ("d", "The total of all bonuses paid")], "c"),
        ("What does a cost performance index below 1 mean?",
         [("a", "The work costs less than planned"), ("b", "The work costs more than budgeted for what has been done"), ("c", "The work finished early"), ("d", "The costs have not changed")], "b"),
        ("What does the schedule performance index show?",
         [("a", "The colour of the chart"), ("b", "The price of steel"), ("c", "The number of invoices"), ("d", "Whether work is ahead of or behind the planned schedule")], "d"),
        ("What is one limit of earned value management?",
         [("a", "It needs no data at all"), ("b", "It replaces all site visits"), ("c", "It depends on honest estimates of progress"), ("d", "It works only for software projects")], "c"),
    ],
}
