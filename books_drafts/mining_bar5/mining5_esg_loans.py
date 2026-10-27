"""ESG-Linked Loans and Bonds: borrowing whose interest rate depends on meeting sustainability targets."""
CODE = 'mining5_esg_loans'
BOOK = {
    "title": 'ESG-Linked Loans and Bonds',
    "subtitle": 'Borrowing whose cost depends on meeting sustainability targets',
    "chapters": [
        ('Sustainability-linked terms', 'A sustainability-linked loan or bond ties its interest rate to targets the borrower agrees to meet. If the borrower meets the targets, the rate may fall. If it misses them, the rate may rise.'),
        ('Targets', 'Targets are set in advance and must be measurable. They might cover energy use, emissions, water or safety. Clear targets make the link between money and performance real.'),
        ('Metrics', 'Each target needs a metric, which is the number used to measure progress. The metric must be defined clearly, with its method and its boundaries. Vague metrics make disputes likely.'),
        ('Penalties', 'A penalty is a higher interest rate charged when a target is missed. Penalties give the borrower a clear reason to meet its goals. The size of the penalty is part of the negotiation.'),
        ('Verification', 'An outside party often verifies the reported results before the rate is changed. Verification gives lenders and investors confidence in the numbers. Honest reporting protects everyone involved.'),
        ('Costs', 'Setting up these loans costs money for advisers, verifiers and reporting systems. The benefit must be weighed against those costs. A well-designed link can lower the total cost of borrowing over time.'),
    ],
    "test": [
        ('What does a sustainability-linked loan tie its interest rate to?', [('a', 'The price of coffee'), ('b', 'The number of birds in a park'), ('c', 'Targets the borrower agrees to meet'), ('d', 'The height of the building')], 'c'),
        ('What is a metric in this kind of loan?', [('a', 'The number used to measure progress toward a target'), ('b', 'A type of ruler for drawing'), ('c', 'A bonus paid to staff'), ('d', 'A fee paid to a hotel')], 'a'),
        ('What is a penalty in these loans?', [('a', 'A prize for early payment'), ('b', 'A higher interest rate when a target is missed'), ('c', 'A reduction in the loan size to zero'), ('d', 'A free holiday for the borrower')], 'b'),
        ('Why is outside verification used?', [('a', 'To hide the results from the public'), ('b', 'To make the loan larger'), ('c', 'To remove the need for targets'), ('d', 'To give lenders and investors confidence in the reported numbers')], 'd'),
        ("Why must a target's metric be defined clearly?", [('a', 'Vague metrics make disputes likely'), ('b', 'Clear metrics are illegal'), ('c', 'Metrics never need numbers'), ('d', 'Metrics only matter in summer')], 'a'),
    ],
}
