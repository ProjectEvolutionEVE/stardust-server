"""Peer-to-Peer Systems and BitTorrent: how people share files directly with each other, and why fairness is hard."""
CODE = 'computing5_p2p_bittorrent'
BOOK = {'title': 'Peer-to-Peer Systems and BitTorrent',
 'subtitle': 'Piece selection, incentives, tit-for-tat, DHT lookup and free riding',
 'chapters': [('Peers sharing directly',
               'In a peer-to-peer system, each computer is both a client and a server. Users share '
               'pieces of files with one another rather than with one central server. The load '
               'grows as more people join.'),
              ('Piece selection',
               'BitTorrent splits a file into pieces. Peers choose which pieces to fetch next, '
               'often the rarest first. This keeps every piece available across the group.'),
              ('Incentives and tit-for-tat',
               'Peers tend to upload to those who upload to them. This tit-for-tat rule was '
               'described by Bram Cohen when he designed BitTorrent. It rewards generous peers '
               'with faster downloads.'),
              ('DHT lookup',
               'A distributed hash table lets peers find each other without a central list. Each '
               'peer knows a few others and can search the group in a few steps. Kademlia is a '
               'well-known design.'),
              ('Free riding',
               'Some users download but never upload. Such free riders use capacity without giving '
               'back. Systems try to limit them with incentives, though none is perfect.'),
              ('Trust',
               'Peers cannot always trust one another, so files can be checked against published '
               'hashes. Trust is built into the protocol through checks and reputation. Trust '
               'remains a real challenge.')],
 'test': [('What is a peer in a peer-to-peer system?',
           [('a', 'A person in a group photo'),
            ('b', 'A computer that is both a client and a server'),
            ('c', 'A type of cable'),
            ('d', 'A printer')],
           'b'),
          ('What is piece selection?',
           [('a', 'Picking a film to watch'),
            ('b', 'Selecting paint colours'),
            ('c', 'Choosing which parts of a file to fetch next'),
            ('d', 'Choosing a bus seat')],
           'c'),
          ('What does tit-for-tat reward?',
           [('a', 'Peers who never share'),
            ('b', 'Peers who are silent'),
            ('c', 'Peers who break the network'),
            ('d', 'Peers who upload to those who upload to them')],
           'd'),
          ('What is a DHT used for?',
           [('a', 'Letting peers find each other without a central list'),
            ('b', 'Printing documents'),
            ('c', 'Cooling the computer'),
            ('d', 'Writing poems')],
           'a'),
          ('What is free riding?',
           [('a', 'Travelling on a free bus'),
            ('b', 'Sharing every piece'),
            ('c', 'Downloading without uploading in return'),
            ('d', 'Running a server')],
           'c')]}
