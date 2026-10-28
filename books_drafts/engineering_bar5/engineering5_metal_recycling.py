"""Recycling Metals: scrap sorting, melting losses, alloy contamination, recycled content rules and the money side of scrap."""
CODE = 'engineering5_metal_recycling'
BOOK = {'title': 'Recycling Metals: Scrap, Melting and Purity',
 'subtitle': 'Sorting scrap, losses in the furnace, keeping alloys clean and what scrap is worth',
 'chapters': [('Why sort scrap',
               'Metal scrap must be sorted by type before melting. Mixing alloys spoils the result, because '
               'each alloy has its own mix of elements. Sorting is the first step to getting useful metal '
               'back.'),
              ('Melting losses',
               'Some metal is lost during melting. It oxidises, and the oxide floats off as dross on the '
               'surface. Dirty scrap, such as scrap with paint or oil, adds to these losses.'),
              ('Alloy contamination',
               'A small amount of the wrong element can ruin an alloy. Copper in steel, for example, can '
               'cause problems in the finished product. Strict sorting and testing keep the metal within its '
               'specification.'),
              ('Recycled content rules',
               'Some products must state or meet a minimum share of recycled content. The rules differ by '
               'product and by country. Records must show where the recycled metal came from.'),
              ('Purity and quality',
               'Purity is how close the metal is to its specified mix. Engineers test melts with chemical '
               'analysis before casting. A melt that fails the test must be corrected or reprocessed.'),
              ('The money side of scrap',
               'Scrap has a market value that rises and falls with the price of new metal. Clean, sorted '
               'scrap sells for more than mixed scrap. Sorting costs labour, but the extra value often pays '
               'for it.')],
 'test': [('Why must metal scrap be sorted by type?',
           [('a', 'Because scrap must be painted first'),
            ('b', 'Because scrap is always heavier when sorted'),
            ('c', 'Because sorting is a legal requirement for weather'),
            ('d', 'Because mixing alloys spoils the result')],
           'd'),
          ('What is dross?',
           [('a', 'Oxidised metal that floats off on the surface during melting'),
            ('b', 'A type of fine wine'),
            ('c', 'A metal beam'),
            ('d', 'A brand of glue')],
           'a'),
          ('What is an example of alloy contamination?',
           [('a', 'Sugar in tea'),
            ('b', 'Copper in steel'),
            ('c', 'Paper in a box'),
            ('d', 'Water in a glass')],
           'b'),
          ('What do recycled content rules require?',
           [('a', 'That all metal is thrown away'),
            ('b', 'That metal is never melted'),
            ('c', 'A minimum share of recycled content, with records of its source'),
            ('d', 'That metal is painted pink')],
           'c'),
          ('What does clean, sorted scrap usually have compared with mixed scrap?',
           [('a', 'A lower value'),
            ('b', 'No value at all'),
            ('c', 'The same value always'),
            ('d', 'A higher value')],
           'd')]}
