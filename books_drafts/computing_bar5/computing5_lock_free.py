"""Lock-Free Data Structures: sharing data between threads without locks, and why the simple cases still go wrong."""
CODE = 'computing5_lock_free'
BOOK = {'title': 'Lock-Free Data Structures',
 'subtitle': 'Compare-and-swap, the ABA problem and the Michael-Scott queue',
 'chapters': [('Progress without locks',
               'A lock-free structure guarantees that some thread always makes progress, even if '
               'others are stalled. A lock can leave everyone waiting if the holder stops. '
               'Lock-free design avoids that trap.'),
              ('Compare-and-swap loops',
               'Compare-and-swap changes a value only if it still holds the expected old value. A '
               'thread reads, computes, and tries again if someone else changed the value. Most '
               'lock-free code is built from loops like this.'),
              ('The ABA problem',
               'A value can change from A to B and back to A between a thread reading it and '
               'writing it. The thread then wrongly believes nothing changed. Tags or counters are '
               'used to catch this.'),
              ('The Michael-Scott queue',
               'Maged Michael and Michael Scott published a lock-free queue in 1996. It is still a '
               'standard example. It uses compare-and-swap on the head and tail of a linked list.'),
              ('Wait-free goals',
               'Wait-free is stronger: every thread finishes in a bounded number of steps. It is '
               'harder to build and often slower in practice. Designers choose the level of '
               'guarantee that the task needs.'),
              ('Testing lock-free code',
               'Bugs in lock-free code depend on rare timing. Tests must run many threads and many '
               'interleavings, and tools that explore orders help. Careful reasoning and review '
               'remain essential.')],
 'test': [('What does lock-free promise?',
           [('a', 'No thread ever makes a mistake'),
            ('b', 'Some thread always makes progress'),
            ('c', 'The computer never sleeps'),
            ('d', 'Locks are added to every line')],
           'b'),
          ('What does compare-and-swap do?',
           [('a', 'Compares two photos'),
            ('b', 'Swaps two monitors'),
            ('c', 'Changes a value only if it still holds the expected value'),
            ('d', 'Sorts a list of names')],
           'c'),
          ('What is the ABA problem?',
           [('a', 'A letter-writing error'),
            ('b', 'A kind of bank account'),
            ('c', 'A fault in printers'),
            ('d', 'A value changes away and back, so a thread wrongly thinks nothing changed')],
           'd'),
          ('When was the Michael-Scott queue published?',
           [('a', 'In 1996'), ('b', 'In 1860'), ('c', 'In 2050'), ('d', 'In 1700')],
           'a'),
          ('How is wait-free different from lock-free?',
           [('a', 'Wait-free uses more locks'),
            ('b', 'Wait-free has no threads'),
            ('c', 'Wait-free finishes every thread in a bounded number of steps'),
            ('d', 'Wait-free is only for printers')],
           'c')]}
