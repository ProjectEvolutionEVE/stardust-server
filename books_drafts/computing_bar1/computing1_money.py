"""Money by the Numbers: a budget as a simple program, saving and needs, compound interest, loans, scams, and keeping safe records."""
CODE = "computing1_money"
BOOK = {
    "title": "Money by the Numbers",
    "subtitle": "Budgets, saving, loans, scams and records, one step at a time",
    "chapters": [
        ("A budget is a simple program",
         "A budget works like a simple program. The input is the credits that come in, from your work, trades and sales, and the costs are what goes out. The result is what is left over; if it is below zero, cut a cost or find more income before your next payment is due. Keep a record of every credit in and out, like a program's log, and check it against your receipts."),
        ("Needs, wants and savings",
         "Pay for your needs first: food and drink, a bed to rest in, and the repairs your craft needs to fly safely. Next, move a set amount into savings before you spend on anything else, and keep an emergency fund for surprises such as a sudden repair. Wants, like a new colour for your uniform, come last and only from what is left. A savings goal names what you are saving for, such as a new ship, and shows how far you have got."),
        ("Compound interest, one step at a time",
         "Compound interest means the interest you earn is added to your balance, so the next interest payment is worked out on a bigger amount. Take 10,000 credits at the Bank's savings rate of 0.5% a week: after one week it is 10,050, after two weeks 10,100.25, and after four weeks 10,201.51. Simple interest, worked out only on the first 10,000, would give 10,200 after four weeks, so the gap is small at first but grows to about 12,960 against 12,600 after a year. The Bank's savings account adds your earned interest to the balance each time you deposit or take money out, so these figures show how compounding works rather than the exact figures your account shows."),
        ("When a loan makes sense",
         "A loan is money you borrow and pay back with interest, which is the fee for using it. The Bank's loans cost 6 to 12 percent a week, depending on your repayment record, far more than a savings account earns. A loan makes sense only when what it helps you earn is more than what it costs, such as a machine that brings in more each week than its weekly payment. Paying early saves interest, because the early-payoff amount is what you owe plus interest only up to that day; missed payments bring a late fee and lower your credit standing."),
        ("Too good to be true",
         "An offer that promises a big, safe gain with no risk, and a deadline to act now, is the classic sign of a scam. Honest savings grow slowly and steadily, and a real bank states its rates and its risks plainly. In the game, players never message each other, so any message that claims to come from another player is not real. Walk away from anyone who asks for an up-front fee to release money, however friendly they sound."),
        ("Protect your account and keep receipts",
         "Your sign-in code is a six-digit number sent to your phone or email each time you sign in. Never share it, and type it only into the sign-in screen, even if someone says they work for the game or the Bank. Every transfer of goods gives you a receipt with a code that anyone can check, so keep your receipts and save copies of the important ones to your own device."),
    ],
    "test": [
        ("Your budget ends the week with less than nothing left over. What is the best first step?",
         [("a", "Spend more on wants and hope the next week is better"), ("b", "Throw away the receipts so the total looks better"), ("c", "Cut a cost or find more income before your next payment is due"), ("d", "Borrow the whole shortfall at once without a plan")], "c"),
        ("Why does compound interest pull ahead of simple interest over a long time?",
         [("a", "The Bank pays a bonus at the very end"), ("b", "Loans never charge interest on the balance"), ("c", "The rate rises a little each week"), ("d", "Interest you have earned is added to the balance, so it earns interest too")], "d"),
        ("Which loan is most likely to be worth taking?",
         [("a", "One for a want that brings in no credits"), ("b", "One for a machine whose weekly earnings are more than its weekly payment"), ("c", "One you plan to skip paying"), ("d", "One you take only because the Bank offered it")], "b"),
        ("You pay off a loan three days into its week. What does paying early do?",
         [("a", "You owe what is left plus interest only up to that day, so the rest of the week's interest is saved"), ("b", "You pay a late fee for finishing early"), ("c", "You owe the full week's interest, as if you had waited"), ("d", "You must wait for the loan to end before you can pay it")], "a"),
        ("A message offers a safe, large gain and asks for your sign-in code to unlock it. What should you do?",
         [("a", "Share the code, since the gain is safe"), ("b", "Pay the up-front fee quickly before the offer ends"), ("c", "Refuse, and never share your sign-in code"), ("d", "Send the code to a friend who is also a player")], "c"),
    ],
}
