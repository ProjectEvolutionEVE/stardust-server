"""Break-Even Costs and Margin of Safety: how far prices can fall before a mine loses money, and what drives that line."""
CODE = "mining5_breakeven"
BOOK = {'title': 'Break-Even Costs and Margin of Safety',
 'subtitle': 'The price at which a mine just covers its costs, and how much room it has above it',
 'chapters': [('The break-even price',
               'The break-even price is the metal price at which revenue just covers all costs. Below it, '
               'the mine loses money. Above it, the mine makes a profit that grows with the price.'),
              ('Operating leverage',
               'Mines with high fixed costs gain more from a rising price, and lose more from a falling one. '
               'This is called operating leverage. It explains why mining profits swing so widely.'),
              ('Margin of safety',
               'The margin of safety is the gap between the current price and the break-even price. A wide '
               'gap gives room to survive a fall. A narrow gap leaves little room for error.'),
              ('Cost drivers',
               'Energy, labour, fuel, reagents and the grade of the ore drive the cost per tonne. A lower '
               'grade means more rock must be moved for each unit of metal, which raises the break-even '
               'price.'),
              ('Sensitivity analysis',
               'Sensitivity analysis changes one input at a time, such as the price or the energy cost, and '
               'shows the effect on profit. It reveals which factors matter most.'),
              ('Decisions',
               'Managers use break-even figures to decide whether to open, pause or close a mine. Decisions '
               'based on several scenarios are safer than decisions based on one price.')],
 'test': [('What is the break-even price?',
           [('a', 'The highest price ever recorded'),
            ('b', 'The price of a truck'),
            ('c', 'The price at which revenue just covers all costs'),
            ('d', 'The price of a holiday')],
           'c'),
          ('What is operating leverage?',
           [('a', 'Mines with high fixed costs gain more from rising prices and lose more from falling ones'),
            ('b', 'A lever in the office door'),
            ('c', 'A tax on drills'),
            ('d', 'A type of rock')],
           'a'),
          ('What is the margin of safety?',
           [('a', 'The number of safety signs at a mine'),
            ('b', 'The weight of the helmet'),
            ('c', 'The distance to the office'),
            ('d', 'The gap between the current price and the break-even price')],
           'd'),
          ('What does a lower ore grade do to the break-even price?',
           [('a', 'It lowers it to zero'),
            ('b', 'It raises it, because more rock must be moved per unit of metal'),
            ('c', 'It has no effect'),
            ('d', 'It removes all costs')],
           'b'),
          ('What does sensitivity analysis do?',
           [('a', 'Measures the heat of the mine'),
            ('b', 'Counts the number of staff'),
            ('c', 'Changes one input at a time to see its effect on profit'),
            ('d', 'Paints the office')],
           'c')]}
