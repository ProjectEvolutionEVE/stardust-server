"""Byzantine Fault Tolerance: agreeing even when some machines lie or act against the group."""
CODE = 'computing5_byzantine_fault_tolerance'
BOOK = {
    "title": 'Byzantine Fault Tolerance',
    "subtitle": 'Agreeing even when some machines lie or act against the group',
    "chapters": [
        ('Machines that lie', 'Most failure models assume a broken machine simply stops. A Byzantine fault is worse: the machine may send wrong or conflicting messages, on purpose or because of a bug. The name comes from a 1982 paper by Lamport, Shostak and Pease, about generals who must agree while some of them may be traitors.'),
        ('The 3f+1 bound', 'To tolerate f faulty machines in a group, the group needs at least 3f+1 members in total. With one traitor, four machines are the minimum. The honest members must be more than twice the number of faulty ones, so they can always outvote them.'),
        ('PBFT', 'Practical Byzantine Fault Tolerance, or PBFT, was introduced by Miguel Castro and Barbara Liskov in 1999. It works in rounds with a leader, and the group checks each step with several rounds of messages, so that honest machines agree on one order of requests.'),
        ('Signatures', 'Digital signatures make a message author checkable, so a machine cannot pretend to be another. Signatures can reduce the number of checks needed, though they add computing cost. They are one tool among several.'),
        ('Permissioned consensus', 'In a permissioned system, the members are known and approved in advance. That makes Byzantine agreement practical, since the group size and identities are fixed. Open systems that let anyone join face a harder setting.'),
        ('The costs of tolerance', 'Tolerating liars costs more messages, more machines and more computing than tolerating simple crashes. Designers pay that price where the risk of a lying member is real, such as in money systems or critical controls.'),
    ],
    "test": [
        ('What is a Byzantine fault?',
         [('a', 'A machine that stops cleanly'), ('b', 'A machine that may send wrong or conflicting messages'), ('c', 'A machine that is painted'), ('d', 'A machine that sleeps')], 'b'),
        ('How many members are needed to tolerate one faulty machine?',
         [('a', '1'), ('b', '2'), ('c', '4'), ('d', '10')], 'c'),
        ('Who introduced PBFT in 1999?',
         [('a', 'Ada Lovelace'), ('b', 'Alan Turing'), ('c', 'Grace Hopper'), ('d', 'Miguel Castro and Barbara Liskov')], 'd'),
        ('What does a permissioned system have?',
         [('a', 'Known and approved members in advance'), ('b', 'Secret members'), ('c', 'No members'), ('d', 'Members chosen by a coin')], 'a'),
        ('What is a cost of tolerating liars?',
         [('a', 'Less computing'), ('b', 'No cost at all'), ('c', 'More messages, machines and computing'), ('d', 'A free lunch')], 'c'),
    ],
}
