"""Chip Verification: finding design bugs before a chip is made, because a mistake in silicon is very expensive."""
CODE = 'computing5_chip_verification'
BOOK = {'title': 'Chip Verification',
 'subtitle': 'Coverage, assertions, formal checks and the cost of a respin',
 'chapters': [('Why verify chips',
               'Once a chip is made, a design bug cannot be patched in software. Verification '
               'means proving, as far as possible, that the design does what it should. It takes '
               'more effort than the design itself in many projects.'),
              ('Coverage',
               'Coverage measures which cases the tests have actually tried. A test suite that '
               'never reaches a part of the design leaves that part unchecked. Teams track '
               'coverage so that gaps are visible.'),
              ('Assertions',
               'An assertion is a rule that must always hold, such as a request always gets an '
               'answer. The simulator checks assertions as it runs. A failed assertion points '
               'straight at the problem.'),
              ('Formal equivalence checking',
               'Formal checking proves mathematically that two versions of a design behave the '
               'same. It does not depend on the tests chosen. It is used when a design is '
               'rewritten or optimised.'),
              ('Respins',
               'A respin means making a new set of chip masks after a bug is found. Each respin '
               'costs time and money. Catching bugs before manufacture is the cheapest route.'),
              ('The cost of a mask set',
               'A set of masks for an advanced chip can cost many millions of dollars. That '
               'expense is why teams invest heavily in verification. The check is cheaper than a '
               'failed build.')],
 'test': [('Why is verification so important for chips?',
           [('a', 'Chips are always free'),
            ('b', 'A design bug cannot easily be patched after manufacture'),
            ('c', 'Chips never have bugs'),
            ('d', 'Chips are only used for toys')],
           'b'),
          ('What does coverage measure?',
           [('a', 'The size of the chip box'),
            ('b', 'How many people are on the team'),
            ('c', 'Which cases the tests have actually tried'),
            ('d', 'The paint colour')],
           'c'),
          ('What is an assertion?',
           [('a', 'A loud argument in a meeting'),
            ('b', 'A kind of wire'),
            ('c', 'A chip package'),
            ('d', 'A rule that must always hold, which the simulator checks')],
           'd'),
          ('What does formal equivalence checking prove?',
           [('a', 'That two versions of a design behave the same'),
            ('b', 'That the chip is cheap'),
            ('c', 'That the office is warm'),
            ('d', 'That the tests are long')],
           'a'),
          ('What is a respin?',
           [('a', 'A dance in the lab'),
            ('b', 'A way to spin a wafer for fun'),
            ('c', 'A new set of masks made after a bug is found'),
            ('d', 'A cleaning cycle')],
           'c')]}
