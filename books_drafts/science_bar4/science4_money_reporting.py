"""Financial Reporting and Audit for Grants: spend reports, supporting documents, audit trails and corrections."""
CODE = "science4_money_reporting"
BOOK = {
    "title": "Financial Reporting and Audit for Grants",
    "subtitle": "Proving every pound was spent as promised",
    "chapters": [
        ("Spend reports", "A spend report shows what was spent on a grant, against each budget line, over a period. Funders use these reports to check progress and value. They should match the accounts exactly."),
        ("Supporting documents", "Every cost needs a supporting document, such as an invoice, a receipt or a payslip. Documents should be filed in a way that makes them easy to find. Missing paperwork is a common reason for audit problems."),
        ("Audit trails", "An audit trail shows who approved each cost, when, and why. It lets an auditor follow a payment from the bank to its original purpose. A clear trail makes an audit faster and calmer."),
        ("Variance reporting", "Variance is the difference between the budget and the actual spend. Reporting variances explains why costs were higher or lower than planned. Large variances should be explained to the funder early."),
        ("Corrections", "Mistakes happen, and they can be corrected. A correction should be recorded with its reason, the amount and the date. Hiding an error is far more harmful than correcting it openly."),
        ("Audit findings", "An audit may find errors, missing documents or costs that break the grant rules. Each finding should be answered with an action plan. Learning from findings makes the next audit easier."),
    ],
    "test": [
        ("What does a spend report show?",
         [("a", "The colour of the lab walls"), ("b", "What was spent on a grant, against each budget line"), ("c", "The number of journal pages"), ("d", "The names of visitors")], "b"),
        ("What is a supporting document?",
         [("a", "An invoice, receipt or payslip that proves a cost"), ("b", "A holiday card"), ("c", "A map of the campus"), ("d", "A lab sticker")], "a"),
        ("What does an audit trail show?",
         [("a", "The weather on the day of purchase"), ("b", "The number of pens in a drawer"), ("c", "The author of a poem"), ("d", "Who approved a cost, when, and why")], "d"),
        ("What is variance in grant reporting?",
         [("a", "The number of staff"), ("b", "The difference between the budget and the actual spend"), ("c", "The price of coffee"), ("d", "The grant's name")], "b"),
        ("What is the best response to a mistake in a grant account?",
         [("a", "Hide it"), ("b", "Delete the record"), ("c", "Correct it openly, with its reason, amount and date"), ("d", "Pretend it never happened")], "c"),
    ],
}
