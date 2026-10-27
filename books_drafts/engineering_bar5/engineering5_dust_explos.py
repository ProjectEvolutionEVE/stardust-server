"""Dust Explosions and Explosion Venting: concentration limits, pressure rise, venting and suppression."""
CODE = 'engineering5_dust_explos'
BOOK = {'title': 'Dust Explosions and Explosion Venting',
 'subtitle': 'Fuel, air, ignition, confinement and how to relieve the pressure',
 'chapters': [('The dust explosion pentagon',
               'A dust explosion needs five things: fuel in the form of dust, oxygen from the air, an '
               'ignition source, dust spread in a cloud, and confinement. Remove any one of the five and the '
               'explosion cannot start or grow. This is often drawn as a pentagon.'),
              ('Concentration limits',
               'Dust must be in the air at a certain density before it can burn. Too little dust will not '
               'ignite, and too much can be too rich to burn well. The lowest concentration that can explode '
               'is called the minimum explosible concentration.'),
              ('Pressure rise',
               'When dust burns inside a closed space, the gas expands and the pressure rises very quickly. '
               'Confined spaces such as silos, mills and ducts build pressure far faster than open ones. '
               'That rise is what destroys walls and roofs.'),
              ('Explosion venting',
               'Explosion venting provides a weak panel or opening that bursts first and lets the pressure '
               'out. It is sized so that the pressure stays below the strength of the structure. Vents must '
               'point to a safe area.'),
              ('Suppression',
               'Suppression detects the start of an explosion and sprays a chemical into the enclosure '
               'within milliseconds. It stops the flame before the pressure gets high. Suppression is often '
               'used where venting is not practical.'),
              ('Housekeeping and the money side',
               'Clean floors and ledges stop dust from settling and building up. Cleaning costs money, but a '
               'fire or explosion costs far more. Good housekeeping is one of the cheapest safeguards a '
               'plant can have.')],
 'test': [('How many things does the dust explosion pentagon list?',
           [('a', 'Five'), ('b', 'Three'), ('c', 'Four'), ('d', 'Six')],
           'a'),
          ('What is the minimum explosible concentration?',
           [('a', 'The largest size of a silo'),
            ('b', 'The lowest dust concentration that can explode'),
            ('c', 'The fastest speed of a fan'),
            ('d', 'The weight of a bag of flour')],
           'b'),
          ('Why does pressure rise faster in a confined space?',
           [('a', 'The walls are painted'),
            ('b', 'The air is colder'),
            ('c', 'The gas has nowhere to expand, so pressure builds'),
            ('d', 'The dust is lighter')],
           'c'),
          ('What does an explosion vent do?',
           [('a', 'It adds more dust'),
            ('b', 'It locks the doors'),
            ('c', 'It measures the weather'),
            ('d', 'It bursts first and lets pressure out to a safe area')],
           'd'),
          ('What does suppression do?',
           [('a', 'It sprays a chemical that stops the flame before pressure gets high'),
            ('b', 'It turns on the lights'),
            ('c', 'It sweeps the floor'),
            ('d', 'It sends an email to the owner')],
           'a')]}
