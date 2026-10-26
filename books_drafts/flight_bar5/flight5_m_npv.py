"""Net Present Value: valuing money received in the future by what it is worth today."""
CODE = 'flight5_m_npv'
BOOK = {
    'title': 'Net Present Value',
    'subtitle': 'What future money is worth today',
    'chapters': [
        ('Money over time', "Money received later is worth less than money in hand today, because today's money can be put to use. Net present value, or NPV, puts all the future cash flows on one scale: their value today."),
        ('Discounting', 'Each future cash flow is divided by one plus the rate, raised to the number of years away. This is called discounting. A higher rate makes the future flows worth less today.'),
        ('Choosing a rate', 'The discount rate reflects what the money could earn elsewhere, plus the risk of the project. Pick it carefully and write down the reason. A wrong rate can flip the answer.'),
        ('Positive against negative', 'If the NPV is positive, the project earns more than the required rate and adds value. If it is negative, it destroys value at that rate. Zero means it just meets the rate.'),
        ('A ship purchase example', 'Suppose a craft costs 100 credits now and returns 60 credits a year for two years at a 10 percent rate. The present values of the returns add up to a little over 100, so the NPV is slightly positive and the purchase is marginally worth it.'),
        ('Pitfalls', 'NPV depends on the cash flow estimates. Test the answer with a higher and a lower rate, and with pessimistic and optimistic flows. A result that holds under both is more trustworthy.'),
    ],
    'test': [
        ('Why is money received later worth less than money today?', [('a', 'Money loses its colour over time'), ('b', 'Future money is always counterfeit'), ('c', "Today's money can be put to use and earn more"), ('d', 'Banks do not accept future money')], 'c'),
        ('What does discounting do?', [('a', "Makes future cash flows worth less in today's terms"), ('b', 'Makes future cash flows worth more'), ('c', 'Removes all cash flows'), ('d', 'Adds a fixed fee')], 'a'),
        ('What does a negative NPV mean?', [('a', 'The project is always the best choice'), ('b', 'The project costs nothing'), ('c', 'The project is too small to count'), ('d', 'The project destroys value at the chosen rate')], 'd'),
        ('Why test the answer with different rates?', [('a', 'Different rates always give the same answer'), ('b', 'A wrong rate can flip the answer, so a result that holds is more trustworthy'), ('c', 'Rates are only for fun'), ('d', 'Rates are not needed at all')], 'b'),
        ('What does an NPV of exactly zero mean?', [('a', 'The project just meets the required rate'), ('b', 'The project loses all its money'), ('c', 'The project has no cash flows'), ('d', 'The project must be painted again')], 'a'),
    ],
}
