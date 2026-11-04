"""Nuclear Fusion Reactors and Plasma Confinement: the deuterium-tritium reaction, the Lawson criterion, tokamaks, stellarators, inertial confinement and engineering challenges."""
CODE = 'science5_phys_fusion_reactors'
BOOK = {
    "title": 'Nuclear Fusion Reactors and Plasma Confinement',
    "subtitle": 'Building a star on Earth, and holding its fuel long enough to burn',
    "chapters": [
        ('The fusion fuel',
         'Fusion joins light nuclei to make heavier ones and release energy. The easiest reaction for a reactor joins deuterium and tritium, two heavy forms of hydrogen. It releases a helium nucleus and a fast neutron.'),
        ('The Lawson criterion',
         'The Lawson criterion says a plasma must be hot, dense and held together long enough for the fusion energy to exceed the energy lost. This is often summed up as the product of density, temperature and confinement time. Meeting it is the central goal of fusion research.'),
        ('Tokamaks',
         'A tokamak is a doughnut-shaped device. Magnetic fields hold the hot plasma away from the walls. A current in the plasma helps shape the field, and the design is the most studied approach to magnetic confinement.'),
        ('Stellarators',
         'A stellarator also uses twisted magnetic coils to confine plasma, but without a large plasma current. Its shape is harder to build, yet it can run steadily without the current-driven instabilities that can afflict tokamaks.'),
        ('Inertial confinement',
         'Inertial confinement compresses a small fuel pellet very quickly with lasers or beams. The pellet is squeezed so hard that fusion begins before it flies apart. The method works in short bursts.'),
        ('Engineering challenges',
         'Reactors must handle intense heat, fast neutrons that damage materials, and the need to make tritium from lithium. Engineers must also deal with long-term maintenance and the cost of building very large machines.'),
    ],
    "test": [
        ('Which fuel is most often used in the easiest fusion reaction?',
         [('a', 'Iron and copper'), ('b', 'Sand and salt'), ('c', 'Deuterium and tritium'), ('d', 'Coal and oil')], 'c'),
        ('What does the Lawson criterion describe?',
         [('a', 'The rules for driving a car'), ('b', 'The price of electricity'), ('c', 'The size of a warehouse'), ('d', 'The conditions a plasma must meet for fusion energy to exceed losses')], 'd'),
        ('What shape is a tokamak?',
         [('a', 'A doughnut'), ('b', 'A pyramid'), ('c', 'A flat disc'), ('d', 'A cube of ice')], 'a'),
        ('What is special about a stellarator?',
         [('a', 'It runs on coal'), ('b', 'It uses twisted magnetic coils without a large plasma current'), ('c', 'It floats on water'), ('d', 'It has no magnets at all')], 'b'),
        ('How does inertial confinement work?',
         [('a', 'It freezes the fuel in ice'), ('b', 'It stores fuel in glass jars'), ('c', 'It squeezes a small fuel pellet very quickly with lasers or beams'), ('d', 'It waits for the fuel to cool')], 'c'),
    ],
}
