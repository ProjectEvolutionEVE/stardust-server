"""Erasure Coding: how parity pieces let lost data come back, with less space than copies."""
CODE = 'computing5_erasure_coding'
BOOK = {'title': 'Erasure Coding',
 'subtitle': 'Parity across fragments, Reed-Solomon codes and repair',
 'chapters': [('Pieces and parity',
               'Erasure coding cuts data into data fragments and then makes parity fragments from '
               'them. The parity fragments hold extra information. If some fragments are lost, the '
               'rest can rebuild them.'),
              ('Reed-Solomon codes',
               'Reed-Solomon is the classic family of erasure codes. With k data fragments and m '
               'parity fragments, any k of the k plus m pieces can rebuild the object. It was '
               'invented in 1960 and is still widely used.'),
              ('Storage overhead',
               'Three full copies use three times the space. A code with 10 data and 4 parity '
               'fragments uses 1.4 times the space and survives any 4 lost pieces. The trade-off '
               'is more work when data is read back or repaired.'),
              ('Repair traffic',
               'When a piece is lost, a Reed-Solomon system may need to read many surviving pieces '
               'to rebuild one. This uses network and disk time. Designers measure repair traffic '
               'as well as storage cost.'),
              ('Locally repairable codes',
               'Locally repairable codes add small groups of parity so that a single lost piece '
               'can be rebuilt from a few neighbours. This cuts repair traffic at a small cost in '
               'space. It is a deliberate trade between cost and speed.'),
              ('Losing a whole region',
               'Pieces must be spread across different machines, racks and places. If all the '
               'pieces sit in one building, one fire can lose everything. Good placement treats '
               'the whole region as a possible failure.')],
 'test': [('What do parity fragments do?',
           [('a', 'They make the data larger for no reason'),
            ('b', 'They hold extra information so lost pieces can be rebuilt'),
            ('c', 'They replace the owner'),
            ('d', 'They hide the data from the network')],
           'b'),
          ('What is Reed-Solomon?',
           [('a', 'A brand of storage drive'),
            ('b', 'A type of web browser'),
            ('c', 'A classic family of erasure codes'),
            ('d', 'A kind of password')],
           'c'),
          ('Compared with three full copies, what does a 10 plus 4 code use?',
           [('a', 'Three times the space'),
            ('b', 'Half the space'),
            ('c', 'Exactly the same space'),
            ('d', 'About 1.4 times the space')],
           'd'),
          ('What is repair traffic?',
           [('a', 'The data sent over the network to rebuild lost pieces'),
            ('b', 'Cars that drive to the data centre'),
            ('c', 'Traffic lights in a city'),
            ('d', 'Emails about repairs')],
           'a'),
          ('Why spread pieces across places?',
           [('a', 'So the pieces are harder to read'),
            ('b', 'So each piece costs more'),
            ('c', 'So one fire or outage cannot take every piece'),
            ('d', 'So the data can be printed')],
           'c')]}
