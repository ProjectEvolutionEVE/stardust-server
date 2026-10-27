"""Critical Chain Project Management: resource constraints, buffers, buffer management and the cost of multitasking."""
CODE = 'engineering5_critical_chain'
BOOK = {'title': 'Critical Chain Project Management',
 'subtitle': 'Scheduling around limited people and protecting the finish date with buffers',
 'chapters': [('Resources set the pace',
               'Critical chain scheduling starts from the limit on scarce resources, such as a specialist '
               'who is needed in several places. The longest chain of tasks that must be done in order, '
               'including those limits, is the critical chain. It sets how long the project really takes.'),
              ('Buffers',
               'A buffer is a block of protected time. A project buffer sits at the end of the critical '
               'chain to guard the finish date. Feeding buffers sit where non-critical chains join the main '
               'chain, so delays there do not push the finish back.'),
              ('Buffer management',
               'Buffer management tracks how much of each buffer is used. If a buffer is used quickly, the '
               'team acts early. If it is barely touched, the team knows the plan is safe. The buffer shows '
               'the health of the project at a glance.'),
              ('The cost of multitasking',
               'Starting many tasks at once spreads people thin and slows every task. Work waits in queues '
               'while people switch between jobs. Finishing one task at a time often gets the whole project '
               'done sooner.'),
              ('Why padding is hidden',
               'People often add safety time to each task, and the safety time is then wasted. Critical '
               'chain pools that protection into buffers, where it protects the whole project. Tasks are '
               'then planned at a realistic, shorter length.'),
              ('The money side of multitasking',
               'Idle time and waiting cost money in wages, equipment and lost opportunity. A shorter, '
               'steadier project cuts those costs. Protecting the finish date with a buffer is cheaper than '
               'late penalties.')],
 'test': [('What does critical chain scheduling use to set the length of a project?',
           [('a', 'The number of windows in the office'),
            ('b', 'The favourite colour of the boss'),
            ('c', 'The longest chain of tasks, including resource limits'),
            ('d', 'The name of the project')],
           'c'),
          ('Where does a project buffer sit?',
           [('a', 'On the office roof'),
            ('b', 'In the car park'),
            ('c', 'At the bottom of the budget sheet'),
            ('d', 'At the end of the critical chain')],
           'd'),
          ('What does buffer management track?',
           [('a', 'How much of each buffer has been used'),
            ('b', 'How many biscuits are in the tin'),
            ('c', 'The height of each desk'),
            ('d', 'The weather each morning')],
           'a'),
          ('What is a common effect of multitasking?',
           [('a', 'Every task finishes twice as fast'),
            ('b', 'Work waits in queues and every task slows'),
            ('c', 'Multitasking removes all delays'),
            ('d', 'Multitasking makes the plan shorter by magic')],
           'b'),
          ('Why does padding each task often waste time?',
           [('a', 'Because padding always saves money'),
            ('b', 'Because padding is a legal requirement'),
            ('c', 'Because the safety time is used up without protecting the whole project'),
            ('d', 'Because padding makes tasks disappear')],
           'c')]}
