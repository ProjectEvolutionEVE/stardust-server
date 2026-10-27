"""The Patriot Missile Timing Error: clock drift over long run times, floating-point conversion, the 1991 failure, delayed updates, error budgets and lessons."""
CODE = 'computing5_patriot_timing'
BOOK = {'title': 'The Patriot Missile Timing Error',
 'subtitle': 'How a tiny clock error grew over long run times',
 'chapters': [('Clock drift',
               'The Patriot missile system kept time by counting tenths of a second. A tiny rounding error '
               'in each count grew steadily the longer the system stayed switched on. Over long runs, the '
               'clock drifted further from true time.'),
              ('Floating-point conversion',
               'Counting in tenths is not exact in binary arithmetic, so each tick was a little off. '
               'Converting the count to seconds added more small errors. The sum of these errors is what '
               'mattered in the end.'),
              ('The 1991 failure',
               'In February 1991, at Dhahran in the Gulf War, a Patriot battery had been running for a long '
               'time without a restart. The timing error made its tracking inaccurate, and a Scud missile '
               'was not intercepted. Twenty-eight soldiers were killed.'),
              ('Delayed updates',
               'A software fix had been prepared, but it had not yet reached the site. Waiting for an update '
               'meant the system kept running with a known fault. The timing of fixes matters as much as the '
               'fixes themselves.'),
              ('Error budgets',
               'Engineers should estimate how much error each part of a system may add, and check that the '
               'total stays within limits. Long-running systems need tests that cover long run times, not '
               'only short ones.'),
              ('Lessons',
               'Test for the situations that users will really meet, including long uptime. Keep a clear '
               'plan for restarts and updates. Treat small, known errors as real risks that grow with '
               'time.')],
 'test': [('What did the Patriot clock count?',
           [('a', 'Tons of fuel'),
            ('b', 'Miles driven'),
            ('c', 'Pages printed'),
            ('d', 'Tenths of a second')],
           'd'),
          ('Why did the timing error grow over time?',
           [('a', 'The clock was made of wood'),
            ('b', 'Each tiny rounding error built up the longer the system ran'),
            ('c', 'The battery was recharged daily'),
            ('d', 'The clock stopped every hour')],
           'b'),
          ('What was the human cost of the 1991 failure at Dhahran?',
           [('a', 'No one was harmed at all'),
            ('b', 'Two hundred ships were sunk'),
            ('c', 'Twenty-eight soldiers were killed'),
            ('d', 'The city was flooded')],
           'c'),
          ('Why did a fix that existed still matter?',
           [('a', 'It had not yet reached the site, so a known fault stayed in service'),
            ('b', 'It was never needed'),
            ('c', 'It made the system slower on purpose'),
            ('d', 'It removed all alarms')],
           'a'),
          ('What kind of testing covers the risk described here?',
           [('a', 'Only tests of very short runs'),
            ('b', 'Tests that cover long run times as well'),
            ('c', 'No testing at all'),
            ('d', 'Tests done only on paper')],
           'b')]}
