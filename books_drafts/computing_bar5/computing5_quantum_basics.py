"""Quantum Computing Basics: qubits, superposition, measurement, entanglement and the speedups they make possible."""
CODE = 'computing5_quantum_basics'
BOOK = {'title': 'Quantum Computing Basics',
 'subtitle': 'Qubits, superposition and what they can and cannot do',
 'chapters': [('Qubits',
               'A classical bit is either 0 or 1. A qubit is a quantum system that can be prepared in a combination of 0 and 1 at once. Its state is described by two amplitudes, '
               'and both must be tracked.'),
              ('Superposition',
               'Superposition is the ability of a qubit to hold a combination of basis states. It is not a secret answer waiting to be read. A quantum algorithm uses interference '
               'between amplitudes to make the right answers stand out.'),
              ('Measurement',
               'Measuring a qubit gives 0 or 1, with probabilities set by its amplitudes, and the measurement changes the state. You cannot read all the amplitudes from one run. '
               'Quantum programs are designed around this limit.'),
              ('Entanglement',
               'Entangled qubits share a joint state that cannot be split into separate states for each qubit. Measuring one affects the statistics of the other. Entanglement is '
               'a resource in many quantum protocols.'),
              ('Gates and speedups',
               "Quantum gates are reversible operations on qubits. Shor's algorithm factors large numbers in polynomial time on a suitable quantum computer. Grover's algorithm "
               'searches an unsorted list of n items in about the square root of n steps.'),
              ('What quantum machines cannot do',
               'Quantum computers do not try every answer at once in a way that makes all problems fast. They are not expected to solve NP-hard problems in polynomial time. '
               'Practical machines are also fragile and need careful error correction.')],
 'test': [('How many basis states can a classical bit hold at one time?', [('a', 'Two, at once in a combination'), ('b', 'One'), ('c', 'Zero'), ('d', 'A million')], 'b'),
          ('What does measuring a qubit give you?',
           [('a', 'A full copy of all the amplitudes'),
            ('b', 'A picture of the circuit'),
            ('c', 'The time of day'),
            ('d', 'A value of 0 or 1 with probabilities set by its state')],
           'd'),
          ('What is entanglement?',
           [('a', 'A broken cable'), ('b', 'A kind of password'), ('c', 'A shared joint state that cannot be split into separate qubit states'), ('d', 'A slow printer')],
           'c'),
          ('Which algorithm factors large numbers on a suitable quantum computer?',
           [('a', "Shor's algorithm"), ('b', 'Bubble sort'), ('c', 'Breadth-first search'), ('d', 'Huffman coding')],
           'a'),
          ('What should you not expect quantum computers to do?',
           [('a', 'Use qubits'), ('b', 'Run gates'), ('c', 'Measure a state'), ('d', 'Solve every NP-hard problem in polynomial time')],
           'd')]}
