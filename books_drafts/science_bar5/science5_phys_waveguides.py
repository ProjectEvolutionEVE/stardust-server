"""Electromagnetic Waves in Waveguides: mode structure, cutoff frequency, coaxial and rectangular guides, dispersion, fibre optics and measurements."""
CODE = 'science5_phys_waveguides'
BOOK = {
    "title": 'Electromagnetic Waves in Waveguides',
    "subtitle": 'Guiding radio and light waves down metal pipes and glass fibres',
    "chapters": [
        ('Guiding a wave',
         'A waveguide is a structure that carries electromagnetic waves along its length, with little loss to the sides. Hollow metal pipes and glass fibres are common examples. They keep signals confined as they travel.'),
        ('Modes',
         'A wave in a guide can only fit in certain patterns, called modes. Each mode has its own field shape across the cross-section. The modes are set by the size and shape of the guide and by the wavelength of the wave.'),
        ('Cutoff frequency',
         'Each mode has a cutoff frequency. Below it, the wave cannot travel down the guide and dies away. Above it, the mode propagates. Choosing the guide size sets the lowest frequency that can pass.'),
        ('Coaxial and rectangular guides',
         'A coaxial cable has a central conductor inside a metal tube. It carries a simple mode with no cutoff, so it works at low frequencies. A rectangular metal waveguide has a cutoff and is common for microwave links and radar.'),
        ('Dispersion',
         'Different modes travel at different speeds in a guide. This spread is called dispersion, and it can blur a signal over distance. Designers choose guides and modes that limit dispersion for the job at hand.'),
        ('Fibre optics and measurements',
         'Optical fibres guide light by total internal reflection in a glass core. They carry signals across oceans with low loss. Engineers measure guides by sending known signals and checking the reflections, which show where faults lie.'),
    ],
    "test": [
        ('What does a waveguide do?',
         [('a', 'It turns sound into heat'), ('b', 'It cools water in a tank'), ('c', 'It makes paper'), ('d', 'It carries electromagnetic waves along its length with little loss')], 'd'),
        ('What is a mode in a waveguide?',
         [('a', 'A type of car'), ('b', 'A pattern a wave can fit inside the guide'), ('c', 'A colour of paint'), ('d', 'A kind of rainfall')], 'b'),
        ('What is a cutoff frequency?',
         [('a', 'The frequency below which a mode cannot travel down the guide'), ('b', 'The frequency of a clock'), ('c', 'The price of cable'), ('d', 'The speed of a bus')], 'a'),
        ('Which guide has a simple mode with no cutoff, suited to low frequencies?',
         [('a', 'A coaxial cable'), ('b', 'A brick wall'), ('c', 'A glass jar'), ('d', 'A wooden plank')], 'a'),
        ('How do optical fibres guide light?',
         [('a', 'By painting the glass black'), ('b', 'By total internal reflection in a glass core'), ('c', 'By heating the glass red'), ('d', 'By freezing the glass solid')], 'b'),
    ],
}
