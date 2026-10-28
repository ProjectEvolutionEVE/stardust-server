"""Linearizability: operations that look instant, and a history that matches a single order."""
CODE = 'computing5_linearizability'
BOOK = {
    "title": 'Linearizability',
    "subtitle": 'Operations that look instant, and a history that matches a single order',
    "chapters": [
        ('Looking instant', 'A system is linearizable if each operation appears to take effect at one instant between its start and its end. Anyone who reads the system sees a single, clear order of changes, as if there were only one copy of the data.'),
        ('Real-time order', 'If one operation finishes before another starts, the first must appear before the second. Linearizability respects this real-time order. It is the strongest common guarantee for a single data item.'),
        ('History checkers', 'A history is a record of the operations and their results. A checker tests whether the history could have happened in some order that respects real time. Tools such as Jepsen have used checks like this to find lost updates in real databases.'),
        ('Analysing histories', 'Checking a history is hard, because the number of possible orders grows very fast. Good tools use search and rules to prune the choices. A failed check shows a real problem, but a passed check only shows the history was possible.'),
        ('The cost of linearizable reads', 'To make reads always current, a system may need to ask a quorum or a leader, which takes time across machines. This cost is one reason some systems offer weaker reads. The choice is a trade-off between freshness and speed.'),
        ('Examples', 'A single lock service, or a counter that every user sees, is a typical case. Linearizability is what makes such shared objects feel like one reliable thing. Herlihy and Wing defined the idea in 1990.'),
    ],
    "test": [
        ('What does a linearizable operation appear to do?',
         [('a', 'Take effect at one instant between its start and end'), ('b', 'Take a week'), ('c', 'Happen twice'), ('d', 'Never happen')], 'a'),
        ('What order does linearizability respect?',
         [('a', 'Alphabetical order'), ('b', 'Colour order'), ('c', 'Real-time order'), ('d', 'Random order')], 'c'),
        ('What is a history in this context?',
         [('a', 'A record of operations and their results'), ('b', 'A school subject'), ('c', 'A lunch menu'), ('d', 'A type of cable')], 'a'),
        ('Who defined linearizability in 1990?',
         [('a', 'Herlihy and Wing'), ('b', 'Ada and Alan'), ('c', 'Grace and Linus'), ('d', 'Niklaus and Edsger')], 'a'),
        ('Why can linearizable reads be costly?',
         [('a', 'They print everything'), ('b', 'They may need to ask a quorum or a leader across machines'), ('c', 'They remove the clock'), ('d', 'They need no network')], 'b'),
    ],
}
