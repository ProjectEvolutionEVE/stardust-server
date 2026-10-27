"""Gearbox Design Procedure: ratio selection, shaft layout, bearing and gear checks, lubrication, and assembly tolerances."""
CODE = 'engineering5_gearbox_procedure'
BOOK = {'title': 'Gearbox Design Procedure',
 'subtitle': 'From ratios to shafts, bearings, lubrication and assembly',
 'chapters': [('Start with the ratio',
               'A gearbox changes speed and torque between a motor and the load. The first design step is '
               'choosing the gear ratio. The ratio sets the speed of the output and the torque it can '
               'deliver.'),
              ('Shaft layout',
               'The shafts carry the gears and bearings in a fixed layout. Their spacing and diameters must '
               'keep the gears meshing correctly. A good layout keeps the shafts stiff so the gears do not '
               'shift under load.'),
              ('Bearing and gear checks',
               'Each gear and bearing is checked for strength and life against the loads it will see. '
               'Standard methods, such as those from the ISO and AGMA standards, give the formulas. Every '
               'check uses a safety factor chosen for the job.'),
              ('Lubrication',
               'Oil or grease reduces friction and carries heat away from the gear teeth and bearings. The '
               'lubricant must suit the speed, the load and the temperature. Poor lubrication is one of the '
               'most common causes of early failure.'),
              ('Assembly tolerances',
               'Parts are made within tolerances, meaning small allowed differences in size. Tolerances '
               'decide how the parts fit and how the gears mesh. Tight tolerances cost more, so engineers '
               'set them only where they matter.'),
              ('Testing and cost',
               'A prototype gearbox is run and inspected before production. Testing finds noise, heat and '
               'wear problems early, when they are cheap to fix. The total cost includes the parts, the '
               'tests and the service over the life of the gearbox.')],
 'test': [('What does the gear ratio set?',
           [('a', 'The output speed and torque'),
            ('b', 'The colour of the housing'),
            ('c', 'The number of passengers'),
            ('d', 'The length of the wing')],
           'a'),
          ('Why must the shafts be kept stiff?',
           [('a', 'So the gearbox makes more noise'),
            ('b', 'So the gears can float'),
            ('c', 'So the gears do not shift under load'),
            ('d', 'So the paint dries faster')],
           'c'),
          ('What do standards such as ISO and AGMA provide?',
           [('a', 'Recipes for food'),
            ('b', 'Formulas for checking gears and bearings'),
            ('c', 'Songs for the crew'),
            ('d', 'Colours for paint')],
           'b'),
          ('What does lubrication do for gear teeth and bearings?',
           [('a', 'It adds weight to the gears'),
            ('b', 'It makes the teeth brittle'),
            ('c', 'It turns the gears into paint'),
            ('d', 'It reduces friction and carries heat away')],
           'd'),
          ('What are assembly tolerances?',
           [('a', 'The length of a holiday'),
            ('b', 'The number of gears'),
            ('c', 'Small allowed differences in part size'),
            ('d', 'The price of the box')],
           'c')]}
