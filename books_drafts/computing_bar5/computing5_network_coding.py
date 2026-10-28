"""Network Coding: mixing packets inside the network to gain throughput, and the theory behind the idea."""
CODE = 'computing5_network_coding'
BOOK = {'title': 'Network Coding',
 'subtitle': 'Max-flow min-cut, linear combinations, gains and reliability',
 'chapters': [('Mixing packets',
               'Network coding lets relay nodes combine packets rather than only forward them. The '
               'receiver then unpacks the mixture. This can carry more data over the same links.'),
              ('Max-flow min-cut',
               'The max-flow min-cut theorem says how much data a network can carry from source to '
               'sink. Its limit is set by the narrowest cut. Network coding was shown in 2000 to '
               'reach this limit in cases where plain routing cannot.'),
              ('Linear combinations',
               'A common form mixes packets as linear combinations, using arithmetic over a finite '
               'field. The receiver solves equations to recover the original packets. Enough '
               'independent mixtures give back all the data.'),
              ('Throughput gains',
               'Examples show that coding can raise throughput when routing alone must send '
               'copies. The gain depends on the network shape. It is not free in every case.'),
              ('Practical deployment',
               'Coding adds computing work at each relay and needs care in design. Some systems '
               'use it in wireless networks and storage. Real benefits must be weighed against the '
               'extra work.'),
              ('Reliability',
               'Mixed packets can be harder to repair when they are lost. Coding can also add '
               'redundancy that helps recovery. Designers choose how much redundancy the network '
               'needs.')],
 'test': [('What does network coding let relay nodes do?',
           [('a', 'Delete all packets'),
            ('b', 'Combine packets rather than only forward them'),
            ('c', 'Print every packet'),
            ('d', 'Turn packets into music')],
           'b'),
          ('What does the max-flow min-cut theorem describe?',
           [('a', 'The price of cables'),
            ('b', 'The height of masts'),
            ('c', 'How much data a network can carry, limited by its narrowest cut'),
            ('d', 'The number of staff')],
           'c'),
          ('What is a linear combination of packets?',
           [('a', 'A straight line drawn on paper'),
            ('b', 'A list of names'),
            ('c', 'A bus timetable'),
            ('d', 'Mixing packets using arithmetic so the receiver can solve for the originals')],
           'd'),
          ('What can network coding improve?',
           [('a', 'Throughput over the same links in some networks'),
            ('b', 'The colour of the cables'),
            ('c', 'The length of the day'),
            ('d', 'The number of users in a room')],
           'a'),
          ('What is a cost of network coding?',
           [('a', 'It stops all data for ever'),
            ('b', 'It needs no design at all'),
            ('c', 'Extra computing work at each relay'),
            ('d', 'It uses only paper')],
           'c')]}
