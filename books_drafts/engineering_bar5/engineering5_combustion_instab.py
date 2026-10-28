"""Combustion Instability and Thermoacoustics: pressure oscillations, the Rayleigh criterion, damping, injector design, and active control."""
CODE = 'engineering5_combustion_instab'
BOOK = {'title': 'Combustion Instability and Thermoacoustics',
 'subtitle': 'Pressure oscillations, the Rayleigh criterion, and taming them with design',
 'chapters': [('Flames that sing',
               'A combustor can start to vibrate, with the pressure rising and falling many times a second. '
               'This is combustion instability. The sound can be strong enough to damage the hardware, and '
               'it is one of the hardest problems in engine design.'),
              ('The Rayleigh criterion',
               'The Rayleigh criterion says that a pressure oscillation grows when heat release happens at '
               'the same moment as the pressure is high. If the heat and the pressure swing in step, the '
               'sound feeds itself. If they are out of step, the sound dies away.'),
              ('Damping',
               'Damping removes energy from the oscillation so that it cannot grow. Engineers add acoustic '
               'liners, Helmholtz resonators and dampers tuned to the frequency of the problem. Damping is '
               'the first line of defence.'),
              ('Injector design',
               'The fuel injectors set where and when the heat is released. A change in the spray or the '
               'mixing can move the heat into or out of step with the pressure. Careful injector design is '
               'the main way to keep the heat release away from the danger timing.'),
              ('Active control',
               'Active control senses the oscillation and drives an actuator to cancel it. The fuel flow can '
               'be pulsed in the right phase to push back against the sound. Active systems respond within '
               'milliseconds and can handle changing conditions.'),
              ('Testing for stability',
               'Engineers test combustors on rigs that reproduce the pressure, temperature and flow of the '
               'real engine. They look for the frequencies that grow and check the margin of safety. A '
               'design that is stable on the rig must still be checked across the full range of operation.')],
 'test': [('What is combustion instability?',
           [('a', 'A cool fire in the cabin'),
            ('b', 'A loss of paint'),
            ('c', 'Pressure oscillations that can grow inside a combustor'),
            ('d', 'A full tank of fuel')],
           'c'),
          ('What does the Rayleigh criterion say?',
           [('a', 'The engine always runs quietly'),
            ('b', 'An oscillation grows when heat release happens when the pressure is high'),
            ('c', 'Fuel never burns'),
            ('d', 'Heat always leaves the engine')],
           'b'),
          ('What does damping do?',
           [('a', 'It adds energy to the oscillation'),
            ('b', 'It makes the fuel heavier'),
            ('c', 'It turns the lights off'),
            ('d', 'It removes energy from the oscillation so it cannot grow')],
           'd'),
          ('What do the fuel injectors control in this story?',
           [('a', 'The colour of the nose'),
            ('b', 'The number of seats'),
            ('c', 'Where and when the heat is released'),
            ('d', 'The shape of the tail fin')],
           'c'),
          ('How does active control cancel an oscillation?',
           [('a', 'By pulsing the fuel flow in the right phase to push back'),
            ('b', 'By turning the engine off forever'),
            ('c', 'By adding more paint'),
            ('d', 'By removing the combustor entirely')],
           'a')]}
