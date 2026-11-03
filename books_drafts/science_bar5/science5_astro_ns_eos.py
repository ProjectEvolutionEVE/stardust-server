"""Neutron Star Equation of State: how the strange matter inside the densest stars is probed by their size, their maximum mass and the waves from their collisions."""
CODE = 'science5_astro_ns_eos'
BOOK = {
    "title": 'Neutron Star Equation of State',
    "subtitle": 'What is inside the densest stars',
    "chapters": [
        ('Matter at extreme density',
         'A neutron star packs more mass than the Sun into a ball about the width of a city. Its matter is denser than an atomic nucleus. No laboratory on Earth can make such matter for long.'),
        ('Nuclear matter models',
         'Physicists build models of how matter behaves at these densities. Each model predicts a different relation between pressure and density. These models are the candidates for the equation of state.'),
        ('Mass-radius constraints',
         'The size of a neutron star of a given mass depends on the equation of state. Measuring mass and radius together tests the models. Each measurement narrows the possibilities.'),
        ('Tidal deformability',
         'Tidal deformability describes how easily a neutron star is stretched by a companion\'s gravity. Gravitational waves from a merger carry this information. It helps rule out some models.'),
        ('The maximum mass',
         'Neutron stars have a maximum mass. Above it, the star collapses into a black hole. The maximum is roughly two times the mass of the Sun.'),
        ('Gravitational-wave constraints',
         'The 2017 merger GW170817 gave the first gravitational-wave limits on neutron star size. The signal and its partner light helped constrain the equation of state. Each new merger adds to the picture.'),
    ],
    "test": [
        ('What is the equation of state for neutron stars?',
         [('a', 'The price of a neutron'), ('b', 'The rule linking pressure and density inside neutron star matter'), ('c', 'A law of traffic'), ('d', 'The colour of a magnet')], 'b'),
        ('What do mass-radius constraints tell us?',
         [('a', 'The age of Earth'), ('b', 'The taste of iron'), ('c', 'How big a neutron star of a given mass is, which tests the equation of state'), ('d', 'The speed of wind')], 'c'),
        ('What is tidal deformability?',
         [('a', 'The heat of the Sun'), ('b', 'The power of a crane'), ('c', 'A tide on the ocean of Earth only'), ('d', 'How easily a neutron star is stretched by a companion\'s gravity')], 'd'),
        ('What is roughly the maximum mass of a neutron star?',
         [('a', 'Roughly two times the mass of the Sun'), ('b', 'About the mass of a grain of sand'), ('c', 'About ten suns'), ('d', 'It has no upper limit')], 'a'),
        ('What did gravitational waves from GW170817 help constrain?',
         [('a', 'The colour of Saturn'), ('b', 'The number of Earth\'s moons'), ('c', 'The taste of ice'), ('d', 'The tidal deformability and radius of neutron stars')], 'd'),
    ],
}
