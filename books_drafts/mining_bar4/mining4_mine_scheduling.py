"""Long-Term Mine Scheduling: deciding which blocks to mine, in what order and at what cut-off grade, over many years."""
CODE = 'mining4_mine_scheduling'
BOOK = {'title': 'Long-Term Mine Scheduling',
 'subtitle': 'Block precedence, cut-off grades and the value of a schedule',
 'chapters': [('Blocks of ore',
               'A mine is divided into a model of blocks, each with an estimate of its ore grade, '
               'its waste content and its cost. The schedule decides when each block is mined.'),
              ('Block precedence',
               'Some blocks cannot be mined until blocks above or beside them are removed. This '
               'order is called precedence, and the schedule must respect it at every step.'),
              ('Cut-off grade',
               'The cut-off grade is the lowest grade worth sending to the mill. It often changes '
               'over time, because prices and costs change, so the schedule may mine richer blocks '
               'first and leave lower-grade ones for later.'),
              ('Mixed-integer models',
               'Mixed-integer programming is a mathematical method that searches for the best '
               'schedule under many rules at once. It can handle yes-or-no choices, such as '
               'whether a block is mined in a given year.'),
              ('Capacity limits',
               'Each year has limits on how much rock the fleet can move and how much ore the mill '
               'can process. The schedule keeps within these limits so the plan can be achieved.'),
              ('The value of a schedule',
               'A good schedule brings money sooner and avoids wasting ore. Small gains in each '
               'year add up over the life of a mine, so careful scheduling is one of the best ways '
               'to add value.')],
 'test': [('What does a block model contain for each block?',
           [('a', 'A photograph of the miners'),
            ('b', 'The name of the truck driver'),
            ('c', 'An estimate of its grade, its waste content and its cost'),
            ('d', 'The weather forecast')],
           'c'),
          ('What is block precedence?',
           [('a', 'The rule that some blocks can only be mined after others are removed'),
            ('b', 'A kind of explosive'),
            ('c', 'The price of a tonne'),
            ('d', 'A ventilation fan')],
           'a'),
          ('What is the cut-off grade?',
           [('a', 'The highest speed of a truck'),
            ('b', 'The depth of the shaft'),
            ('c', 'The weight of a drill'),
            ('d', 'The lowest grade worth sending to the mill')],
           'd'),
          ('What can mixed-integer models handle?',
           [('a', 'Only the colour of the ore'),
            ('b', 'Yes-or-no choices, such as whether a block is mined in a given year'),
            ('c', 'Only the weather'),
            ('d', 'Nothing but the price')],
           'b'),
          ('Why does a schedule have capacity limits?',
           [('a', 'Because mines must stay small'),
            ('b', 'To keep the ore dry'),
            ('c', 'The fleet and the mill can only handle so much each year'),
            ('d', 'To stop all mining at noon')],
           'c')]}
