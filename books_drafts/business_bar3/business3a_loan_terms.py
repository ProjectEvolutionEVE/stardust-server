"""Loan Terms in Business (Manager, bar 3, part A): rates (APR), weekly payments and what a loan really costs over its life."""
CODE = "business3a_loan_terms"
BOOK = {
    "title": "Loan Terms in Business",
    "subtitle": "Rates (APR), weekly payments and what a loan really costs over its life",
    "chapters": [
        ("The three terms",
         "A loan's terms are its rate, its length and its payment. The rate is the price of the money, given as an APR, a year's rate, at the Starship Bank. Each week the Bank charges the APR divided by 52 on what you owe. The length is the number of weeks to repay it. The payment is what is due each week. Read all three before you sign. If your top Business bar is silver, the Bank lends only 80% of what you ask and you pay the other 20% down from your own credits; a gold top bar waives the down payment."),
        ("Interest on what is left",
         "Interest is charged on what you still owe, not on the amount you first borrowed. Each week the balance grows by that week's interest and falls by the payment. So the interest itself shrinks over time, as the balance comes down."),
        ("The weekly payment",
         "The payment that clears a loan in a set number of weeks comes from a formula, rounded up to a whole credit. The Bank works it out for you. For example, a loan of 2,000 credits at 8% APR over 5 weeks has a weekly payment of 402 credits."),
        ("Total cost",
         "Multiply the payment by the number of weeks to get the total you pay back. Take away the amount borrowed, and what is left is the cost of borrowing. For that loan, the Bank's total is 2,009 credits in all, so the loan costs 9 credits. At 16% APR the same loan costs 18 credits: 404 a week, 2,018 in all."),
        ("Compare on the same basis",
         "An APR is a year's rate, so it puts every loan on the same time basis. Look at the total cost as well as the rate. A lower rate over a much longer term can still cost more in total than a higher rate over a short one."),
        ("Early payment and missed payments",
         "Paying early saves the interest not yet charged. A late payment adds a fee to what you owe and lowers your standing, which makes later loans harder to get. Before you sign, check the rate, the length, the payment, the total and the late fee."),
    ],
    "test": [
        ("What are the three main terms of a loan?",
         [("a", "Colour, weight and size"), ("b", "Rate, length and payment"), ("c", "Price, floor and bid"), ("d", "Savings, goals and receipts")], "b"),
        ("What is interest charged on, in a loan that is being repaid?",
         [("a", "The first amount ever borrowed"), ("b", "The payments you make"), ("c", "The fees you have paid"), ("d", "What you still owe")], "d"),
        ("A loan of 2,000 credits at 8% APR over 5 weeks has weekly payments of 402 and 2,009 paid in all. What does the loan cost in interest?",
         [("a", "9 credits"), ("b", "402 credits"), ("c", "2,000 credits"), ("d", "2,009 credits")], "a"),
        ("Why compare loans on their total cost, not only on the rate?",
         [("a", "The rate is always the same"), ("b", "The total cost is always lower"), ("c", "A lower rate over a longer term can still cost more in total"), ("d", "The Bank hides the total")], "c"),
        ("What happens if a weekly payment is missed?",
         [("a", "The loan is forgiven"), ("b", "A late fee is added to what you owe, and your standing falls"), ("c", "The rate falls"), ("d", "Nothing changes")], "b"),
    ],
}
