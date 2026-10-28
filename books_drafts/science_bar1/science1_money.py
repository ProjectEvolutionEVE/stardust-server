"""Budgeting a Research Project: planning a budget before an experiment, tracking spending against it, and using the Starship Bank wisely. Science career, bar 1 (Research Assistant)."""
CODE = 'science1_money'
BOOK = {
    "title": 'Budgeting a Research Project',
    "subtitle": 'Planning a budget, tracking it, and thinking about money the way you think about an experiment',
    "chapters": [
        ('Plan the budget first',
         'A budget starts with two lists: what comes in and what goes out. Write it down before you spend a single credit, just as you write down a guess before you test it. Put the needs first, such as the ore lots and parts your experiment cannot run without, and let wants like a new uniform from the closet wait. Credits here are for the game only and never turn into real money.'),
        ('Measure, compare, adjust',
         'Track what you actually spend, and check it against the plan, the way you measure an experiment. Keep a record of every purchase: the receipts log in your filing cabinet holds a copy of each transfer. Compare the total you spent with the plan for the same week. If you are over, adjust the next week\'s plan instead of hoping it will fix itself.'),
        ('Saving and long-term goals',
         'Money you do not need yet can grow in savings. The Starship Bank\'s savings account pays 4% APR, a year\'s rate, and you may take money out at any time. Savings goals name what you are saving for, such as a new ship, a production plant or an emergency fund, and show how close you are. Some big goals take years of steady saving, so small amounts put aside each week matter more than one lucky trade.'),
        ('Interest earned and interest paid',
         'Interest is the price of money. When you put credits in the Bank, the Bank pays you interest, and when you borrow, you pay it. A term deposit locks your credits for 2, 4 or 8 weeks and pays more, at 5%, 6% or 7% APR, paid when the term ends. Each week the Bank pays or charges the APR divided by 52 on the balance. Close it early and you get back only what you put in, so the interest is lost.'),
        ('When a loan makes sense',
         'A loan is worth taking when what you buy earns back more than the loan costs. At 12% APR, a 1,000-credit loan over 8 weeks costs 10 credits in interest (127 a week, 1,010 in all), so the thing you buy must bring back more than that. Only the Bank lends, and only to a player wearing the Business uniform from the Closet; the APR runs from 16% with one bar down to 8% with five, and a silver top bar means a 20% down payment. Supplies that are used up and bring nothing back are the hardest to justify. If you cannot see how the money pays itself back, do not borrow it.'),
        ('Paying off early and the safety fund',
         'Paying a loan off early saves the interest for the weeks that would still have been charged, and the Bank works out the payoff from today. A missed payment brings a late fee of 5% of the payment, added to what you owe, and it lowers your standing. Keep an emergency fund in savings, so an unexpected cost does not force a costly loan. In real life, many people aim for several months of basic costs.'),
    ],
    "test": [
        ('What should a budget list before you spend anything?',
         [('a', 'Only the things you would like to own'), ('b', 'The Bank\'s rates and nothing else'), ('c', 'What comes in and what goes out'), ('d', 'Only the costs that have already been paid')], 'c'),
        ('When is a loan worth taking?',
         [('a', 'When what it buys earns back more than the loan costs'), ('b', 'Whenever you want something right now'), ('c', 'Only when your savings are empty'), ('d', 'Because borrowing is always cheaper than saving')], 'a'),
        ('What is an emergency fund for?',
         [('a', 'Buying wants when you feel lucky'), ('b', 'Keeping money out of the Bank altogether'), ('c', 'Earning the highest interest of all'), ('d', 'Covering an unexpected cost, so you do not have to borrow at a high rate or miss a payment')], 'd'),
        ('What happens if you close a term deposit before its term ends?',
         [('a', 'You get the full interest, paid early'), ('b', 'You get back what you put in, but the interest it would have earned is given up'), ('c', 'The Bank keeps the whole deposit as a fee'), ('d', 'It turns into a loan at the Bank')], 'b'),
        ('What does paying a loan off early usually do?',
         [('a', 'It adds a late fee to the loan'), ('b', 'It makes the Bank raise the rate on your other loans'), ('c', 'It saves the interest for the weeks that would still have been charged'), ('d', 'It cancels all of your savings goals')], 'c'),
    ],
}
