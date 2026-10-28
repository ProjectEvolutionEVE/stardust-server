"""Warehouse-Scale Computers: treating a whole data centre as one machine, and what that means for cost and failure."""
CODE = 'computing5_warehouse_scale'
BOOK = {'title': 'Warehouse-Scale Computers',
 'subtitle': 'Racks, power, cooling, failure at scale and cost',
 'chapters': [('One computer made of many',
               'A warehouse-scale computer is a whole data centre run as one system. Thousands of '
               'machines work together on shared jobs. Designers think about the whole building, '
               'not single boxes.'),
              ('Power and cooling',
               'Power enters the building, reaches the racks and leaves as heat. Each step loses '
               'some energy. The cooling plant is often as large a design problem as the computers '
               'themselves.'),
              ('Failure at scale',
               'With thousands of machines, something breaks every day. Software must expect '
               'failures and keep running. Hardware that is perfectly reliable alone can still '
               'fail often in large numbers.'),
              ('Networks',
               'Machines must talk to each other quickly, so the network is a central part of the '
               'design. A slow link can hold up many jobs. Network planning shapes the layout of '
               'the racks.'),
              ('Cost structure',
               'The cost of such a system splits into buying machines, powering them, cooling them '
               'and running the staff. Buying cost is large but spread over years. Energy is a '
               'constant cost that efficiency can cut.'),
              ('Efficiency metrics',
               'Operators track measures such as power usage effectiveness and the work done per '
               'unit of energy. Comparing these numbers over time shows whether changes are '
               'working. Good metrics are honest about what they include.')],
 'test': [('What is a warehouse-scale computer?',
           [('a', 'A large cupboard for cups'),
            ('b', 'A whole data centre run as one system'),
            ('c', 'A single small laptop'),
            ('d', 'A type of car')],
           'b'),
          ('Where does most electrical energy in a data centre end up?',
           [('a', 'In the paint on the walls'),
            ('b', 'In the staff lunch'),
            ('c', 'As heat that cooling must remove'),
            ('d', 'In the sky')],
           'c'),
          ('Why must software expect failures in a large system?',
           [('a', 'Because failures are impossible'),
            ('b', 'Because software never runs'),
            ('c', 'Because failures are good for profits'),
            ('d', 'With many machines, some break every day')],
           'd'),
          ('Why is the network central to the design?',
           [('a', 'Machines must talk quickly, and a slow link can hold up jobs'),
            ('b', 'Networks store the data forever'),
            ('c', 'Networks replace the power supply'),
            ('d', 'Networks are only for printing')],
           'a'),
          ('What is a constant cost of such a system?',
           [('a', 'The colour of the racks'),
            ('b', 'The name of the building'),
            ('c', 'Energy to power the machines'),
            ('d', 'The number of windows')],
           'c')]}
