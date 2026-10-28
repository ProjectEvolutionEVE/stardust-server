"""Magnetic Levitation Vehicle Engineering: electromagnetic suspension, guidance, gap control, energy needs, and guideway design."""
CODE = 'engineering5_maglev'
BOOK = {'title': 'Magnetic Levitation Vehicle Engineering',
 'subtitle': 'Electromagnetic suspension, gap control, energy needs and the guideway',
 'chapters': [('Floating on magnets',
               'A maglev vehicle is held above its track by magnetic forces rather than wheels. Without '
               'wheels there is no rolling friction, so the vehicle can run smoothly at high speed. The '
               'track and the vehicle are designed together.'),
              ('Electromagnetic suspension',
               'In electromagnetic suspension, magnets on the vehicle are attracted up to a steel rail '
               'beneath it. The attraction is unstable on its own, so a control system adjusts the current '
               'many times a second. This keeps the vehicle floating.'),
              ('Guidance',
               'Guidance magnets keep the vehicle centred on its track in the sideways direction. Without '
               'guidance the vehicle would drift off line. Guidance and suspension are both needed for a '
               'safe ride.'),
              ('Gap control',
               'The gap between the vehicle and the guideway must stay at a set width. A sensor measures the '
               'gap, and the controller changes the magnet current to hold it. A steady gap gives a smooth '
               'and safe ride.'),
              ('Energy needs',
               'The magnets and the propulsion need electrical power. Most of the energy goes into moving '
               'the vehicle through the air, and some goes into the magnets. Designers balance the energy '
               'use against the speed and the number of trips.'),
              ('Guideway design',
               'The guideway is the track that carries the magnetic rail. Its shape must be straight and '
               'smooth within tight limits. Building it costs a great deal, so the route and the design are '
               'chosen with the full lifetime cost in mind.')],
 'test': [('What holds a maglev vehicle above its track?',
           [('a', 'Magnetic forces'),
            ('b', 'Wheels on the rail'),
            ('c', 'Balloons'),
            ('d', 'Ropes from the sky')],
           'a'),
          ('What does the control system do in electromagnetic suspension?',
           [('a', 'It turns the lights off'),
            ('b', 'It paints the rail'),
            ('c', 'It adjusts the magnet current many times a second to hold the vehicle up'),
            ('d', 'It sets the timetable')],
           'c'),
          ('What is the job of guidance magnets?',
           [('a', 'To store fuel'),
            ('b', 'To keep the vehicle centred on its track sideways'),
            ('c', 'To light the cabin'),
            ('d', 'To carry the cargo')],
           'b'),
          ('What is gap control?',
           [('a', 'Cutting a hole in the floor'),
            ('b', 'Painting the gap'),
            ('c', 'Measuring the price of tickets'),
            ('d', 'Holding the gap between vehicle and guideway at a set width')],
           'd'),
          ('What is the guideway?',
           [('a', 'A type of cabin light'),
            ('b', 'A kind of sail'),
            ('c', 'The track that carries the magnetic rail'),
            ('d', 'A seat cover')],
           'c')]}
