"""Bills of Exchange: an order to pay, acceptance, discounting, the merchant banks, the London bill market and its legacy."""
CODE = 'business5_billsofexchange'
BOOK = {
    "title": 'Bills of Exchange',
    "subtitle": 'An order to pay later, and the market that traded it',
    "chapters": [
        ('An order to pay',
         'A bill of exchange is a written order from one party, the drawer, telling another, the drawee, to pay a fixed sum to a third party, the payee, on a set date. It let merchants move money over distance without carrying coins. It is one of the oldest tools of trade finance.'),
        ('Acceptance',
         'When the drawee writes an acceptance on the bill, it promises to pay. An accepted bill is much easier to sell, because the promise now comes from a party with a name to protect. Acceptance is what gave the bill its value as a trading asset.'),
        ('Discounting',
         'The holder of an accepted bill can sell it before its due date, at a discount. The buyer pays less today and collects the full sum at maturity. The gap is the return, which depends on how far away the due date is and how safe the name is.'),
        ('The merchant banks',
         "In the nineteenth century, London merchant banks, often called accepting houses, put their names on bills for trading firms. Their name made the bill easy to sell around the world. The bills market was a large part of London's money business for a long time."),
        ('The London bill market',
         'London became the centre of the bill market, where discount houses bought and held bills and the Bank of England would lend against good ones. The market was a steady source of short-term credit for trade and for industry. It declined in the late twentieth century as other forms of short-term borrowing grew.'),
        ('The legacy',
         'The Bills of Exchange Act of 1882 in the United Kingdom set out the rules for these instruments, and many of its ideas live on in modern law. Bills are one reason why trust in a name still matters in finance. Today the same ideas show up in cheques and commercial paper.'),
    ],
    "test": [
        ('What is a bill of exchange?',
         [('a', 'A ticket to a concert'), ('b', 'A coin of gold'), ('c', 'A written order to pay a fixed sum on a set date'), ('d', 'A map of trade routes')], 'c'),
        ('What does acceptance add to a bill?',
         [('a', 'A change of date'), ('b', 'A guarantee that the goods are sound'), ('c', 'Nothing; it is only a signature'), ('d', 'A promise to pay by the drawee')], 'd'),
        ('What is discounting?',
         [('a', 'Selling a bill before its due date for less than its full sum'), ('b', 'Adding a tax to a bill'), ('c', 'Paying a bill early for a prize'), ('d', 'Printing a bill on cheaper paper')], 'a'),
        ('What role did merchant banks play?',
         [('a', 'They printed the bills in gold'), ('b', 'They lent their name to bills so they were easy to sell'), ('c', 'They forbade trade'), ('d', 'They owned all the ships')], 'b'),
        ('What law set out rules for these instruments in the United Kingdom?',
         [('a', 'The Navigation Act of 1651'), ('b', 'The Federal Reserve Act'), ('c', 'The Bills of Exchange Act of 1882'), ('d', 'The Factory Act of 1833')], 'c'),
    ],
}
