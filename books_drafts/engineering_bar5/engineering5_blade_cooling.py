"""Turbine Blade Cooling Passages: film cooling holes, internal impingement, heat transfer coefficients, and the money side of cooling air."""
CODE = 'engineering5_blade_cooling'
BOOK = {'title': 'Turbine Blade Cooling Passages',
 'subtitle': 'Film holes, impingement, heat transfer, and the cost of cooling air',
 'chapters': [('Blades in very hot gas',
               'Gas leaving the combustor can be hotter than the blade metal can safely survive. Engineers '
               'protect the blades by cooling them with air bled from the compressor. The cooling air is a '
               'cost, so every passage must earn its place.'),
              ('Film cooling holes',
               'Film cooling holes are small holes drilled through the blade surface. Cool air leaves them '
               'and forms a thin layer that shields the metal from the hot gas. The shape and angle of each '
               'hole decide how well the layer stays attached.'),
              ('Internal impingement',
               'Inside the blade, cool air is often sprayed through small holes onto the inner wall. This is '
               'impingement cooling. It removes heat quickly from the hottest parts, such as the leading '
               'edge.'),
              ('Heat transfer coefficients',
               'The heat transfer coefficient measures how well a surface gives heat to the air moving past '
               'it. Engineers use it to size the passages and holes. A higher coefficient removes more heat, '
               'but it also raises the pressure loss in the cooling air.'),
              ('The money side of cooling air',
               'Cooling air comes from the compressor, so it does work that never reaches the turbine. Every '
               'kilogram of cooling air lowers the engine efficiency a little. Designers must weigh the '
               'metal life gained against the fuel and power lost.'),
              ('A balance, not a maximum',
               'More cooling is not always better. Too much air wastes compressor work, while too little '
               'lets the blade wear out early. The best design is the one that gives the longest blade life '
               'for the least cooling air.')],
 'test': [('Where does the cooling air for turbine blades usually come from?',
           [('a', 'The compressor'), ('b', 'The fuel tank'), ('c', 'The hold'), ('d', 'The paint shop')],
           'a'),
          ('What is the job of a film cooling hole?',
           [('a', 'To drain the fuel'),
            ('b', 'To carry passengers'),
            ('c', 'To let cool air form a layer that shields the metal'),
            ('d', 'To make noise')],
           'c'),
          ('What is impingement cooling?',
           [('a', 'Painting the blade white'),
            ('b', 'Spraying cool air onto the inner wall of the blade'),
            ('c', 'Heating the blade with a flame'),
            ('d', 'Removing the blade from the engine')],
           'b'),
          ('What does the heat transfer coefficient measure?',
           [('a', 'The weight of the blade'),
            ('b', 'The length of the wing'),
            ('c', 'The number of passengers'),
            ('d', 'How well a surface gives heat to the air moving past it')],
           'd'),
          ('What is the cost of using more cooling air?',
           [('a', 'It costs nothing at all'),
            ('b', 'It makes the engine stronger'),
            ('c', 'It takes compressor work that never reaches the turbine and lowers efficiency'),
            ('d', 'It fills the hold with fuel')],
           'c')]}
