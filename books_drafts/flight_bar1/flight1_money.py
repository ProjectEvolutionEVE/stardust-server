"""A Pilot's Money: the cost of flying, saving for your own ship, when a loan pays for itself, and an emergency fund for repairs."""
CODE = 'flight1_money'
BOOK = {
    "title": "A Pilot's Money",
    "subtitle": "The cost of flying, saving for a ship, borrowing wisely and a repair fund",
    "chapters": [
        ('What flying really costs',
         'Every flight costs more than fuel. Your time is the first cost: a long run keeps you from other work. Your body pays too, because your three bars drain about 2.2 points an hour on average while you are awake, and your bed is the fastest way to win them back. Your craft wears out like any machine, so it needs upkeep, which is called maintenance: checking and servicing it before it breaks.'),
        ('Income minus costs',
         'Budgeting comes down to one simple sum: what comes in, minus what goes out. Income is what you earn from trades, auctions and the Bank\'s desks. Costs include fuel, food, maintenance and the weekly payments on any loan. Every transfer gives you a receipt in your filing cabinet, so you can check where the money really went.'),
        ('Needs and wants',
         'A need keeps you flying and safe: fuel, food and the repairs that keep your craft fit to fly. A want is nice to have. Pay for your needs first, and decide on wants with what is left. Some foods give a quick burst and then a crash, and a crash can cost you more rest later, so a treat is a want, not a need.'),
        ('Saving, and the interest it earns',
         'Saving means setting money aside for a goal, such as a bigger hold or a new ship, before you spend it. Interest is money the Bank pays you for keeping your credits with it. Every Bank rate is an APR, a year\'s rate, and each week the Bank pays or charges the APR divided by 52 on the balance. A savings account pays 4% APR and lets you take money out at any time. A term deposit locks your money for 2, 4 or 8 weeks for a higher rate (5%, 6% or 7% APR), paid at the end, but if you close it early you lose all the interest it would have earned.'),
        ('Borrowing: when a loan pays for itself',
         'A loan lets you have something now and pay for it later, with interest on what you still owe. Before you sign, the Bank shows you the total you will pay back and the cost of borrowing. Ask one question: will this earn back more than it costs? A bigger hold that brings back more ore on each trip can pay for itself. A loan for treats earns nothing back, so every payment comes out of your income. Only the Bank lends, and only to a player wearing the Business uniform from the Closet: no Business bar, no loan. The APR falls as the bars rise, from 16% with one bar to 8% with five. If your top Business bar is silver, the Bank lends 80% of what you ask and you pay the other 20% down; a gold bar waives that. At a fair APR a short loan costs little: 1,000 credits at 16% APR over 8 weeks is 127 a week, 1,014 in all, so 14 of interest.'),
        ('Paying off early, and an emergency fund',
         'Paying a loan off early saves interest, because the early payoff is only what you still owe plus the interest up to that day. A missed payment brings a late fee, and your credit standing with the Bank falls, which makes the next loan harder to get. An emergency fund is money kept aside for surprises, such as a broken part, so a repair does not force you to borrow at a high rate.'),
    ],
    "test": [
        ('What is the simplest way to see whether you made a profit?',
         [('a', 'Count how many trips you took'), ('b', 'Add your income and your costs together'), ('c', 'Take your costs away from your income'), ('d', 'Look only at the credits you hold today')], 'c'),
        ('What happens if you close a term deposit before its term ends?',
         [('a', 'You get your money back but lose the interest it would have earned'), ('b', 'You earn double interest for closing early'), ('c', 'You lose the whole deposit'), ('d', 'Nothing changes, because the two kinds of deposit are the same')], 'a'),
        ('Which loan is most likely to pay for itself?',
         [('a', 'A loan for a treat you will eat this week'), ('b', 'A loan for a fancy ornament for your quarters'), ('c', 'A loan for new clothes for your closet'), ('d', 'A loan for a bigger hold that will bring back more ore than the loan costs')], 'd'),
        ('A repair you did not plan for suddenly costs a lot. What protects you best?',
         [('a', 'Borrowing at the highest APR straight away'), ('b', 'An emergency fund: money you set aside for surprises like this'), ('c', 'Ignoring the problem and hoping it fixes itself'), ('d', 'Spending your savings on wants first')], 'b'),
        ('What happens if a weekly loan payment is missed?',
         [('a', 'Nothing at all, because the Bank forgives it'), ('b', 'The loan is cancelled and you get a refund'), ('c', 'A late fee is added to what you owe, and your standing falls, so future loans are harder'), ('d', 'The interest rate drops for the next week')], 'c'),
    ],
}
