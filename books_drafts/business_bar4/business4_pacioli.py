"""Pacioli and Double-Entry Bookkeeping: Venice in 1494, the Summa, debits and credits, the trial balance, why it spread, and its place today."""
CODE = 'business4_pacioli'
BOOK = {
    "title": 'Pacioli and Double-Entry Bookkeeping',
    "subtitle": 'The method that records every money move twice, and still underpins accounts today',
    "chapters": [
        ('Venice in 1494',
         'In 1494 the Franciscan friar Luca Pacioli published a large mathematics book in Venice, the Summa de arithmetica. A section of it described how merchants should keep their accounts. Venice was then a centre of trade, and its traders needed clear records.'),
        ('The Summa',
         "Pacioli's account of bookkeeping was not invented by him, but he set it out in print in a clear form. He described journals, ledgers and the balancing of accounts. His work became one of the first widely read guides to the method."),
        ('Debits and credits',
         'In double-entry bookkeeping, each transaction is recorded twice: once as a debit and once as a credit, with equal totals on each side. If a firm buys a machine for cash, the asset rises and the cash falls by the same amount. Every entry has a matching entry.'),
        ('The trial balance',
         'A trial balance lists all the account balances at a point in time and checks that debits equal credits. If they do not, an error has been made somewhere. The check does not catch every mistake, but it catches many of them quickly.'),
        ('Why it spread',
         'Double entry made it easier to spot errors and fraud, to show the owner the state of the business, and to share records between partners. Its rules travelled with merchants and clerks across Europe and beyond, and later into companies of every size.'),
        ('Its place today',
         'Modern accounting software still records double entry behind the scenes. Every bank transfer, sale and wage payment is posted to at least two accounts. The method is old, but it remains the foundation for the financial statements used today.'),
    ],
    "test": [
        ('In what year did Luca Pacioli publish the Summa in Venice?',
         [('a', '1394'), ('b', '1494'), ('c', '1594'), ('d', '1694')], 'b'),
        ('What does double-entry bookkeeping mean?',
         [('a', 'Each account is kept in two currencies'), ('b', 'Each sale is counted twice for tax'), ('c', 'Each transaction is recorded twice, as a debit and a credit'), ('d', 'Each week has two audits')], 'c'),
        ('What is a trial balance?',
         [('a', 'A court case about money'), ('b', 'A test of a new product'), ('c', 'A bank loan agreement'), ('d', 'A list of account balances that checks debits equal credits')], 'd'),
        ('What is the purpose of the balance check?',
         [('a', 'To spot many errors quickly, though not every error'), ('b', 'To guarantee a profit'), ('c', 'To replace the owner'), ('d', 'To set the price of stock')], 'a'),
        ('Why did double-entry bookkeeping spread?',
         [('a', 'It removed the need for any records'), ('b', 'It made errors and fraud easier to spot'), ('c', 'It was required only in one town'), ('d', 'It made money worthless')], 'b'),
    ],
}
