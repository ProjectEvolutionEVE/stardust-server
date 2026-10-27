"""Multi-Paxos and Flexible Paxos: a running log of agreed decisions, with quorums that can be tuned."""
CODE = 'computing5_multi_paxos'
BOOK = {
    "title": 'Multi-Paxos and Flexible Paxos',
    "subtitle": 'A running log of agreed decisions, and quorums that can be tuned',
    "chapters": [
        ('A log of decisions', 'Paxos decides one value at a time. Multi-Paxos runs the same process again and again, so the group builds an ordered log of decisions, such as the sequence of updates to a database. Every copy of the log ends up the same.'),
        ('Leader stability', 'Multi-Paxos usually keeps one leader, who proposes new entries without repeating the full process each time. Keeping the same leader for a long time makes the system fast. When the leader fails, a new election takes place.'),
        ('Quorum intersection', 'A quorum is a set of members large enough to make a decision. In classic Paxos, any two quorums share at least one member. That shared member carries the earlier decision forward, which keeps the group consistent.'),
        ('Flexible quorums', 'Flexible Paxos, shown by Heidi Howard and her co-authors in 2016, notes that only the quorums for choosing a leader and for adding entries must overlap. The two sizes can be set differently, so a system can favour reads or writes by trading one against the other.'),
        ('Reconfiguration', 'Real groups change over time, as machines are added or removed. Reconfiguration is the process of changing membership safely, so that the old and new groups never make conflicting decisions. It is one of the harder parts of the protocol.'),
        ('Comparison with Raft', 'Raft was designed in 2014 to be easier to understand than Multi-Paxos, with a clear leader and simple log rules. Both reach the same kind of agreement. Teams often choose Raft for clarity and Paxos variants for their flexibility.'),
    ],
    "test": [
        ('What does Multi-Paxos build?',
         [('a', 'An ordered log of decisions'), ('b', 'A song'), ('c', 'A map of stars'), ('d', 'A chess board')], 'a'),
        ('What does a leader do in Multi-Paxos?',
         [('a', 'Paints the servers'), ('b', 'Proposes new entries without repeating the full process each time'), ('c', 'Sleeps'), ('d', 'Deletes the log')], 'b'),
        ('What must any two classic Paxos quorums share?',
         [('a', 'At least one member'), ('b', 'Nothing'), ('c', 'A colour'), ('d', 'A password')], 'a'),
        ('What does Flexible Paxos change?',
         [('a', 'Only the leader and entry quorums must overlap, and their sizes can differ'), ('b', 'Nothing about quorums'), ('c', 'The colour of the log'), ('d', 'The number of machines in the world')], 'a'),
        ('When was Raft designed?',
         [('a', '1066'), ('b', '1492'), ('c', '2014'), ('d', '1800')], 'c'),
    ],
}
