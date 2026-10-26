"""The Financial Crisis of 2008: mortgage lending, securitisation, leverage, Lehman Brothers, the freeze, and the response."""
CODE = 'business4_crisis08'
BOOK = {
    "title": 'The Financial Crisis of 2008',
    "subtitle": 'How risky home loans, heavy borrowing and a frozen market brought down banks',
    "chapters": [
        ('Mortgage lending',
         'In the years before 2008, lenders in the United States made many home loans to buyers with weak credit or uncertain incomes. Many loans had low starting payments that later rose. Lenders often expected house prices to keep climbing, which would cover any problem.'),
        ('Securitisation',
         'Banks bundled many mortgages together and sold them to investors as securities. This spread the loans far beyond the original lenders. The packaging made the risks harder to see, and many buyers relied on ratings that proved too generous.'),
        ('Leverage',
         'Many banks and investment firms borrowed heavily to hold these securities, so a small fall in their value could wipe out their capital. High leverage made the whole system fragile. When losses came, firms had little room to absorb them.'),
        ('Lehman Brothers',
         'On 15 September 2008, the investment bank Lehman Brothers filed for bankruptcy. It was one of the largest failures in American history. Its collapse shook confidence across the financial system, since many firms had dealings with it and nobody knew who was exposed.'),
        ('The freeze',
         'Banks became unwilling to lend to each other, because they feared their counterparts might fail. Credit markets froze, and firms that depended on short-term funding struggled. The freeze spread from finance to the wider economy, which slowed sharply.'),
        ('The response',
         'Governments and central banks acted to stabilise the system. They supported banks, lowered interest rates, and provided emergency lending. Later, new rules required banks to hold more capital and to be more open about their risks. The recession that followed was severe.'),
    ],
    "test": [
        ('What did many lenders in the years before 2008 expect about house prices?',
         [('a', 'That they would fall to zero'), ('b', 'That they would be fixed by law'), ('c', 'That they would keep climbing'), ('d', 'That they would never change')], 'c'),
        ('What is securitisation?',
         [('a', 'Keeping all loans in a single vault'), ('b', 'Paying off a loan early'), ('c', "Removing a bank's name from its building"), ('d', 'Bundling many loans together and selling them to investors as securities')], 'd'),
        ('What does high leverage mean for a firm?',
         [('a', 'It has borrowed heavily, so small losses can wipe out its capital'), ('b', 'It has no debt at all'), ('c', 'It pays no tax'), ('d', 'It sells only one product')], 'a'),
        ('On what date did Lehman Brothers file for bankruptcy?',
         [('a', '1 January 1999'), ('b', '15 September 2008'), ('c', '4 July 2001'), ('d', '31 December 2010')], 'b'),
        ('What happened when banks grew unwilling to lend to each other?',
         [('a', 'Interest rates became fixed for ever'), ('b', 'Every bank earned more'), ('c', 'Credit markets froze'), ('d', 'Loans became free')], 'c'),
    ],
}
