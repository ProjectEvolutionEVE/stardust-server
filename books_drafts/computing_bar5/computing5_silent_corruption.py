"""Silent Data Corruption: hardware errors that go unnoticed, and how large fleets catch them."""
CODE = 'computing5_silent_corruption'
BOOK = {'title': 'Silent Data Corruption',
 'subtitle': 'Undetected hardware errors, checksums, faulty cores and fleet testing',
 'chapters': [('Errors nobody sees',
               'Silent data corruption is a wrong result that the hardware does not report. The '
               'program carries on with bad data and no alarm rings. Such errors are hard to find '
               'because nothing crashes.'),
              ('Detection',
               'Detection needs checks that compare results, repeat calculations, or verify stored '
               'data. Each check costs time, so teams choose where they matter most. Finding a '
               'fault early saves much larger damage later.'),
              ('End-to-end checksums',
               'A checksum computed at the start and checked at the end can reveal corruption on '
               'the way. Checking the whole path catches errors that a check on one part would '
               'miss. Storage systems use this idea widely.'),
              ('Faulty cores',
               'Sometimes one processor core in a chip gives wrong answers while the others are '
               'fine. Finding that core can be a long hunt. Once found, it can be taken out of '
               'service.'),
              ('Testing at fleet scale',
               'Large operators run special tests across thousands of machines to find rare '
               'faults. A fault that shows up once in many millions of operations needs a lot of '
               'testing. Patterns across machines help narrow the search.'),
              ('Response',
               'When a fault is confirmed, teams isolate the machine, record the evidence and '
               'inform the makers. They also check the data it touched. A calm, written response '
               'keeps trust high.')],
 'test': [('What is silent data corruption?',
           [('a', 'A quiet keyboard'),
            ('b', 'A wrong result the hardware does not report'),
            ('c', 'A dark screen'),
            ('d', 'A bug in a song')],
           'b'),
          ('What is an end-to-end checksum?',
           [('a', 'A bill for the cables'),
            ('b', 'A list of staff names'),
            ('c', 'A check made at the start and verified at the end of a path'),
            ('d', 'A colour code')],
           'c'),
          ('What is a faulty core?',
           [('a', 'A core of apple'),
            ('b', 'A broken chair'),
            ('c', 'A loose cable'),
            ('d', 'One processor core that gives wrong answers')],
           'd'),
          ('Why is testing at fleet scale useful?',
           [('a', 'Rare faults show up only over many operations on many machines'),
            ('b', 'Single machines never have faults'),
            ('c', 'It makes the machines cheaper'),
            ('d', 'It stops all checks')],
           'a'),
          ('What is a good response to a confirmed fault?',
           [('a', 'Ignore it and hope'),
            ('b', 'Delete all the logs'),
            ('c', 'Isolate the machine, keep evidence and check the data it touched'),
            ('d', 'Tell no one ever')],
           'c')]}
