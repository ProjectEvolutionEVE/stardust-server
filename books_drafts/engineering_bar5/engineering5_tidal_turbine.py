"""Tidal and Water Turbine Design: water density loads, cavitation, debris strikes, seals, and marine installation risks."""
CODE = 'engineering5_tidal_turbine'
BOOK = {'title': 'Tidal and Water Turbine Design',
 'subtitle': 'Dense water loads, cavitation, debris, seals and installation at sea',
 'chapters': [('Water is heavy',
               'Water is about eight hundred times denser than air. A turbine that turns in a tidal stream '
               'therefore sees far larger forces than a wind turbine of the same size. The blades and the '
               'structure must be built for that force.'),
              ('Cavitation',
               'Cavitation happens when the pressure on a blade falls so low that vapour bubbles form. The '
               'bubbles collapse with force and can pit the blade surface over time. Designers keep the '
               'pressure above the danger point by shaping the blades carefully.'),
              ('Debris strikes',
               'Sea and river water carry logs, rocks, weed and other debris. A strike can break a blade or '
               'bend a shaft. The design must survive the expected impacts, and the blades can be shaped to '
               'shed debris.'),
              ('Seals',
               'The turbine has bearings and shafts that must keep salt water out. Seals must resist '
               'corrosion, pressure and the grit that water carries. A leak in a sealed unit can destroy the '
               'bearings and the generator.'),
              ('Marine installation risks',
               'Installing a turbine on the sea bed needs ships, divers or remote tools, and the work '
               'depends on the weather and the tide. Each step carries risk. Engineers plan the work to '
               'reduce the time spent at sea.'),
              ('Maintenance and cost',
               'Maintenance at sea is costly, so the design aims for long gaps between visits. Each visit '
               'costs ship time and crew. The money side is judged over the whole life of the turbine, '
               'including the cost of the visits.')],
 'test': [('Why does a tidal turbine see larger forces than a wind turbine of the same size?',
           [('a', 'Water is lighter than air'),
            ('b', 'Tides are colder'),
            ('c', 'Water is much denser than air'),
            ('d', 'Fish push harder')],
           'c'),
          ('What is cavitation?',
           [('a', 'A type of paint'),
            ('b', 'Vapour bubbles forming when the pressure on a blade falls too low'),
            ('c', 'A kind of fish'),
            ('d', 'A rope on a deck')],
           'b'),
          ('What do debris strikes threaten?',
           [('a', 'Painting the tower'),
            ('b', 'Lighting the sea'),
            ('c', 'Cooling the air'),
            ('d', 'Breaking blades or bending shafts')],
           'd'),
          ('Why do the seals in a water turbine matter?',
           [('a', 'They make the turbine float'),
            ('b', 'They paint the blades'),
            ('c', 'They keep salt water out of the bearings and generator'),
            ('d', 'They store the power')],
           'c'),
          ('Why does the design aim for long gaps between maintenance visits?',
           [('a', 'Visits at sea are costly in ship time and crew'),
            ('b', 'Visits are free and quick'),
            ('c', 'Turbines never need any service'),
            ('d', 'Visits only change the colour')],
           'a')]}
