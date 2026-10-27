"""Cut-and-Fill Stoping: mining in horizontal slices from the bottom up, with fill as the working floor."""
CODE = 'mining4_cut_fill'
BOOK = {'title': 'Cut-and-Fill Stoping',
 'subtitle': 'Horizontal slices, backfill floors and careful ground support',
 'chapters': [('The idea',
               'In cut-and-fill mining, the ore is taken out in thin horizontal slices, starting '
               'at the bottom of the stope. After each slice is removed, the empty space is '
               'filled, and the next slice is cut on top of the fill.'),
              ('Backfill as a floor',
               'The fill becomes the floor the miners stand on while they cut the next slice. This '
               'means the miners never work on bare, unsupported ground above a void.'),
              ('Ground support',
               'Rock bolts, mesh and shotcrete hold the walls and roof while each slice is open. '
               'Support is checked before anyone enters the work area.'),
              ('The mining sequence',
               'A cut is drilled, blasted, and the broken ore is loaded out. Then the space is '
               'filled, and the cycle repeats level by level, so the stope rises as the work goes '
               'on.'),
              ('Weak ground',
               'Cut-and-fill is a good choice where the rock is weak or broken, because the fill '
               'supports the walls as you go. Very weak ground still needs close monitoring and '
               'strong support.'),
              ('Productivity trade-offs',
               'Cut-and-fill is slower than methods that leave voids open, and it needs fill '
               'material and extra handling. In return it recovers more of the ore and keeps the '
               'ground under control.')],
 'test': [('In which direction is the ore removed in cut-and-fill mining?',
           [('a', 'Straight down in a shaft'),
            ('b', 'Sideways from the surface'),
            ('c', 'In thin horizontal slices, from the bottom up'),
            ('d', 'In a spiral from the top')],
           'c'),
          ('What does the backfill become once it is placed?',
           [('a', 'The working floor for the next slice'),
            ('b', 'A pipe for water'),
            ('c', 'A roof that must be removed'),
            ('d', 'A store for fuel')],
           'a'),
          ('Which of these is a form of ground support?',
           [('a', 'Blast fuse'),
            ('b', 'Ore cars'),
            ('c', 'Ventilation fans only'),
            ('d', 'Rock bolts and mesh')],
           'd'),
          ('What is a main trade-off of cut-and-fill?',
           [('a', 'It is faster than leaving voids open'),
            ('b', 'It is slower and needs fill material, but recovers more ore'),
            ('c', 'It never needs support'),
            ('d', 'It works only in hard granite')],
           'b'),
          ('Why is cut-and-fill a good choice in weak ground?',
           [('a', 'Weak ground makes the ore heavier'),
            ('b', 'It removes the need for any monitoring'),
            ('c', 'The fill supports the walls as the mining goes on'),
            ('d', 'Weak rock produces no dust')],
           'c')]}
