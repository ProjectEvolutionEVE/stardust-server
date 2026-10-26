"""Loan Terms in Business (Manager, bar 3, part A): weekly rates, weekly payments and what a loan really costs over its life."""
CODE = "business3a_loan_terms"
BOOK = {
    "title": "Loan Terms in Business",
    "subtitle": "Weekly rates, weekly payments and what a loan really costs over its life",
    "chapters": [
        ("The three terms",
         "A loan's terms are its rate, its length and its payment. The rate is the price of the money, given as a percentage per week at the Starship Bank. The length is the number of weeks to repay it. The payment is what is due each week. Read all three before you sign."),
        ("Interest on what is left",
         "Interest is charged on what you still owe, not on the amount you first borrowed. Each week the balance grows by the interest and falls by the payment. So the interest itself shrinks over time, as the balance comes down."),
        ("The weekly payment",
         "The payment that clears a loan in a set number of weeks comes from a formula, rounded up to a whole credit. The Bank works it out for you. For example, a loan of 2,000 credits at 8% a week over 5 weeks has a weekly payment of 501 credits."),
        ("Total cost",
         "Multiply the payment by the number of weeks to get the total you pay back. Take away the amount borrowed, and what is left is the cost of borrowing. For that loan, 501 times 5 is 2,505, so the loan costs 505 credits."),
        ("Compare on the same basis",
         "A weekly rate adds up quickly over a year, so compare loans on the same time basis. Look at the total cost as well as the rate. A lower rate over a much longer term can still cost more in total than a higher rate over a short one."),
        ("Early payment and missed payments",
         "Paying early saves the interest not yet charged. A late payment adds a fee to what you owe and lowers your standing, which makes later loans harder to get. Before you sign, check the rate, the length, the payment, the total and the late fee."),
    ],
    "test": [
        ("What are the three main terms of a loan?",
         [("a", "Colour, weight and size"), ("b", "Rate, length and payment"), ("c", "Price, floor and bid"), ("d", "Savings, goals and receipts")], "b"),
        ("What is interest charged on, in a loan that is being repaid?",
         [("a", "The first amount ever borrowed"), ("b", "The payments you make"), ("c", "The fees you have paid"), ("d", "What you still owe")], "d"),
        ("A loan of 2,000 credits at 8% a week over 5 weeks has weekly payments of 501. What is its total cost?",
         [("a", "505 credits"), ("b", "501 credits"), ("c", "2,000 credits"), ("d", "2,505 credits")], "a"),
        ("Why compare loans on their total cost, not only on the rate?",
         [("a", "The rate is always the same"), ("b", "The total cost is always lower"), ("c", "A lower rate over a longer term can still cost more in total"), ("d", "The Bank hides the total")], "c"),
        ("What happens if a weekly payment is missed?",
         [("a", "The loan is forgiven"), ("b", "A late fee is added to what you owe, and your standing falls"), ("c", "The rate falls"), ("d", "Nothing changes")], "b"),
    ],
}
