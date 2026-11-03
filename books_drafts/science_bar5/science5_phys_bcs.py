"""Superconductivity: BCS Theory and Beyond: Cooper pairs, the energy gap, the isotope effect, the Meissner effect, Josephson junctions and unconventional pairing."""
CODE = 'science5_phys_bcs'
BOOK = {
    "title": 'Superconductivity: BCS Theory and Beyond',
    "subtitle": 'Electrons that pair up and flow with no resistance',
    "chapters": [
        ('Zero resistance',
         'Some materials, when cooled below a critical temperature, carry electric current with no resistance at all. This state is called superconductivity. It was first seen in mercury by Heike Kamerlingh Onnes in 1911.'),
        ('Cooper pairs',
         'In 1957, Bardeen, Cooper and Schrieffer explained the effect with the BCS theory. Electrons pair up through vibrations of the crystal lattice, and these pairs, called Cooper pairs, move together without scattering. This is the core of the theory.'),
        ('The energy gap',
         'The paired state has an energy gap, a minimum energy needed to break a pair. The gap blocks small scattering events, which is why the current flows smoothly. The size of the gap depends on the material and the temperature.'),
        ('The isotope effect',
         'The critical temperature depends on the mass of the atoms in the lattice. Heavier isotopes give lower critical temperatures. This was an important clue that lattice vibrations drive the pairing in conventional superconductors.'),
        ('The Meissner effect',
         'A superconductor expels magnetic fields from its interior when it is cooled below the critical temperature. This is the Meissner effect. It makes a superconductor able to float above a magnet.'),
        ('Josephson junctions and beyond',
         'A Josephson junction is two superconductors separated by a thin barrier, and pairs can tunnel across it. This effect powers very sensitive magnetic sensors and some quantum computing circuits. Unconventional superconductors, such as some copper oxides, pair electrons in other ways, which the BCS theory does not fully explain.'),
    ],
    "test": [
        ('What is a Cooper pair?',
         [('a', 'Two electrons that pair up and move together without scattering'), ('b', 'Two coins stacked together'), ('c', 'A pair of copper wires'), ('d', 'Two magnets joined with glue')], 'a'),
        ('What does the energy gap do in a superconductor?',
         [('a', 'It makes the metal melt'), ('b', 'It blocks small scattering events so current flows smoothly'), ('c', 'It turns the metal into glass'), ('d', 'It makes the metal glow')], 'b'),
        ('What did the isotope effect suggest about superconductivity?',
         [('a', 'That lattice vibrations drive the pairing'), ('b', 'That superconductors are made of paper'), ('c', 'That heavier atoms never conduct'), ('d', 'That temperature does not matter')], 'a'),
        ('What is the Meissner effect?',
         [('a', 'A superconductor pulls in all nearby metal'), ('b', 'A superconductor gets hotter when cooled'), ('c', 'A superconductor expels magnetic fields from its interior'), ('d', 'A superconductor turns into light')], 'c'),
        ('What is a Josephson junction?',
         [('a', 'A type of bridge over a river'), ('b', 'Two superconductors separated by a thin barrier that pairs can tunnel across'), ('c', 'A kind of glass window'), ('d', 'A tube for pumping water')], 'b'),
    ],
}
