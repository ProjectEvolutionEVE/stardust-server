"""Crankshaft Design and Torsional Vibration: crank loads, torsional natural frequencies, damper design, fatigue at fillets, and balance."""
CODE = 'engineering5_crankshaft'
BOOK = {'title': 'Crankshaft Design and Torsional Vibration',
 'subtitle': 'Crank loads, twisting vibration, dampers, fatigue and balance',
 'chapters': [('Turning push into spin',
               'A crankshaft turns the up-and-down motion of the pistons into rotation. Each piston pushes '
               'on its own crank throw. The crankshaft must carry these loads for millions of cycles without '
               'failing.'),
              ('Crank loads',
               'The crank carries the gas pressure from the piston, the inertia of the moving parts and the '
               'forces from the connecting rods. These loads change with every stroke. Engineers add them up '
               'over the whole cycle to find the peak stresses.'),
              ('Torsional natural frequencies',
               'A crankshaft can twist back and forth like a spring. Its natural frequencies are the speeds '
               'at which it twists most easily. If an engine forcing matches one of these frequencies, the '
               'twisting builds up, which is called torsional resonance.'),
              ('Dampers',
               'A torsional damper removes energy from the twisting vibration. Many dampers use a rubber or '
               'viscous layer between two parts of a pulley. The damper is tuned to the frequency that '
               'causes the most trouble.'),
              ('Fatigue at the fillets',
               'Fatigue cracks often start at the fillets, the rounded corners where the journal meets the '
               'web. These corners carry high stress. Designers use large fillets and surface treatments '
               'such as rolling to raise the fatigue strength.'),
              ('Balance',
               'A crankshaft is balanced with counterweights so that the spinning masses do not shake the '
               'engine. Good balance reduces vibration, wear and noise. Balance is checked on a machine '
               'before the shaft is fitted.')],
 'test': [('What does a crankshaft do?',
           [('a', 'It stores fuel'),
            ('b', 'It turns up-and-down piston motion into rotation'),
            ('c', 'It cools the cabin'),
            ('d', 'It steers the craft')],
           'b'),
          ('What is torsional resonance?',
           [('a', 'A sound of a bell'),
            ('b', 'A fire in the cabin'),
            ('c', 'A paint problem'),
            ('d', 'Twisting that builds up when the forcing matches a natural frequency')],
           'd'),
          ('What does a torsional damper do?',
           [('a', 'It adds fuel to the engine'),
            ('b', 'It lights the cabin'),
            ('c', 'It removes energy from the twisting vibration'),
            ('d', 'It makes the crankshaft longer')],
           'c'),
          ('Where do fatigue cracks often start on a crankshaft?',
           [('a', 'At the fillets, the rounded corners'),
            ('b', 'On the paint'),
            ('c', 'On the seats'),
            ('d', 'On the windows')],
           'a'),
          ('What are counterweights for?',
           [('a', 'To store electricity'),
            ('b', 'To hold the cargo'),
            ('c', 'To balance the spinning masses and reduce shaking'),
            ('d', 'To paint the shaft')],
           'c')]}
