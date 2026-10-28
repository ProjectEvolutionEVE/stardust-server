"""Asphalt Pavement Design and Traffic Loading: load spectra, layer thickness, fatigue, rutting and life-cycle cost."""
CODE = 'engineering5_pavement'
BOOK = {'title': 'Asphalt Pavement Design and Traffic Loading',
 'subtitle': 'Traffic loads, layer thickness, cracking, rutting and the money over a road life',
 'chapters': [('Why loads matter',
               'A road is built to carry traffic for many years. Heavy trucks do far more damage than cars, '
               'because damage grows fast with axle weight. A pavement design starts by counting how many '
               'heavy loads it must carry.'),
              ('Traffic load spectra',
               'A load spectrum lists the mix of vehicles and axle weights expected on a road. Engineers '
               'convert the mix into equivalent loads, so that every vehicle is measured against one '
               'standard axle. The total over the design life sets how strong the road must be.'),
              ('Layer thickness',
               'An asphalt pavement is built in layers over a base and a prepared subgrade. Thicker layers '
               'spread the load over a wider area below. The right thickness balances the traffic load '
               'against the strength of the ground.'),
              ('Fatigue cracking and rutting',
               'Repeated bending under traffic can make cracks grow from the bottom of the asphalt layer. '
               'This is called fatigue cracking. Rutting is a permanent groove that forms in the wheel paths '
               'when the layers are pushed down under load.'),
              ('Design checks',
               'Designers check the pavement against both cracking and rutting. Each check compares the '
               'strain or stress in the layers with the limits the material can carry. A pavement must pass '
               'both checks to be sound.'),
              ('The money side of life-cycle cost',
               'A thicker or better pavement costs more on day one but may need repairs less often. '
               'Life-cycle cost adds up building, maintenance and repair over the whole life. The cheapest '
               'pavement to build is not always the cheapest to own.')],
 'test': [('Why do heavy trucks damage roads more than cars?',
           [('a', 'Because trucks are a better colour'),
            ('b', 'Because damage grows fast with axle weight'),
            ('c', 'Because roads are painted for cars only'),
            ('d', 'Because cars never touch the road')],
           'b'),
          ('What does a load spectrum list?',
           [('a', 'The names of the road workers'),
            ('b', 'The price of asphalt per tonne'),
            ('c', 'The mix of vehicles and axle weights expected on a road'),
            ('d', 'The weather for the year')],
           'c'),
          ('What does rutting look like?',
           [('a', 'A bright painted line'),
            ('b', 'A small hole in a window'),
            ('c', 'A stack of cones'),
            ('d', 'A permanent groove in the wheel paths')],
           'd'),
          ('What is fatigue cracking caused by?',
           [('a', 'Repeated bending under traffic'),
            ('b', 'Too much sunshine on a Monday'),
            ('c', 'A parked car'),
            ('d', 'Paint that is too bright')],
           'a'),
          ('What does life-cycle cost add up?',
           [('a', 'Only the price of the first day'),
            ('b', 'Building, maintenance and repair over the whole life'),
            ('c', 'The number of signs'),
            ('d', 'The age of the driver')],
           'b')]}
