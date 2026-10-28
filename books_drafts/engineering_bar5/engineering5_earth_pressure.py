"""Earth Pressure Theory: Rankine and Coulomb, active and passive pressure, wall friction, surcharge and wall checks."""
CODE = 'engineering5_earth_pressure'
BOOK = {'title': 'Earth Pressure Theory: Rankine and Coulomb',
 'subtitle': 'Active and passive pressure, wall friction, surcharge loads and the checks for a retaining '
             'wall',
 'chapters': [('Why soil pushes on walls',
               'Soil pushes sideways on any wall that holds it back. That push, called earth pressure, is '
               'one of the main loads a retaining wall must carry. Engineers estimate it with theories that '
               'model how soil behaves.'),
              ('Active and passive pressure',
               'Active pressure is the lowest push, and it acts when a wall moves slightly away from the '
               'soil. Passive pressure is the largest resistance, and it acts when a wall is pushed into the '
               'soil. Designers use the active value for most retaining walls.'),
              ('Rankine and Coulomb',
               'Rankine theory assumes a smooth wall with no friction and a flat soil surface. Coulomb '
               'theory includes friction between the wall and the soil. The two give close answers when the '
               'wall is smooth, and Coulomb is more realistic when friction is high.'),
              ('Surcharge loads',
               'A surcharge is an extra load on top of the soil, such as a road, a building or stored '
               'materials. A surcharge adds to the earth pressure on the wall. Designers add its effect to '
               'the soil pressure before checking the wall.'),
              ('Wall design checks',
               'A retaining wall must be checked against sliding, tipping and the strength of the soil under '
               'it. Each check compares the resisting forces with the pushing forces. A wall that fails any '
               'check must be made stronger or changed.'),
              ('The money side',
               'Walls cost money in concrete, steel and labour. A wall designed too heavily wastes money, '
               'and one designed too lightly can fail. Careful use of the correct theory keeps the wall safe '
               'without excess cost.')],
 'test': [('Which earth pressure is the lowest?',
           [('a', 'Passive pressure'),
            ('b', 'Surcharge pressure'),
            ('c', 'Wall pressure'),
            ('d', 'Active pressure')],
           'd'),
          ('When does active pressure act?',
           [('a', 'When a wall moves slightly away from the soil'),
            ('b', 'When the wall is painted'),
            ('c', 'When the sun is high'),
            ('d', 'When the soil is dry and warm')],
           'a'),
          ('What does Coulomb theory include that Rankine theory assumes away?',
           [('a', 'The price of cement'),
            ('b', 'Wall friction'),
            ('c', 'The colour of the soil'),
            ('d', 'The age of the engineer')],
           'b'),
          ('What is a surcharge?',
           [('a', 'A discount on steel'),
            ('b', 'A type of drainage pipe'),
            ('c', 'An extra load on top of the soil'),
            ('d', 'A kind of weather')],
           'c'),
          ('Which of these is a wall design check?',
           [('a', 'Checking the wall for a favourite colour'),
            ('b', 'Counting the bricks in a shop'),
            ('c', 'Asking the wall how it feels'),
            ('d', 'Checking the wall against sliding')],
           'd')]}
