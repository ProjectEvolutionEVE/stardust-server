"""Data integrity and audits: making sure every credit is accounted for, and checking the books."""
CODE = 'computing3a_data_integrity'
BOOK = {
    "title": 'Data Integrity and Audits',
    "subtitle": 'Making sure every credit is accounted for, and checking the books',
    "chapters": [
        ('Right data, every time',
         'Data integrity means the data is correct and stays correct, with nothing lost, duplicated or changed by accident. Money and goods need the strictest care, because one slip creates or destroys value that someone will notice.'),
        ('Double-entry books',
         'Accountants have kept double-entry books for hundreds of years. Every amount that leaves one account enters another, so the total across all accounts never changes. The game\'s credit ledger works the same way: each transfer takes credits from one account, puts them in another, and writes a row in the paper trail.'),
        ('The total must be zero',
         'When credits only move between accounts, the sum over every account is always zero. The mint, which issues new credits, is negative by exactly the amount it has issued. If the total is not zero, something was created or lost, and the audit reports it.'),
        ('The paper trail must match',
         'Each account\'s balance should match the sum of its incoming and outgoing rows in the paper trail. If it does not, the balance was changed without a record, which is a serious warning sign.'),
        ('Money set aside',
         'When a bid is open, its credits are set aside, and the set-aside amount should equal what the open bids need. The audit checks this too, so no credit is counted twice, and goods set aside for open sales are checked the same way.'),
        ('Running an audit',
         'An audit is a check run on a schedule or after changes, and it lists every problem it finds. An empty list means the books balance. A test run can call the audit after its actions, so a bug that breaks the books is caught at once.'),
    ],
    "test": [
        ('What is data integrity?',
         [('a', 'Data that is correct and stays correct, with nothing lost or changed by accident'), ('b', 'Data stored in the largest file'), ('c', 'Data that is always encrypted'), ('d', 'Data that nobody can read')], 'a'),
        ('In double-entry books, what happens to an amount that leaves one account?',
         [('a', 'It enters another account, so the total never changes'), ('b', 'It disappears'), ('c', 'It is doubled'), ('d', 'It is hidden from the paper trail')], 'a'),
        ('When credits only move between accounts, what should the total over all accounts be?',
         [('a', 'One million'), ('b', 'Zero, once the mint\'s negative balance is counted'), ('c', 'The size of the largest account'), ('d', 'The number of players')], 'b'),
        ('What does it mean when an audit finds a balance that does not match its paper trail?',
         [('a', 'The player must be very rich'), ('b', 'The screen needs a reset'), ('c', 'The paper trail has too many rows'), ('d', 'The balance was changed without a matching record, a serious warning sign')], 'd'),
        ('Why does an audit check the credits set aside for open bids?',
         [('a', 'So the same credits are not counted twice'), ('b', 'Because bids are always free'), ('c', 'To speed up the screen'), ('d', 'Because bids can never be cancelled')], 'a'),
    ],
}
