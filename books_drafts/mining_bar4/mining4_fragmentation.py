"""Rock Fragmentation Models: predicting how big the broken pieces will be, and measuring it with images."""
CODE = 'mining4_fragmentation'
BOOK = {'title': 'Rock Fragmentation Models',
 'subtitle': 'Size distributions, blast design and measuring the rubble',
 'chapters': [('Why size matters',
               'The size of the broken rock decides how fast the loaders work, how well the '
               'crusher runs and how much energy the mill needs. A good blast gives pieces of the '
               'right size with few very large ones.'),
              ('Size distributions',
               'A size distribution shows what share of the broken rock falls in each size range. '
               'Mines describe it with a curve, so they can compare one blast with another.'),
              ('The Rosin-Rammler curve',
               'The Rosin-Rammler model is a common curve for blasted rock. It uses a size '
               'constant and a uniformity index, so a single equation describes the whole spread '
               'of sizes.'),
              ('Energy and blast design',
               'More explosive energy usually gives finer rock, but it also costs more and can '
               'throw rock or vibrate the ground. Blast design sets hole spacing, burden and '
               'timing to balance size against cost.'),
              ('Oversize and fines',
               'Oversize boulders must be broken again, which costs time and money. Fines are very '
               'small particles, which can be wasteful if they are not needed. Good design limits '
               'both.'),
              ('Measuring with images',
               'Cameras photograph the muckpile after a blast, and software estimates the sizes of '
               'the pieces in the picture. This gives fast feedback on the blast without stopping '
               'the work.')],
 'test': [('Why does rock size matter to the mine?',
           [('a', 'It decides the colour of the ore'),
            ('b', 'It changes the weather'),
            ('c', 'It affects loading, crushing and the energy the mill needs'),
            ('d', 'It sets the price of diesel')],
           'c'),
          ('What does a size distribution show?',
           [('a', 'The share of the broken rock in each size range'),
            ('b', 'The depth of the mine'),
            ('c', 'The number of blasts per year'),
            ('d', 'The age of the workers')],
           'a'),
          ('What is an oversize boulder?',
           [('a', 'A type of explosive'),
            ('b', 'A very fine dust'),
            ('c', 'A tool for drilling'),
            ('d', 'A piece too big and needing to be broken again')],
           'd'),
          ('How are cameras used in fragmentation work?',
           [('a', 'To film the miners at lunch'),
            ('b', 'To photograph the muckpile and estimate the sizes of the pieces'),
            ('c', 'To measure the air pressure'),
            ('d', 'To read the ore grade directly')],
           'b'),
          ('What does more explosive energy usually give?',
           [('a', 'Larger rock at lower cost'),
            ('b', 'No change at all'),
            ('c', 'Finer rock, but at higher cost'),
            ('d', 'Rock that cannot be loaded')],
           'c')]}
