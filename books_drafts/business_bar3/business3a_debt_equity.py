"""Debt and Equity (Manager, bar 3, part A): borrowing money you must repay, against owners who share in the business."""
CODE = "business3a_debt_equity"
BOOK = {
    "title": "Debt and Equity",
    "subtitle": "Borrowing money you must repay, against owners who share in the business",
    "chapters": [
        ("Two ways to fund a business",
         "A business can fund itself with debt or with equity. Debt is money borrowed and repaid with interest. Equity is money put in by owners, who share in the results instead. Each choice has a different cost and a different risk."),
        ("Debt is a fixed promise",
         "Debt comes with a promise. The loan must be repaid on its schedule, with interest, whether the business has a good week or a bad one. The lender does not share in your profit, but a missed payment brings fees and a lower standing."),
        ("Equity shares the result",
         "Equity means the owners share the results. They gain when the business earns, and they carry some of the loss when it does not. Equity needs no fixed repayment schedule, but the owners give up a share of what the business earns, and some say in how it is run."),
        ("The debt-to-equity ratio",
         "The debt-to-equity ratio divides what the business owes by its equity. Two thousand credits of debt against three thousand of equity gives a ratio of about 0.67. A higher ratio means more of the business is funded by borrowing, and so more risk."),
        ("Which to choose",
         "Borrowing often makes sense when the purchase is expected to earn more than the loan costs and a steady income covers the payments. Owners' money fits better when income is uncertain, because nothing has to be paid back on a fixed day."),
        ("A note on the game",
         "The Starship Bank's loans in the game are debt: borrowed, repaid on a set schedule, with interest. This book describes the real-world choice between debt and equity that sits behind every such loan."),
    ],
    "test": [
        ("What is debt?",
         [("a", "Money put in by owners"), ("b", "Profit kept in the business"), ("c", "Stock waiting to be sold"), ("d", "Money borrowed and repaid with interest")], "d"),
        ("What does equity mean for its owners?",
         [("a", "They share in the results, gaining when the business earns and carrying some loss when it does not"), ("b", "They must repay a fixed schedule"), ("c", "They pay interest to lenders"), ("d", "They never face any risk")], "a"),
        ("A business owes 2,000 credits and has equity of 3,000. What is its debt-to-equity ratio?",
         [("a", "1.5"), ("b", "3"), ("c", "About 0.67"), ("d", "5,000")], "c"),
        ("Why is a high debt-to-equity ratio riskier?",
         [("a", "Because equity must always be repaid"), ("b", "Because more of the business is funded by borrowing, with fixed payments to make"), ("c", "Because it means no interest is paid"), ("d", "Because it lowers the stock")], "b"),
        ("When is borrowing most sensible?",
         [("a", "When a purchase is expected to earn less than the loan costs"), ("b", "When the loan is due tomorrow with no plan"), ("c", "When income is unknown and uncertain"), ("d", "When a purchase is expected to earn more than the loan costs and steady income covers the payments")], "d"),
    ],
}
