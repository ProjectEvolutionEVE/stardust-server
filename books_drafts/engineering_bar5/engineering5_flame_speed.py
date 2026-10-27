"""Laminar Flame Speed and Flame Stabilisation: premixed flames, flame speed measurement, flashback, blow-off, and stabilisation by bluff bodies."""
CODE = 'engineering5_flame_speed'
BOOK = {'title': 'Laminar Flame Speed and Flame Stabilisation',
 'subtitle': 'How fast a flame travels, and how to keep it in place',
 'chapters': [('A premixed flame',
               'In a premixed flame, the fuel and the air are mixed before they burn. The flame front then '
               'travels into the fresh mixture at a definite speed. That speed is the laminar flame speed, '
               'and it depends on the fuel, the mixture and the temperature.'),
              ('Measuring the flame speed',
               'Engineers measure the flame speed in a burner, a tube or a bomb, and read the flame front '
               'from photographs or light sensors. The result depends on the mixture strength and the '
               'pressure. Good measurements are the foundation of every flame model.'),
              ('Flashback',
               'Flashback happens when the flame moves back into the mixing tube or nozzle. It can occur '
               'when the flow speed falls below the flame speed. A flashback can destroy a burner, so '
               'designers keep the flow faster than the flame at every point.'),
              ('Blow-off',
               'Blow-off is the opposite problem: the flow is so fast that the flame is pushed away from its '
               'place and goes out. The flame can only stay lit where the local flow speed is close to its '
               'flame speed. Good designs keep a stable zone for the flame.'),
              ('Bluff bodies',
               'A bluff body is a blunt object placed in the flow behind which a small region of slow, hot '
               'gas forms. The flame anchors itself in that zone. The bluff body is a simple and robust way '
               'to hold a flame in a fast stream.'),
              ('Designing the stable zone',
               'A stable flame needs a balance: the flow must be fast enough to avoid flashback and slow '
               'enough to avoid blow-off. Engineers tune the burner geometry and the mixture until the zone '
               'is wide enough for every operating point. The result is a flame that stays put when the '
               'power changes.')],
 'test': [('What is a premixed flame?',
           [('a', 'A flame that burns nothing'),
            ('b', 'A flame where fuel and air are mixed before they burn'),
            ('c', 'A flame made of water'),
            ('d', 'A flame that never moves')],
           'b'),
          ('What is flashback?',
           [('a', 'A photo of a fire'),
            ('b', 'A light show'),
            ('c', 'A cooling step'),
            ('d', 'The flame moving back into the mixing tube or nozzle')],
           'd'),
          ('What is blow-off?',
           [('a', 'The flame turning blue on purpose'),
            ('b', 'A paint technique'),
            ('c', 'The flame being pushed away and going out in a fast flow'),
            ('d', 'A sort of shutter')],
           'c'),
          ('What is a bluff body used for in a burner?',
           [('a', 'To anchor the flame in a zone of slow, hot gas'),
            ('b', 'To make the flame colder'),
            ('c', 'To store the fuel'),
            ('d', 'To cool the cabin')],
           'a'),
          ('When does flashback tend to occur?',
           [('a', 'When the flow speed is very high'),
            ('b', 'When there is no fuel'),
            ('c', 'When the flow speed falls below the flame speed'),
            ('d', 'When the lights are on')],
           'c')]}
