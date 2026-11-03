"""Quantum Hall Effects and Topology: two-dimensional electron gases, Landau levels, quantised Hall conductance, topological invariants and edge states."""
CODE = 'science5_phys_quantum_hall'
BOOK = {
    "title": 'Quantum Hall Effects and Topology',
    "subtitle": 'Electrons in two dimensions, measured to extraordinary precision',
    "chapters": [
        ('A flat electron sea',
         'Electrons can be trapped in a very thin layer, so they move in only two dimensions. This is a two-dimensional electron gas. Such layers are made in semiconductor devices at very low temperatures and high magnetic fields.'),
        ('Landau levels',
         "In a strong magnetic field, the electrons' energy becomes split into discrete levels called Landau levels. Each level holds a set number of electrons per unit area, set by the field strength."),
        ('Quantised Hall conductance',
         'In 1980, Klaus von Klitzing found that the Hall conductance rises in exact steps. Each step is a whole-number multiple of a fixed constant, e squared over h. The steps are exact to a few parts in a billion, and the effect is now used to define the unit of resistance.'),
        ('Topological invariants',
         'The whole number that sets each step is a topological invariant, meaning it does not change under smooth deformations of the system. Small defects and impurities do not shift it, which is why the steps are so precise.'),
        ('Edge states',
         'At the edge of the sample, electrons can travel along the boundary in one direction only. These edge states carry current without backscattering. They are a key signature of the topological nature of the effect.'),
        ('Topological materials',
         'The same ideas appear in topological insulators, which conduct on their surfaces but not in their interior. Researchers aim to use such surface states in future electronics and in quantum devices, where the protection from defects could help.'),
    ],
    "test": [
        ('What is a two-dimensional electron gas?',
         [('a', 'A balloon filled with electrons'), ('b', 'A glass of salt water'), ('c', 'Electrons trapped in a very thin layer so they move in two dimensions'), ('d', 'A cloud of dust')], 'c'),
        ('What are Landau levels?',
         [('a', 'Floors of a building'), ('b', 'Layers of paint'), ('c', 'Maps of a mountain'), ('d', 'Discrete energy levels that electrons form in a strong magnetic field')], 'd'),
        ('Who found the quantised Hall conductance in 1980?',
         [('a', 'Klaus von Klitzing'), ('b', 'Isaac Newton'), ('c', 'Marie Curie'), ('d', 'Galileo Galilei')], 'a'),
        ('Why are the Hall steps so precise?',
         [('a', 'They are set by the colour of the sample'), ('b', 'They are set by the weather outside'), ('c', 'They are set by a random guess'), ('d', 'They are set by a topological whole number that does not change under small defects')], 'd'),
        ('Where do edge states travel?',
         [('a', 'Straight up into the air'), ('b', 'Along the boundary of the sample, in one direction only'), ('c', 'Through the walls of the lab'), ('d', 'Only in circles in the centre')], 'b'),
    ],
}
