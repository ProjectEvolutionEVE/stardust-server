"""Consensus Numbers and the Wait-Free Hierarchy: which building blocks can solve agreement, and which cannot."""
CODE = 'computing5_consensus_numbers'
BOOK = {
    "title": 'Consensus Numbers and the Wait-Free Hierarchy',
    "subtitle": 'Which building blocks can solve agreement, and which cannot',
    "chapters": [
        ('Building blocks of concurrency', 'Processes that share memory need building blocks, such as reads, writes and special atomic operations. Some blocks are strong enough to let processes agree on a value in a wait-free way, and some are not.'),
        ('Consensus numbers', 'A primitive consensus number is the largest number of processes for which it can solve consensus. Reads and writes on plain registers have consensus number one. Maurice Herlihy introduced this idea, and the hierarchy built on it, in 1991.'),
        ('Compare-and-swap', 'Compare-and-swap checks a value and sets it in one atomic step. Its consensus number is infinite, so it can solve consensus for any number of processes. That is why it sits at the top of the hierarchy and is widely used.'),
        ('Test-and-set', 'Test-and-set has consensus number two. It can solve agreement between two processes, but not among three or more with this one primitive. The hierarchy shows why some tools are stronger than others.'),
        ('Wait-freedom', 'Wait-freedom means every process finishes its operation in a bounded number of its own steps, whatever the others do. It is a strong promise, and it is what the hierarchy measures. Weaker progress rules are easier to achieve.'),
        ('Universal objects and implications', 'An object with infinite consensus number is universal: it can be used to build any other wait-free object. This has practical implications for choosing hardware instructions and for designing concurrent libraries.'),
    ],
    "test": [
        ('What is a consensus number?',
         [('a', 'A phone number'), ('b', 'The count of pages'), ('c', 'A price'), ('d', 'The largest number of processes a primitive can solve consensus for')], 'd'),
        ('What is the consensus number of plain reads and writes?',
         [('a', 'Two'), ('b', 'Infinite'), ('c', 'Zero'), ('d', 'One')], 'd'),
        ('Which primitive has infinite consensus number?',
         [('a', 'Paper'), ('b', 'Pencil'), ('c', 'Compare-and-swap'), ('d', 'Glue')], 'c'),
        ('What is the consensus number of test-and-set?',
         [('a', 'Two'), ('b', 'Five'), ('c', 'Ten'), ('d', 'One hundred')], 'a'),
        ('What does wait-freedom promise?',
         [('a', 'Every process finishes in a bounded number of its own steps'), ('b', 'Processes never start'), ('c', 'Processes always wait forever'), ('d', 'No steps at all')], 'a'),
    ],
}
