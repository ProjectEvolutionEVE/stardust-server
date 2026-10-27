"""Ultimate Pit Limits: valuing every block in a model and finding the most profitable pit outline."""
CODE = 'mining4_ultimate_pit'
BOOK = {'title': 'Ultimate Pit Limits',
 'subtitle': 'Economic block values, nested pit shells and choosing a pit',
 'chapters': [('Economic block values',
               'Each block is given an economic value: the money its ore earns, minus the cost of '
               'mining, processing and selling it. Blocks with a positive value are worth mining, '
               'and blocks with a negative value are not.'),
              ('The Lerchs-Grossmann method',
               'The Lerchs-Grossmann algorithm finds the outline that gives the most total value, '
               'while keeping the pit walls at a safe slope. It is a classic method for planning '
               'the ultimate pit.'),
              ('Revenue factors',
               'A revenue factor scales the price of the product up or down. Engineers run the '
               'model with several factors, so they can see how the pit changes as the price '
               'changes.'),
              ('Nested pit shells',
               'A set of nested shells is a series of pits, each one inside the next, made at '
               'different revenue factors. Each shell shows the pit that would be best at a given '
               'price.'),
              ('Sensitivity to price',
               'The pit is sensitive to the metal price. When the price is high, the pit grows '
               'bigger, because more low-grade blocks become worth mining.'),
              ('Choosing a pit',
               'The chosen pit is often a shell that balances value, risk and the ease of mining. '
               'The final choice is made by people, using the model as a guide and not as the only '
               'answer.')],
 'test': [('How is the economic value of a block worked out?',
           [('a', 'The weight of the block alone'),
            ('b', 'The colour of its rock'),
            ('c', 'The money its ore earns, minus the costs of mining, processing and selling it'),
            ('d', 'The age of the drill')],
           'c'),
          ('What does a positive-value block mean?',
           [('a', 'It is worth mining'),
            ('b', 'It must be left forever'),
            ('c', 'It is a fuel tank'),
            ('d', 'It is a road')],
           'a'),
          ('What does the Lerchs-Grossmann method find?',
           [('a', 'The best route for the trucks home'),
            ('b', 'The cheapest paint'),
            ('c', 'The number of workers needed'),
            ('d', 'The pit outline with the most total value, at a safe slope')],
           'd'),
          ('What does a revenue factor do?',
           [('a', 'It sets the number of shifts'),
            ('b', 'It scales the product price up or down in the model'),
            ('c', 'It chooses the drill colour'),
            ('d', 'It counts the trucks')],
           'b'),
          ('What happens to the pit when the metal price is high?',
           [('a', 'It shrinks to a single block'),
            ('b', 'It is no longer possible to mine it'),
            ('c', 'It grows bigger, as more low-grade blocks become worth mining'),
            ('d', 'Nothing changes at all')],
           'c')]}
