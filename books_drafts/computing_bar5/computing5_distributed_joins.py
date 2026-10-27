"""Distributed joins: broadcast and hash joins, shuffles, data skew, network costs and planning."""
CODE = 'computing5_distributed_joins'
BOOK = {
    "title": 'Distributed Joins and Shuffles',
    "subtitle": 'Moving data between computers so that matching rows meet',
    "chapters": [
        ('Data on many machines',
         'A large table is often split across many computers. A join needs matching rows to meet, so data has to move across the network.'),
        ('Broadcast join',
         'If one table is small, the system can copy the whole small table to every machine. Each machine then joins its local part of the big table with the copy, with little movement of the big table.'),
        ('Hash join and shuffle',
         'When both tables are large, the system uses a hash of the join key to send matching rows to the same machine. This movement of rows is called a shuffle.'),
        ('Skew',
         'If one key appears in many rows, one machine may receive far more work than the rest. That machine finishes late and slows the whole query.'),
        ('The network cost',
         'Moving data across the network is often slower than the work of joining it. Planners try to move as little data as possible.'),
        ('Planning',
         'A planner uses statistics about table sizes to choose the method. A wrong size estimate can lead to a costly shuffle where a broadcast would have been cheap.'),
    ],
    "test": [
        ('What does a broadcast join copy?',
         [('a', 'The big table to every machine'), ('b', 'The small table to every machine'), ('c', "The user's password"), ('d', 'The index of the printer')], 'b'),
        ('What is a shuffle?',
         [('a', 'A card game'), ('b', 'A backup method'), ('c', 'Random deletion'), ('d', 'Sending rows to machines based on the join key')], 'd'),
        ('What is data skew?',
         [('a', 'A tilted screen'), ('b', 'A missing network cable'), ('c', 'One key holding far more rows than others'), ('d', 'A type of backup')], 'c'),
        ('What usually costs the most in a distributed join?',
         [('a', 'Moving data across the network'), ('b', 'The colour of the output'), ('c', 'Reading the user manual'), ('d', 'Drawing the chart')], 'a'),
        ('Why does a planner need size estimates?',
         [('a', 'To print invoices'), ('b', 'To pick the cheapest method'), ('c', 'To name the tables'), ('d', 'To stop backups')], 'b'),
    ],
}
