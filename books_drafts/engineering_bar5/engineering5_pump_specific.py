"""Pump Impeller Design and Specific Speed: specific speed, impeller shapes, volute design, efficiency scaling, and selection."""
CODE = 'engineering5_pump_specific'
BOOK = {'title': 'Pump Impeller Design and Specific Speed',
 'subtitle': 'Specific speed, impeller shapes, volutes and choosing the right pump',
 'chapters': [('Moving liquid with a wheel',
               'A centrifugal pump uses a spinning impeller to throw liquid outward and raise its pressure. '
               'The impeller is the heart of the pump. Its shape decides how much flow and head the pump can '
               'make.'),
              ('Specific speed',
               'Specific speed is a single number that links the speed, flow and head of a pump. It tells '
               'engineers which impeller shape suits the job. Low specific speed suits high head and low '
               'flow, and high specific speed suits high flow and low head.'),
              ('Impeller shapes',
               'Radial impellers suit low specific speed, mixed-flow impellers suit middle values, and axial '
               'impellers suit high specific speed. The shape of the blades follows the flow path. Each '
               'shape is chosen to keep losses low for its job.'),
              ('The volute',
               'The volute is the spiral casing around the impeller. It collects the liquid as it leaves and '
               'guides it to the outlet. A well-shaped volute recovers pressure and keeps the pump quiet and '
               'steady.'),
              ('Efficiency scaling',
               'A pump designed for one size can be scaled to another with known rules. These rules predict '
               'how the efficiency changes with size and speed. They save testing time when a new pump size '
               'is needed.'),
              ('Selection',
               'A pump is selected for the flow and head the system needs, at the lowest cost over its life. '
               'The best choice runs near its best efficiency point. The power bill of the pump is often '
               'bigger than its purchase price.')],
 'test': [('What does a centrifugal pump use to move liquid?',
           [('a', 'A rope'), ('b', 'A spinning impeller'), ('c', 'A ladder'), ('d', 'A sail')],
           'b'),
          ('What does specific speed link together?',
           [('a', 'Colour, weight and time'),
            ('b', 'Seats, windows and doors'),
            ('c', 'Paint, paper and glue'),
            ('d', 'Speed, flow and head')],
           'd'),
          ('Which impeller shape suits high specific speed?',
           [('a', 'Solid bricks'),
            ('b', 'Tiny rubber balls'),
            ('c', 'Axial impellers'),
            ('d', 'Flat boards')],
           'c'),
          ('What does the volute do?',
           [('a', 'It collects the liquid and guides it to the outlet'),
            ('b', 'It stores the fuel'),
            ('c', 'It turns the lights on'),
            ('d', 'It seals the cabin')],
           'a'),
          ('Why does the power bill often matter more than the price of a pump?',
           [('a', 'Pumps use no power'),
            ('b', 'Pumps are always free'),
            ('c', 'The pump uses power for years, which can cost more than the pump itself'),
            ('d', 'Power is always cheaper than water')],
           'c')]}
