"""Interest Rate Swaps for Mine Debt: how a mine can exchange one kind of interest payment for another to manage its borrowing costs."""
CODE = "mining5_rate_swaps"
BOOK = {'title': 'Interest Rate Swaps for Mine Debt',
 'subtitle': 'Trading one kind of interest payment for another to reduce risk',
 'chapters': [('What a swap is',
               'An interest rate swap is an agreement between two parties to exchange interest payments on '
               'the same amount of money. One side pays a fixed rate and the other pays a rate that moves '
               'with the market. The loan itself is not swapped.'),
              ('Why a mine uses one',
               'A mine with a floating-rate loan pays more when rates rise. A swap can turn those payments '
               'into a fixed amount, so the cost is easier to plan. This makes budgeting and lending terms '
               'simpler.'),
              ('Valuing a swap',
               'A swap is worth the present value of the payments expected in the future. As market rates '
               'move, the value moves too. Both sides check this value regularly.'),
              ('Hedge accounting',
               'Companies often treat swaps as hedges, which means the gains and losses are recorded '
               'alongside the risk they cover. The accounting rules are strict. Auditors check that the '
               'hedge really matches the loan.'),
              ('Counterparty risk',
               'The other side of the swap might not pay. This is called counterparty risk. Many deals use '
               'collateral, which is money or assets held as security, to reduce the danger.'),
              ('Costs to weigh',
               'Swaps carry fees, and collateral can tie up cash. A mine should compare the total cost of a '
               'swap with the risk it removes. Good debt planning looks at the whole picture, not just the '
               'headline rate.')],
 'test': [('In a basic interest rate swap, what is exchanged?',
           [('a', 'The loan itself'),
            ('b', "The mine's ore"),
            ('c', 'The interest payments on the same amount of money'),
            ('d', 'Shares in the company')],
           'c'),
          ('Why might a mine use a swap?',
           [('a', 'To turn variable payments into a more predictable fixed amount'),
            ('b', 'To increase the price of gold'),
            ('c', 'To avoid paying any interest at all'),
            ('d', 'To sell its tools')],
           'a'),
          ('What does counterparty risk mean?',
           [('a', 'The risk of a mine fire'),
            ('b', 'The risk of a fall in ore grade'),
            ('c', 'The risk of losing a vote'),
            ('d', 'The risk that the other side of the deal does not pay')],
           'd'),
          ('What is collateral?',
           [('a', 'A type of ore'),
            ('b', 'Money or assets held as security'),
            ('c', 'A law about tax'),
            ('d', 'A map of the mine')],
           'b'),
          ('What is the value of a swap based on?',
           [('a', 'The weather at the mine'),
            ('b', 'The number of trucks'),
            ('c', 'The present value of expected future payments'),
            ('d', 'The price of one bar of gold only')],
           'c')]}
