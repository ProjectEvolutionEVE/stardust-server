"""BBR Congestion Control: a sending method that measures bandwidth and delay rather than waiting for packets to be lost."""
CODE = 'computing5_bbr'
BOOK = {'title': 'BBR Congestion Control',
 'subtitle': 'Bandwidth and delay estimates, probing cycles, bufferbloat and fairness',
 'chapters': [('Sending at the right speed',
               'Congestion control decides how fast a sender should transmit. Too fast and the '
               'network queues and drops data. Too slow and capacity goes unused. BBR is one '
               'method for finding the right speed.'),
              ('Bandwidth and delay estimates',
               'BBR measures how much data gets through and how long it takes. From these it '
               'estimates the bottleneck speed and the round-trip delay. It aims to send at the '
               'rate the path can carry.'),
              ('Probing cycles',
               'BBR periodically tests for more bandwidth, then eases off to clear any queue it '
               'created. These cycles let it track changes in the path. The pattern repeats '
               'through each connection.'),
              ('Bufferbloat',
               'Bufferbloat is the build-up of long queues in network equipment, which adds delay '
               'and makes calls stutter. Loss-based methods fill the buffers before reacting. BBR '
               'tries to keep queues short.'),
              ('Comparison with loss-based control',
               'Loss-based methods treat a dropped packet as the signal to slow down. BBR relies '
               'on measurements instead. The two approaches can behave very differently on the '
               'same path.'),
              ('Fairness and deployment',
               'Researchers have debated whether BBR shares capacity fairly with loss-based '
               'methods. Google published BBR in 2016 and deployed it on its services. Its use '
               'continues to be studied and improved.')],
 'test': [('What does congestion control decide?',
           [('a', 'The colour of the router'),
            ('b', 'How fast a sender should transmit'),
            ('c', 'The name of a website'),
            ('d', 'The size of the screen')],
           'b'),
          ('What does BBR measure?',
           [('a', 'The number of staff'),
            ('b', 'The weather at the server'),
            ('c', 'Bandwidth and round-trip delay'),
            ('d', 'The length of a film')],
           'c'),
          ('What is bufferbloat?',
           [('a', 'A balloon for computers'),
            ('b', 'A fault in a monitor'),
            ('c', 'A bigger hard disk'),
            ('d', 'Long queues that add delay in network equipment')],
           'd'),
          ('How do loss-based methods usually react to a dropped packet?',
           [('a', 'They slow down'),
            ('b', 'They speed up sharply to fill the gap'),
            ('c', 'They stop the clock'),
            ('d', 'They print the packet')],
           'a'),
          ('Which company published BBR in 2016?',
           [('a', 'A bakery'), ('b', 'A car maker'), ('c', 'Google'), ('d', 'A bank in Lisbon')],
           'c')]}
