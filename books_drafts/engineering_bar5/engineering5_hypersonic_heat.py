"""Hypersonic Heating and Aerothermodynamics: stagnation heating, radiative heating, catalytic walls, heat flux correlations, and test facilities."""
CODE = 'engineering5_hypersonic_heat'
BOOK = {'title': 'Hypersonic Heating and Aerothermodynamics',
 'subtitle': 'Stagnation heating, radiation, catalytic walls and the facilities that test them',
 'chapters': [('Why hypersonic flight gets hot',
               'At very high speed, the air in front of a craft is squeezed and heated so much that it '
               'glows. The gas, not the craft, carries most of this heat. Thermal protection must survive '
               'the heat for the whole flight, not just a moment.'),
              ('Stagnation heating',
               'Heating is strongest at the stagnation point, the spot where the flow stops against the '
               'nose. A blunt nose spreads the heat over a larger area and lowers the peak heat flux. A '
               'sharp nose gives less drag but must survive much more heat.'),
              ('Radiative heating',
               'At the highest speeds the hot gas itself radiates heat onto the surface. This radiation '
               'grows very fast with speed and can rival convective heating. Designers must count both '
               'paths, because either one can burn through a poor shield.'),
              ('Catalytic walls',
               'At high temperature the air splits into single atoms. If those atoms recombine on the '
               'surface, they release heat and add to the load. Some surface materials encourage this '
               'recombination and some do not, so the choice of surface changes the heat flux.'),
              ('Heat flux correlations',
               'Engineers estimate the heat flux with correlations, which are simple formulas fitted to '
               'tests and detailed theory. Well-known examples are the Fay-Riddell and Sutton-Graves forms. '
               'These give a fast first answer before the full computer simulation runs.'),
              ('Test facilities',
               'Hypersonic conditions are hard to make on the ground. Shock tunnels, arc jets and ballistic '
               'ranges each reproduce part of the real heating. Each facility has limits on test time and '
               'gas composition, so results must be read with care.')],
 'test': [('Where is the heating strongest on a hypersonic craft?',
           [('a', 'At the tail'),
            ('b', 'On the landing gear'),
            ('c', 'At the stagnation point on the nose'),
            ('d', 'Inside the hold')],
           'c'),
          ('What is radiative heating?',
           [('a', 'Heat the hot gas radiates onto the surface'),
            ('b', 'Heat from a cold wind'),
            ('c', 'Heat from the fuel tank'),
            ('d', 'Heat from the hull paint')],
           'a'),
          ('What does a catalytic wall do?',
           [('a', 'It cools the gas to freezing'),
            ('b', 'It removes all heat'),
            ('c', 'It encourages atoms to recombine and release heat'),
            ('d', 'It makes the air thinner')],
           'c'),
          ('What are Fay-Riddell and Sutton-Graves?',
           [('a', 'Two types of engine'),
            ('b', 'Names of two heat flux correlations'),
            ('c', 'Two shuttles'),
            ('d', 'Two kinds of fuel')],
           'b'),
          ('Why must ground test facilities be read with care?',
           [('a', 'They always match flight exactly'),
            ('b', 'They use no gas at all'),
            ('c', 'They only test the paint'),
            ('d', 'They have limits on test time and gas composition')],
           'd')]}
