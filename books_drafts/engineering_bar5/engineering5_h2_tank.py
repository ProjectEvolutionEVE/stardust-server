"""Hydrogen Storage Tanks and Liner Design: high-pressure tank layers, liner materials, burst margins, fill cycles, and boil-off in cold storage."""
CODE = 'engineering5_h2_tank'
BOOK = {'title': 'Hydrogen Storage Tanks and Liner Design',
 'subtitle': 'Layers of a high-pressure tank, the margin of safety, and boil-off',
 'chapters': [('Layers in a tank',
               'A high-pressure hydrogen tank is built in layers. An inner liner stops the gas from leaking '
               'out. Around it, a shell of fibre, often carbon fibre in a resin, carries the load of the '
               'pressure. Each layer does one job.'),
              ('Liner materials',
               'The liner must be gas-tight and must not be damaged by hydrogen. Polymer liners and metal '
               'liners are both used, each with its own strengths. The liner choice affects the weight, the '
               'cost and how the tank ages.'),
              ('Burst margin',
               'A tank is designed to hold well beyond its working pressure before it bursts. This burst '
               'margin is a legal and engineering requirement in many places. Testing proves the margin on '
               'sample tanks before the design is approved.'),
              ('Fill cycles',
               'A tank is filled and emptied again and again over its life. Each cycle stresses the layers a '
               'little. Engineers test for many thousands of cycles to find the point where a crack could '
               'start.'),
              ('Boil-off in cold storage',
               'Cold liquid hydrogen warms up slowly by taking in heat from the surroundings. The gas that '
               'boils off must be vented or reused. Insulation and careful design keep the boil-off low, and '
               'it is a cost that builds up over time.'),
              ('The money side',
               'A tank costs more when it holds more pressure, and the carbon fibre is a large share of that '
               'cost. Engineers compare the weight saved against the price of the fibre and the risk of '
               'failure. A cheaper tank that fails is never the bargain it first seems.')],
 'test': [('What does the inner liner of a hydrogen tank do?',
           [('a', 'It carries the passengers'),
            ('b', 'It stops the gas from leaking out'),
            ('c', 'It makes the tank colder'),
            ('d', 'It stores the paint')],
           'b'),
          ('What usually carries the pressure load in a high-pressure tank?',
           [('a', 'A sheet of paper'),
            ('b', 'A bag of sand'),
            ('c', 'The seats'),
            ('d', 'A fibre shell, often carbon fibre in a resin')],
           'd'),
          ('What is a burst margin?',
           [('a', 'The price of the tank'),
            ('b', 'The number of valves'),
            ('c', 'The margin the tank holds beyond its working pressure before it bursts'),
            ('d', 'The colour of the cap')],
           'c'),
          ('What is boil-off?',
           [('a', 'Cold liquid hydrogen warming and turning to gas'),
            ('b', 'Water boiling in a kettle'),
            ('c', 'Paint drying on the wall'),
            ('d', 'Metal melting in a furnace')],
           'a'),
          ('Why does the number of fill cycles matter?',
           [('a', 'Each fill makes the tank lighter'),
            ('b', 'Fills have no effect at all'),
            ('c', 'Each cycle stresses the layers a little, so a crack could grow'),
            ('d', 'Fills only change the colour')],
           'c')]}
