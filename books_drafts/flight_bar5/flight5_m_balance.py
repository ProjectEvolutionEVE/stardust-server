"""Reading a Balance Sheet: what an organisation owns, what it owes and what is left for its owners."""
CODE = 'flight5_m_balance'
BOOK = {
    'title': 'Reading a Balance Sheet',
    'subtitle': 'What you own, what you owe, and what is left',
    'chapters': [
        ('A snapshot', 'A balance sheet is a snapshot of an organisation at one date. It lists what it owns, what it owes, and the value left for its owners. It is taken at a single moment, not over a year.'),
        ('The basic equation', "Assets equal liabilities plus equity. Whatever the organisation owns is paid for either by borrowing or by the owners' money. The two sides must always balance."),
        ('Assets', 'Assets are things of value the organisation controls, such as cash, craft, equipment and money owed to it. Current assets can be turned into cash within a year. Long-term assets last longer.'),
        ('Liabilities', 'Liabilities are what the organisation owes to others, such as loans, bills to suppliers and wages due. Current liabilities fall due within a year.'),
        ('Equity and working capital', "Equity is the owners' share after liabilities are paid. Working capital is current assets minus current liabilities. Positive working capital means short-term bills can be met."),
        ('Spotting trouble', 'Watch for rising debts, falling cash, and assets that are worth less than their book value. A balance sheet alone does not tell the whole story, so read it alongside the other statements.'),
    ],
    'test': [
        ('What does a balance sheet show?', [('a', 'Only the weather'), ('b', 'A list of games played'), ('c', 'A snapshot of assets, liabilities and equity at one date'), ('d', 'The number of crew for a year')], 'c'),
        ('What is the basic equation?', [('a', 'Assets equal liabilities plus equity'), ('b', 'Assets equal zero'), ('c', 'Liabilities equal assets times two'), ('d', 'Equity equals the weather')], 'a'),
        ('What are current liabilities?', [('a', 'Things owned for a hundred years'), ('b', 'The price of a ship'), ('c', 'Gifts from friends'), ('d', 'Debts that fall due within a year')], 'd'),
        ('What is working capital?', [('a', 'The total weight of the hull'), ('b', 'Current assets minus current liabilities'), ('c', 'The number of shares sold'), ('d', 'The fee for a loan')], 'b'),
        ('What is a warning sign on a balance sheet?', [('a', 'Rising debts with falling cash'), ('b', 'Cash that is growing steadily'), ('c', 'Debts that are being repaid'), ('d', 'Assets that are kept in good order')], 'a'),
    ],
}
