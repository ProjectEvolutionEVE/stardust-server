"""Memory Consistency Models: the rules for what one processor may see of another's writes, and when order is promised."""
CODE = 'computing5_memory_consistency'
BOOK = {'title': 'Memory Consistency Models',
 'subtitle': 'Reordering, acquire and release, fences and data races',
 'chapters': [('Why order matters',
               'When two processors share memory, the order in which writes become visible decides '
               'what the other sees. A memory model is the agreed set of rules for that order. '
               'Programmers rely on it every time they share data between threads.'),
              ('Reordering',
               'Compilers and processors reorder memory operations to run faster, as long as one '
               'thread cannot tell the difference. Other threads, however, can notice the '
               'reordering. The model says how much reordering is allowed.'),
              ('Acquire and release',
               'A release write publishes earlier writes, and an acquire read that sees it gets '
               'those writes too. Together they make a handover between threads safe without a '
               'full lock. Many lock-free methods depend on this pair.'),
              ('Sequential consistency',
               'Sequential consistency means all threads see one shared order of operations, as if '
               'they took turns. It is easy to reason about but costly to build. Most machines '
               'offer weaker models that are faster.'),
              ('Fences',
               'A fence is an instruction that stops certain reorderings across it. Fences cost '
               'time, so programmers use them only where needed. Knowing where a fence belongs is '
               'a key skill.'),
              ('Data races',
               'A data race happens when two threads access the same memory at once and at least '
               'one writes, with no ordering rule between them. In most languages a data race has '
               'undefined results. Good programs avoid races entirely.')],
 'test': [('What does a memory model define?',
           [('a', 'The shape of the keyboard'),
            ('b', 'The agreed rules for the order in which writes are seen'),
            ('c', 'The price of memory'),
            ('d', 'The name of the operating system')],
           'b'),
          ('Why do compilers reorder memory operations?',
           [('a', 'To make programs longer'),
            ('b', 'To hide errors from the programmer'),
            ('c', 'To run faster when no thread can tell the difference'),
            ('d', 'To stop the clock')],
           'c'),
          ('What does a release write do?',
           [('a', 'It deletes the file system'),
            ('b', 'It sends an email'),
            ('c', 'It turns off the screen'),
            ('d', 'It publishes earlier writes to a thread that acquires it')],
           'd'),
          ('What is a data race?',
           [('a', 'Two threads accessing shared memory at once, with a write and no ordering'),
            ('b', 'A contest between programmers'),
            ('c', 'A fast download'),
            ('d', 'A sort of car race')],
           'a'),
          ('What is a fence?',
           [('a', 'A garden wall'),
            ('b', 'A shop window'),
            ('c', 'An instruction that stops certain reorderings'),
            ('d', 'A way to store passwords')],
           'c')]}
