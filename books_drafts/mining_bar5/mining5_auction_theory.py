"""Auctions for Mineral Rights: how governments and companies sell rights to explore and mine, and how bidders behave."""
CODE = "mining5_auction_theory"
BOOK = {'title': 'Auctions for Mineral Rights',
 'subtitle': "How rights are sold, how bidders decide, and the winner's curse",
 'chapters': [('Why auction rights',
               'Governments often sell the right to explore or mine by auction. An auction aims to get a '
               'fair price for a public resource and to pick a capable operator. The design of the auction '
               'matters a great deal.'),
              ('Auction formats',
               'Common formats include the open auction, where bids rise in public, and the sealed-bid '
               'auction, where each bidder submits one private bid. Each format changes how bidders behave.'),
              ('Bidding',
               'Bidders estimate what the rights are worth and bid below that to keep some profit. How much '
               'they shade the bid depends on how many rivals there are and how sure they are of their '
               'estimate.'),
              ("The winner's curse",
               'When many bidders estimate the same value with error, the winner is often the one who '
               "guessed highest. This is the winner's curse. A careful bidder lowers the bid to allow for "
               'it.'),
              ('Reserve prices',
               'A reserve price is the lowest price the seller will accept. Setting it too high can leave '
               'rights unsold, while setting it too low can give them away cheaply.'),
              ('Revenue and design',
               'Good designs aim to raise fair revenue, attract serious bidders and avoid collusion. '
               'Governments review results and adjust the rules for the next round.')],
 'test': [('Why do governments often auction mineral rights?',
           [('a', 'To close all mines'),
            ('b', 'To remove the ore'),
            ('c', 'To get a fair price and pick a capable operator'),
            ('d', 'To avoid all bidders')],
           'c'),
          ('What is a sealed-bid auction?',
           [('a', 'An auction where each bidder makes one private bid'),
            ('b', 'An auction held underwater'),
            ('c', 'An auction where the bids are shouted in public'),
            ('d', 'An auction of gold coins only')],
           'a'),
          ("What is the winner's curse?",
           [('a', 'A fine for losing a bid'),
            ('b', 'A type of lightning'),
            ('c', 'A rule that stops all bids'),
            ('d', 'A tendency for the winner to be the one who guessed highest')],
           'd'),
          ('What is a reserve price?',
           [('a', 'The price of a meal'),
            ('b', 'The lowest price the seller will accept'),
            ('c', 'The total weight of the ore'),
            ('d', 'A bonus paid to staff')],
           'b'),
          ('What can happen if a reserve price is set too high?',
           [('a', 'Rights always sell at once'),
            ('b', 'The ore grows'),
            ('c', 'Rights may be left unsold'),
            ('d', 'The bids are doubled')],
           'c')]}
