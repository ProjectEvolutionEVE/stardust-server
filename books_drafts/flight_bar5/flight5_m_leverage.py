"""Leverage and Debt: borrowing to grow, the true cost of debt, and how much debt is safe to carry."""
CODE = 'flight5_m_leverage'
BOOK = {
    'title': 'Leverage and Debt',
    'subtitle': 'Borrowing to grow, and how much is safe',
    'chapters': [
        ('What leverage is', 'Leverage means using borrowed money to fund part of what you own. When the investment earns more than the loan costs, the owners gain more. When it earns less, the owners lose more.'),
        ('The cost of debt', 'The cost of debt is the interest paid, after any tax relief. Compare it with what the money can earn. Borrowing at a high rate for a weak return is a poor bargain, however attractive it looks.'),
        ('Modigliani and Miller', 'In 1958, Franco Modigliani and Merton Miller showed that in a perfect market, how a firm is financed would not change its value. Real markets have taxes and costs, which is why debt matters in practice.'),
        ('Covenants', 'Lenders often set covenants, which are promises the borrower must keep. A covenant may limit more debt or require a minimum level of cash. Breaking one can call the loan in early.'),
        ('Distress', 'Too much debt can push a business into distress, where it cannot pay its bills. A business in distress may have to sell assets cheaply. Keep a margin of safety for bad years.'),
        ('Sizing debt', 'Size debt to what the business earns in a poor year, not a good one. Make sure the cash flow covers the repayments with room to spare. Borrow for a purpose that will pay the loan back.'),
    ],
    'test': [
        ('What does leverage mean?', [('a', 'Lifting heavy cargo by hand'), ('b', "Painting a craft's hull"), ('c', 'Using borrowed money to fund part of what you own'), ('d', 'Reading the stars')], 'c'),
        ('When does leverage help the owners?', [('a', 'When the investment earns more than the loan costs'), ('b', 'When the investment earns nothing'), ('c', 'When the loan is never repaid'), ('d', 'When the owners are asleep')], 'a'),
        ('What did Modigliani and Miller show in 1958?', [('a', 'Debt is always forbidden'), ('b', 'Interest rates never change'), ('c', 'Firms cannot borrow'), ('d', "In a perfect market, financing does not change a firm's value")], 'd'),
        ('What is a covenant?', [('a', 'A type of spacesuit'), ('b', 'A promise the borrower must keep, set by the lender'), ('c', 'A fee for the crew'), ('d', 'A name for a bank')], 'b'),
        ('How should debt be sized?', [('a', 'To what the business earns in a poor year, with room to spare'), ('b', 'To the best year ever seen'), ('c', 'To whatever the lender offers'), ('d', 'To the price of paint')], 'a'),
    ],
}
