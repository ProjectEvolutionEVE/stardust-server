"""Capital Allocation Across a Portfolio: how a company decides which projects deserve its limited money."""
CODE = "mining5_capital_alloc"
BOOK = {'title': 'Capital Allocation Across a Portfolio',
 'subtitle': 'Choosing which projects get limited money, and when to stop one',
 'chapters': [('Hurdle rates',
               'A hurdle rate is the minimum return a project must earn before it is accepted. It reflects '
               'what the money could earn elsewhere and how risky the project is. A project that cannot '
               'clear the hurdle is turned down.'),
              ('Ranking projects',
               'Common tools for ranking projects include net present value, internal rate of return and '
               "payback period. Net present value adds up all future cash flows in today's money. A company "
               'usually looks at several measures together.'),
              ('Budget constraints',
               'Money is limited, so the company cannot fund every good project. It must choose the set of '
               'projects that gives the best return within the budget.'),
              ('Risk weights',
               'Riskier projects need a higher return to be worth the money. A new mine in an unproven area '
               'is judged more harshly than an expansion of a proven one.'),
              ('Regular reviews',
               'Projects are reviewed as conditions change. Costs, prices and risks move, so a project that '
               'was good last year may not be good today.'),
              ('Discipline',
               'The hardest part is stopping a poor project, even after money has been spent. Good companies '
               'judge a project on future cash flows, not on the cost already spent.')],
 'test': [('What is a hurdle rate?',
           [('a', 'The height of a fence at a mine'),
            ('b', 'The price of ore'),
            ('c', 'The minimum return a project must earn to be accepted'),
            ('d', 'A weekly staff meeting')],
           'c'),
          ('What does net present value add up?',
           [('a', "All future cash flows in today's money"),
            ('b', 'The number of workers'),
            ('c', 'The weight of the ore'),
            ('d', 'The number of trucks')],
           'a'),
          ('Why do companies rank projects when money is limited?',
           [('a', 'To paint them in order'),
            ('b', 'To hide them from shareholders'),
            ('c', 'To spend every dollar on one project'),
            ('d', 'To choose the set of projects that gives the best return within the budget')],
           'd'),
          ('How are riskier projects treated?',
           [('a', 'They are always approved first'),
            ('b', 'They need a higher return to be worth the money'),
            ('c', 'They are ignored'),
            ('d', 'They need no return at all')],
           'b'),
          ('What is the hardest discipline in capital allocation?',
           [('a', 'Buying the newest drill'),
            ('b', 'Hiring the most staff'),
            ('c', 'Stopping a poor project, even after money has been spent'),
            ('d', 'Printing the annual report')],
           'c')]}
