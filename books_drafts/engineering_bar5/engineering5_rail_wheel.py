"""Wheel-Rail Contact and Rail Vehicle Dynamics: conicity, hunting oscillation, contact patch, wheel wear profiles, and track geometry."""
CODE = 'engineering5_rail_wheel'
BOOK = {'title': 'Wheel-Rail Contact and Rail Vehicle Dynamics',
 'subtitle': 'Conicity, hunting, the contact patch, wear and track geometry',
 'chapters': [('A small contact patch',
               'A railway wheel touches the rail over a patch about the size of a coin. All the weight of '
               'the vehicle passes through that small area. The shape of the wheel and the rail controls how '
               'the vehicle runs.'),
              ('Conicity',
               'Railway wheels are slightly cone-shaped, a property called conicity. When the wheelset moves '
               'off centre, the wheel on the wider side rolls on a larger radius, and the set steers back '
               'toward the middle. Conicity helps a train run straight on track.'),
              ('Hunting oscillation',
               'At high speed, the wheelset can swing from side to side in a growing motion called hunting. '
               'If it grows, it can cause the train to run unsafely. Designers control hunting with the '
               'wheel shape, the suspension and the mass of the vehicle.'),
              ('The contact patch',
               'The contact patch is the small area where wheel and rail touch. Its shape and size set the '
               'friction and the forces that steer the wheel. Engineers model the patch to predict how the '
               'wheel will behave.'),
              ('Wheel wear profiles',
               'Wheels wear as they run, and their profile changes shape over time. A worn profile can '
               'change the conicity and bring back hunting. Maintenance profiles the wheels and turns or '
               'replaces them at set limits.'),
              ('Track geometry',
               'The track must be level, aligned and smooth within tight tolerances. Errors in track '
               'geometry shake the vehicle and cause wear. Regular inspection and tamping keep the track '
               'within its limits and the trains running safely.')],
 'test': [('How large is the contact patch between a railway wheel and the rail?',
           [('a', 'About the size of a house'),
            ('b', 'About the size of a sea'),
            ('c', 'About the size of a coin'),
            ('d', 'About the size of a seat')],
           'c'),
          ('What is conicity?',
           [('a', 'The slight cone shape of railway wheels that helps keep a train on track'),
            ('b', 'A type of paint'),
            ('c', 'A kind of cabin light'),
            ('d', 'A brake part')],
           'a'),
          ('What is hunting oscillation?',
           [('a', 'A search for animals'),
            ('b', 'A sound in the cabin'),
            ('c', 'A growing side-to-side swing of the wheelset at speed'),
            ('d', 'A fuel leak')],
           'c'),
          ('Why does wheel wear matter for handling?',
           [('a', 'Wear makes the wheels heavier for no reason'),
            ('b', 'A worn profile can change the conicity and bring back hunting'),
            ('c', 'Wear makes the rail paint brighter'),
            ('d', 'Wear has no effect at all')],
           'b'),
          ('What must track geometry stay within?',
           [('a', 'Any shape at all'),
            ('b', 'The colour of the sleepers'),
            ('c', 'The price of the ballast'),
            ('d', 'Tight tolerances for level, alignment and smoothness')],
           'd')]}
