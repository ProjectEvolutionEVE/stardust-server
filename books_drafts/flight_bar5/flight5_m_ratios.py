"""Financial Ratios: simple comparisons that turn the statements into answers about safety, debt and return."""
CODE = 'flight5_m_ratios'
BOOK = {
    'title': 'Financial Ratios',
    'subtitle': 'Simple comparisons that show health at a glance',
    'chapters': [
        ('Why ratios', 'A ratio divides one number by another, so that a big business and a small one can be compared. Ratios answer questions such as can we pay our bills, and how much debt do we carry.'),
        ('Liquidity', 'The current ratio is current assets divided by current liabilities. A ratio above one means short-term assets cover short-term bills. A ratio far below one is a sign to watch.'),
        ('Leverage', "The debt-to-equity ratio compares borrowed money with the owners' money. A high ratio means the business relies on debt, which adds risk when income falls."),
        ('Return', 'Return on assets is net income divided by total assets. It shows how well the business turns what it owns into profit. Compare it with similar businesses, not with a number from another trade.'),
        ('Coverage', 'The interest coverage ratio is operating profit divided by interest owed. A ratio well above one means the business can comfortably pay its interest. A ratio near one leaves little room for error.'),
        ('Peers and limits', 'A ratio means little on its own. Compare it with the same business in earlier years and with similar businesses. Each ratio also has limits, so use several together.'),
    ],
    'test': [
        ('How is the current ratio found?', [('a', 'Total weight divided by crew'), ('b', 'Current assets divided by current liabilities'), ('c', 'Price times colour'), ('d', 'Profit plus hours')], 'b'),
        ('What does a current ratio above one suggest?', [('a', 'The business has no assets'), ('b', 'The business must close'), ('c', 'The business owes nothing ever'), ('d', 'Short-term assets can cover short-term bills')], 'd'),
        ('What does the debt-to-equity ratio compare?', [('a', 'Crew with craft'), ('b', 'Sales with weather'), ('c', "Borrowed money with the owners' money"), ('d', 'Paint with fuel')], 'c'),
        ('How is interest coverage found?', [('a', 'Operating profit divided by interest owed'), ('b', 'Interest owed divided by the number of crew'), ('c', 'Total assets minus the weather'), ('d', 'Revenue plus paint')], 'a'),
        ('Why should a ratio be compared over years and with peers?', [('a', 'Ratios never change'), ('b', 'Peers always have the same numbers'), ('c', 'Years make ratios wrong'), ('d', 'A ratio means little on its own')], 'd'),
    ],
}
