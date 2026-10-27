"""Valvetrain and Variable Valve Timing Engineering: cam profiles, valve springs, valve float, variable timing actuators, and emissions trade-offs."""
CODE = 'engineering5_valvetrain'
BOOK = {'title': 'Valvetrain and Variable Valve Timing Engineering',
 'subtitle': 'Cam profiles, springs, valve float, and timing that changes with the engine',
 'chapters': [('Opening and closing on time',
               'The valvetrain opens and closes the valves of an engine at set moments in each cycle. A '
               'camshaft turns, and its lobes push the valves open. The shape of each lobe decides how far '
               'and how long each valve opens.'),
              ('Cam profiles',
               'A cam profile is the shape of the lobe. A gentle profile keeps the forces low, while a sharp '
               'profile opens the valve faster. Designers choose the profile to balance power, smoothness '
               'and wear.'),
              ('Valve springs',
               'Springs push each valve back closed. The spring must be strong enough to close the valve at '
               'high engine speed, but not so strong that it wastes power or wears the cam. The spring is '
               'chosen to match the cam.'),
              ('Valve float',
               'At very high engine speed, the valve can fail to follow the cam. The spring loses control, '
               'and the valve floats above the cam. Valve float can cause a collision inside the engine, so '
               'the spring and the cam must be matched to keep the valve under control.'),
              ('Variable valve timing',
               'Variable valve timing changes when the valves open and close as the engine runs. An actuator '
               'turns the camshaft a little, which moves the timing. The engine can then make more power at '
               'high speed and more economy at low speed.'),
              ('Emissions and trade-offs',
               'The timing and lift of the valves affect the emissions, the fuel use and the power. A '
               'setting that cuts one kind of emission can raise another. Engineers check every trade-off '
               'against the rules the engine must meet.')],
 'test': [('What does a camshaft do in a valvetrain?',
           [('a', 'It stores fuel'),
            ('b', 'It drives the wheels directly'),
            ('c', 'Its lobes push the valves open at set moments'),
            ('d', 'It cools the cabin')],
           'c'),
          ('What does the valve spring do?',
           [('a', 'It opens the valve by itself with no cam'),
            ('b', 'It pushes the valve back closed'),
            ('c', 'It fills the fuel tank'),
            ('d', 'It turns the lights on')],
           'b'),
          ('What is valve float?',
           [('a', 'A valve floating in a pool'),
            ('b', 'A type of paint'),
            ('c', 'A part of the cabin door'),
            ('d', 'The valve failing to follow the cam at very high speed')],
           'd'),
          ('What does variable valve timing change?',
           [('a', 'The colour of the valves'),
            ('b', 'The number of seats'),
            ('c', 'When the valves open and close as the engine runs'),
            ('d', 'The length of the hold')],
           'c'),
          ('What is the trade-off in valve timing and emissions?',
           [('a', 'A setting that cuts one emission can raise another'),
            ('b', 'No setting affects emissions at all'),
            ('c', 'Emissions always fall with every change'),
            ('d', 'Valves have no effect on fuel')],
           'a')]}
