"""Engineering Portfolio Prioritisation: value scoring, capacity limits, scenario comparison, sunset decisions and the money side."""
CODE = 'engineering5_portfolio'
BOOK = {'title': 'Engineering Portfolio Prioritisation',
 'subtitle': 'Choosing which projects to fund when the team and the money are limited',
 'chapters': [('A portfolio of projects',
               'An engineering portfolio is the set of projects a team or company is working on or planning. '
               'Resources are always limited, so not every good idea can go ahead. Prioritisation decides '
               'which projects get the time and money.'),
              ('Value scoring',
               'Value scoring gives each project points for its benefits, such as safety, revenue or '
               'strategic fit. The points are weighted by how much each benefit matters. Scores make the '
               'comparison clearer, though they still rest on judgment.'),
              ('Capacity limits',
               'Capacity is the number of people, machines and hours available. A portfolio that asks for '
               'more capacity than exists will fail. Setting a capacity limit forces the team to choose.'),
              ('Scenario comparison',
               'Scenario comparison tests the portfolio under different futures, such as a good market or a '
               'poor one. A set of projects that works in every scenario is more robust. Scenarios show '
               'which choices depend on luck.'),
              ('Sunset decisions',
               'A sunset decision ends a project that no longer earns its place. Sunsetting frees people and '
               'money for better work. Teams often keep projects too long out of attachment, so clear review '
               'rules help.'),
              ('The money side of each choice',
               'Each project takes money that could go to another project. The cost of the choice is the '
               'value of the best option given up. Comparing the money at stake for each option keeps '
               'prioritisation honest.')],
 'test': [('What is an engineering portfolio?',
           [('a', 'A leather case for drawings'),
            ('b', 'A type of expense claim'),
            ('c', 'A holiday photo album'),
            ('d', 'The set of projects being worked on or planned')],
           'd'),
          ('What does value scoring give points for?',
           [('a', 'Benefits such as safety, revenue or strategic fit'),
            ('b', 'The colour of the project folder'),
            ('c', 'The number of coffee breaks'),
            ('d', 'The age of the office')],
           'a'),
          ('Why set a capacity limit?',
           [('a', 'So projects can be unlimited'),
            ('b', 'So the team does not ask for more than exists'),
            ('c', 'So nobody has to choose'),
            ('d', 'So the budget can be ignored')],
           'b'),
          ('What does scenario comparison test?',
           [('a', 'How fast the printer runs'),
            ('b', 'The height of the ceiling'),
            ('c', 'How the portfolio performs under different futures'),
            ('d', 'The spelling of project names')],
           'c'),
          ('What is a sunset decision?',
           [('a', 'Starting a project at dusk'),
            ('b', 'Painting a project red'),
            ('c', 'Moving an office to the west'),
            ('d', 'Ending a project that no longer earns its place')],
           'd')]}
