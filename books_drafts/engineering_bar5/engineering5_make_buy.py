"""Make-or-Buy Decisions for Components: direct costs, overheads, capacity, quality risk and total cost comparison."""
CODE = 'engineering5_make_buy'
BOOK = {'title': 'Make-or-Buy Decisions for Components',
 'subtitle': 'Should you build a part yourself or buy it in, and what really decides it',
 'chapters': [('The question',
               'A make-or-buy decision asks whether to produce a part in-house or buy it from a supplier. '
               'The answer affects cost, control, speed and risk. The choice should be made on the total '
               'cost, not on one line of the budget.'),
              ('Direct costs and overheads',
               'Direct costs are the materials and labour used to make the part. Overheads are the shared '
               'costs, such as rent, power and management time. Overheads are often missed in a quick '
               'comparison and can change the answer.'),
              ('Capacity',
               'Making a part uses machines and people who may be needed for other work. If there is no '
               'spare capacity, making the part may push other work back. Spare capacity can make in-house '
               'production cheaper.'),
              ('Quality risk',
               'Making a part in-house gives control over quality, but it also means owning the risk of '
               'mistakes. Buying from a supplier shifts some of that risk, though it needs checks. The cost '
               'of a quality failure should be counted.'),
              ('Total cost comparison',
               'A fair comparison adds up all the costs for each option over the same period. Include direct '
               'costs, overheads, capacity effects and quality risk. The option with the lower total is '
               'usually the better choice.'),
              ('The money side of the decision',
               'Buying a part ties money to supplier prices, which may rise. Making a part ties money to '
               'equipment and staff. Each path changes the cash needed up front and over time, so both '
               'should be shown.')],
 'test': [('What does a make-or-buy decision ask?',
           [('a', 'Which colour to paint the office'),
            ('b', 'Whether to hire a driver'),
            ('c', 'Which holiday to take'),
            ('d', 'Whether to produce a part in-house or buy it from a supplier')],
           'd'),
          ('What are overheads?',
           [('a', 'Shared costs such as rent, power and management time'),
            ('b', 'The cost of the cheapest bolt'),
            ('c', 'The height of a shelf'),
            ('d', 'A type of paint')],
           'a'),
          ('Why can spare capacity make in-house production cheaper?',
           [('a', 'Because spare capacity makes parts heavier'),
            ('b', 'Because the machines and people are already paid for'),
            ('c', 'Because spare capacity is always illegal'),
            ('d', 'Because spare capacity costs nothing to hire')],
           'b'),
          ('What does making a part in-house mean for quality risk?',
           [('a', 'Quality risk disappears'),
            ('b', 'Quality is decided by the weather'),
            ('c', 'You own the risk of mistakes but also control quality'),
            ('d', 'Quality has no cost')],
           'c'),
          ('What is the fair way to compare the two options?',
           [('a', 'Compare only the cheapest line on one invoice'),
            ('b', 'Pick the supplier with the nicest website'),
            ('c', 'Toss a coin'),
            ('d', 'Add up all the costs for each option over the same period')],
           'd')]}
