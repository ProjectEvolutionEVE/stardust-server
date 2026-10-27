"""Equity Pay and Vesting: how share-based pay is granted, earned over time, and diluted, and what to check in the terms."""
CODE = 'computing4_equity_pay'
BOOK = {
    "title": 'Equity Pay and Vesting',
    "subtitle": 'How share-based pay is granted, earned over time, and diluted',
    "chapters": [
        ('Grants',
         'An equity grant is a promise of shares or options in a company, given as part of pay. A grant is not money in hand. Its value depends on what the company becomes, and it may end up worth nothing.'),
        ('Vesting schedules and cliffs',
         'Vesting is the schedule on which you earn the grant, often over four years. A cliff is a period at the start, often one year, before any shares vest. Leaving before the cliff usually means keeping nothing.'),
        ('Dilution',
         'Dilution happens when new shares are issued, so each existing share owns a smaller part of the company. Dilution is normal as companies raise money. A small share of a much larger company can still be valuable.'),
        ('Strike price',
         'Share options have a strike price, the fixed price at which you may buy the shares. If the company is worth more than the strike price, the options have value. If not, they may be worth nothing.'),
        ('Liquidity events',
         'A liquidity event, such as a sale or a listing on a stock market, is when shares can be turned into cash. Until then, shares may be hard to sell. Check what happens to your grant in a sale.'),
        ('Reading equity terms',
         'Read the grant document carefully, including the vesting dates, the exercise period after leaving, and any tax rules. Ask for a plain explanation of anything unclear. Seek independent advice before making large decisions.'),
    ],
    "test": [
        ('What is an equity grant?',
         [('a', 'A cash bonus paid at once'), ('b', 'A discount on the office lunch'), ('c', 'A loan from the bank'), ('d', 'A promise of shares or options given as part of pay')], 'd'),
        ('What is a vesting cliff?',
         [('a', 'A steep hill near the office'), ('b', 'A period at the start before any shares vest'), ('c', 'A type of share certificate'), ('d', 'A bank holiday')], 'b'),
        ('What is dilution?',
         [('a', 'Adding water to the company'), ('b', 'A rise in salary'), ('c', 'When new shares make each existing share own a smaller part'), ('d', 'A discount on the product')], 'c'),
        ('What is a strike price?',
         [('a', 'The fixed price at which you may buy shares under an option'), ('b', 'The price of a football ticket'), ('c', 'The daily rate for contractors'), ('d', 'The cost of a server')], 'a'),
        ('Why check the terms for a sale of the company?',
         [('a', 'To choose the office colour'), ('b', 'To see what happens to your grant in a liquidity event'), ('c', 'To find the lunch menu'), ('d', 'To set the holiday rota')], 'b'),
    ],
}
