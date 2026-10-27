"""The Bond Work Index and Mill Power: estimating how much energy it takes to grind a tonne of ore."""
CODE = 'mining4_bond_index'
BOOK = {'title': 'The Bond Work Index and Mill Power',
 'subtitle': 'Grindability tests, energy per tonne and sizing mill circuits',
 'chapters': [('Why grinding energy matters',
               'Grinding is one of the biggest energy costs in a mill. Knowing how hard an ore is '
               'to grind helps the designer choose the right mill, the right power and the right '
               'budget.'),
              ('The Bond work index',
               'The Bond work index is a measure of how hard an ore is to grind. It is found with '
               'a standard laboratory test, and it is given in kilowatt-hours per tonne.'),
              ('Energy per tonne',
               "Bond's law links the energy needed to grind a tonne of ore to the work index and "
               'the sizes of the feed and product. Finer product needs more energy, and a harder '
               'ore needs more energy too.'),
              ('Mill power draw',
               'The power a mill draws depends on its size, speed and load. Engineers estimate the '
               'power needed for a given throughput, and then choose a motor large enough to '
               'deliver it.'),
              ('Circuit sizing',
               'A grinding circuit is sized so that the mill, the classifiers and the other '
               'equipment work together. The Bond method helps set the size of each part from the '
               'work index and the target product size.'),
              ('Ore hardness variation',
               'Real ore bodies vary, so the work index changes from one part of the deposit to '
               'another. Test samples from across the body are needed to estimate the energy for '
               'the whole mine.')],
 'test': [('What does the Bond work index measure?',
           [('a', 'The colour of the ore'),
            ('b', 'The height of the mill'),
            ('c', 'How hard an ore is to grind'),
            ('d', 'The price of the ore')],
           'c'),
          ('In which units is the Bond work index given?',
           [('a', 'Kilowatt-hours per tonne'),
            ('b', 'Litres per hour'),
            ('c', 'Tonnes per metre'),
            ('d', 'Degrees per second')],
           'a'),
          ('What happens to the grinding energy if the product must be finer?',
           [('a', 'It goes down to zero'),
            ('b', 'It stays exactly the same'),
            ('c', 'It turns into water'),
            ('d', 'It goes up')],
           'd'),
          ('What sets how much power a mill draws?',
           [('a', 'The colour of its paint'),
            ('b', 'Its size, speed and load'),
            ('c', 'The number of cups in the canteen'),
            ('d', 'The name of the mine')],
           'b'),
          ('Why do test samples come from across the ore body?',
           [('a', 'Because the ore is always the same'),
            ('b', 'Because samples are used for paint'),
            ('c', 'Because ore hardness varies from one part of the deposit to another'),
            ('d', 'Because samples are sold at the gate')],
           'c')]}
