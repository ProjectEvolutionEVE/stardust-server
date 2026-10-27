"""Safe Memory Reclamation: freeing memory that other threads may still be reading, without crashes."""
CODE = 'computing5_hazard_pointers'
BOOK = {'title': 'Safe Memory Reclamation',
 'subtitle': 'Hazard pointers, epochs, read-copy-update and their costs',
 'chapters': [('The freeing problem',
               'In lock-free code a thread may remove a node while another thread is still reading '
               'it. Freeing the memory too early causes crashes or wrong results. Deciding when '
               'memory is safe to free is the hard part.'),
              ('Hazard pointers',
               'Each thread publishes the pointers it is about to read, called hazard pointers. '
               'Before freeing a node, a thread checks that no hazard pointer points to it. '
               'Michael described this method in 2004.'),
              ('Epochs',
               'Epoch-based reclamation groups time into periods. Memory removed in one period is '
               'freed once every thread has moved past it. It is fast but can be held up by a '
               'thread that stalls.'),
              ('Read-copy-update',
               'Read-copy-update lets readers run without locks while a writer makes a new copy '
               'and swaps it in. The old copy is freed after all current readers finish. It is '
               'widely used in the Linux kernel.'),
              ('Garbage in lock-free code',
               'Removed nodes wait in a list until it is safe to free them. This garbage uses '
               'memory and must be managed. Good designs keep the waiting list short.'),
              ('Costs',
               'Each method adds some work on every read or write, and some slow down when threads '
               'stall. Designers weigh speed, memory use and simplicity. No method is best in '
               'every case.')],
 'test': [('Why is freeing memory tricky in lock-free code?',
           [('a', 'Memory cannot be freed at all'),
            ('b', 'Another thread may still be reading the node'),
            ('c', 'Memory is always full of paint'),
            ('d', 'Nodes cannot be removed')],
           'b'),
          ('What do hazard pointers record?',
           [('a', 'The weather of each thread'),
            ('b', 'The names of the programmers'),
            ('c', 'The pointers a thread is about to read'),
            ('d', 'The price of the server')],
           'c'),
          ('What does epoch-based reclamation do?',
           [('a', 'Frees memory at random'),
            ('b', 'Stops all threads for ever'),
            ('c', 'Copies the whole disk'),
            ('d', 'Frees memory once every thread has moved past its period')],
           'd'),
          ('Where is read-copy-update widely used?',
           [('a', 'In the Linux kernel'),
            ('b', 'In paper calendars'),
            ('c', 'In garden hoses'),
            ('d', 'In school timetables')],
           'a'),
          ('What is a cost of these methods?',
           [('a', 'They make all threads faster for free'),
            ('b', 'They remove the need for memory'),
            ('c', 'Extra work and memory, and some slow when threads stall'),
            ('d', 'They cost nothing at all')],
           'c')]}
