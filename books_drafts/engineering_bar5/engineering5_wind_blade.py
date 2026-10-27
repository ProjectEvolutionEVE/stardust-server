"""Wind Turbine Blade Loads and Fatigue: aerodynamic loads, gust response, blade fatigue, fatigue testing, and the money side of lifetime cost."""
CODE = 'engineering5_wind_blade'
BOOK = {'title': 'Wind Turbine Blade Loads and Fatigue',
 'subtitle': 'Aerodynamic loads, gusts, fatigue testing and the lifetime cost of a blade',
 'chapters': [('Blades as wings',
               'A wind turbine blade works like an aircraft wing. Wind passing over it creates lift that '
               'turns the rotor. The blade carries large bending loads each time it turns through the wind.'),
              ('Aerodynamic loads',
               'The loads on a blade come from the wind pressure across its surface. They change with wind '
               'speed, direction and the angle of the blade. Engineers calculate these loads for the full '
               'range of conditions the turbine will see.'),
              ('Gust response',
               'Sudden gusts give sharp increases in load on the blade. The blade flexes, and the flex '
               'changes the loads again. Designers test the gust response to make sure the blade stays safe '
               'in strong winds.'),
              ('Blade fatigue',
               'Each turn of the rotor flexes the blade a little, and the repeated flexing causes fatigue. '
               'Over twenty years or more, millions of cycles can cause cracks. Engineers design the blade '
               'so the stresses stay low enough for its full life.'),
              ('Fatigue testing',
               'Full-size blades are tested in a laboratory by flexing them for many cycles at high load. '
               'The test checks the design long before a blade goes to a site. The results are used to prove '
               'the blade will last.'),
              ('The money side of lifetime cost',
               'The cost of a turbine is judged by its cost of energy over its life. A blade that lasts '
               'longer or needs less repair can give a better return even if it costs more to make. '
               'Designers weigh the blade cost against the energy it will make over its life.')],
 'test': [('How does a wind turbine blade work?',
           [('a', 'It works like a wing, creating lift that turns the rotor'),
            ('b', 'It works like a sail on a boat only'),
            ('c', 'It is a wheel on a road'),
            ('d', 'It works like a hammer')],
           'a'),
          ('What causes the loads on a blade?',
           [('a', 'Paint on the surface'),
            ('b', 'Passengers in the cabin'),
            ('c', 'Wind pressure across its surface'),
            ('d', 'Sunlight only')],
           'c'),
          ('What is fatigue in a blade?',
           [('a', 'Tiredness of the crew'),
            ('b', 'Cracks that grow from repeated flexing'),
            ('c', 'Paint wearing out in a day'),
            ('d', 'Loss of colour')],
           'b'),
          ('Why are full-size blades tested in a laboratory?',
           [('a', 'To paint them'),
            ('b', 'To weigh them only'),
            ('c', 'To sell them by the metre'),
            ('d', 'To flex them for many cycles and prove they will last')],
           'd'),
          ('What is the best measure to judge a turbine by?',
           [('a', 'The colour of the tower'),
            ('b', 'The number of birds nearby'),
            ('c', 'Its cost of energy over its life'),
            ('d', 'The number of paint coats')],
           'c')]}
