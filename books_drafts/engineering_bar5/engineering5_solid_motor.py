"""Solid Rocket Motor Grain Design: grain geometry, burn surface, thrust profile, case stress, and casting of propellant."""
CODE = 'engineering5_solid_motor'
BOOK = {'title': 'Solid Rocket Motor Grain Design',
 'subtitle': 'Grain shape, burn surface, thrust profile, and the case that holds it',
 'chapters': [('The grain is the engine',
               'In a solid rocket motor, the propellant is cast into a solid block called the grain. The '
               'grain burns from its inside or its outside surfaces. Its shape is the single most important '
               'choice in the motor design.'),
              ('Burn surface and thrust',
               'Thrust depends on how much burning surface there is at each moment. As the grain burns, its '
               'surface changes, so the thrust changes too. Designers shape the grain to give the thrust '
               'curve the mission needs.'),
              ('Thrust profiles',
               'A neutral grain keeps the burn surface nearly constant, so the thrust stays steady. A '
               'progressive grain grows its surface, so the thrust rises over time. A regressive grain '
               'shrinks its surface, so the thrust falls as it burns.'),
              ('The case',
               'The case is the strong shell that holds the pressure of the burning gas. Its walls must '
               'carry the pressure with a safety margin, and the joints and the nozzle need extra care. The '
               'case often dominates the weight of the motor.'),
              ('Casting the propellant',
               'The propellant is mixed and poured into the case, then cured. Any void, crack or bond '
               'failure inside the grain can change the burn and cause a failure. Casting is a precise '
               'process, and quality checks are made at every stage.'),
              ('Testing and cost',
               'Each motor design is tested on the ground before flight. The tests check the thrust curve, '
               'the case and the bond. Because each test uses up a motor, the cost of testing is part of the '
               'price of every design.')],
 'test': [('What is the grain in a solid rocket motor?',
           [('a', 'The crew compartment'),
            ('b', 'The passenger seats'),
            ('c', 'The solid block of propellant'),
            ('d', 'The paint layer')],
           'c'),
          ('What does a neutral grain give?',
           [('a', 'Thrust that always rises'),
            ('b', 'Nearly steady thrust'),
            ('c', 'No thrust at all'),
            ('d', 'Thrust in the hold')],
           'b'),
          ('What does the case of a motor do?',
           [('a', 'It stores water'),
            ('b', 'It carries cargo'),
            ('c', 'It lights the cabin'),
            ('d', 'It holds the pressure of the burning gas')],
           'd'),
          ('What can cause a failure in a cast grain?',
           [('a', 'A clean surface'),
            ('b', 'A steady temperature'),
            ('c', 'A void, crack or bad bond inside the grain'),
            ('d', 'A calm day')],
           'c'),
          ('Why is the cost of testing part of the price of a solid motor?',
           [('a', 'Each test uses up a motor'),
            ('b', 'Testing is free of charge'),
            ('c', 'Motors are never tested'),
            ('d', 'Tests only use paint')],
           'a')]}
