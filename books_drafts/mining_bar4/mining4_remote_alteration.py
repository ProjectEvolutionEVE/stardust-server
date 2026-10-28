"""Remote Sensing for Alteration Mapping: using multispectral and hyperspectral images to detect clay and iron oxide signatures from above."""
CODE = 'mining4_remote_alteration'
BOOK = {'title': 'Remote Sensing for Alteration Mapping',
 'subtitle': 'Seeing alteration minerals from space and from the air',
 'chapters': [('Multispectral bands',
               'A multispectral sensor records light in a few broad bands, including some outside the '
               'visible range. Different minerals reflect these bands in different ways. Comparing the bands '
               'shows which minerals are on the surface.'),
              ('Hyperspectral sensors',
               'A hyperspectral sensor records hundreds of narrow bands. The detail is much finer, so it can '
               'tell apart many alteration minerals. The large data volume needs careful processing.'),
              ('Clay and iron oxide signatures',
               'Clay minerals and iron oxides have strong, known signatures in the reflected light. Finding '
               'them in an image points to alteration at the surface. These signatures are a useful first '
               'pass for exploration.'),
              ('Vegetation stress as a clue',
               'Some ore-related metals can stress plants, changing their colour and health. A geologist can '
               'use plant stress as a clue, though it can also come from other causes. Ground checks are '
               'needed to confirm it.'),
              ('Satellite archives',
               'Many satellite image archives are free or low cost. They let a team compare the ground over '
               'many years. Older images can show changes that help narrow the search.'),
              ('Ground truthing',
               'Every remote result must be checked on the ground. Geologists visit the sites, take samples '
               'and test them. Ground truthing is what turns an image into a trusted map.')],
 'test': [('What does a multispectral sensor record?',
           [('a', 'Sound waves'),
            ('b', 'Smells'),
            ('c', 'Light in a few broad bands'),
            ('d', 'Temperatures of the ocean only')],
           'c'),
          ('How many narrow bands does a hyperspectral sensor record?',
           [('a', 'Hundreds'), ('b', 'Exactly two'), ('c', 'Only one'), ('d', 'None at all')],
           'a'),
          ('Which minerals have strong signatures for alteration mapping?',
           [('a', 'Pure water and ice'),
            ('b', 'Air and smoke'),
            ('c', 'Glass and plastic'),
            ('d', 'Clay minerals and iron oxides')],
           'd'),
          ('Why is plant stress only a clue?',
           [('a', 'Plants never react to anything'),
            ('b', 'It can have causes other than ore-related metals'),
            ('c', 'Plants only grow in the dark'),
            ('d', 'Plants cannot be seen from space')],
           'b'),
          ('What is ground truthing?',
           [('a', 'Digging a tunnel'),
            ('b', 'Painting the ground'),
            ('c', 'Measuring the sky'),
            ('d', 'Checking remote results on the ground with samples')],
           'd')]}
