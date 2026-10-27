"""Hedging Inflation With Real Assets: how investors try to protect their money's buying power when prices rise."""
CODE = "mining5_inflation_hedge"
BOOK = {'title': 'Hedging Inflation With Real Assets',
 'subtitle': 'Protecting buying power when prices rise, and where the protection falls short',
 'chapters': [('Real and nominal returns',
               'A nominal return is the headline gain on an investment. The real return is what is left '
               'after inflation. A 5% gain with 3% inflation leaves about 2% real growth.'),
              ('Commodities',
               'Raw materials such as metals and energy sometimes rise with inflation, because their prices '
               'follow costs. This link is not reliable every year, so commodities are a partial hedge at '
               'best.'),
              ('Inflation-linked bonds',
               'Some governments issue bonds whose value rises with an official inflation index. The '
               'investor receives protection against rising prices, but the return is usually lower than on '
               'ordinary bonds.'),
              ('Diversification',
               'Spreading money across many kinds of asset reduces the risk that one fall will ruin the '
               'whole plan. A mix of shares, bonds, property and commodities is common.'),
              ('Costs',
               'Funds charge fees, storage costs money for physical goods, and buying and selling has '
               'spreads. These costs reduce the gain from any hedge, so they should be counted in advance.'),
              ('Limits',
               'No hedge is perfect, especially over short periods. A hedge that works in one period may '
               'fail in the next. Expect partial protection and plan for it.')],
 'test': [('What is the real return on an investment?',
           [('a', 'The headline gain only'),
            ('b', 'The gain before tax'),
            ('c', 'The gain left after inflation'),
            ('d', 'The price of the asset')],
           'c'),
          ('What do inflation-linked bonds adjust?',
           [('a', 'The value, following an official inflation index'),
            ('b', 'The colour of the bond'),
            ('c', 'The name of the issuer'),
            ('d', "The date of the mine's first blast")],
           'a'),
          ('Why is a commodity only a partial hedge against inflation?',
           [('a', 'Commodities never change in price'),
            ('b', 'Commodities are illegal to hold'),
            ('c', 'Commodities pay large monthly interest'),
            ('d', 'The link with inflation is not reliable every year')],
           'd'),
          ('What does diversification aim to do?',
           [('a', 'Put all money into one asset'),
            ('b', 'Reduce the risk that one fall ruins the whole plan'),
            ('c', 'Remove all costs'),
            ('d', 'Guarantee a profit each year')],
           'b'),
          ("Which is a cost that cuts into a hedge's gain?",
           [('a', 'The colour of a bar of metal'),
            ('b', 'The number of years in school'),
            ('c', 'Fund fees and storage costs'),
            ('d', 'The date on a calendar')],
           'c')]}
