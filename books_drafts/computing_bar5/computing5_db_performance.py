"""Database performance at scale: measuring first, query regressions, index bloat, lock contention, partitioning and hardware sizing."""
CODE = 'computing5_db_performance'
BOOK = {
    "title": 'Database Performance at Scale',
    "subtitle": 'Finding slow queries, fixing them, and sizing hardware with evidence',
    "chapters": [
        ('Measure first',
         'Before changing anything, teams measure where the time goes. A slow-query log and plan tools such as EXPLAIN ANALYZE show the real cost of each step.'),
        ('Query regressions',
         'A query can suddenly slow down after a new plan, a data change or an update. Keeping past plans and timings helps spot the change.'),
        ('Index bloat',
         'Indexes can grow with old, unused space after many updates. Rebuilding them can recover speed, but it needs planning.'),
        ('Lock contention',
         'When many transactions fight for the same rows, they wait for each other. Shorter transactions and a consistent order for updates reduce the waiting.'),
        ('Partitioning',
         'Splitting a large table by range, such as by month, lets queries read only the parts they need. Old partitions can be dropped quickly.'),
        ('Hardware sizing',
         'More memory, faster disks or more processors help only if the bottleneck is there. Teams confirm the bottleneck before buying hardware.'),
    ],
    "test": [
        ('What does EXPLAIN ANALYZE show?',
         [('a', 'The real cost of each step of a query'), ('b', 'The price of the server'), ('c', 'The weather report'), ('d', 'The staff list')], 'a'),
        ('Why keep past query plans?',
         [('a', 'To delete tables'), ('b', "To change the user's name"), ('c', 'To spot when a query slows down after a change'), ('d', 'To print them on posters')], 'c'),
        ('What is index bloat?',
         [('a', 'A very fast index'), ('b', 'A missing table'), ('c', 'A printer error'), ('d', 'Indexes with old unused space after many updates')], 'd'),
        ('What do shorter transactions help reduce?',
         [('a', 'Waiting on locks'), ('b', 'The number of users'), ('c', 'The brightness'), ('d', 'The price of storage')], 'a'),
        ('Why check the bottleneck before buying hardware?',
         [('a', 'Hardware is always useless'), ('b', 'Extra hardware only helps if it is the bottleneck'), ('c', 'Hardware must be bought every day'), ('d', 'Hardware costs nothing')], 'b'),
    ],
}
