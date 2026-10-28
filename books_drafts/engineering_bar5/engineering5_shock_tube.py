"""Shock Tubes and Test Facilities: diaphragm bursting, shock speed, test times, reservoir conditions, and measuring gas properties."""
CODE = 'engineering5_shock_tube'
BOOK = {'title': 'Shock Tubes and Test Facilities',
 'subtitle': 'Bursting the diaphragm, shock speed, and measuring gas in a short, sharp test',
 'chapters': [('A tube and a diaphragm',
               'A shock tube is a long tube split in two by a thin diaphragm. One side holds high-pressure '
               'gas, and the other holds low-pressure gas. When the diaphragm bursts, a shock wave runs down '
               'the low-pressure side and a set of expansion waves runs back into the high-pressure side.'),
              ('The shock and the contact surface',
               'Behind the shock, the gas is hot and compressed. A contact surface separates the hot gas '
               'from the gas that came from the driver side. The test gas is the one that sits in the region '
               'behind the shock.'),
              ('Shock speed',
               'The speed of the shock depends on how hard the diaphragm was loaded, meaning the pressure '
               'ratio across it. Engineers measure the shock speed with sensors along the tube. From that '
               'speed they work out the conditions behind the wave.'),
              ('Test time',
               'The hot, steady test gas lasts only a short time, often a few milliseconds. The test ends '
               'when the reflected expansions and the contact surface reach the measuring point. Long tests '
               'need a very large tube or a very long driver.'),
              ('Reservoir conditions',
               'Reservoir conditions are the pressure and temperature of the gas before the flow starts. '
               'They set the test state that the model will meet. Matching the reservoir state to the flight '
               'condition is the central problem of ground testing.'),
              ('Measuring the gas',
               'Because the shock speed and the pressure jump are both measured, the properties of the gas '
               'can be checked against theory. Engineers use this to find heat capacities and reaction '
               'rates. A shock tube is a precise instrument for learning how real gases behave.')],
 'test': [('What happens when the diaphragm in a shock tube bursts?',
           [('a', 'A shock wave runs down the low-pressure side'),
            ('b', 'Nothing at all'),
            ('c', 'The tube fills with water'),
            ('d', 'The tube turns into a boat')],
           'a'),
          ('What separates the hot gas from the driver gas behind the shock?',
           [('a', 'A heavy door'), ('b', 'A cloud of dust'), ('c', 'A contact surface'), ('d', 'A magnet')],
           'c'),
          ('What sets the speed of the shock?',
           [('a', 'The colour of the tube'),
            ('b', 'The pressure ratio across the diaphragm'),
            ('c', 'The number of windows'),
            ('d', 'The length of the carpet')],
           'b'),
          ('Why is the test time in a shock tube so short?',
           [('a', 'Because the gas freezes at once'),
            ('b', 'Because the tube is always empty'),
            ('c', 'Because the sensors are too slow'),
            ('d', 'Because reflected expansions and the contact surface soon reach the measuring point')],
           'd'),
          ('What is measured to find the gas properties?',
           [('a', 'The shape of the cloud'),
            ('b', 'The name of the pilot'),
            ('c', 'The shock speed and the pressure jump'),
            ('d', 'The weight of the hold')],
           'c')]}
