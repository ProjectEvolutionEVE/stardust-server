"""Spectre and Meltdown: how speed tricks inside processors leaked secrets, and what it cost to close the gaps."""
CODE = 'computing5_spectre_meltdown'
BOOK = {'title': 'Spectre and Meltdown',
 'subtitle': 'Speculative execution, cache side channels and the cost of mitigation',
 'chapters': [('Guessing ahead',
               'Modern processors guess which way a program will go and start work early. This '
               'speculative execution makes them faster. If the guess is wrong, the results are '
               'thrown away.'),
              ('Side channels',
               'Thrown-away work can still leave traces, such as which memory is now in the fast '
               'cache. An attacker who can time memory accesses can read those traces. This is a '
               'side channel: information leaks without any direct read.'),
              ('Disclosure in 2018',
               'In early 2018 researchers publicly described two families of these attacks, named '
               'Spectre and Meltdown. They affected many processors from several makers. The news '
               'led to rapid patches.'),
              ('Mitigations',
               'Fixes include separating the kernel from user programs more strictly and adding '
               'checks to some code. Each fix changes how the processor works. Some fixes are in '
               'software and some in new hardware.'),
              ('Performance trade-offs',
               'Some mitigations slowed certain workloads, often by small amounts and sometimes by '
               'more. Owners had to weigh security against speed. The trade-off is still discussed '
               'today.'),
              ('Lessons',
               'The attacks showed that speed features can have hidden security costs. Designers '
               'now test for leaks as part of design, not only after a scare.')],
 'test': [('What is speculative execution?',
           [('a', 'Stopping all work for lunch'),
            ('b', 'Guessing ahead and starting work early'),
            ('c', 'Printing the program'),
            ('d', 'Deleting the cache')],
           'b'),
          ('What is a side channel?',
           [('a', 'A TV channel'),
            ('b', 'A kind of cable'),
            ('c', 'A way information leaks through traces, such as timing'),
            ('d', 'A type of password')],
           'c'),
          ('When were Spectre and Meltdown publicly described?',
           [('a', 'In 1950'), ('b', 'In 2030'), ('c', 'In the year 1900'), ('d', 'Early 2018')],
           'd'),
          ('What is one kind of mitigation?',
           [('a', 'Stricter separation of the kernel from user programs'),
            ('b', 'Painting the processor'),
            ('c', 'Turning off the power for ever'),
            ('d', 'Removing the screen')],
           'a'),
          ('What trade-off do mitigations often bring?',
           [('a', 'They make the chip heavier to lift'),
            ('b', 'They change the colour of the case'),
            ('c', 'They can slow some workloads'),
            ('d', 'They remove all data')],
           'c')]}
