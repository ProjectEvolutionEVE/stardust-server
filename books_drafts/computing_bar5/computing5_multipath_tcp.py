"""Multipath TCP: one connection that uses several network paths at once, and how it handles a phone changing networks."""
CODE = 'computing5_multipath_tcp'
BOOK = {'title': 'Multipath TCP',
 'subtitle': 'One connection over many paths, subflows and handover',
 'chapters': [('One connection, many paths',
               'Ordinary TCP uses one path between two computers. Multipath TCP lets one '
               'connection use several paths, such as Wi-Fi and mobile data, at the same time. The '
               'user sees one normal connection.'),
              ('Subflows',
               'Each path carries a subflow, which behaves like a small TCP connection. The '
               'subflows share one stream of data. If one slows, the others can carry more.'),
              ('Coupled congestion control',
               'The subflows must not take more than a fair share together at a shared bottleneck. '
               'Coupled congestion control balances them so that a multipath user is not unfair to '
               'others. This is a central design goal.'),
              ('Mobile handover',
               'A phone that moves from Wi-Fi to mobile data can keep its connection alive by '
               'using the new path. The old path is dropped when it fails. This makes handover '
               'smoother for users.'),
              ('Deployment obstacles',
               'Some networks and middleboxes block or change unfamiliar TCP options. Multipath '
               'TCP is designed to fall back to ordinary TCP when this happens. Deployment still '
               'needs careful testing.'),
              ('Uses',
               'Phones, servers and some operating systems use multipath TCP to gain speed and '
               'resilience. It is most useful where two or more links are available. The benefit '
               'grows with the number of good paths.')],
 'test': [('What does multipath TCP allow?',
           [('a', 'Ten computers to share one cable'),
            ('b', 'One connection to use several network paths at once'),
            ('c', 'A network without any cable'),
            ('d', 'Email without a server')],
           'b'),
          ('What is a subflow?',
           [('a', 'A river beside a city'),
            ('b', 'A kind of password'),
            ('c',
             'A path-carrying part of one connection that behaves like a small TCP connection'),
            ('d', 'A printer driver')],
           'c'),
          ('What does coupled congestion control aim to do?',
           [('a', 'Stop all traffic at night'),
            ('b', 'Double every bill'),
            ('c', 'Remove the screen'),
            ('d', 'Keep a multipath user from taking an unfair share at a shared bottleneck')],
           'd'),
          ('How does multipath TCP help a phone moving between networks?',
           [('a', 'It can keep the connection alive by using the new path'),
            ('b', 'It always disconnects the phone'),
            ('c', 'It turns the phone off'),
            ('d', 'It changes the phone colour')],
           'a'),
          ('What happens if a network blocks unfamiliar TCP options?',
           [('a', 'The computer explodes'),
            ('b', 'All data is printed'),
            ('c', 'Multipath TCP is designed to fall back to ordinary TCP'),
            ('d', 'The connection is made faster')],
           'c')]}
