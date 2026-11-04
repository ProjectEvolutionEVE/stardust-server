"""Earned Value and Project Cost Tracking: measuring how much work is really done for the money spent, and what that suggests about the finish."""
CODE = "science5_money_earned_value"
BOOK = {
    "title": "Earned Value and Project Cost Tracking",
    "subtitle": "Planned value, earned value, the cost performance index, the schedule index, forecasting and the limits of the metrics",
    "chapters": [
        ("Planned value", "Planned value is the budgeted cost of the work scheduled to be finished by a given date. It is the plan written in money. Comparing later results with it shows whether the project is on track."),
        ("Earned value", "Earned value is the budgeted value of the work actually completed by that date. It measures progress in money, not in days or effort. Two projects may have spent the same, but the one with more earned value has done more."),
        ("The cost performance index", "The cost performance index, or CPI, is earned value divided by actual cost. A value above 1 means the work is costing less than planned, and below 1 means it costs more. It is a simple way to read the cost picture."),
        ("The schedule performance index", "The schedule performance index compares the work completed with the work planned by now. A value below 1 means the project is behind its schedule. Read alongside the CPI, it shows whether problems are in cost, time or both."),
        ("Forecasting completion cost", "Forecasts estimate the final cost by assuming the current cost performance continues. The estimate is only as good as that assumption. Forecasts should be revisited as the work goes on."),
        ("Limits of the metrics", "Earned value depends on how well the work has been measured and how good the original estimates were. Early in a project, the figures can mislead because little work has been completed. The metrics are useful, but they need judgement and a check on the facts."),
    ],
    "test": [
        ("What is planned value?",
         [("a", "The money actually spent so far"), ("b", "The budgeted cost of the work scheduled to be done by a given date"), ("c", "The value of the building"), ("d", "The profit the project will make")], "b"),
        ("What is earned value?",
         [("a", "The cost of the team's lunch"), ("b", "Money held in the bank"), ("c", "The budgeted value of the work actually completed"), ("d", "The price of the next job")], "c"),
        ("What does the cost performance index show?",
         [("a", "The number of meetings held"), ("b", "The weather on site"), ("c", "The colour of the project plan"), ("d", "Earned value divided by actual cost, where a value below 1 means the work costs more than planned")], "d"),
        ("What does the schedule performance index compare?",
         [("a", "Cost with the paint colour"), ("b", "Staff numbers with room numbers"), ("c", "Work completed against work planned by now"), ("d", "Two different suppliers")], "c"),
        ("What is a limit of these metrics?",
         [("a", "They depend on the quality of estimates and of the work measure, and can mislead early in a project"), ("b", "They are always perfect"), ("c", "They cannot use cost figures"), ("d", "They only work for shops")], "a"),
    ],
}
