"""Cash Flow and Payment Timing in Research: payment schedules, reimbursement delays, buffers and forecasts."""
CODE = "science4_money_cash_flow"
BOOK = {
    "title": "Cash Flow and Payment Timing in Research",
    "subtitle": "When money arrives, and when it must leave",
    "chapters": [
        ("Payment schedules", "A payment schedule lists when a funder will pay each instalment. Many grants pay in parts, tied to progress or dates. The schedule shows when money will be available."),
        ("Reimbursement delays", "Some grants pay back costs only after they have been spent and reported. This creates a gap, because bills must be paid before the money arrives. Delays of several months are common in some systems."),
        ("Cash buffers", "A cash buffer is money kept in the bank to cover these gaps. It lets a group pay salaries and suppliers on time. Setting a buffer size is part of sound financial planning."),
        ("Timing of purchases", "Buying a large item at the wrong time can drain cash when it is needed most. Planning purchases around payment dates avoids shortages. Some purchases can be delayed without harm to the work."),
        ("Grant drawdown", "Drawdown is the act of claiming grant money as costs are incurred. Some funders release money only on request, and others pay on a set timetable. Knowing the rules prevents delays."),
        ("Cash forecasts", "A cash forecast tracks the money coming in and going out, month by month. It shows gaps before they happen, so action can be taken early. Cash forecasts differ from budgets, because they focus on timing."),
    ],
    "test": [
        ("What does a payment schedule show?",
         [("a", "The lab's chemical list"), ("b", "The shape of the lab bench"), ("c", "When each instalment of funding will be paid"), ("d", "The names of reviewers")], "c"),
        ("Why do reimbursement delays cause problems?",
         [("a", "Bills must be paid before the money arrives"), ("b", "They make costs disappear"), ("c", "They change the colour of the budget"), ("d", "They remove the need for reports")], "a"),
        ("What is a cash buffer for?",
         [("a", "Covering the walls of a lab"), ("b", "Storing samples at low temperature"), ("c", "Keeping a chemical reaction stable"), ("d", "Covering gaps so bills and salaries are paid on time")], "d"),
        ("What is grant drawdown?",
         [("a", "Drawing a picture of the project"), ("b", "Removing a grant from the bank"), ("c", "Claiming grant money as costs are incurred"), ("d", "Cancelling a project")], "c"),
        ("How does a cash forecast differ from a budget?",
         [("a", "It ignores all money"), ("b", "It focuses on when money moves, month by month"), ("c", "It is written in a different language only"), ("d", "It is never updated")], "b"),
    ],
}
