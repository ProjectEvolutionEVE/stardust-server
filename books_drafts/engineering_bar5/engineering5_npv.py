"""Net Present Value for Engineering Projects: discounting, cash flow timing, NPV decisions, sensitivity and ranking."""
CODE = 'engineering5_npv'
BOOK = {'title': 'Net Present Value for Engineering Projects',
 'subtitle': 'Discounting future money, timing cash flows and choosing between projects',
 'chapters': [('Money now and money later',
               'A pound, dollar or euro today is worth more than the same amount in a year. It could earn '
               'interest, and the future is uncertain. Net present value, or NPV, converts future cash into '
               'today’s value so that projects can be compared fairly.'),
              ('Discounting',
               'Discounting shrinks each future cash flow by a rate for each year it is away. The further '
               'away it is, the smaller its value today. The discount rate reflects the return the money '
               'could earn elsewhere and the risk of the project.'),
              ('Cash flow timing',
               'The timing of cash flows changes the answer. Money received early is worth more than the '
               'same money received late. Engineers draw out the cash flows year by year, so the timing is '
               'clear.'),
              ('The NPV decision',
               'If the NPV is positive at the chosen discount rate, the project adds value on paper and is '
               'worth considering. A negative NPV means it returns less than the discount rate. Among '
               'projects that all clear the rate, a higher NPV is generally better.'),
              ('Sensitivity',
               'A sensitivity check shows how the NPV changes when an input changes, such as the price or '
               'the cost. It reveals which inputs matter most. A project that stays positive under most '
               'changes is a safer bet.'),
              ('Ranking projects with the money side in view',
               'Ranking projects by NPV helps when capital is limited. Rank projects by NPV per unit of '
               'capital, the profitability index, and choose the set with the highest total NPV within the budget. The capital available sets which choices can actually be made.')],
 'test': [('Why is future money worth less than money today?',
           [('a', 'Future money is printed in a worse colour'),
            ('b', 'It could earn a return elsewhere and the future is uncertain'),
            ('c', 'Future money is always smaller on paper'),
            ('d', 'Money never changes value')],
           'b'),
          ('What does discounting do to a future cash flow?',
           [('a', 'It doubles it'),
            ('b', 'It moves it to the past'),
            ('c', 'It shrinks its value in today’s terms'),
            ('d', 'It turns it into shares')],
           'c'),
          ('When is a project generally worth considering on NPV?',
           [('a', 'When its NPV is negative'),
            ('b', 'When it has no cash flows'),
            ('c', 'When the name is short'),
            ('d', 'When its NPV is positive at the chosen discount rate')],
           'd'),
          ('What does a sensitivity check show?',
           [('a', 'How the NPV changes when an input changes'),
            ('b', 'The age of the project team'),
            ('c', 'The number of coffee cups used'),
            ('d', 'The shape of the office')],
           'a'),
          ('Why does the timing of cash flows matter?',
           [('a', 'Timing never changes the answer'),
            ('b', 'Early money is worth more than the same money received late'),
            ('c', 'Late money is always worth more'),
            ('d', 'Timing only matters for weather')],
           'b')]}
