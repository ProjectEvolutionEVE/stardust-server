"""Profit, Cash and Credit (Trader, bar 1): profit versus cash in hand, budgeting, a cash reserve, and what borrowing really costs. Builds on the Trading book and the Starship Bank's rules (CLAUDE.md rule 36); credits are game credits only."""
CODE = "business1_money"
BOOK = {
    "title": "Profit, Cash and Credit",
    "subtitle": "Profit versus cash in hand, budgeting, saving, and the true cost of borrowing",
    "chapters": [
        ("Profit is not cash in hand",
         "Profit is what is left after your costs, worked out on paper. Cash in hand is the credits you can spend today. A trader can show a good profit and still be short of cash, because ore sitting in the cargo hold is not credits until it is sold. Your receipts log in the filing cabinet shows the money in and the money out, so check it before you count your profit."),
        ("Budgeting: income minus costs",
         "A budget is simple: your income minus your costs. Income comes from your sales, your auctions and the Bank's desks. Costs include the lots you buy, any fees such as the 2.5% auction fee or the printing fees, loan payments, and the food and supplies you need. Plan the week before you place your orders, so you know what you can afford."),
        ("Needs first, then wants",
         "A need is something your work depends on, such as the supplies that keep you working. A want is nice to have, such as a new uniform from the closet. Pay for your needs first, and only spend on wants from what is left. When money is tight, a want is the first thing to wait for."),
        ("A cash reserve for hard weeks",
         "A cash reserve is money set aside for things that go wrong: a bad week of prices, a repair, or a fee you did not expect. A common goal is enough to cover a few weeks of your costs. The savings account is a good place for it, because you can take money out at any time, and the Bank's savings goal for an emergency fund keeps you on track. Real households and businesses do the same thing."),
        ("The cost of borrowing",
         "Interest is the price of money. Savings and term deposits earn it for you, at the Bank's rates. A loan charges it to you, at 6 to 12 percent a week, worked out on what you still owe. Before you sign, the Bank shows the total cost of borrowing and what the purchase is expected to earn. A loan of 1,000 credits at 6 percent a week over 4 weeks costs about 289 credits a week, or 1,156 in all, so borrowing costs 156 credits."),
        ("Paying early, and why interest grows",
         "Interest added to your balance then earns interest too, which is compound growth. Saving and reinvesting your earnings lets it grow faster over time. Paying a loan off early saves interest, because the Bank only charges interest on what is still owed up to the day you pay. Missed payments bring a late fee and lower your credit standing, so pay on time."),
    ],
    "test": [
        ("What is the difference between profit and cash in hand?",
         [("a", "They are always the same number"), ("b", "Cash in hand is the value of your ship"), ("c", "Profit is what is left after costs, on paper; cash in hand is the credits you can spend now"), ("d", "Profit is always bigger than cash in hand")], "c"),
        ("What does a simple budget work out?",
         [("a", "Income plus savings"), ("b", "Costs minus the floor price"), ("c", "Income minus costs"), ("d", "The value of the cargo hold")], "c"),
        ("What is a cash reserve for?",
         [("a", "To buy every item the moment its price falls"), ("b", "To cover unexpected costs, so you need not borrow at high weekly rates when something goes wrong"), ("c", "To make your savings look bigger to other traders"), ("d", "To pay for wants before needs")], "b"),
        ("A loan costs 6 percent a week. The trade you would borrow for is expected to earn 4 percent a week. What should you do?",
         [("a", "Borrow the full amount, since any earning is good"), ("b", "Borrow for the longest term, since it has the lowest weekly payment"), ("c", "Do not borrow for it, because it costs more than it earns"), ("d", "Borrow, since the Bank will forgive the interest later")], "c"),
        ("Why does paying a loan off early save you interest?",
         [("a", "The Bank pays you back the interest you have paid"), ("b", "The interest is fixed at the start, so it is cheaper to finish early"), ("c", "Early payoff raises your standing by one payment"), ("d", "Interest is charged only on what is still owed up to the day you pay, so the interest not yet charged is saved")], "d"),
    ],
}
