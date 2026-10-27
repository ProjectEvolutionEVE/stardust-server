"""Mars Climate Orbiter: units mismatch, navigation errors, loss of the spacecraft, review failures, checks at interfaces and lessons."""
CODE = 'computing5_mars_climate_orbiter'
BOOK = {'title': 'Mars Climate Orbiter: Units Mismatch',
 'subtitle': 'A small error in units that cost a spacecraft',
 'chapters': [('Imperial and metric data',
               'In 1999 NASA lost the Mars Climate Orbiter. One team of engineers supplied thruster data in '
               'pound-force seconds, while the navigation software expected newton-seconds. The two systems '
               'disagreed about the same numbers.'),
              ('Navigation errors',
               'The mismatch caused small errors in the calculated thrust. Over months of flight they built '
               'up, and the spacecraft came too close to Mars than intended. The errors were not noticed in '
               'time to correct them.'),
              ('The loss of the spacecraft',
               'The orbiter entered the Martian atmosphere at the wrong height and was lost. The mission had '
               'cost a large sum, and the failure was a painful public lesson. The investigation was clear '
               'that the cause was an avoidable mistake.'),
              ('Review failures',
               'Reviews and checks had not caught the difference in units. Documents and interfaces did not '
               'state clearly which unit each value used. Good review is about checking the assumptions, not '
               'just the code.'),
              ('Checks at interfaces',
               'Wherever two systems exchange data, the units and meaning must be stated and tested. Teams '
               'add automated checks at these boundaries and label values clearly. The boundary between '
               'teams is where most such failures hide.'),
              ('Lessons',
               'Small details, such as a unit label, can decide the outcome of a large project. Clear '
               'specifications, independent checks and honest reporting of doubts are cheap compared with '
               'the cost of a lost mission.')],
 'test': [('What two unit systems were mixed up in the Mars Climate Orbiter loss?',
           [('a', 'Pounds and kilograms in the kitchen'),
            ('b', 'Miles and kilometres per bottle'),
            ('c', 'Pound-force seconds and newton-seconds'),
            ('d', 'Degrees and hours of sleep')],
           'c'),
          ('What did the mismatch cause over the months of flight?',
           [('a', 'A stronger radio signal'),
            ('b', 'Longer days on Earth'),
            ('c', 'More fuel in the tanks'),
            ('d', 'Small thrust errors that built up')],
           'd'),
          ('What had reviews failed to catch?',
           [('a', 'The difference in units between the two systems'),
            ('b', 'The colour of the spacecraft'),
            ('c', 'A spelling error in the logo'),
            ('d', 'The name of the launch pad')],
           'a'),
          ('Where do most failures of this kind tend to hide?',
           [('a', 'In the paint of the hardware'),
            ('b', 'At the boundary where two teams or systems exchange data'),
            ('c', 'Inside the printed manuals only'),
            ('d', 'In the weather forecast')],
           'b'),
          ('What is a good lesson from this loss?',
           [('a', 'Units never matter in science'),
            ('b', 'Reviews are a waste of time'),
            ('c', "Small details like a unit label can decide a large project's outcome"),
            ('d', 'Only large errors need attention')],
           'c')]}
