"""Pay Equity Audits in Engineering: how a team checks that similar work is paid fairly, and what to do about gaps."""
CODE = "computing5_pay_equity_audits"
BOOK = {
    "title": "Pay Equity Audits in Engineering",
    "subtitle": "Checking that similar work is paid fairly, and acting on what the check finds",
    "chapters": [
        ("Audit scope",
         "A pay equity audit defines which roles, levels and locations it covers before any numbers are pulled. A clear scope stops the review from drifting. Write down the questions the audit must answer."),
        ("Statistical comparisons",
         "Statistics compare pay for people in similar roles, at similar levels, with similar experience. A regression model can test whether a gap remains after those factors are accounted for. Small groups can give unreliable results, so read the figures with care."),
        ("Explaining gaps",
         "A gap is not proof of unfairness on its own. Some gaps come from the mix of roles, start dates or location. The audit should say which gaps are explained by known factors and which are not."),
        ("Remediation budgets",
         "Where a gap is unexplained, the team sets a budget to correct it. Corrections are often spread over several review cycles. Plan the budget before announcing the audit, so promises can be kept."),
        ("Privacy of pay data",
         "Pay records are sensitive. Limit who can see individual figures, and report only group results. Keep the working files secure and delete them when the audit ends."),
        ("Reporting",
         "Report the method, the results and the actions taken, in plain language. Show what was checked and what was not. An honest report earns more trust than a short, polished one."),
    ],
    "test": [
        ("Why must the scope of a pay equity audit be set first?",
         [("a", "So the results can be hidden"), ("b", "So the review does not drift away from its questions"), ("c", "So no one needs to check the figures"), ("d", "So pay can be set lower")], "b"),
        ("What does a regression model help the audit test?",
         [("a", "The colour of each team's office"), ("b", "The number of coffee breaks"), ("c", "The age of each employee"), ("d", "Whether a gap remains after known factors are accounted for")], "d"),
        ("Why is a gap alone not proof of unfairness?",
         [("a", "Some gaps come from roles, start dates or location"), ("b", "Gaps never exist in pay"), ("c", "Statistics cannot measure pay"), ("d", "Audits are only for managers")], "a"),
        ("How should pay data be reported?",
         [("a", "Only as individual names and figures"), ("b", "Posted publicly with every salary"), ("c", "Only in group results, with individual figures kept private"), ("d", "Never shared with anyone at all")], "c"),
        ("What should an honest audit report include?",
         [("a", "Only the results that look good"), ("b", "The method, the results and the actions taken"), ("c", "A list of who to blame"), ("d", "A promise without a budget")], "b"),
    ],
}
