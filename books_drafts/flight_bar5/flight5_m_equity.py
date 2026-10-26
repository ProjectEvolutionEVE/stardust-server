"""Shares and Ownership: owning a piece of a business, its dividends, its value, and what new shares do to your stake."""
CODE = 'flight5_m_equity'
BOOK = {
    'title': 'Shares and Ownership',
    'subtitle': 'Owning a piece of a business',
    'chapters': [
        ('What a share is', "A share is a unit of ownership in a company. Each share gives its holder a part of the company's value and, usually, a vote on major decisions in proportion to the number held."),
        ('Dividends', "A dividend is a payment of part of the company's profit to its shareholders. Not every company pays dividends. A company may keep its profit to grow instead."),
        ('Valuation', "A share's value depends on what the business will earn in the future. Analysts compare price with earnings, and with the value of the assets. Share prices can move far from these measures in the short term."),
        ('Dilution', "Dilution happens when a company issues new shares. Each existing share then owns a smaller part of the company. Dilution can be right if the new money grows the business, but it reduces each holder's stake."),
        ('Control', 'Owning more than half the shares usually gives control of the vote. Owning a smaller part can still matter when the vote is close or when others hold many small stakes.'),
        ('Risk', 'Shares can fall in value, and the holder can lose the money put in. Spread holdings across several businesses, and invest only what you can afford to leave in place for years.'),
    ],
    'test': [
        ('What is a share?', [('a', 'A unit of ownership in a company'), ('b', 'A type of crew uniform'), ('c', 'A bill from a shop'), ('d', 'A gift to the crew')], 'a'),
        ('What is a dividend?', [('a', 'A fee paid to the government for the hull'), ('b', 'A type of paint'), ('c', "A payment of part of the company's profit to shareholders"), ('d', 'A penalty for late work')], 'c'),
        ('What is dilution?', [('a', 'A way of making coffee weaker'), ('b', "A fall in each existing share's stake when new shares are issued"), ('c', 'The sale of all shares at once'), ('d', 'A rise in the number of crew')], 'b'),
        ("Why does a share's price depend on future earnings?", [('a', 'Shares are paid in paint'), ('b', 'Shares only pay out once'), ('c', 'Shares have no value'), ('d', "A share's value rests on what the business will earn")], 'd'),
        ('What is a sensible way to manage the risk of shares?', [('a', 'Put all savings into one share'), ('b', 'Borrow to buy as many as possible'), ('c', 'Spread holdings across several businesses'), ('d', 'Never look at the price')], 'c'),
    ],
}
