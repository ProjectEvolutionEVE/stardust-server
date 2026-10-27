"""Lower Bounds and Adversary Arguments: proving that no method can do better than a certain cost."""
CODE = 'computing5_lower_bounds'
BOOK = {'title': 'Lower Bounds and Adversary Arguments',
 'subtitle': 'Proving that a task cannot be done cheaper',
 'chapters': [('Proving a limit',
               'A lower bound says no method can do better than a certain cost for a problem. Upper bounds show a method that works, while lower bounds show a wall. Proving one '
               'is harder, because the proof must cover every possible method, not only the ones we have thought of.'),
              ('The adversary',
               'An adversary argument plays a game against any algorithm. The adversary answers each question in whatever way forces the algorithm to look at more of the input. '
               'If the algorithm must look at every item before it can answer, it has no shortcut.'),
              ('Information and bits',
               'Information-theoretic bounds count how many different answers are possible. Each yes or no comparison gives at most one bit, so when many outcomes exist, a '
               'minimum number of comparisons is needed. This method does not depend on any clever trick.'),
              ('Decision trees',
               'A decision tree shows every sequence of questions an algorithm may ask. Its depth is the worst-case number of questions. If a problem has many possible answers, '
               'the tree must be deep, and that depth gives a lower bound.'),
              ('The sorting limit',
               'Any sorting method that only compares pairs of items needs about n log n comparisons in the worst case. There are n factorial possible orders, and each comparison '
               'can cut the possibilities at most in half. Merge sort already matches this bound.'),
              ('Reading lower-bound claims',
               'When someone claims a faster method is impossible, ask under what model. A bound often assumes only comparisons, or only certain operations, and a different model '
               'can beat it. Read the assumptions before accepting the conclusion.')],
 'test': [('What does a lower bound show?',
           [('a', 'A method that always works'), ('b', 'The fastest computer ever built'), ('c', 'The least cost any method can have'), ('d', 'The size of a hard drive')],
           'c'),
          ('In an adversary argument, what does the adversary try to do?',
           [('a', 'Force the algorithm to look at more of the input'),
            ('b', 'Give the algorithm the answer at once'),
            ('c', 'Shut down the computer'),
            ('d', 'Hide the size of the input')],
           'a'),
          ('Why does n log n appear as a sorting limit for comparisons?',
           [('a', 'Because sorting always needs n squared steps'),
            ('b', 'Because computers have a fixed clock'),
            ('c', 'Because lists are always short'),
            ('d', 'Because there are n factorial orders and each comparison halves the possibilities at most')],
           'd'),
          ('What is the depth of a decision tree?',
           [('a', 'The number of items in the input'), ('b', 'The worst-case number of questions asked'), ('c', 'The colour of the tree'), ('d', 'The number of computers used')],
           'b'),
          ('Why must you read the assumptions behind a lower bound?',
           [('a', 'A different model of operations can beat the bound'),
            ('b', 'Lower bounds never apply to anything'),
            ('c', 'Assumptions are always correct'),
            ('d', 'Bounds are only written in red ink')],
           'a')]}
