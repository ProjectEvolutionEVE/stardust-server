"""Ion and Hall Thrusters: electrostatic acceleration, ionisation, thrust per unit power, lifetime erosion, and electric power demands."""
CODE = 'engineering5_ion_thruster'
BOOK = {'title': 'Ion and Hall Thrusters',
 'subtitle': 'Electric push from ionised gas, with high efficiency and low thrust',
 'chapters': [('Pushing with ions',
               'An ion thruster ionises a gas, usually xenon, and accelerates the ions with electric fields. '
               'The ions leave at very high speed, and the reaction pushes the spacecraft forward. The '
               'thrust is small, but it acts for a very long time.'),
              ('Ionisation',
               'Ionisation strips electrons from the gas atoms, leaving positive ions. The energy needed to '
               'ionise the gas is a key part of the power budget. A good design ionises the gas with little '
               'wasted energy.'),
              ('Hall thrusters',
               'A Hall thruster traps electrons in a magnetic field, and the trapped electrons create a '
               'strong electric field that accelerates the ions. This design gives strong thrust for its '
               'size. It is widely used for satellite station keeping.'),
              ('Thrust per unit of power',
               'Electric thrusters give a high exhaust speed, so they get more impulse from each kilogram of '
               'propellant than chemical rockets, which means a higher specific impulse. Their thrust per unit of power is small, so they need a '
               'lot of electrical power for even a modest push.'),
              ('Erosion and lifetime',
               'The ions strike the walls and the grids of the thruster and slowly wear them away. Lifetime '
               'is set by how fast the wear goes through the thruster channel. Engineers test for thousands '
               'of hours to prove the life.'),
              ('Power demands',
               'The power for an electric thruster must come from solar panels or a reactor. The size of the '
               'power source sets the mass and cost of the whole spacecraft. Designers weigh the propellant '
               'saved against the power needed to make it work.')],
 'test': [('How does an ion thruster push a spacecraft?',
           [('a', 'By burning wood'),
            ('b', 'By accelerating ions that leave at high speed'),
            ('c', 'By spraying paint'),
            ('d', 'By rolling on wheels')],
           'b'),
          ('What does a Hall thruster use to trap electrons?',
           [('a', 'A bag of sand'),
            ('b', 'A piece of wood'),
            ('c', 'A bicycle chain'),
            ('d', 'A magnetic field')],
           'd'),
          ('What sets the lifetime of an ion thruster?',
           [('a', 'The colour of the nose cone'),
            ('b', 'The number of windows'),
            ('c', 'How fast the ions wear away the channel and grids'),
            ('d', 'The weather on Earth')],
           'c'),
          ('Compared with chemical rockets, what do electric thrusters give?',
           [('a', 'More impulse for each kilogram of propellant, but small thrust'),
            ('b', 'Much larger thrust with no power'),
            ('c', 'Nothing at all'),
            ('d', 'The same thrust with no power')],
           'a'),
          ('What must provide the power for an electric thruster?',
           [('a', 'A candle'),
            ('b', 'A bicycle'),
            ('c', 'Solar panels or a reactor'),
            ('d', 'Water in a bucket')],
           'c')]}
