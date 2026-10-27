"""Real-Time Scheduling Guarantees: making sure urgent work always finishes on time."""
CODE = 'computing5_rate_monotonic'
BOOK = {'title': 'Real-Time Scheduling Guarantees',
 'subtitle': 'Deadlines, rate-monotonic and earliest-deadline-first scheduling',
 'chapters': [('What real time means',
               'Real-time software must finish each job by a deadline. Fast on average is not '
               'enough: a late answer can be a failure. Designers plan for the worst case, not the '
               'typical one.'),
              ('Rate-monotonic scheduling',
               'Tasks that repeat more often get higher priority. This simple rule was studied by '
               'Liu and Layland in 1973. It works well when the tasks are fixed and their timing '
               'is known.'),
              ('Earliest-deadline-first',
               'Earliest-deadline-first always runs the job whose deadline is nearest. On one '
               'processor it can use the full capacity, where the fixed-priority rule may not. The '
               'price is a more complex scheduler.'),
              ('Schedulability tests',
               'Before a system runs, engineers apply a test to show that every task will meet its '
               'deadline. A failed test means the design must change, such as by reducing work or '
               'adding a processor.'),
              ('Priority inversion',
               'A low-priority task can hold a lock that a high-priority task needs, and the high '
               'one then waits. Famous failures of this kind have been fixed with priority '
               'inheritance. Designers must watch for it.'),
              ('Safety-critical use',
               'Brakes, flight controls and medical devices depend on timing as much as on correct '
               'answers. Each such system needs proof that its timing holds under the worst load. '
               'This is why real-time design is a discipline of its own.')],
 'test': [('What does a real-time system have to do?',
           [('a', 'Be as fast as possible on average'),
            ('b', 'Finish each job by its deadline'),
            ('c', 'Show the time in big letters'),
            ('d', 'Run only at night')],
           'b'),
          ('In rate-monotonic scheduling, which task gets higher priority?',
           [('a', 'The one with the longest name'),
            ('b', 'The one that runs least often'),
            ('c', 'The one that repeats more often'),
            ('d', 'The one written last')],
           'c'),
          ('What does earliest-deadline-first always run?',
           [('a', 'The job with the most colours'),
            ('b', 'The job that started first ever'),
            ('c', 'A random job'),
            ('d', 'The job with the nearest deadline')],
           'd'),
          ('What is priority inversion?',
           [('a', 'A low-priority task holds something a high-priority task needs'),
            ('b', 'Two processors swap places'),
            ('c', 'A clock runs backwards'),
            ('d', 'A screen flips upside down')],
           'a'),
          ('What does a schedulability test show?',
           [('a', 'The price of the processor'),
            ('b', 'The colour of the code'),
            ('c', 'That every task can meet its deadline'),
            ('d', 'How many users are online')],
           'c')]}
