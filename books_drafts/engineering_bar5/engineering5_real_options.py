"""Real Options Valuation of Engineering Choices: the option to wait, to expand, decision trees, volatility and simple valuation."""
CODE = 'engineering5_real_options'
BOOK = {'title': 'Real Options Valuation of Engineering Choices',
 'subtitle': 'Why keeping a choice open can be worth money, and how to value it simply',
 'chapters': [('Choices have value',
               'A real option is the right, but not the duty, to take a decision later. A project that can '
               'be delayed, expanded or dropped holds value that a simple NPV can miss. Real options '
               'thinking puts a price on that flexibility.'),
              ('The option to wait',
               'Waiting lets a team learn more before committing money. If the market or the technology is '
               'uncertain, the option to wait can be worth a lot. The cost of waiting, such as lost sales, '
               'must be weighed against the gain in knowledge.'),
              ('The option to expand',
               'A project may start small and grow later if results are good. The right to expand is '
               'valuable when demand is uncertain. Building in room for growth can be cheaper than building '
               'the full size at once.'),
              ('Decision trees',
               'A decision tree maps the choices and the possible outcomes at each step. Each branch carries '
               'a probability and a payoff. Working back from the end of the tree shows the best choice at '
               'each point.'),
              ('Volatility',
               'Volatility measures how much a value could swing up or down. Higher volatility makes '
               'flexibility more valuable, because a team can act when the news is good and hold back when '
               'it is bad. Estimating volatility needs past data or careful judgment.'),
              ('Simplified valuation and the money at stake',
               'Full option pricing can be complex, so a simple tree is often enough. The aim is to see how '
               'much money the flexibility adds. If the answer is small, a simple plan may do. If it is '
               'large, the flexibility deserves a place in the decision.')],
 'test': [('What is a real option?',
           [('a', 'A type of cheap lunch'),
            ('b', 'A fixed salary for life'),
            ('c', 'A shop discount card'),
            ('d', 'The right, but not the duty, to take a decision later')],
           'd'),
          ('When is the option to wait most valuable?',
           [('a', 'When the outcome is uncertain and learning helps'),
            ('b', 'When everything is certain and known'),
            ('c', 'When the project is painted red'),
            ('d', 'When no one is available to decide')],
           'a'),
          ('What does a decision tree show?',
           [('a', 'The shape of a tree in a park'),
            ('b', 'Choices and possible outcomes at each step'),
            ('c', 'The names of the team'),
            ('d', 'The price of paper')],
           'b'),
          ('Why does higher volatility make flexibility more valuable?',
           [('a', 'Because volatility always lowers costs'),
            ('b', 'Because volatility removes choices'),
            ('c', 'Because a team can act when news is good and hold back when it is bad'),
            ('d', 'Because volatility is a type of paint')],
           'c'),
          ('Why is a simple valuation often enough?',
           [('a', 'Because valuation is always free'),
            ('b', 'Because flexibility is worthless'),
            ('c', 'Because no numbers are needed'),
            ('d', 'Because it shows how much money the flexibility adds')],
           'd')]}
