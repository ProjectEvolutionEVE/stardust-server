"""Electrostatic and Eddy Current Separation: sorting dry particles by electric charge and by the currents induced in metals."""
CODE = 'mining4_electrostatic_sep'
BOOK = {'title': 'Electrostatic and Eddy Current Separation',
 'subtitle': 'Particle charging, dry separation and sorting scrap metals',
 'chapters': [('Particle charging',
               'When dry particles are charged, conductors and non-conductors take up charge in '
               'different ways. Electrostatic separators use this difference to pull one kind of '
               'particle away from the rest.'),
              ('Conductors and non-conductors',
               'Metal particles conduct electricity and lose their charge quickly, while many '
               'minerals do not. Because of this, a charged particle stream splits into groups as '
               'it passes an electric field.'),
              ('Dry separation',
               'Electrostatic separation works on dry material, so it needs no water. This is '
               'useful in dry places, and it saves the cost of drying the product afterwards.'),
              ('Eddy currents in metal scrap',
               'An eddy current separator uses a rapidly changing magnetic field. It induces '
               'currents in non-ferrous metal pieces, which are then pushed away from the stream, '
               'so aluminium and other metals can be recovered.'),
              ('Recycling streams',
               'Scrap from cars, electronics and building waste passes through several separators. '
               'Each stage removes a different material, so the streams end up as clean, sellable '
               'products.'),
              ('Plant design',
               'A separator plant is designed around the feed size, its moisture and the materials '
               'to be removed. Good design keeps the particles dry and evenly spread so each '
               'separator works well.')],
 'test': [('What does an electrostatic separator use to pull particles apart?',
           [('a', 'Heat from a furnace'),
            ('b', 'Pressure from water'),
            ('c', 'Differences in electric charge'),
            ('d', 'Gravity alone')],
           'c'),
          ('Why does electrostatic separation need no water?',
           [('a', 'It works on dry material'),
            ('b', 'It works only in a river'),
            ('c', 'It uses water to charge particles'),
            ('d', 'It needs wet clay')],
           'a'),
          ('What does an eddy current separator do to non-ferrous metal pieces?',
           [('a', 'It melts them'),
            ('b', 'It paints them'),
            ('c', 'It folds them'),
            ('d', 'It induces currents in them so they are pushed away from the stream')],
           'd'),
          ('Which material is often recovered from scrap by eddy current separators?',
           [('a', 'Sand'), ('b', 'Aluminium'), ('c', 'Clean water'), ('d', 'Coal dust')],
           'b'),
          ('Why are scrap streams passed through several separators?',
           [('a', 'To make the scrap heavier'),
            ('b', 'To melt it in stages'),
            ('c', 'Each stage removes a different material'),
            ('d', 'To hide the metals')],
           'c')]}
