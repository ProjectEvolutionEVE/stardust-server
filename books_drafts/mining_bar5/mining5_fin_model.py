"""Building a Mine Financial Model: the inputs, timing and checks behind a mine's numbers."""
CODE = 'mining5_fin_model'
BOOK = {
    "title": 'Building a Mine Financial Model',
    "subtitle": "The inputs, timing and checks behind a mine's numbers",
    "chapters": [
        ('Inputs', 'A mine model starts with inputs: the ore grade, the recovery rate, the production rate, the prices, the costs and the capital needed. Each input should have a stated source. A model is only as good as the inputs it is given.'),
        ('Timing', 'Timing shows when money is spent and when it comes back. Construction spending comes first, then years of production, then closure costs. Getting the timing right matters because money today is worth more than money later.'),
        ('Working capital', 'Working capital is the cash tied up in stock, unpaid bills and unpaid customers. A growing mine often needs extra working capital before it earns. Forgetting it can make a sound project run short of cash.'),
        ('Tax', 'Tax is calculated on profit after allowed deductions, and the rules can be complex. The model should follow the local tax rules, including loss carry-forwards and depreciation. Simple tax rates can hide important detail.'),
        ('Sensitivity', 'A sensitivity analysis changes one input at a time to see how much the result moves. The inputs that move the result most need the closest attention. A simple chart of sensitivities is a clear way to show risk.'),
        ('Model checks', 'Good models are checked for errors, such as broken links, wrong signs and double counting. A second person should review the logic and test the totals. The final model should be documented well enough for someone else to use.'),
    ],
    "test": [
        ('What are the main inputs in a mine model?', [('a', 'The colour of the office walls'), ('b', 'The name of the cafe nearby'), ('c', 'Ore grade, recovery, production, prices and costs'), ('d', 'The number of birds on the site')], 'c'),
        ('Why does timing matter in a mine model?', [('a', 'Money today is worth more than money later'), ('b', 'Timing changes the colour of ore'), ('c', 'Timing removes all tax'), ('d', 'Timing makes rock lighter')], 'a'),
        ('What is working capital?', [('a', 'The cash kept in a jar at home'), ('b', 'Cash tied up in stock, unpaid bills and unpaid customers'), ('c', 'Money given away as a gift'), ('d', 'The price of a truck')], 'b'),
        ('What does sensitivity analysis do?', [('a', 'Measures how loud a machine is'), ('b', 'Sorts ore by colour'), ('c', 'Counts the staff'), ('d', 'Changes one input at a time to see how much the result moves')], 'd'),
        ('What is a common model check?', [('a', 'Looking for broken links, wrong signs and double counting'), ('b', 'Painting the spreadsheet blue'), ('c', 'Deleting the inputs'), ('d', 'Printing the model on paper and burning it')], 'a'),
    ],
}
