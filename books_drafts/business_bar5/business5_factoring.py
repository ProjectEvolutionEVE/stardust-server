"""Factoring and Invoice Finance: selling what customers owe, the advance and the fee, recourse or not, and when it helps."""
CODE = 'business5_factoring'
BOOK = {
    "title": 'Factoring and Invoice Finance',
    "subtitle": 'Selling what customers owe, and what it really costs',
    "chapters": [
        ('Money tied up in invoices',
         'When you deliver goods or services, the customer often pays 30, 60 or 90 days later. Until then, the money you are owed sits on paper while your bills come due now. Factoring is one way to turn those unpaid invoices into cash today.'),
        ('How factoring works',
         'A business sells its invoices to a factor, a finance company, at a discount. The factor usually pays an advance of most of the invoice value at once, often 70% to 90%. When the customer pays the invoice, the factor pays the rest, minus its fee.'),
        ('Recourse and non-recourse',
         'With recourse factoring, the business must buy back any invoice the customer never pays. With non-recourse factoring, the factor takes on the risk of non-payment, usually for a higher fee and only for certain kinds of customer failure. Read which one you are signing.'),
        ('Comparing the cost',
         'The fee is a percentage of each invoice, and it rises the longer the customer takes to pay. Add up the fee over a full year and compare it with the interest on a bank loan. Factoring can be dear, but it may still be cheaper than missing payroll or turning down orders.'),
        ('Old roots',
         'Trade finance by selling claims on goods is very old. Agents called factors handled sales and extended credit for merchants in Europe for centuries, and the modern business grew out of that trade. Today factoring is a common tool for small firms that sell to large companies.'),
        ('When it helps',
         'Factoring suits a business that grows fast, has slow-paying customers, and has real sales to show. It does not fix a business that sells at a loss, because the factor only turns good invoices into cash sooner. Ask what each sale really earns after the fee.'),
    ],
    "test": [
        ('What does a factor usually pay up front for an invoice?',
         [('a', 'Most of the invoice value, often 70% to 90%'), ('b', 'Nothing until the customer pays'), ('c', 'The full amount plus interest'), ('d', 'Exactly one tenth of the invoice')], 'a'),
        ('What does recourse factoring mean?',
         [('a', 'The factor never asks for money back'), ('b', 'The business must buy back invoices the customer never pays'), ('c', 'The customer chooses the factor'), ('d', 'The invoices are paid in gold')], 'b'),
        ('Why can factoring be a poor fix on its own?',
         [('a', 'It is only for banks'), ('b', 'It removes all fees'), ('c', 'It speeds up cash but cannot make a loss-making sale profitable'), ('d', 'It only works with cash customers')], 'c'),
        ('Which factor is the best comparison when judging the cost?',
         [('a', 'The colour of the invoice'), ('b', 'The number of staff at the factor'), ('c', 'The distance to the customer'), ('d', 'The fee over a full year, set beside a bank loan')], 'd'),
        ('Where do the roots of factoring lie?',
         [('a', 'In agents who handled sales and credit for merchants in Europe for centuries'), ('b', 'In modern online banking'), ('c', 'In the Starship library'), ('d', 'In Chicago grain pits')], 'a'),
    ],
}
