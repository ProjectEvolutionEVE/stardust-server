"""HAZOP: guide words, deviations, consequences, safeguards and action lists."""
CODE = 'engineering5_hazop'
BOOK = {'title': 'HAZOP: Guide Words and Deviations',
 'subtitle': 'Nodes, guide words, deviations and the actions that follow',
 'chapters': [('What a HAZOP is',
               'A hazard and operability study, called a HAZOP, is a team review of a process design. The '
               'team asks what could go wrong at each part of the plant. It is done in a structured way so '
               'that few possibilities are missed.'),
              ('Nodes',
               'The plant is split into nodes, which are sections such as a tank, a pipe run or a pump. Each '
               'node is studied on its own. Clear node boundaries keep the review organised and easy to '
               'follow.'),
              ('Guide words',
               'Guide words are short prompts such as NO, MORE, LESS, REVERSE and OTHER THAN. Each one is '
               'applied to each process condition, like flow, pressure or temperature. A guide word like NO '
               'flow asks what happens if the flow stops completely.'),
              ('Deviations and consequences',
               'A deviation is a guide word combined with a process condition, such as MORE pressure. The '
               'team then works out the consequences. They ask what harm, delay or loss would follow if that '
               'deviation happened.'),
              ('Safeguards',
               'Safeguards are the protections already in the design, such as alarms, relief valves and '
               'trips. The team records each one and judges whether it would stop the consequence. A '
               'safeguard that has not been tested is not counted with confidence.'),
              ('Action lists',
               'When a safeguard is not enough, the team writes an action. An action has an owner and a due '
               'date, and it is tracked to the end. Good action lists turn the study into real changes on '
               'the plant.')],
 'test': [('What is a HAZOP?',
           [('a', 'A type of paint'),
            ('b', 'A kind of pay scheme'),
            ('c', 'A team review that asks what could go wrong in a process design'),
            ('d', 'A software game for children')],
           'c'),
          ('Which guide word describes the complete absence of the intended flow?',
           [('a', 'MORE'), ('b', 'REVERSE'), ('c', 'LESS'), ('d', 'NO')],
           'd'),
          ('What is a node in a HAZOP?',
           [('a', 'A section of the plant studied on its own'),
            ('b', 'A type of valve'),
            ('c', 'A name for a team member'),
            ('d', 'A grade of steel')],
           'a'),
          ('What is a deviation?',
           [('a', 'A late delivery of paint'),
            ('b', 'A guide word combined with a process condition'),
            ('c', 'A change of shift'),
            ('d', 'A fire drill')],
           'b'),
          ('What should an action in an action list have?',
           [('a', 'A picture of the team'),
            ('b', 'A guess that nobody checks'),
            ('c', 'An owner and a due date'),
            ('d', 'No name at all')],
           'c')]}
