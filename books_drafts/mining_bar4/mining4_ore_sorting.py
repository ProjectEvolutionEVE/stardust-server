"""Sensor-Based Ore Sorting: rejecting waste rock early, using X-ray and optical sensors on each rock as it passes."""
CODE = 'mining4_ore_sorting'
BOOK = {'title': 'Sensor-Based Ore Sorting',
 'subtitle': 'X-ray transmission, colour sensors and throwing away waste early',
 'chapters': [('The idea',
               'Ore sorting looks at each rock piece as it passes on a belt, and it decides '
               'whether to keep the piece or reject it. Waste is removed before the ore goes to '
               'the expensive grinding and processing steps.'),
              ('X-ray transmission sorting',
               'In X-ray transmission sorting, the rock is passed between an X-ray source and a '
               'detector. Denser pieces, which often hold more valuable metal, block more of the '
               'X-rays, and the sorter uses this to tell pieces apart.'),
              ('Colour and near-infrared sensors',
               'Cameras and near-infrared sensors read the colour and the reflected light of each '
               'piece. They are useful for minerals that look different from the waste around '
               'them.'),
              ('Pre-concentration',
               'Sorting makes the feed richer before it reaches the mill. This is called '
               'pre-concentration, and it lowers the cost of the processing that follows.'),
              ('Water saved',
               'Rejecting waste early means less rock is ground and treated with water. Mines that '
               'sort ore often save water and reduce the size of the tailings.'),
              ('Setting thresholds',
               'Each sorter uses a threshold to separate ore from waste. Engineers set the '
               'threshold to balance the grade of the ore kept against the amount of ore lost to '
               'rejects.')],
 'test': [('What does ore sorting do to each rock piece?',
           [('a', 'It paints it'),
            ('b', 'It names it'),
            ('c', 'It decides whether to keep it or reject it'),
            ('d', 'It weighs the truck')],
           'c'),
          ('How does X-ray transmission sorting tell pieces apart?',
           [('a', 'Denser pieces block more X-rays, and the sorter uses this'),
            ('b', 'It listens for sound'),
            ('c', 'It smells the rock'),
            ('d', 'It tastes the ore')],
           'a'),
          ('What is pre-concentration?',
           [('a', 'Heating the ore in a pan'),
            ('b', 'Drying the tailings'),
            ('c', 'Mixing the ore with sand'),
            ('d', 'Making the feed richer before it reaches the mill')],
           'd'),
          ('Why does early rejection save water?',
           [('a', 'Water is poured onto the belt'),
            ('b', 'Less rock is ground and treated with water'),
            ('c', 'Water is not used in mines at all'),
            ('d', 'Water is only used for drinking')],
           'b'),
          ('What does a threshold in a sorter balance?',
           [('a', 'The price of diesel and the colour of the belt'),
            ('b', 'The number of cameras and the size of the mine'),
            ('c', 'The grade of ore kept against the ore lost to rejects'),
            ('d', 'The speed of the trucks and the weather')],
           'c')]}
