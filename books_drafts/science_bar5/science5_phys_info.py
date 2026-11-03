"""Information, Entropy and Computation: Shannon entropy, Landauer's principle, reversible computing, the thermodynamic cost of a bit and limits of computation."""
CODE = 'science5_phys_info'
BOOK = {
    "title": 'Information, Entropy and Computation',
    "subtitle": 'Information is physical, and erasing it has a cost',
    "chapters": [
        ('Measuring surprise',
         'Claude Shannon showed that information can be measured. The Shannon entropy of a message is a measure of how unpredictable its symbols are. A message that is always the same carries no new information.'),
        ('Information is physical',
         'Information must be stored in a physical thing, such as a switch, a magnet or a molecule. Because of this, the laws of physics apply to information too. Storing and erasing it has real energy and heat consequences.'),
        ("Landauer's principle",
         "Rolf Landauer showed that erasing one bit of information must release at least a small amount of heat, about k times T times the natural log of 2. Here k is Boltzmann's constant and T is the temperature. This is the thermodynamic cost of a bit."),
        ('Reversible computing',
         'A computation that never erases information can, in principle, avoid this minimum heat. Reversible logic gates keep every input recoverable from the output. Such designs are studied for future low-energy computers.'),
        ('The cost of a bit',
         "At room temperature, the Landauer limit is tiny, far below the energy used by today's chips. Real computers still waste far more energy than the limit, mostly through wires, switching and heat losses."),
        ('Limits of computation',
         'Physics sets hard limits on computation. The speed, size and energy of any computer are bounded by the laws of physics. These limits guide thinking about how far computing can go, even in principle.'),
    ],
    "test": [
        ('What does Shannon entropy measure?',
         [('a', 'How heavy a message is'), ('b', 'How long a letter takes to write'), ('c', 'How unpredictable the symbols in a message are'), ('d', 'How many colours a page has')], 'c'),
        ('Why is information physical?',
         [('a', 'It is always stored in clouds'), ('b', 'It only exists in books'), ('c', 'It must be stored in a physical thing such as a switch or magnet'), ('d', 'It has no link to matter')], 'c'),
        ("What does Landauer's principle say about erasing a bit?",
         [('a', 'It always makes the room colder'), ('b', 'It costs nothing at all'), ('c', 'It makes the bit heavier'), ('d', 'It must release at least a small amount of heat')], 'd'),
        ('What is reversible computing?',
         [('a', 'Computing that runs backwards in time'), ('b', 'Computation that never erases information, so inputs can be recovered'), ('c', 'Computing with no electricity'), ('d', 'Computing that never ends')], 'b'),
        ('Why do real computers use far more energy than the Landauer limit?',
         [('a', 'Wires, switching and heat losses waste much more energy'), ('b', 'The limit is larger than the chip'), ('c', 'Computers do not use any energy'), ('d', 'Computers only run in the dark')], 'a'),
    ],
}
