"""Working Capital in a Mining Business: the cash tied up in stock, spares and unpaid bills, and how to keep enough on hand."""
CODE = 'mining4_working_capital'
BOOK = {
    "title": 'Working Capital in a Mining Business',
    "subtitle": 'Cash tied up in stock and bills, and keeping enough on hand',
    "chapters": [
        ('Stock of ore and spares',
         'A mine holds stock: ore waiting to be processed, and spare parts for the machines. This stock is money that has been spent and is not yet earning. Too much stock ties up cash.'),
        ('Receivables and payables',
         'Receivables are the sums customers owe the mine. Payables are the sums the mine owes suppliers and staff. The gap between the two decides how much cash the business needs.'),
        ('The cash cycle',
         'The cash cycle is the time from paying for ore and labour to receiving payment for the metal. A longer cycle needs more working capital to bridge the gap.'),
        ('Credit lines',
         'A credit line is a bank facility the business can draw on when cash runs short. It covers the gap between paying out and being paid, but it must be repaid with interest.'),
        ('Seasonal swings',
         'Many mines face wet and dry seasons that change output and costs. Cash needs rise and fall through the year, so the plan must cover the lean months.'),
        ('Keeping enough cash',
         'A business that runs out of cash can stop even when it is profitable on paper. Keeping a cash reserve and a credit line in place protects the business through a slow patch.'),
    ],
    "test": [
        ('What is working capital tied up in?',
         [('a', 'The office paint'), ('b', "The mine's history books"), ('c', 'Stock of ore and spares that has not yet been turned into cash'), ('d', 'The weather forecast')], 'c'),
        ('What are receivables?',
         [('a', 'Sums that customers owe the mine'), ('b', 'Sums the mine owes suppliers'), ('c', 'The price of a drill'), ('d', 'Staff holidays')], 'a'),
        ('What is the cash cycle?',
         [('a', 'The rotation of a drill bit'), ('b', 'The weekly bus route'), ('c', 'The loop of a river'), ('d', 'The time from paying for ore and labour to being paid for the metal')], 'd'),
        ('What does a credit line do?',
         [('a', 'Gives free cash for ever'), ('b', 'Covers a cash gap, to be repaid with interest'), ('c', 'Sells the mine'), ('d', 'Replaces the staff')], 'b'),
        ('Why can a profitable business still run out of cash?',
         [('a', 'Profit is always paid in gold bars'), ('b', 'Profit is banned by law'), ('c', 'Profit on paper does not always mean cash in the bank when it is needed'), ('d', 'Profit never has to be counted')], 'c'),
    ],
}
