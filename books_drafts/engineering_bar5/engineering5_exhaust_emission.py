"""Engine Emission Modelling and Control: emission formation, models, after-treatment, test cycles, and the money side of compliance."""
CODE = 'engineering5_exhaust_emission'
BOOK = {'title': 'Engine Emission Modelling and Control',
 'subtitle': 'How pollutants form, how they are modelled, and how they are cleaned up',
 'chapters': [('What comes out of the pipe',
               'Engines produce pollutants such as nitrogen oxides, carbon monoxide, unburnt hydrocarbons '
               'and soot. Each forms in a different way inside the cylinder. Knowing where each one forms is '
               'the first step in controlling it.'),
              ('Forming the pollutants',
               'Nitrogen oxides form at high temperature when nitrogen and oxygen meet. Carbon monoxide and '
               'soot form when fuel does not burn fully, often in rich mixtures. Each pollutant responds to '
               'a different change in the burn.'),
              ('Emission models',
               'Engineers use models that predict emissions from the engine settings. The models are checked '
               'against measured data from test rigs. A good model saves many hours of engine testing.'),
              ('After-treatment',
               'After-treatment cleans the exhaust after it leaves the engine. A three-way catalyst handles '
               'petrol engine exhaust. Diesel engines use selective catalytic reduction, which adds a '
               'reagent to cut nitrogen oxides, and particulate filters catch soot.'),
              ('Test cycles',
               'Emissions are measured on standard test cycles, which run the engine through set patterns of '
               'speed and load. The Worldwide Harmonised Light Vehicles Test Procedure is one such cycle. '
               'Real driving can differ from the cycle, so the design must work in both.'),
              ('The money side of compliance',
               'Meeting emission rules costs money in parts, testing and fuel. Each part must pay its way in '
               'the law and in sales. Engineers compare the cost of each control with the emissions it '
               'removes.')],
 'test': [('Which of these is a pollutant from an engine?',
           [('a', 'Clean water vapour only'),
            ('b', 'Fresh air'),
            ('c', 'Nitrogen oxides'),
            ('d', 'Sunlight')],
           'c'),
          ('When do nitrogen oxides tend to form?',
           [('a', 'At high temperature, when nitrogen and oxygen meet'),
            ('b', 'At very low temperature'),
            ('c', 'Only in the dark'),
            ('d', 'When there is no air')],
           'a'),
          ('What does a three-way catalyst handle?',
           [('a', 'Water in the hold'),
            ('b', 'Passenger seats'),
            ('c', 'Petrol engine exhaust'),
            ('d', 'Paint in the cabin')],
           'c'),
          ('What does a particulate filter catch?',
           [('a', 'Air bubbles'), ('b', 'Soot'), ('c', 'Fuel vapour in the tank'), ('d', 'Light beams')],
           'b'),
          ('What is a standard test cycle?',
           [('a', 'A dance for the crew'),
            ('b', 'A kind of exhaust pipe'),
            ('c', 'A type of paint'),
            ('d', 'A set pattern of engine speed and load used to measure emissions')],
           'd')]}
