"""The Growth-Share Matrix: the Boston Consulting Group, stars, cash cows, question marks, dogs, and the critics of the tool."""
CODE = 'business4_bcg'
BOOK = {
    "title": 'The Growth-Share Matrix',
    "subtitle": "Sorting a firm's products by market growth and market share",
    "chapters": [
        ('The Boston Consulting Group',
         'The growth-share matrix was developed in the 1970s at the Boston Consulting Group, a firm of management consultants. It helps a company that sells many products decide where to put its money. Each product or business unit is placed on a simple grid.'),
        ('The two axes',
         "One axis shows the growth rate of the market the product sits in. The other shows the product's share of that market compared with its largest rival. High share in a fast-growing market is a strong position, and low share in a slow one is a weak position."),
        ('Stars',
         'A star has a high market share in a fast-growing market. It earns good profit, but often needs heavy spending to keep up. A star can become a cash cow once its market growth slows, if it keeps its lead.'),
        ('Cash cows',
         'A cash cow has a high share in a slow-growing market. It needs little new investment and throws off steady cash. The cash can fund stars and question marks elsewhere in the firm.'),
        ('Question marks',
         'A question mark sits in a fast-growing market with a small share. It needs money to grow, and its future is uncertain. The firm must decide whether to invest in it and try to win share, or to let it go.'),
        ('Dogs, and the critics',
         'A dog has a small share in a slow-growing market and usually earns little. Firms often sell or close these. Critics say the matrix oversimplifies, relies on the idea that share drives profit, and can push managers to abandon units too quickly. It is best treated as a starting point for talk.'),
    ],
    "test": [
        ('Where was the growth-share matrix developed?',
         [('a', 'At the Bank of England'), ('b', 'At a car factory in Detroit'), ('c', 'At a school of art'), ('d', 'At the Boston Consulting Group')], 'd'),
        ('What is a star in the matrix?',
         [('a', 'A product with high share in a fast-growing market'), ('b', 'A product with low share in a slow market'), ('c', 'A product that is about to close'), ('d', 'A product sold only abroad')], 'a'),
        ('What is a cash cow?',
         [('a', 'A product with no buyers'), ('b', 'A product with high share in a slow-growing market that throws off steady cash'), ('c', 'A government subsidy'), ('d', 'A loan from a bank')], 'b'),
        ('What does a question mark need from the firm?',
         [('a', 'Nothing at all, since it earns a lot'), ('b', 'Its own bank'), ('c', 'Investment, since its future is uncertain'), ('d', 'A new name every day')], 'c'),
        ('What is one criticism of the growth-share matrix?',
         [('a', 'It is illegal in most countries'), ('b', 'It only works for banks'), ('c', 'It requires no data at all'), ('d', 'It oversimplifies and can push managers to drop units too quickly')], 'd'),
    ],
}
