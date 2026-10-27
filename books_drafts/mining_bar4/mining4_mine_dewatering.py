"""Pumping Water Out of a Mine: finding the inflow, moving water through pumps and pipes, and lowering the water table."""
CODE = 'mining4_mine_dewatering'
BOOK = {'title': 'Pumping Water Out of a Mine',
 'subtitle': 'Inflow sources, sumps, pump stations and grout curtains',
 'chapters': [('Where water comes from',
               'Water enters a mine from rain, from streams, from groundwater in the rock and from '
               'old flooded workings. A good dewatering plan starts by finding each source and '
               'estimating how much water each one brings.'),
              ('Sumps and pump stations',
               'Water runs to a low point called a sump, where it collects. Pump stations lift it '
               'up through pipes, usually in stages, to the surface or to a settling pond.'),
              ('Pressure in pipes',
               'Pumping water up a deep shaft needs pressure, which is measured as a head. The '
               'pumps and pipes are sized so the head is enough to lift the water with a margin to '
               'spare.'),
              ('Grout curtains',
               'A grout curtain is a barrier of cement or other grout pumped into the rock to seal '
               'cracks. It cuts off water coming into the mine from a particular direction.'),
              ('Lowering the water table',
               'Pumping from wells can lower the water table around the mine. This keeps the '
               'workings dry, but it also changes the water supply for people and wildlife nearby, '
               'so the effect must be planned.'),
              ('Monitoring wells',
               'Monitoring wells are drilled around the mine to measure the water level over time. '
               'Their readings show whether the dewatering works and whether the nearby water is '
               'affected.')],
 'test': [('Which of these is a source of water entering a mine?',
           [('a', 'Dry air from the fans'),
            ('b', 'The lights'),
            ('c', 'Groundwater in the rock'),
            ('d', 'The explosives')],
           'c'),
          ('What is a sump?',
           [('a', 'A low point where water collects before it is pumped out'),
            ('b', 'A type of drill'),
            ('c', 'A tunnel for trucks'),
            ('d', 'A roof bolt')],
           'a'),
          ('What is a grout curtain?',
           [('a', 'A curtain of fabric for the office'),
            ('b', 'A type of fuse'),
            ('c', 'A map of the ore'),
            ('d', 'A barrier of grout pumped into rock to seal cracks')],
           'd'),
          ('What do monitoring wells measure?',
           [('a', 'The number of trucks'),
            ('b', 'The water level over time'),
            ('c', 'The price of copper'),
            ('d', 'The age of the miners')],
           'b'),
          ('What can lowering the water table affect nearby?',
           [('a', 'Only the paint on the office walls'),
            ('b', 'The colour of the sky'),
            ('c', 'The water supply for people and wildlife'),
            ('d', 'Nothing at all')],
           'c')]}
