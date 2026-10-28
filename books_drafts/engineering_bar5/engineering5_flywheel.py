"""Flywheel Rotor Design and Stresses: rim stress, composite rotors, speed limits, bearings, containment, and the money side of cost per stored kilowatt-hour."""
CODE = 'engineering5_flywheel'
BOOK = {'title': 'Flywheel Rotor Design and Stresses',
 'subtitle': 'Spinning rotors, rim stress, containment, and the cost of stored energy',
 'chapters': [('Energy in a spin',
               'A flywheel stores energy as rotation. The energy grows with the square of the speed, so '
               'doubling the speed gives four times the energy. A heavy rotor spun fast holds a great deal '
               'of energy in a small space.'),
              ('Rim stress',
               'As a rotor spins, its rim is pulled outward by the force of its own spin. This rim stress is '
               'the main limit on the speed of a rotor. Engineers design the shape and the material so that '
               'the stress stays well below the strength of the rotor.'),
              ('Composite rotors',
               'Carbon fibre composite rotors can spin much faster than steel because they are light and '
               'very strong along the fibres. Their design is harder, since they are weak across the fibres. '
               'Careful layup and testing are essential.'),
              ('Bearings',
               'Bearings hold the rotor and let it spin with little loss. Magnetic bearings can remove most '
               'friction, while mechanical bearings are simpler and cheaper. The choice affects the losses '
               'and the service needs.'),
              ('Containment',
               'If a rotor fails, its parts fly out at high speed. A containment vessel is a strong shell '
               'that catches the parts and protects people and equipment nearby. Containment is a required '
               'part of any high-speed flywheel.'),
              ('The money side',
               'Engineers judge a flywheel by its cost per stored kilowatt-hour, which includes the rotor, '
               'the bearings, the vessel and the power electronics. A flywheel that lasts for many cycles '
               'can cost less per unit of energy than a battery that wears out sooner. The lifetime number '
               'tells the story.')],
 'test': [('How does the energy of a flywheel change when its speed doubles?',
           [('a', 'It stays the same'),
            ('b', 'It becomes zero'),
            ('c', 'It becomes four times as large'),
            ('d', 'It doubles exactly')],
           'c'),
          ('What is rim stress?',
           [('a', 'The outward pull on the rim from the rotor spinning'),
            ('b', 'The stress in a pair of shoes'),
            ('c', 'A paint problem'),
            ('d', 'A problem with the lights')],
           'a'),
          ('Why can carbon fibre rotors spin faster than steel ones?',
           [('a', 'They are heavier'),
            ('b', 'They do not spin at all'),
            ('c', 'They are light and very strong along the fibres'),
            ('d', 'They are made of paper')],
           'c'),
          ('What is the job of a containment vessel?',
           [('a', 'To hold the cargo'),
            ('b', 'To catch parts if the rotor fails'),
            ('c', 'To make the rotor spin slower'),
            ('d', 'To store water')],
           'b'),
          ('What is the cost measure used to judge a flywheel?',
           [('a', 'Cost per seat'),
            ('b', 'Cost per window'),
            ('c', 'Cost per colour'),
            ('d', 'Cost per stored kilowatt-hour')],
           'd')]}
