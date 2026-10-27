"""Safety Integrity Levels: the probability of failure on demand, fault tolerance and proof testing."""
CODE = 'engineering5_sil'
BOOK = {'title': 'Safety Integrity Levels and Calculations',
 'subtitle': 'Demand modes, failure probability, fault tolerance and proof testing',
 'chapters': [('What a safety integrity level is',
               'A safety integrity level, or SIL, is a grade of how reliably a safety function must work. It '
               'runs from SIL 1, the lowest, to SIL 4, the highest. Each level sets a limit on how often the '
               'function may fail.'),
              ('Demand modes',
               'A safety function that acts only when called upon works in low demand mode. One that acts '
               'all the time, or very often, works in high demand or continuous mode. The mode decides which '
               'way of measuring the failure rate applies.'),
              ('Probability of failure on demand',
               'For low demand functions, the average probability of failure on demand, or PFDavg, sets the '
               'SIL. A PFDavg from one in ten to one in a hundred is SIL 1. From one in a hundred to one in '
               'a thousand is SIL 2. Each step up is ten times stricter.'),
              ('Hardware fault tolerance',
               'Hardware fault tolerance is the number of faults a device can have while the safety function '
               'still works. A device with a tolerance of one keeps working after one fault. Higher '
               'tolerance usually means more parts and more money.'),
              ('Proof testing',
               'A proof test checks a safety function at set intervals to find hidden faults. The interval '
               'must be short enough to keep the failure probability within its limit. Skipping proof tests '
               'lets faults build up unseen.'),
              ('The money side of certification',
               'Certifying a SIL costs money for analysis, testing and paperwork. Higher levels cost more to '
               'design and to keep working. Choose the level the risk truly needs, because paying for a '
               'higher level than needed wastes money.')],
 'test': [('What does SIL stand for?',
           [('a', 'Steel Import Limit'),
            ('b', 'System Input Loop'),
            ('c', 'Safety Integrity Level'),
            ('d', 'Standard Insulation Line')],
           'c'),
          ('Which demand mode applies to a function that acts only when called upon?',
           [('a', 'Continuous mode'),
            ('b', 'High demand mode'),
            ('c', 'Zero mode'),
            ('d', 'Low demand mode')],
           'd'),
          ('A PFDavg from one in a hundred to one in a thousand is which level?',
           [('a', 'SIL 2'), ('b', 'SIL 1'), ('c', 'SIL 3'), ('d', 'SIL 4')],
           'a'),
          ('What is hardware fault tolerance?',
           [('a', 'The colour of the device'),
            ('b', 'The number of faults a device can have while still working'),
            ('c', 'The weight of the device'),
            ('d', 'The price of the device')],
           'b'),
          ('Why are proof tests carried out at set intervals?',
           [('a', 'To change the paint colour'),
            ('b', 'To count the operators'),
            ('c', 'To find hidden faults before they build up'),
            ('d', 'To delay the next purchase')],
           'c')]}
