"""Locks and deadlocks: how a lock keeps a change safe, and how two jobs can end up waiting on each other forever."""
CODE = 'computing3a_deadlocks'
BOOK = {
    "title": 'Locks and Deadlocks',
    "subtitle": 'How locks keep changes safe, and how two jobs can wait on each other forever',
    "chapters": [
        ('A lock is a claim',
         'A lock says: I am changing this now, so wait your turn. Locks stop two changes from mixing, but they also make other jobs wait. Keep each lock for a short time, so the waiting stays short too.'),
        ('Waiting for each other',
         'A deadlock happens when job A holds lock 1 and waits for lock 2, while job B holds lock 2 and waits for lock 1. Neither can move, and neither lets go. Nothing crashes, but nothing finishes either.'),
        ('The four conditions',
         'A deadlock needs four things at once: exclusive use of a resource, holding one lock while waiting for another, no way to take a lock away from its holder, and a circle of waiting. Breaking any one of these stops the deadlock. Most practical fixes break the circle.'),
        ('Lock in the same order',
         'The simplest fix is to agree on an order. If every job takes its locks in the same sorted order, a circle cannot form. The game\'s money transfer does this: it locks the two accounts in order of their numbers, so two transfers between the same accounts cannot wait on each other.'),
        ('Timeouts and retries',
         'Another approach is to give up after a set wait. A job that cannot get its second lock in time lets go of the first, waits a moment and tries again. A small random wait before retrying helps stop the two jobs from colliding again and again.'),
        ('Spotting one',
         'A program that hangs with no error is a common sign of a deadlock. Logs that show which lock each job holds and which one it wants next help find the circle. Keep the number of locks small, and keep the time each one is held short.'),
    ],
    "test": [
        ('What is a lock for?',
         [('a', 'To make a job wait its turn while it changes shared data'), ('b', 'To make files smaller'), ('c', 'To speed up the screen'), ('d', 'To hide a password')], 'a'),
        ('What is a deadlock?',
         [('a', 'A lock that is too heavy to carry'), ('b', 'A program that runs too fast'), ('c', 'A password that never expires'), ('d', 'Two jobs that each hold a lock the other needs, and wait forever')], 'd'),
        ('Which simple rule prevents the circle of waiting?',
         [('a', 'Every job takes its locks at random'), ('b', 'Every job holds one lock forever'), ('c', 'Every job takes its locks in the same agreed order'), ('d', 'Locks are never used at all')], 'c'),
        ('Why does the money transfer lock its two accounts in order of their numbers?',
         [('a', 'So the accounts are sorted from largest to smallest'), ('b', 'Because the numbers are needed for the receipt'), ('c', 'To make the transfer faster by skipping one lock'), ('d', 'So two transfers between the same accounts take their locks in the same order and cannot deadlock')], 'd'),
        ('A program hangs and shows no error. What is a good thing to look at first?',
         [('a', 'The colour of the screen'), ('b', 'The length of the job name'), ('c', 'Logs that show which lock each job holds and wants next'), ('d', 'The size of the font')], 'c'),
    ],
}
