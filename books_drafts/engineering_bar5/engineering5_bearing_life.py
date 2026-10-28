"""Bearing Life Ratings and L10 Calculations: dynamic load ratings, L10 life, reliability adjustment, load spectra, and the money side of bearing downtime."""
CODE = 'engineering5_bearing_life'
BOOK = {'title': 'Bearing Life Ratings and L10 Calculations',
 'subtitle': 'Dynamic load ratings, L10 life, and the cost of downtime',
 'chapters': [('What a bearing rating means',
               'A bearing is rated by its dynamic load rating, which is the load it can carry for one '
               'million revolutions with about ninety percent of a group surviving. This standard load '
               'rating is printed in the maker catalogue. It is the starting point for every life '
               'calculation.'),
              ('L10 life',
               'The L10 life is the number of revolutions, or hours at a set speed, that ninety percent of a '
               'group of bearings reach before fatigue. For ball bearings it is found with the load rating '
               'divided by the applied load, cubed. For roller bearings the power is ten thirds.'),
              ('Reliability adjustment',
               'Designers may need a life with more than ninety percent surviving, such as ninety-five or '
               'ninety-nine percent. An adjustment factor reduces the L10 life to give the higher '
               'reliability. The choice depends on how serious a failure would be.'),
              ('Load spectra',
               'Real machines do not carry one steady load. A load spectrum lists the loads and the time '
               'spent at each. Engineers combine the spectrum into one equivalent load, so the life estimate '
               'reflects the actual work the bearing does.'),
              ('Lubrication and speed',
               'Life also depends on speed, lubrication and temperature, which affect the film of oil '
               'between the rolling parts. A good film keeps the surfaces apart. Poor lubrication can cut '
               'the real life well below the calculated L10 figure.'),
              ('The money side of downtime',
               'A bearing that fails stops the machine, and the cost of that stop can be far larger than the '
               'cost of the bearing. Engineers weigh the cost of a larger bearing against the cost of '
               'downtime. The cheapest bearing is often the most expensive choice once the stop is '
               'counted.')],
 'test': [('What does the dynamic load rating of a bearing describe?',
           [('a', 'The colour of the housing'),
            ('b', 'The number of seats in the cabin'),
            ('c', 'The load it can carry for a set life with most of a group surviving'),
            ('d', 'The price of the paint')],
           'c'),
          ('For ball bearings, what power is used in the L10 formula?',
           [('a', 'Ten'), ('b', 'Three'), ('c', 'Two'), ('d', 'One hundred')],
           'b'),
          ('What does the L10 life represent?',
           [('a', 'The life of the paint'),
            ('b', 'The number of passengers'),
            ('c', 'The colour of the crew'),
            ('d', 'The life that about ninety percent of a group reaches')],
           'd'),
          ('What is a load spectrum?',
           [('a', 'A colour chart'),
            ('b', 'A map of the stars'),
            ('c', 'A list of loads and the time spent at each'),
            ('d', 'A menu of foods')],
           'c'),
          ('Why can the cheapest bearing be the most expensive choice?',
           [('a', 'Because downtime from a failure can cost far more than the bearing'),
            ('b', 'Because cheap bearings are always heavier'),
            ('c', 'Because bearings never fail'),
            ('d', 'Because bearings are sold by the kilogram only')],
           'a')]}
