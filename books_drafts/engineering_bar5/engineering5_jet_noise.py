"""Jet Noise and Aeroacoustics: shear layer noise, Lighthill's theory, noise scaling, acoustic liners, and noise limits."""
CODE = 'engineering5_jet_noise'
BOOK = {'title': 'Jet Noise and Aeroacoustics',
 'subtitle': 'Where jet noise comes from, how it scales, and how engines are made quieter',
 'chapters': [('Noise from mixing',
               'A jet engine is loud because its fast exhaust mixes with the still air around it. The mixing '
               'happens in a thin shear layer, where fast and slow gas rub together and throw out pressure '
               'waves. Most of the noise of a jet comes from this turbulent mixing.'),
              ('Lighthill and the acoustic analogy',
               'In 1952 Sir James Lighthill showed how turbulent flow can be treated as a source of sound. '
               'His acoustic analogy rewrites the flow equations so that the noise can be calculated from '
               'the turbulence. It remains the basis of much jet noise theory.'),
              ('How noise scales with speed',
               'For subsonic jets, the acoustic power grows very steeply with exhaust speed, roughly with '
               'the eighth power of the velocity. A small rise in exhaust speed therefore brings a large '
               'rise in noise. This is why engineers fight for lower exhaust speed in quiet designs.'),
              ('Acoustic liners',
               'Acoustic liners are honeycomb or perforated panels lining the engine inlet and fan duct. '
               'They absorb sound waves before the waves can leave the engine. Liners are chosen for the '
               'frequencies they absorb best, and they must survive heat, dirt and ice.'),
              ('Designing a quieter engine',
               'Designers can lower the exhaust speed by making the fan larger and slower, or by mixing the '
               'hot and cold flows more gently. Each change has a cost in weight, size or fuel use. The best '
               'design balances noise against the other demands of the engine.'),
              ('Noise limits',
               'Aircraft noise is controlled by international limits set through the International Civil '
               'Aviation Organization. Airports and communities rely on these limits, and engines must be '
               'certified against them. A quieter engine is also a cheaper one to operate near busy '
               'cities.')],
 'test': [('Where does most jet engine noise come from?',
           [('a', 'The paint on the wings'),
            ('b', 'The seats in the cabin'),
            ('c', 'Turbulent mixing in the shear layer'),
            ('d', 'The landing lights')],
           'c'),
          ('What does Lighthill theory allow engineers to do?',
           [('a', 'Stop the engine from turning'),
            ('b', 'Calculate the noise from the turbulence'),
            ('c', 'Measure the weight of the fuel'),
            ('d', 'Paint the nose cone')],
           'b'),
          ('Roughly how does the acoustic power of a subsonic jet scale with exhaust speed?',
           [('a', 'Not at all'),
            ('b', 'It falls as speed rises'),
            ('c', 'With the square of the colour'),
            ('d', 'With about the eighth power of the velocity')],
           'd'),
          ('What is the job of an acoustic liner?',
           [('a', 'To store fuel'),
            ('b', 'To carry passengers'),
            ('c', 'To absorb sound waves inside the engine'),
            ('d', 'To cool the cabin')],
           'c'),
          ('What sets the noise limits that engines must meet?',
           [('a', 'The International Civil Aviation Organization'),
            ('b', 'The local weather'),
            ('c', 'The price of fuel alone'),
            ('d', 'The colour of the runway')],
           'a')]}
