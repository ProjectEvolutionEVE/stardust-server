"""Quantum Spin and Angular Momentum: spin-half systems, Pauli matrices, adding angular momenta, and the Stern-Gerlach experiment."""
CODE = 'science5_phys_spin'
BOOK = {
    "title": 'Quantum Spin and Angular Momentum',
    "subtitle": 'The intrinsic spin of particles and how it is measured',
    "chapters": [
        ('An intrinsic spin',
         'Particles such as electrons carry an intrinsic angular momentum called spin. It is not a literal spinning ball, but it behaves like angular momentum in the mathematics. Spin is a basic property, like charge or mass.'),
        ('Spin one-half',
         'An electron has spin one-half. When you measure its spin along any direction, you find only two results, often called up and down. The measured value is either plus or minus one-half of a fixed unit, never anything in between.'),
        ('Pauli matrices',
         'Three special 2-by-2 matrices, the Pauli matrices, describe spin-half systems. Each one corresponds to measuring spin along one axis. They also show that measurements along different axes do not commute, so their order matters.'),
        ('Adding angular momenta',
         'When two spins combine, the total spin can take several values. Two spin-half particles can have a total of zero or one. The rules for adding them follow the same pattern used for orbital angular momentum.'),
        ('The Stern-Gerlach experiment',
         'In 1922, Stern and Gerlach sent silver atoms through a magnetic field that bent their paths. The beam split into two separate spots, not a smooth smear. This showed that spin takes only discrete values.'),
        ('Spin in magnetic resonance',
         'Spin links to magnetic resonance. A spin in a magnetic field has two energy levels, and radio waves can flip it between them. Magnetic resonance imaging and nuclear magnetic resonance use this principle to probe materials and the body.'),
    ],
    "test": [
        ('What is spin in quantum physics?',
         [('a', 'An intrinsic angular momentum that is a basic property of particles'), ('b', 'A type of tyre'), ('c', 'A kind of weather'), ('d', 'A gas leak')], 'a'),
        ('How many results do you get when measuring the spin of an electron along any direction?',
         [('a', 'Two'), ('b', 'Ten'), ('c', 'One hundred'), ('d', 'An endless range')], 'a'),
        ('What do the Pauli matrices describe?',
         [('a', 'The colour of metals'), ('b', 'Spin-half systems'), ('c', 'Ocean tides'), ('d', 'Bridge designs')], 'b'),
        ('What did the Stern-Gerlach experiment show?',
         [('a', 'Light moves in a circle'), ('b', 'Gold is a liquid'), ('c', 'Spin takes only discrete values, so the beam splits into separate spots'), ('d', 'Magnets have no poles')], 'c'),
        ('What uses spin to probe materials and the body?',
         [('a', 'A pair of scissors'), ('b', 'A kitchen timer'), ('c', 'Magnetic resonance'), ('d', 'A bicycle pump')], 'c'),
    ],
}
