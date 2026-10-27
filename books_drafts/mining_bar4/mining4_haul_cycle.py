"""Haul Cycle Time and Fleet Sizing: how road slope, load and queues set how many trucks a mine needs."""
CODE = 'mining4_haul_cycle'
BOOK = {'title': 'Haul Cycle Time and Fleet Sizing',
 'subtitle': 'Road gradients, payloads, queues and cost per tonne-kilometre',
 'chapters': [('One haul cycle',
               'A haul cycle is one trip: the truck is loaded, drives to the dump, unloads and '
               'drives back. The time for each part adds up to the cycle time, and the cycle time '
               'decides how much a truck can move in a shift.'),
              ('Road gradients',
               'A steep uphill road slows a loaded truck badly. Engineers keep the gradient gentle '
               'where they can, because a flatter road lets the truck keep its speed.'),
              ('Rolling resistance',
               'Rolling resistance is the drag of the tyres on the road. Good road surfaces and '
               'firm, clean roads reduce it, so the truck uses less fuel and goes faster.'),
              ('Queues at the loader',
               'If several trucks arrive at the loader at once, some must wait. Queue time is '
               'often a large part of the cycle, so the number of trucks is matched to the number '
               'of loaders.'),
              ('Fleet sizing',
               'Fleet sizing works out how many trucks are needed to move the planned tonnes. It '
               'balances the cost of each truck against the cost of the delays it causes.'),
              ('Cost per tonne-kilometre',
               'A tonne-kilometre is one tonne of material moved one kilometre. Dividing the '
               'haulage cost by this figure shows how cheaply the trucks move the rock, which '
               'helps compare road designs.')],
 'test': [('What is a haul cycle?',
           [('a', 'A type of blast'),
            ('b', 'A shift change'),
            ('c', 'One trip: loading, driving to the dump, unloading and driving back'),
            ('d', 'A pump test')],
           'c'),
          ('Why is a steep uphill road a problem for a loaded truck?',
           [('a', 'It slows the loaded truck badly'),
            ('b', 'It makes the truck lighter'),
            ('c', 'It stops the radio working'),
            ('d', 'It changes the colour of the ore')],
           'a'),
          ('What is rolling resistance?',
           [('a', 'The pressure in the drill'),
            ('b', 'The weight of the ore'),
            ('c', 'The heat of the sun'),
            ('d', 'The drag of the tyres on the road')],
           'd'),
          ('What is queue time?',
           [('a', 'The time it takes to paint a truck'),
            ('b', 'The time trucks wait at the loader'),
            ('c', 'The lunch break'),
            ('d', 'The time to dig a shaft')],
           'b'),
          ('What is a tonne-kilometre?',
           [('a', 'A unit of pressure'),
            ('b', 'The weight of a truck'),
            ('c', 'One tonne of material moved one kilometre'),
            ('d', 'The depth of a pit')],
           'c')]}
