"""Quantum Optics and Single Photons: photon statistics, coherent states, single-photon sources, interference and detectors."""
CODE = 'science5_phys_quantum_optics'
BOOK = {
    "title": 'Quantum Optics and Single Photons',
    "subtitle": 'Light studied one photon at a time',
    "chapters": [
        ('Light in packets',
         'Light comes in packets of energy called photons. Quantum optics studies light at the level of single photons, where its particle nature shows up clearly. Many effects that look simple in classical light become surprising here.'),
        ('Photon statistics',
         'Photons can arrive in a steady stream, bunched together, or spread out evenly. Statistics of arrival times reveal which kind of light a source gives. A single-photon source gives one photon at a time, so two of its photons never arrive together.'),
        ('Coherent states',
         'A laser produces a coherent state, which is the closest quantum match to a steady classical wave. Its photon arrivals follow a random pattern with a fixed average rate. Coherent states form the standard reference for comparison.'),
        ('Single-photon sources',
         'Single-photon sources can be built from single atoms, quantum dots or special crystals that emit one photon per trigger. Making a reliable source is a key step toward secure communication and quantum computing.'),
        ('Photon interference',
         'Two photons meeting at a beam splitter can interfere in a way that depends on their quantum state. The Hong-Ou-Mandel effect shows that identical photons arriving together leave the splitter as a pair, not one each way.'),
        ('Detectors and noise',
         'Single-photon detectors can register one photon, but they have limits. Some photons are missed, and some clicks come from dark counts with no light at all. Good experiments measure and correct for these imperfections.'),
    ],
    "test": [
        ('What is a photon?',
         [('a', 'A small piece of wood'), ('b', 'A drop of water'), ('c', 'A grain of sand'), ('d', 'A packet of energy in light')], 'd'),
        ('What does a single-photon source give out?',
         [('a', 'A flood of thousands at once'), ('b', 'One photon at a time'), ('c', 'Only sound'), ('d', 'Only heat')], 'b'),
        ('What kind of light state does a laser produce?',
         [('a', 'A coherent state'), ('b', 'A frozen state'), ('c', 'A dark state'), ('d', 'A smoky state')], 'a'),
        ('What is the Hong-Ou-Mandel effect?',
         [('a', 'A way to paint photographs'), ('b', 'Identical photons arriving together leave a beam splitter as a pair'), ('c', 'A type of thermometer'), ('d', 'A method of weighing gold')], 'b'),
        ('What are dark counts in a photon detector?',
         [('a', 'Photons hidden in a box'), ('b', 'Lights turned off by a switch'), ('c', 'Clicks that come from the detector with no light present'), ('d', 'Stars seen at night')], 'c'),
    ],
}
