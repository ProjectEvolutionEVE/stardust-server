"""Valuing a Mining Company: multiples, asset values and reserve-based methods for a whole company."""
CODE = 'mining5_valuing_co'
BOOK = {
    "title": 'Valuing a Mining Company',
    "subtitle": 'Multiples, asset values and reserve-based methods',
    "chapters": [
        ('Multiples', "A multiple compares a company's value with a measure of its earnings, such as its EBITDA. Investors use multiples to compare companies quickly. A multiple is a shortcut, so it needs context."),
        ('EV/EBITDA', 'Enterprise value divided by EBITDA is a common multiple. Enterprise value counts the debt as well as the shares, and EBITDA is earnings before interest, tax, depreciation and amortisation. The ratio helps compare companies with different debts.'),
        ('Asset value', 'A net asset value method adds up the value of each mine, project and asset, then subtracts the debts. Each asset is valued separately using its own model. This method works well for companies with clear, separate assets.'),
        ('Reserve-based valuation', 'Reserve-based valuation values a company by the metal or minerals it holds in proven and probable reserves. Each unit of reserve is given a value based on price and cost. The result depends heavily on the reserve estimate.'),
        ('Peer sets', 'A peer set is a group of similar companies used for comparison. Good peers match in commodity, size, location and stage of development. A badly chosen peer set can mislead the valuation.'),
        ('Limits', 'No single method gives the true value of a mining company. Prices, costs and reserves all change over time. A careful valuation uses several methods and explains the differences.'),
    ],
    "test": [
        ('What does a multiple compare?', [('a', 'The number of trucks in a yard'), ('b', 'The number of letters in a name'), ('c', 'The weight of a bag of salt'), ('d', "A company's value with a measure of its earnings")], 'd'),
        ('What does EBITDA stand for?', [('a', 'Extra bonus for every ton of drills'), ('b', 'Earnings before interest, tax, depreciation and amortisation'), ('c', 'Estimated balance of trucks and drills'), ('d', 'Each boat is taxed daily')], 'b'),
        ('How does a net asset value method work?', [('a', 'It counts the workers on site'), ('b', 'It measures the length of roads'), ('c', "It adds up each asset's value and subtracts the debts"), ('d', 'It guesses the weather')], 'c'),
        ('What does reserve-based valuation depend on?', [('a', 'The price, cost and size of the reserves'), ('b', 'The colour of the company logo'), ('c', 'The number of staff parking spaces'), ('d', 'The name of the chief executive')], 'a'),
        ('Why is a peer set used?', [('a', 'To choose the company colours'), ('b', 'To compare with similar companies'), ('c', 'To pick a new office'), ('d', 'To set the price of coffee')], 'b'),
    ],
}
