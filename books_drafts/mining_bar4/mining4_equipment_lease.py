"""Leasing Versus Buying Equipment: comparing the full cost of owning machinery against paying to use it."""
CODE = 'mining4_equipment_lease'
BOOK = {
    "title": 'Leasing Versus Buying Equipment',
    "subtitle": 'Comparing the full cost of owning machinery with paying to use it',
    "chapters": [
        ('Purchase price and resale',
         'Buying equipment costs the full price up front. Machines lose value over time, so their resale value at the end matters. A machine that holds its value costs less to own in the end.'),
        ('Lease payments',
         'A lease pays for the use of equipment in regular instalments over a set term. The payments are often smaller than the purchase price, but they add up over the full term.'),
        ('Tax effects',
         'Both buying and leasing can reduce tax. Buying brings depreciation and interest deductions. Leasing brings lease payments as an expense. The effects differ by country and must be checked.'),
        ('Maintenance packages',
         'Some leases include maintenance, which spreads repair costs evenly. A buyer must plan and pay for repairs, which can be large and uneven.'),
        ('Lease terms',
         'Lease terms set the length, the end options and any penalties for early return. Reading these terms closely shows the true cost of the arrangement.'),
        ('Choosing',
         'The best choice compares the total cost over the life of the machine, including resale, tax, maintenance and cash timing. The lowest monthly payment is not always the cheapest deal.'),
    ],
    "test": [
        ('What matters at the end when buying equipment?',
         [('a', 'Its paint colour only'), ('b', 'The name of the seller'), ('c', 'Its resale value'), ('d', 'The weather that day')], 'c'),
        ('What is a lease?',
         [('a', 'Paying regular instalments to use equipment for a set term'), ('b', 'Giving equipment away for ever'), ('c', 'Buying a town'), ('d', 'Hiring a cook for a day')], 'a'),
        ('What might a maintenance package in a lease do?',
         [('a', 'Remove all repairs for ever'), ('b', 'Pay the staff'), ('c', 'Build a new mine'), ('d', 'Spread repair costs evenly')], 'd'),
        ("What should a lease's terms be read for?",
         [('a', 'The number of pages only'), ('b', 'The true cost, including end options and early return penalties'), ('c', 'The font size only'), ('d', "The name of the lawyer's dog")], 'b'),
        ('What is the best basis for choosing between leasing and buying?',
         [('a', 'The lowest monthly payment alone'), ('b', 'The colour of the machine'), ('c', "The total cost over the machine's life, including resale and tax"), ('d', 'Whichever is first on the list')], 'c'),
    ],
}
