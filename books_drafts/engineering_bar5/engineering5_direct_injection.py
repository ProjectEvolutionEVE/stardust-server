"""Direct Injection Spray Physics: atomisation, spray penetration, mixing, injector flow, and combustion phasing."""
CODE = 'engineering5_direct_injection'
BOOK = {'title': 'Direct Injection Spray Physics',
 'subtitle': 'Breaking fuel into a spray, mixing it, and timing the burn',
 'chapters': [('Fuel straight into the cylinder',
               'A direct injection engine sprays fuel straight into the cylinder rather than into the '
               'intake. The timing and shape of the spray decide how the charge mixes and burns. Good spray '
               'physics gives more power with less fuel.'),
              ('Atomisation',
               'Atomisation breaks the liquid fuel into a fine mist of droplets. Smaller droplets evaporate '
               'faster and burn more cleanly. The pressure at the injector nozzle is the main driver of how '
               'fine the mist becomes.'),
              ('Spray penetration',
               'Spray penetration is how far the fuel spray travels into the gas before it slows down. Too '
               'little penetration leaves fuel in the wrong place, and too much can wet the cylinder wall. '
               'Engineers match the penetration to the shape of the piston and the bowl.'),
              ('Mixing',
               'The fuel must mix with air before it burns, but the mixing time is very short. Swirl and '
               'tumble motion in the cylinder help spread the fuel and the air together. Mixing decides how '
               'smoothly the flame spreads.'),
              ('Injector flow',
               'The injector flow rate sets how much fuel is delivered each time. Its size and its shape '
               'decide how the fuel leaves the nozzle. Engineers check the flow in test rigs to make sure '
               'every injector delivers the same amount.'),
              ('Combustion phasing',
               'Combustion phasing is the moment in the cycle when most of the fuel burns. Timing the '
               'injection moves that moment. A well-phased burn gives the best power and the least knock, '
               'while a poor one wastes energy.')],
 'test': [('Where does a direct injection engine spray its fuel?',
           [('a', 'Into the fuel tank'),
            ('b', 'Straight into the cylinder'),
            ('c', 'Into the exhaust pipe'),
            ('d', 'Into the cabin')],
           'b'),
          ('What is atomisation?',
           [('a', 'Turning fuel into a solid block'),
            ('b', 'Mixing paint with water'),
            ('c', 'Freezing the fuel'),
            ('d', 'Breaking liquid fuel into a fine mist of droplets')],
           'd'),
          ('What is spray penetration?',
           [('a', 'The depth of the fuel tank'),
            ('b', 'The number of pilots'),
            ('c', 'How far the fuel spray travels into the gas before it slows'),
            ('d', 'The colour of the nozzle')],
           'c'),
          ('What helps the fuel and air mix in a cylinder?',
           [('a', 'Swirl and tumble motion'),
            ('b', 'Heavy cargo'),
            ('c', 'Cold paint'),
            ('d', 'A closed door')],
           'a'),
          ('What is combustion phasing?',
           [('a', 'The colour of the flame'),
            ('b', 'The number of cylinders'),
            ('c', 'The moment in the cycle when most of the fuel burns'),
            ('d', 'The price of the fuel')],
           'c')]}
