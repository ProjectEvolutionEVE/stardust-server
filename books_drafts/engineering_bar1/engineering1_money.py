"""Costing a Build: materials, labour and printing fees, what each copy really costs, and how to pay for a plant without losing ground."""
CODE = 'engineering1_money'
BOOK = {
    "title": 'Costing a Build',
    "subtitle": 'What a build really costs, and how to pay for it',
    "chapters": [
        ('What a build costs',
         'Every build has three kinds of cost. Materials are the raw materials you take from the cargo hold, at what they cost you on the market. Labour is the time your crew spends on the job, and it counts even when no credits change hands. Printing fees are what the Starship Bank charges to print copies of a design: 100 credits once, with a design\'s first run, and then 10 credits for each copy.'),
        ('Cost per copy',
         'Add up everything a run costs, then divide by the number of copies. Take a first run of 25 copies. The setup fee is 100, and the copies come to 25 times 10, so the printing alone is 350 credits. That is 14 a copy. Materials and labour for each copy come on top. The setup fee is paid only once, so the bigger the run, the less of it each copy carries.'),
        ('Saving or borrowing',
         'A production plant costs a lot before it earns anything. You can save up for it, or borrow from the Bank and build now. Saving costs you time, but you pay no interest. Your savings grow at the Bank\'s savings rate, and a term deposit pays more the longer you lock it up. Take a term deposit out early and you give up its interest, so choose the term before you start.'),
        ('What borrowing really costs',
         'Take a loan of 1,000 credits at 8% a week, paid back over 8 weeks, and each weekly payment is 175 credits. That comes to 1,400 in all, so the loan costs 400 in interest. Interest is charged only on what you still owe, so every payment clears some interest and the rest cuts the debt. Before you sign, the Bank shows you the total cost and what the purchase should earn. Ask one question: will it pay for itself?'),
        ('Payback time',
         'Payback time is the cost divided by what the build earns each week after its running costs. A plant that costs 1,000 and earns 250 a week pays back in 4 weeks. With a loan, the weekly payments come out of that same money, so the loan is paid first. Paying a loan off early saves interest: the payoff is what you still owe, plus interest only up to that day.'),
        ('Upkeep and records',
         'Set money aside each week for upkeep, before anything breaks. A machine that stops costs you output, and a repair you must borrow for at 6 to 12% a week costs far more than the same repair paid from savings. Pay every loan payment on its date: a late payment adds a fee and lowers your credit standing. Keep every receipt in the receipts log in your Private Quarters, and check your numbers against them.'),
    ],
    "test": [
        ('How many credits does a first print run of 25 copies cost in printing fees?',
         [('a', '250'), ('b', '125'), ('c', '350'), ('d', '2,500')], 'c'),
        ('Why does the cost per copy fall as a print run gets bigger?',
         [('a', 'The Bank pays part of each copy'), ('b', 'The setup fee is paid once, so it is shared across more copies'), ('c', 'Each copy needs less material'), ('d', 'Copies are printed faster')], 'b'),
        ('What is the main reason to pay a loan off early?',
         [('a', 'The Bank gives you back the fee'), ('b', 'The Bank charges a bigger late fee'), ('c', 'Your credit standing goes down'), ('d', 'It saves the interest you have not yet been charged')], 'd'),
        ('A plant costs 1,000 credits and earns 250 a week after its running costs. About how many weeks does it take to pay for itself?',
         [('a', '10'), ('b', '40'), ('c', '4'), ('d', '25')], 'c'),
        ('Why is it wise to set money aside for upkeep each week?',
         [('a', 'So a needed repair can be paid from savings, not borrowed at a high weekly rate'), ('b', 'Because the Bank pays nothing on savings'), ('c', 'So a machine never needs a receipt'), ('d', 'Because upkeep is free once it has been paid for')], 'a'),
    ],
}
