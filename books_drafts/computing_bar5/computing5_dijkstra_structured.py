"""The Letter That Changed Programming: the goto debate, structured programming, program correctness, influence, teaching and lessons from the debate."""
CODE = 'computing5_dijkstra_structured'
BOOK = {'title': 'The Letter That Changed Programming',
 'subtitle': 'Edsger Dijkstra and the case against the goto statement',
 'chapters': [('The goto debate',
               'In 1968 Edsger Dijkstra published a short letter titled "Go To Statement Considered '
               'Harmful". It argued that jumping freely around a program made it hard to understand and to '
               'check. The letter started a long and lively debate.'),
              ('Structured programming',
               'Structured programming uses a small set of clear blocks: sequence, choice and repetition. '
               'Programs built from these blocks can be read from top to bottom and reasoned about more '
               'easily. The idea spread into most modern languages.'),
              ('Program correctness',
               'Dijkstra argued that a program should be understood as a precise statement of what it does. '
               'Careful reasoning about each step gives greater confidence than testing alone. Testing can '
               'show that errors exist, but it cannot prove their absence.'),
              ('Influence',
               'Ideas from the debate shaped languages, teaching and software practice for decades. Many '
               'modern languages discourage or replace unrestricted jumps, while still offering limited '
               'forms of early exit.'),
              ('Teaching',
               'Dijkstra believed that programming should be taught with rigour. Students learned to think '
               'about correctness and clarity from the start, rather than only about how to make a program '
               'run.'),
              ('Lessons from the debate',
               'Simple structures make complex work easier to check. Debates about style can reveal deep '
               'issues about how people understand code. Clear reasoning is an asset in any engineering '
               'field.')],
 'test': [('In what year did Dijkstra publish the letter on the goto statement?',
           [('a', '1901'), ('b', '1995'), ('c', '1968'), ('d', '1743')],
           'c'),
          ('What did Dijkstra argue about the goto statement?',
           [('a', 'That it was the fastest way to write code'),
            ('b', 'That it should be printed in gold'),
            ('c', 'That it should be used in every line'),
            ('d', 'That free jumping made programs hard to understand and check')],
           'd'),
          ('What are the three basic blocks of structured programming named here?',
           [('a', 'Paint, paper and glue'),
            ('b', 'Sequence, choice and repetition'),
            ('c', 'Start, pause and stop'),
            ('d', 'Red, green and blue')],
           'b'),
          ('What did Dijkstra say testing can show?',
           [('a', 'That errors exist, but not that they are absent'),
            ('b', 'That errors are absent for ever'),
            ('c', 'That programs never have errors'),
            ('d', 'That code is always correct')],
           'a'),
          ('What does the story suggest about debates over style?',
           [('a', 'They are always pointless'),
            ('b', 'They should be banned'),
            ('c', 'They only concern colours'),
            ('d', 'They can reveal deep issues about how people understand code')],
           'd')]}
