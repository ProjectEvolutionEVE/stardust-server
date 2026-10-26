"""Race conditions: what goes wrong when two things change the same value at the same time, and how to stop it."""
CODE = 'computing3a_race_conditions'
BOOK = {
    "title": 'Race Conditions',
    "subtitle": 'When two things change the same value at once, and what can go wrong',
    "chapters": [
        ('Two things at once',
         'Concurrency means several things happening at the same time: two players, two requests, two background loops. A computer often works on parts of a job in turn, so two jobs may be partway through the same value together. This can cause mistakes that are hard to predict.'),
        ('The lost update',
         'Suppose two purchases of 80 credits each read a balance of 100 at the same moment. Each one checks that it can pay, and each writes back 20. Both goods are handed over, but only 80 credits have left the account. Goods have been given away for money that was never taken.'),
        ('Why it is hard to see',
         'A race condition may only show up now and then, when two events fall at just the right moment. A test run once may pass, and the bug waits for a busy day. Look for shared values early, before the game reaches players.'),
        ('Lock the row first',
         'One fix is to lock the row before reading it. The second purchase must then wait until the first one has finished, and when it reads the balance it sees the new, lower amount. Databases do this with a locking read, such as SELECT ... FOR UPDATE, inside a transaction. The game\'s tow fee code does this before it takes the fee.'),
        ('One step is safer',
         'When the database can change a number in one statement, such as taking 80 away from the balance, there is no gap for another change to slip into. The game\'s transfer code locks both accounts and then changes each balance with a single update.'),
        ('Finding them on purpose',
         'To find a race, run many copies of the same action at the same time, then check the totals afterwards. If the books do not balance, a race is the first suspect. The book on data integrity explains how totals are checked.'),
    ],
    "test": [
        ('What is a race condition?',
         [('a', 'A contest between two players'), ('b', 'A mistake that depends on the order in which two things happen at once'), ('c', 'A type of game level'), ('d', 'A fast sorting method')], 'b'),
        ('In the lost update example, what went wrong?',
         [('a', 'Both purchases read the same old balance, so one change was overwritten'), ('b', 'The balance was too large to store'), ('c', 'The computer ran out of memory'), ('d', 'The goods had no price')], 'a'),
        ('Why is a race condition hard to catch in testing?',
         [('a', 'It only shows up when events happen at just the right moment'), ('b', 'It always fails on the very first run'), ('c', 'Computers never run two things at once'), ('d', 'It only happens with negative numbers')], 'a'),
        ('What does a locking read such as SELECT ... FOR UPDATE do?',
         [('a', 'It deletes the old balance'), ('b', 'It prints the balance on the screen'), ('c', 'It updates the row for everyone at once'), ('d', 'It locks the row so other changes must wait until this one finishes')], 'd'),
        ('What is a good way to find race conditions?',
         [('a', 'Read the code once and trust it'), ('b', 'Turn off all the locks'), ('c', 'Test with only one player'), ('d', 'Run many copies of the same action at once and check the totals')], 'd'),
    ],
}
