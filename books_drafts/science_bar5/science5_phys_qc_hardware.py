"""Quantum Computing Hardware: qubit platforms, superconducting and trapped-ion qubits, error rates, error correction basics, coherence times and scaling challenges."""
CODE = 'science5_phys_qc_hardware'
BOOK = {
    "title": 'Quantum Computing Hardware',
    "subtitle": 'Building qubits that hold their quantum states long enough to compute',
    "chapters": [
        ('What a qubit is',
         'A qubit is the quantum version of a bit. It can hold a mix of 0 and 1 at once, described by a quantum state. Many physical systems can serve as qubits, and each has its own strengths and weaknesses.'),
        ('Superconducting qubits',
         'Superconducting qubits are tiny electrical circuits cooled to very low temperatures. They are controlled with microwave pulses and can be made with chip-making methods. Their gates are fast, but they must be kept extremely cold.'),
        ('Trapped-ion qubits',
         'Trapped-ion qubits store information in the states of single charged atoms held in electric fields. They have long coherence times and very accurate gates. They tend to run more slowly than superconducting qubits.'),
        ('Error rates',
         'Every gate in a real quantum computer has a chance of error. Error rates must be very low before large calculations can succeed. Engineers measure these rates carefully and try to lower them with better control.'),
        ('Error correction',
         'Quantum error correction spreads one logical qubit across many physical qubits. Errors can be detected and fixed without reading the stored information directly. This needs many physical qubits for each useful logical one.'),
        ('Coherence and scaling',
         'Coherence time is how long a qubit keeps its quantum state. Scaling up means more qubits, better wiring, and tight control of noise. Building a large, reliable machine remains one of the hardest engineering problems in the field.'),
    ],
    "test": [
        ('What is a qubit?',
         [('a', 'A type of printer'), ('b', 'A wire for power'), ('c', 'The quantum version of a bit, able to hold a mix of 0 and 1'), ('d', 'A chip for music')], 'c'),
        ('How are superconducting qubits kept working?',
         [('a', 'By keeping them in hot sand'), ('b', 'By placing them in water'), ('c', 'By painting them red'), ('d', 'By keeping them extremely cold')], 'd'),
        ('What do trapped-ion qubits use to store information?',
         [('a', 'The states of single charged atoms held in electric fields'), ('b', 'Paper labels'), ('c', 'Glass beads'), ('d', 'Sound waves')], 'a'),
        ('What does error correction do?',
         [('a', 'Deletes every qubit'), ('b', 'Prints the answer on paper'), ('c', 'Spreads one logical qubit across many physical qubits to detect and fix errors'), ('d', 'Stops all calculations')], 'c'),
        ('What is coherence time?',
         [('a', 'How long a computer is switched on each day'), ('b', 'How long a cable is'), ('c', 'How long a qubit keeps its quantum state'), ('d', 'How long a meeting lasts')], 'c'),
    ],
}
