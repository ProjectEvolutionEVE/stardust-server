"""Quorum Systems: choosing groups of machines so every read sees the latest write."""
CODE = 'computing5_quorum_systems'
BOOK = {
    "title": 'Quorum Systems',
    "subtitle": 'Choosing groups of machines so every read sees the latest write',
    "chapters": [
        ('Read and write groups', 'A quorum system names groups of machines for reads and for writes. A write is confirmed once enough members of its write group store it, and a read asks enough members of its read group to find the latest value.'),
        ('The intersection property', 'The key rule is intersection: every read group must share at least one machine with every write group. That shared member holds the latest write, so the read can find it. Without intersection, reads could miss new data.'),
        ('Grid and majority systems', 'In a majority system, any group of more than half the machines is a quorum, so any two quorums overlap. A grid arranges machines in rows and columns, with a quorum taking a full row and a full column. Grids can give smaller groups for each operation.'),
        ('Load and availability', 'Load is how much work each machine carries, and availability is the chance a quorum can still be reached when machines fail. Different systems trade these two. A design that suits a busy service may not suit a rarely used one.'),
        ('Sloppy quorums', 'A sloppy quorum lets a write go to machines outside the usual group when the proper ones cannot be reached. This keeps the system writable during faults. It weakens the intersection promise, so reads must be handled with care.'),
        ('Trade-offs', 'Quorum choices balance speed, safety and resilience. Larger quorums give stronger guarantees but are slower and more fragile. Systems in the style of Amazon Dynamo let teams set these sizes to suit their needs.'),
    ],
    "test": [
        ('What does a quorum system name?',
         [('a', 'Groups of friends'), ('b', 'Groups of machines for reads and writes'), ('c', 'Groups of songs'), ('d', 'Groups of colours')], 'b'),
        ('What must every read group share with every write group?',
         [('a', 'Nothing'), ('b', 'A sound'), ('c', 'At least one machine'), ('d', 'A date')], 'c'),
        ('In a majority system, what counts as a quorum?',
         [('a', 'Any group of more than half the machines'), ('b', 'Any group of one machine'), ('c', 'Only the first machine'), ('d', 'None')], 'a'),
        ('What is load?',
         [('a', 'A kind of loan'), ('b', 'A type of ship'), ('c', 'The weight of a box'), ('d', 'How much work each machine carries')], 'd'),
        ('What does a sloppy quorum do?',
         [('a', 'Lets a write go to machines outside the usual group when needed'), ('b', 'Removes all machines'), ('c', 'Stops every read'), ('d', 'Prints the group list')], 'a'),
    ],
}
