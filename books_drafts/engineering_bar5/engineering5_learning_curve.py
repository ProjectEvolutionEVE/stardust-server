"""Learning Curves in Production Costing: Wright's law, learning rates, cumulative output, pricing and forecasting unit costs."""
CODE = 'engineering5_learning_curve'
BOOK = {'title': 'Learning Curves in Production Costing',
 'subtitle': 'Why the same product gets cheaper to make as a maker gains experience',
 'chapters': [('Making things again',
               'The more times a team makes the same product, the faster and cheaper each unit tends to '
               'become. Workers learn the steps, tools improve and mistakes fall. This pattern is called a '
               'learning curve.'),
              ('Wright’s law',
               'Wright’s law describes the pattern. It says that each time cumulative output doubles, the '
               'unit cost falls by a fixed share. The law was first described in the aircraft industry in '
               'the 1930s and has since been seen in many industries.'),
              ('Learning rates',
               'The learning rate is the share the unit cost keeps after each doubling. A rate of eighty '
               'percent means each doubling cuts the unit cost by twenty percent. A lower rate means faster '
               'learning and a steeper fall in cost.'),
              ('Cumulative output',
               'Cumulative output is the total number of units made so far. The curve is drawn against this '
               'total, not against time. Doubling the total takes longer when the rate of production is '
               'slow.'),
              ('Pricing',
               'A maker who expects costs to fall can plan prices that follow the curve. Pricing too high '
               'early loses sales, and pricing too low early can cause losses. The curve helps set a path '
               'that is fair and profitable.'),
              ('Forecasting unit costs and the money side',
               'Forecasting uses the curve to estimate the cost of future units. The forecast shapes the '
               'budget and the cash needed to start production. A forecast that ignores learning overstates '
               'the cost and can wrongly kill a good product.')],
 'test': [('What does a learning curve show?',
           [('a', 'How tall a building is'),
            ('b', 'How fast a car drives'),
            ('c', 'How unit cost falls as a maker gains experience'),
            ('d', 'How many lunch breaks are taken')],
           'c'),
          ('What does Wright’s law say?',
           [('a', 'Costs never change'),
            ('b', 'Every product gets more expensive over time'),
            ('c', 'Learning only happens in schools'),
            ('d', 'Each doubling of cumulative output cuts unit cost by a fixed share')],
           'd'),
          ('What does an eighty percent learning rate mean?',
           [('a', 'Each doubling cuts unit cost by twenty percent'),
            ('b', 'Each doubling adds eighty percent to cost'),
            ('c', 'Output doubles every eighty days'),
            ('d', 'The factory closes at eighty percent')],
           'a'),
          ('What is cumulative output?',
           [('a', 'The number of days in a year'),
            ('b', 'The total number of units made so far'),
            ('c', 'The weight of one unit'),
            ('d', 'The number of managers')],
           'b'),
          ('Why does pricing follow the learning curve?',
           [('a', 'Because prices never change'),
            ('b', 'Because the curve sets the weather'),
            ('c', 'Because costs are expected to fall, and prices can follow that path'),
            ('d', 'Because customers do not care about price')],
           'c')]}
