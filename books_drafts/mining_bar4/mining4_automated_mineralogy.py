"""Automated Mineralogy and Grain Maps: using scanning electron microscopes to map minerals, grain sizes and liberation for planning and processing."""
CODE = 'mining4_automated_mineralogy'
BOOK = {'title': 'Automated Mineralogy and Grain Maps',
 'subtitle': 'Mapping every mineral grain in a sample',
 'chapters': [('SEM-based mineral mapping',
               'A scanning electron microscope can be set to scan a polished sample automatically. It '
               'records the mineral at every point across the surface. The result is a colour map of the '
               'minerals in the rock.'),
              ('Grain size distributions',
               'The map shows the size of each mineral grain. The distribution of sizes matters for '
               'processing. Fine grains are harder to separate than coarse ones.'),
              ('Mineral associations',
               'The map also shows which minerals touch one another. Ore minerals that sit inside other '
               'minerals are harder to free. Association tells the team how the ore will behave in the '
               'plant.'),
              ('Liberation estimates',
               'Liberation is the share of an ore mineral that is free, not locked inside another mineral. A '
               'high liberation means the ore can be separated more easily. Liberation estimates guide the '
               'grinding size.'),
              ('Data reports',
               'Automated systems produce reports with tables and charts. Each report lists the minerals, '
               'their amounts and their sizes. The reports are checked by a trained mineralogist before '
               'use.'),
              ('Using maps in planning',
               'Grain maps help plan how fine the ore should be ground. They also help predict recovery at '
               'the plant. A plant designed with the maps in mind is more likely to work as planned.')],
 'test': [('What does a scanning electron microscope do in automated mineralogy?',
           [('a', 'Cooks the sample'),
            ('b', 'Maps the minerals at each point across a polished sample'),
            ('c', 'Paints the sample'),
            ('d', 'Sends the sample into space')],
           'b'),
          ('What is liberation?',
           [('a', 'The price of the sample'),
            ('b', 'The weight of the box'),
            ('c', 'The colour of the map'),
            ('d', 'The share of an ore mineral that is free from other minerals')],
           'd'),
          ('Why do grain sizes matter for processing?',
           [('a', 'Fine grains are harder to separate than coarse ones'),
            ('b', 'Grain size has no effect'),
            ('c', 'Coarse grains are always gold'),
            ('d', 'Fine grains float away')],
           'a'),
          ('What does a high liberation mean?',
           [('a', 'The ore cannot be used'),
            ('b', 'The ore is hidden inside ice'),
            ('c', 'The ore can be separated more easily'),
            ('d', 'The ore is too hot')],
           'c'),
          ('Why is a mineralogist still needed to check the reports?',
           [('a', 'The reports are always wrong'),
            ('b', 'Automated results must be checked before use'),
            ('c', 'Reports cannot be read'),
            ('d', 'The machine needs a driver')],
           'b')]}
