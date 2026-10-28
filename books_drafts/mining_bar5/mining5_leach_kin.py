"""Leach kinetics and the shrinking core model: diffusion, reaction control, particle size, tests and design."""
CODE = 'mining5_leach_kin'
BOOK = {
    'title': 'Leach Kinetics and the Shrinking Core',
    'subtitle': 'How a leaching particle dissolves from the outside in',
    "chapters": [
        ('Dissolving a particle', 'Leaching dissolves metal from a particle from the outside in. The unreacted core shrinks over time.'),
        ('The shrinking core model', 'The shrinking core model describes this process. A reacted outer layer forms, while the unreacted core gets smaller.'),
        ('Diffusion', 'Leach liquid must diffuse through the outer layer to reach the core. Diffusion can control the rate of leaching.'),
        ('Reaction control', 'If the chemical reaction at the surface is the slowest step, reaction control applies instead. The rate then depends on the chemistry at the particle surface, not on how fast liquid reaches it.'),
        ('Particle size', 'Smaller particles have more surface and leach faster. Crushing choices therefore matter.'),
        ('Tests and design', 'Lab tests find which step controls the rate. The plant is then designed around that step.'),
    ],
    "test": [
        ('Where does leaching dissolve a particle from?', [('a', 'The outside in'), ('b', 'The inside out'), ('c', 'The top down only'), ('d', 'The middle first')], 'a'),
        ('What does the shrinking core model describe?', [('a', 'A core growing larger'), ('b', 'A particle that never changes'), ('c', 'A reacted outer layer forming while the unreacted core shrinks'), ('d', 'A shaft getting deeper')], 'c'),
        ('What can diffusion control?', [('a', 'The colour of the solution'), ('b', 'The number of workers'), ('c', 'The price of the shift'), ('d', 'The leaching rate')], 'd'),
        ('Why do smaller particles leach faster?', [('a', 'They are lighter to carry'), ('b', 'They have more surface'), ('c', 'They are harder to see'), ('d', 'They have fewer atoms')], 'b'),
        ('What do lab tests find?', [('a', 'Which step controls the rate'), ('b', 'Which team is fastest'), ('c', 'Which truck is newest'), ('d', 'Which menu is popular')], 'a'),
    ],
}
