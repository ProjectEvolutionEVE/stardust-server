"""Quantum Field Theory: fields and particles, creation and annihilation, Feynman diagrams, renormalisation and vacuum fluctuations."""
CODE = 'science5_phys_qft'
BOOK = {
    "title": 'Quantum Field Theory: Fields and Particles',
    "subtitle": 'Particles as ripples in fields that fill all of space',
    "chapters": [
        ('Fields everywhere',
         'In quantum field theory, the basic objects are fields that fill all of space. A particle is a quantum of one of these fields, a small packet of energy. The electron is the quantum of the electron field, and the photon is the quantum of the electromagnetic field.'),
        ('Creation and annihilation',
         'Operators in the theory can create a particle or destroy one. Creating a particle adds one quantum to a field, and annihilating it removes one. This makes the number of particles flexible, which matches experiments where particles are made and lost.'),
        ('Feynman diagrams',
         'Feynman diagrams are pictures that show interactions between particles. Lines stand for particles, and vertices stand for points where they meet and interact. Each diagram gives a term in the calculation of a probability.'),
        ('Renormalisation',
         'Calculations in field theory often produce infinite terms. Renormalisation absorbs these infinities into measured quantities, such as the electron mass and charge. After this, the predictions are finite and match experiment to remarkable accuracy.'),
        ('Vacuum fluctuations',
         'Even the vacuum is not empty in the theory. Quantum fluctuations briefly create and destroy pairs of particles. These fluctuations have measurable effects, such as a tiny shift in atomic energy levels called the Lamb shift.'),
        ('A theory of great success',
         'Quantum field theory underlies the Standard Model of particle physics. Its predictions for the magnetic moment of the electron agree with experiment to better than one part in a billion. The theory is among the most tested in all of science.'),
    ],
    "test": [
        ('In quantum field theory, what is a particle?',
         [('a', 'A quantum or packet of energy in a field'), ('b', 'A tiny ball of glass'), ('c', 'A bit of dust'), ('d', 'A unit of sound')], 'a'),
        ('What do creation and annihilation operators do?',
         [('a', 'Add or remove a quantum from a field'), ('b', 'Paint the field a colour'), ('c', 'Measure the size of a room'), ('d', 'Cool the field to zero')], 'a'),
        ('What do lines in a Feynman diagram stand for?',
         [('a', 'Roads on a map'), ('b', 'Particles'), ('c', 'Rainfall'), ('d', 'Temperature readings')], 'b'),
        ('What does renormalisation do?',
         [('a', 'It makes the field disappear'), ('b', 'It doubles the mass of every particle'), ('c', 'It removes all energy from space'), ('d', 'It absorbs infinite terms into measured quantities')], 'd'),
        ('What are vacuum fluctuations?',
         [('a', 'Changes in the weather'), ('b', 'Waves in the ocean'), ('c', 'Shakes in a building'), ('d', 'Brief creations and destructions of particle pairs in the vacuum')], 'd'),
    ],
}
