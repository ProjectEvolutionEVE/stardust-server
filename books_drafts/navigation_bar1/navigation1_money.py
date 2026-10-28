"""Charting a Course to Your Goals: budgets, savings goals, interest and loans, planned like a voyage."""
CODE = 'navigation1_money'
BOOK = {
    "title": 'Charting a Course to Your Goals',
    "subtitle": 'Budgets, savings goals, interest and loans, planned like a voyage',
    "chapters": [
        ('Income minus costs',
         'Every voyage starts with two numbers: what comes in and what goes out. Your income is the credits you earn, from sales on the market, from auctions and from the Bank\'s desks. Your costs are everything you pay out, such as supplies, repairs and loan payments. Your budget is income minus costs, and it tells you whether you are moving forward or drifting back.'),
        ('Needs and wants',
         'A need is something you cannot do without, such as the food and supplies that keep your crew working. A want is something nice that you could live without, such as a new coat for your closet. Pay for your needs first, every time. Then see what is left, and decide which wants fit inside it.'),
        ('A goal is a destination',
         'A goal turns saving into a trip with an end. Name what you are saving for, set a target, and note the date you hope to arrive. The Starship Bank lets you set savings goals for a new ship, a production plant, printing your blueprints, an emergency fund or retirement on the New Earth. Everything you hold at the Bank counts toward the goal.'),
        ('Plotting the route',
         'To plan the trip, take the target and subtract what you already have. Divide what is left by how much you can put aside each week, and you have the number of weeks to go. For example, a target of 3,000 credits with 600 saved, and 200 put aside each week, is 2,400 divided by 200: twelve weeks. Check your position every week, and write down what you saved, so you can see whether the route still holds.'),
        ('Interest: money that works both ways',
         'Interest is the price of money. When you save with the Bank, your savings earn interest, at 4% APR in a savings account, and you can take money out any time. Every Bank rate is an APR, a year\'s rate, and each week the Bank pays or charges the APR divided by 52. A term deposit earns more (5% APR for 2 weeks, 6% for 4, 7% for 8), but the money is locked until the end, and taking it out early gives up the interest. When you borrow, the interest is what you pay, so the longer money is owed, the more it costs.'),
        ('Loans, early payoff and course corrections',
         'A loan makes sense when what it lets you do earns more than it costs. Only the Bank lends, and only to a player wearing the Business uniform, at 16% APR with one bar down to 8% with five. For example, 1,000 credits at 16% APR over 8 weeks costs 127 a week, 1,014 in all, so 14 credits of interest. Before you sign, the Bank shows you the total cost and the weekly payments. Paying off early saves the interest that has not yet been charged, and a missed payment brings a late fee and lowers your standing. Keep a small emergency fund so one bad week does not knock you off course, and if you fall behind, spend less on wants, earn more, or move the date of the goal.'),
    ],
    "test": [
        ('Your income for the week is 1,000 credits and your costs are 700. What does your budget say you can put aside?',
         [('a', '1,700 credits'), ('b', '700 credits'), ('c', '300 credits'), ('d', '1,000 credits')], 'c'),
        ('Which of these is a need rather than a want?',
         [('a', 'Food and supplies that keep your crew working'), ('b', 'A fancy coat for your closet'), ('c', 'A bigger bookshelf'), ('d', 'A brighter wall poster')], 'a'),
        ('Your goal is 3,000 credits. You have 600 and can put aside 200 a week. Roughly how many weeks until you reach the goal, ignoring interest?',
         [('a', 'Three weeks'), ('b', 'Six weeks'), ('c', 'Nine weeks'), ('d', 'Twelve weeks')], 'd'),
        ('You have a term deposit locked for 8 weeks and you need the money after 3 weeks. What happens if you take it out now?',
         [('a', 'You keep all the interest it would have earned'), ('b', 'You get back your deposit but give up the interest'), ('c', 'The Bank doubles your deposit'), ('d', 'The deposit is lost for good')], 'b'),
        ('You can afford to clear a loan early. Which is the wiser choice?',
         [('a', 'Pay only the last weekly amount and ignore the rest'), ('b', 'Miss a few payments, since the late fee is small'), ('c', 'Pay it off early, because that saves the interest not yet charged'), ('d', 'Borrow more so you keep your cash on hand')], 'c'),
    ],
}
