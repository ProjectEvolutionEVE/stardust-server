"""Medicine, bar 1: Health, Wealth and Choices. Money management for the Medic track: budgets, savings, needs and wants, interest, loans and receipts, tied to the Starship Bank and to your health. Credits are in-game only."""
CODE = 'medicine1_money'
BOOK = {
    "title": 'Health, Wealth and Choices',
    "subtitle": 'Budgets, savings and loans, and how money choices touch your health',
    "chapters": [
        ('Income minus costs',
         'A budget is simple arithmetic: what comes in, minus what goes out. Credits come in from trades, auctions and the Bank\'s market desks. Costs go out for food, supplies and the gear your work needs, so check the sum before you spend, and write it down once a week.'),
        ('Needs and wants',
         'A need is something your work and your health depend on, such as a wholesome meal, enough sleep and gear that keeps you safe. A want is nice to have, so pay for the needs first. A cheap-looking choice can cost you later: an energy drink lifts you fast, but both energy and focus then drain faster for hours, and your next sleep refills you more slowly. Food never replaces sleep.'),
        ('Saving and the emergency fund',
         'Saving means setting aside part of what you earn now, so you can use it later. The Bank\'s savings account pays a little interest and lets you take your credits out at any time. An emergency fund is money kept for surprises, such as an injury, an illness or broken gear, when you cannot work for a while. The Bank\'s savings goals include one called An emergency fund, so you can watch it grow.'),
        ('Interest earned and interest paid',
         'Interest is the price of money over time. When you deposit credits, the Bank pays you interest; when you borrow, you pay it. A term deposit pays more than a savings account, and the longer you lock it away, the higher its rate, but the interest is paid only at the end of the term. The Bank\'s screen shows the current rates before you choose.'),
        ('Borrowing well, and paying early',
         'A loan makes sense when what it buys earns more than it costs. The Bank\'s quote shows the weekly payment, the total you will pay back and the expected return, so ask "will it pay for itself?" before you sign. Loan rates run from 6% to 12% a week, and a weaker repayment record means a higher rate. Paying off early saves the interest that has not been charged yet, so use spare credits to clear the loan first.'),
        ('Receipts and steady money',
         'Every transfer of credits gives you a receipt with a code you can check, so keep them. They show where your money went and help you check your budget. A late payment adds a fee to what you owe and lowers your credit standing, which makes later borrowing harder. Money worry is a health cost too: stress can keep you awake, and poor sleep makes stamina and focus fall, so a simple, calm money plan protects your body as well as your credits.'),
    ],
    "test": [
        ('What is the simplest way to see whether you can afford your spending this week?',
         [('a', 'Add up your costs and ignore your income'), ('b', 'Spend first and see what is left later'), ('c', 'Subtract your costs from your income'), ('d', 'Ask someone else to pay for it')], 'c'),
        ('Over a long shift, which choice usually leaves you with more energy at the end?',
         [('a', 'A wholesome meal and a proper rest'), ('b', 'A sugary snack, then another, then another'), ('c', 'An energy drink every hour'), ('d', 'Skipping meals to save credits')], 'a'),
        ('What is the main job of an emergency fund?',
         [('a', 'To buy the newest ship as soon as it appears'), ('b', 'To pay the Bank interest on a loan you already have'), ('c', 'To earn the highest interest possible, whatever happens'), ('d', 'To cover surprise costs, such as an injury or broken gear, without borrowing in a hurry')], 'd'),
        ('You put credits into an eight-week term deposit and close it after three weeks. What do you get back?',
         [('a', 'Your credits plus the full interest'), ('b', 'Only what you put in, with no interest'), ('c', 'Double your credits'), ('d', 'Nothing at all')], 'b'),
        ('You have spare credits and a loan at a high weekly rate. What saves you the most?',
         [('a', 'Take out a second loan to cover the first'), ('b', 'Leave the loan alone and let the credits sit'), ('c', 'Pay the loan down early with the spare credits'), ('d', 'Skip the loan payment and pay the fee later')], 'c'),
    ],
}
