"""Depreciation: spreading the cost of a long-lived asset over the years it helps to earn money."""
CODE = 'flight5_m_depreciation'
BOOK = {
    'title': 'Depreciation',
    'subtitle': 'Spreading the cost of a long-lived asset',
    'chapters': [
        ('Why spread the cost', "A craft or a machine helps earn money for many years. Depreciation spreads its cost across those years, so that each year's accounts show a fair share of the expense."),
        ('Straight line', 'The simplest method is straight-line depreciation. Take the cost, subtract the expected salvage value, and divide by the useful life in years. The same amount is charged each year.'),
        ('Declining balance', "Declining balance charges more in the early years, when an asset loses value fastest. Each year's charge is a fixed share of what is left. It matches some assets better, such as electronics."),
        ('Useful life and salvage', 'Useful life is how long the asset is expected to earn. Salvage value is what it may be worth at the end. Both are estimates, so write down the reason for each.'),
        ('Tax effect', 'Depreciation can reduce taxable profit, because the charge counts as an expense. Tax rules set how it may be claimed. Check the rules for your place and purpose.'),
        ('Book value and market value', 'Book value is cost minus the depreciation so far. Market value is what someone would pay today. The two often differ, and a large gap is worth understanding.'),
    ],
    'test': [
        ('What does depreciation spread?', [('a', 'The cost of a long-lived asset over the years it helps earn money'), ('b', 'The colour of a craft'), ('c', "The crew's meals over a week"), ('d', 'The distance between stars')], 'a'),
        ('How is straight-line depreciation found?', [('a', 'Cost plus salvage value times the crew'), ('b', 'Colour times weight'), ('c', 'Cost minus salvage value, divided by useful life'), ('d', 'Revenue divided by the weather')], 'c'),
        ('What does declining balance do?', [('a', 'Charges nothing ever'), ('b', 'Charges more in the early years'), ('c', 'Charges the same as the paint'), ('d', 'Charges only at the end')], 'b'),
        ('What is salvage value?', [('a', 'The first price of the asset'), ('b', 'A fine paid to the bank'), ('c', 'A crew bonus'), ('d', 'What an asset may be worth at the end of its life')], 'd'),
        ('What is book value?', [('a', 'The price a stranger would pay today'), ('b', 'The weight of the book'), ('c', 'Cost minus the depreciation charged so far'), ('d', 'The number of pages')], 'c'),
    ],
}
