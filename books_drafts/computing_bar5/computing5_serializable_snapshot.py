"""Serializable snapshot isolation: serializability, snapshots, write skew, dangerous structures and the PostgreSQL implementation."""
CODE = 'computing5_serializable_snapshot'
BOOK = {
    "title": 'Serializable Snapshot Isolation',
    "subtitle": 'Fully safe transactions without locking everything up',
    "chapters": [
        ('Why transactions need care',
         'When many people change a database at once, the results must make sense as if each transaction ran alone. That property is called serializability.'),
        ('Snapshots',
         'Snapshot isolation lets each transaction read a consistent copy of the data from the moment it began. Readers do not block writers, which keeps things fast.'),
        ('The anomaly',
         'Snapshot isolation alone can allow a problem called write skew, where two transactions each check a rule and then both break it. Each one sees a valid picture, but together the result is wrong.'),
        ('Dangerous structures',
         'Serializable snapshot isolation watches for a specific pattern of overlapping reads and writes, called a dangerous structure. When one shows up, the system stops one of the transactions.'),
        ('PostgreSQL',
         'PostgreSQL added serializable snapshot isolation in version 9.1, using light predicate locks that record what was read without blocking others. The application must retry any transaction that is aborted.'),
        ('Performance',
         'Most workloads see little slowdown, but some aborts happen and must be retried. Good design keeps transactions short and clear.'),
    ],
    "test": [
        ('What does serializability promise?',
         [('a', 'Transactions behave as if run one after another'), ('b', 'Every query is faster'), ('c', 'Passwords are longer'), ('d', 'Backups happen every minute')], 'a'),
        ('What does a snapshot give a transaction?',
         [('a', 'A photo of the screen'), ('b', 'A new table'), ('c', 'A consistent view of the data from when it began'), ('d', 'A printed report')], 'c'),
        ('What is write skew?',
         [('a', 'A slanted table'), ('b', 'A disk that is too full'), ('c', 'A slow printer'), ('d', 'Two transactions each check a rule, then both break it')], 'd'),
        ('What does SSI do when it sees a dangerous structure?',
         [('a', 'It ignores it'), ('b', 'It stops one of the transactions'), ('c', 'It prints the result'), ('d', 'It deletes the table')], 'b'),
        ('What must an application do when a transaction is aborted?',
         [('a', 'Ignore the user'), ('b', 'Change the password'), ('c', 'Retry it'), ('d', 'Delete the database')], 'c'),
    ],
}
