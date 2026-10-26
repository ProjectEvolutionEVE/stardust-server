"""Reading an Income Statement: money earned, money spent, and what is left over over a period."""
CODE = 'flight5_m_income'
BOOK = {
    'title': 'Reading an Income Statement',
    'subtitle': 'Money earned, money spent, and what is left',
    'chapters': [
        ('Over a period', 'An income statement shows money earned and spent over a period, such as a year or a quarter. Unlike a balance sheet, it is a record of flow, not of a single day.'),
        ('Revenue', 'Revenue is the money earned from selling goods or services. It is the top line of the statement. Check it against what the customers really paid, not only what was promised.'),
        ('Costs', 'Costs are the money spent to earn the revenue. They include the cost of goods, wages, rent and the day-to-day running of the business. Separate the cost of making a sale from other running costs.'),
        ('Margins and profit', 'The gross margin is revenue minus the direct cost of goods, shown as a share of revenue. Operating profit is what is left after running costs. Net profit is what remains after interest and tax.'),
        ('One-off items', 'Some items happen only once, such as the sale of an old craft or a fine. They can make a year look better or worse than usual. Look for them and judge the steady trend separately.'),
        ('Trends', 'One year tells you little. Compare several years and watch whether margins are rising or falling. A steady fall in margin is an early warning worth acting on.'),
    ],
    'test': [
        ('What period does an income statement cover?', [('a', 'A single moment'), ('b', 'Only one hour'), ('c', 'No period at all'), ('d', 'A period such as a year or a quarter')], 'd'),
        ('What is revenue?', [('a', 'The money owed to suppliers'), ('b', 'The money earned from selling goods or services'), ('c', "The value of the ship's paint"), ('d', 'The number of crew')], 'b'),
        ('What is operating profit?', [('a', 'What is left after running costs'), ('b', 'The total of all shares'), ('c', 'The price of a loan'), ('d', 'The first sale ever made')], 'a'),
        ('What are one-off items?', [('a', 'Items sold every day'), ('b', 'Items kept forever'), ('c', 'Items that happen only once and can distort a single year'), ('d', 'Items with no value')], 'c'),
        ('Why compare several years of income statements?', [('a', 'Because one year is always wrong'), ('b', 'To see whether margins are rising or falling over time'), ('c', 'To make the statements longer'), ('d', 'To avoid reading them')], 'b'),
    ],
}
