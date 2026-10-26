"""Credit Scores and Reports: what is measured, and how a good record is built."""
CODE = "business4_creditscore"
BOOK = {
    "title": "Credit Scores and Reports",
    "subtitle": "What is measured, and how a good record is built",
    "chapters": [
        ("What a report holds",
         "A credit report lists accounts, balances, payment history and enquiries. Credit reference agencies compile it from lenders and public records. A credit score summarises the report as one number."),
        ("What is measured",
         "Common scores weigh payment history most heavily. Then they look at how much of the available credit is in use, how long accounts have been open, how many new accounts were opened, and the mix of credit types. The exact weights vary by scoring model."),
        ("Payment history",
         "Paying on time is the most important habit. A missed payment can stay on a report for years and lower a score. Setting up automatic payments of at least the minimum is a simple protection."),
        ("Utilisation",
         "Utilisation is the share of a credit limit that is in use. Keeping balances low relative to limits usually helps a score. Using a small amount of credit regularly, and paying it off in full, is a common approach."),
        ("Fixing errors",
         "Mistakes on reports do happen. Check your report regularly. If you find an error, file a dispute with the agency and the lender. Keep copies of your records, and follow up until the error is corrected."),
        ("Building a good record",
         "Build a long record of on-time payments, keep balances modest, and avoid applying for many accounts at once. Patience matters, because a good history takes time. This is general education, not personal financial advice."),
    ],
    "test": [
        ("What does a credit report list?",
         [("a", "Only the borrower's height"), ("b", "Accounts, balances, payment history and enquiries"), ("c", "The price of cars"), ("d", "The country's GDP")], "b"),
        ("Which factor do common credit scores weigh most heavily?",
         [("a", "Shoe size"), ("b", "The bank's logo"), ("c", "Payment history"), ("d", "The age of the phone")], "c"),
        ("What is utilisation?",
         [("a", "The share of a credit limit in use"), ("b", "The interest rate"), ("c", "The number of pages in a report"), ("d", "A bank fee")], "a"),
        ("What should you do about an error on your report?",
         [("a", "Ignore it"), ("b", "Pay the error"), ("c", "Close all accounts"), ("d", "Dispute it with the agency and the lender")], "d"),
        ("Why do missed payments matter?",
         [("a", "They can stay on a report for years and lower a score"), ("b", "They are free"), ("c", "They raise the score at once"), ("d", "They are never recorded")], "a"),
    ],
}
