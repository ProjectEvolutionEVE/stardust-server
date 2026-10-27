"""Transactional Memory: grouping memory changes into all-or-nothing blocks, and why that is harder than it sounds."""
CODE = 'computing5_transactional_memory'
BOOK = {'title': 'Transactional Memory',
 'subtitle': 'Atomic blocks, conflicts, retries and the limits of the idea',
 'chapters': [('All or nothing',
               'A transaction groups several memory changes so that they either all happen or none '
               'do. Other threads see the group as one step. The idea borrows from databases.'),
              ('Conflict detection',
               'If two transactions touch the same memory, one must be stopped. Detecting this '
               'early keeps the results correct. The detection can be done by software or by the '
               'processor.'),
              ('Retries',
               'When a transaction conflicts, it is rolled back and tried again. Retries cost '
               'time, so a busy shared location can slow everything. Good designs keep '
               'transactions short.'),
              ('Hardware history',
               'Intel added hardware transactional memory to some processors in 2013, but later '
               'found bugs and disabled it on many chips. The history shows how hard the hardware '
               'side is to get right.'),
              ('Composability',
               'Transactions can be combined into bigger ones, which is their great appeal to '
               'programmers. Locks do not combine as easily. This makes larger programs simpler to '
               'build.'),
              ('Limits',
               'Transactions cannot undo outside actions such as sending a message or writing to a '
               'screen. Long transactions conflict more often. The method helps, but it does not '
               'replace all other tools.')],
 'test': [('What does a transaction do?',
           [('a', 'Buys goods from a shop'),
            ('b', 'Groups memory changes so they all happen or none do'),
            ('c', 'Sends a letter'),
            ('d', 'Changes the screen colour')],
           'b'),
          ('What happens when two transactions conflict?',
           [('a', 'Both are printed'),
            ('b', 'The computer restarts for a week'),
            ('c', 'One is stopped and can be tried again'),
            ('d', 'Nothing ever happens')],
           'c'),
          ('Why keep transactions short?',
           [('a', 'Short ones use more memory'),
            ('b', 'Short ones cannot run'),
            ('c', 'Long ones are cheaper'),
            ('d', 'Long ones conflict more often')],
           'd'),
          ('What did Intel do with its hardware transactional memory?',
           [('a', 'Disabled it on many chips after finding bugs'),
            ('b', 'Sold it as a toy'),
            ('c', 'Turned it into a printer'),
            ('d', 'Made it the only memory')],
           'a'),
          ('What is one limit of transactional memory?',
           [('a', 'It cannot store numbers'),
            ('b', 'It only works on paper'),
            ('c', 'It cannot undo outside actions such as sending a message'),
            ('d', 'It cannot use any processor')],
           'c')]}
