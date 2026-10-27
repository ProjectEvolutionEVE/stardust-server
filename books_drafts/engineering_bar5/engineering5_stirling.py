"""Stirling Engines and Regenerators: the ideal cycle, regenerator effectiveness, displacer and piston design, and heat input choices."""
CODE = 'engineering5_stirling'
BOOK = {'title': 'Stirling Engines and Regenerators',
 'subtitle': 'The ideal cycle, the regenerator, and choosing a heat source',
 'chapters': [('A closed cycle',
               'A Stirling engine keeps a fixed amount of gas sealed inside. Heat is added at one end and '
               'removed at the other, and the gas expands and contracts to turn a shaft. Because the gas '
               'never leaves the engine, the heat can come from almost any source.'),
              ('The ideal cycle',
               'The ideal cycle has two constant-temperature steps and two constant-volume steps. Gas is '
               'heated while it expands at the hot end, then cooled while it is squeezed at the cold end. '
               'Real engines miss this ideal, but it sets the best possible performance.'),
              ('The regenerator',
               'The regenerator is a porous mass that the gas passes through twice on each cycle. It takes '
               'heat from the gas on the way hot to cold and gives it back on the way cold to hot. A '
               'regenerator that holds on to more heat raises the efficiency of the whole engine.'),
              ('Displacer and piston',
               'Many designs use two parts: a displacer that moves the gas between the hot and cold ends, '
               'and a piston that does the work. The two must move in the right timing, or the gas is pushed '
               'to the wrong place. Clearance, seals and the swept volume all change the output.'),
              ('Choosing the heat input',
               'Because heat enters through a wall, an engineer may burn fuel, use concentrated sunlight, or '
               'use waste heat from another process. Each choice has a cost. Sunlight is free but needs a '
               'large collector, while waste heat is cheap if it is already available.'),
              ('Quiet and steady',
               'Stirling engines run quietly and can be built to run for long periods with little '
               'maintenance. They are slow to start and bulky for their power, so they suit steady jobs more '
               'than sudden ones. The best choice depends on the hours of use and the price of the heat.')],
 'test': [('What stays sealed inside a Stirling engine?',
           [('a', 'A stream of fuel'),
            ('b', 'A supply of water'),
            ('c', 'A fixed amount of gas'),
            ('d', 'Nothing at all')],
           'c'),
          ('What does the regenerator do on each cycle?',
           [('a', 'It adds water to the gas'),
            ('b', 'It stores heat and gives it back to the gas'),
            ('c', 'It cools the shaft'),
            ('d', 'It makes the engine louder')],
           'b'),
          ('What does the displacer do?',
           [('a', 'It stores electricity'),
            ('b', 'It paints the engine'),
            ('c', 'It seals the fuel tank'),
            ('d', 'It moves the gas between the hot and cold ends')],
           'd'),
          ('Why can a Stirling engine use many kinds of heat?',
           [('a', 'Its gas is burned away each cycle'),
            ('b', 'It needs no heat at all'),
            ('c', 'Heat enters through a wall, not by mixing with the gas'),
            ('d', 'It runs only on electricity')],
           'c'),
          ('What is a common trade-off in choosing a heat source?',
           [('a', 'Sunlight is free but needs a large collector'),
            ('b', 'Waste heat is always expensive'),
            ('c', 'Fuel is always free'),
            ('d', 'The engine cannot be used with heat at all')],
           'a')]}
