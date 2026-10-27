"""Information Flow Control: tracking where data travels so secrets cannot leak to places they should never reach."""
CODE = 'computing5_information_flow'
BOOK = {'title': 'Information Flow Control',
 'subtitle': 'Labels, lattices, noninterference, taint tracking and timing leaks',
 'chapters': [('Following the data',
               'Information flow control tracks where data goes inside a program. A secret should '
               'not reach a public output. Access checks alone cannot always see such leaks.'),
              ('Labels and lattices',
               'Data carries labels such as secret or public. Labels form an ordering called a '
               'lattice, and data may move only in allowed directions. Dorothy Denning described '
               'this idea in 1976.'),
              ('Noninterference',
               'Noninterference says that secret inputs must not change what a public observer can '
               'see. Goguen and Meseguer introduced the idea in 1982. It is a strong test of '
               'whether a system leaks.'),
              ('Taint tracking',
               'Taint tracking marks data from untrusted sources and checks it before it reaches '
               'sensitive code. The mark follows the data through each step. Web applications use '
               'it to block some attacks.'),
              ('Enforcement',
               'Enforcement can happen in a compiler, a runtime or a language type system. Each '
               'place catches leaks at a different point. Strong designs check at more than one '
               'point.'),
              ('Leaks through timing',
               'Even correct answers can leak through how long they take. An attacker who times '
               'requests can learn secrets. Designers must treat time as a channel that carries '
               'information.')],
 'test': [('What does information flow control track?',
           [('a', 'The number of printers'),
            ('b', 'Where data goes inside a program'),
            ('c', 'The price of a laptop'),
            ('d', 'The height of a tower')],
           'b'),
          ('What is a label used for?',
           [('a', 'Decorating a cake'),
            ('b', 'Sticking on a shoe'),
            ('c', 'Marking data as secret or public'),
            ('d', 'Measuring rain')],
           'c'),
          ('What does noninterference say?',
           [('a', 'Programs must never talk'),
            ('b', 'Every input must be public'),
            ('c', 'Every output must be secret'),
            ('d', 'Secret inputs must not change what a public observer sees')],
           'd'),
          ('What does taint tracking mark?',
           [('a', 'Data from untrusted sources, which follows it through the program'),
            ('b', 'The screen colour'),
            ('c', 'The number of users'),
            ('d', 'The date of a holiday')],
           'a'),
          ('How can correct answers still leak secrets?',
           [('a', 'Only if they are wrong'),
            ('b', 'Never, if they are correct'),
            ('c', 'Through how long they take to produce'),
            ('d', 'Only on paper')],
           'c')]}
