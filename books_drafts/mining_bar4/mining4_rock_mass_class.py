"""Rock Mass Classification Systems: scoring the rock to choose the right support and the right mining method."""
CODE = 'mining4_rock_mass_class'
BOOK = {'title': 'Rock Mass Classification Systems',
 'subtitle': 'Rock Mass Rating, the Q-system and the Geological Strength Index',
 'chapters': [('Why classify rock',
               'Rock is never the same from one place to the next. A classification system gives a '
               'score to a section of rock, so engineers can compare places and choose the right '
               'support in a clear, repeatable way.'),
              ('Rock Mass Rating',
               'Rock Mass Rating, developed by Bieniawski, adds up scores for the strength of the '
               'rock, the spacing of its joints, the condition of those joints, groundwater and '
               'the orientation of the joints. The total gives a rating from 0 to 100.'),
              ('The Q-system',
               'The Q-system, developed by Barton and colleagues, uses six parameters to give a '
               'single number for the rock. It is widely used to choose tunnel support and bolt '
               'spacing.'),
              ('The Geological Strength Index',
               'The Geological Strength Index, or GSI, is a quick visual way to estimate the '
               'condition of a rock mass. Engineers look at the blockiness and the surface of the '
               'joints, and read a value from a chart.'),
              ('Choosing support',
               'Each score points to a type of support, such as bolts, mesh, or shotcrete. Weaker '
               'rock needs heavier support, and stronger rock needs less.'),
              ('Limits of ratings',
               'Ratings are guides, not guarantees. They depend on the quality of the data, and '
               'they can be wrong if the rock is not sampled well. Engineers always check the '
               'ratings against what they see in the mine.')],
 'test': [('Why do mines use rock classification systems?',
           [('a', 'To set the price of the ore'),
            ('b', 'To count the workers'),
            ('c', 'To compare places and choose support in a repeatable way'),
            ('d', 'To pick the colour of the trucks')],
           'c'),
          ('What does Rock Mass Rating add up?',
           [('a',
             'Scores for rock strength, joint spacing, joint condition, groundwater and joint '
             'orientation'),
            ('b', 'The number of trucks and their fuel'),
            ('c', 'The price of the explosives'),
            ('d', 'The hours worked by each crew')],
           'a'),
          ('What is the Geological Strength Index?',
           [('a', 'A pump rating'),
            ('b', 'A shift schedule'),
            ('c', 'A type of drill bit'),
            ('d', 'A quick visual way to estimate the condition of a rock mass')],
           'd'),
          ('What does weaker rock usually need?',
           [('a', 'No support at all'),
            ('b', 'Heavier support'),
            ('c', 'Less inspection'),
            ('d', 'A bigger truck')],
           'b'),
          ('What is a limit of rock ratings?',
           [('a', 'They are always exact'),
            ('b', 'They tell the colour of the ore'),
            ('c', 'They are guides, and can be wrong if the rock is not sampled well'),
            ('d', 'They replace all inspection')],
           'c')]}
