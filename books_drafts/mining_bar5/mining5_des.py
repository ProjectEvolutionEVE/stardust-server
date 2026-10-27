"""Deep eutectic solvents: hydrogen bond donors, metal solubility, recycling, viscosity, toxicity and recovery."""
CODE = 'mining5_des'
BOOK = {
    'title': 'Deep Eutectic Solvents',
    'subtitle': 'Mixed liquids that may dissolve metals with less harsh chemistry',
    "chapters": [
        ('A mixture of two', 'Deep eutectic solvents are mixtures of two solid compounds that melt into a liquid at a low temperature. Mixing them lowers the melting point well below that of either part.'),
        ('Hydrogen bond donors', 'One partner is usually a hydrogen bond donor, and the other is often a salt such as choline chloride. The two partners are chosen so that they melt together at a low temperature.'),
        ('Metal solubility', 'Many metal oxides dissolve in these solvents. That makes them of interest for leaching.'),
        ('Recycling', 'The solvents can be reused. How many times they can be reused strongly affects the economics.'),
        ('Viscosity', 'These liquids are often thick, which slows mixing and flow. Warming them can help.'),
        ('Recovery and toxicity', 'Metals are recovered from the solution afterwards. Toxicity depends on the components, so each mix must be checked.'),
    ],
    "test": [
        ('What are deep eutectic solvents?', [('a', 'Pure gold in water'), ('b', 'Solid rock crushed to dust'), ('c', 'Mixtures of two compounds that melt into a liquid at a low temperature'), ('d', 'Gases pressed into steel')], 'c'),
        ('Which salt is often used in deep eutectic solvents?', [('a', 'Table salt only'), ('b', 'Sea sand'), ('c', 'Limestone'), ('d', 'Choline chloride')], 'd'),
        ('What property makes these solvents of interest for leaching?', [('a', 'Many metal oxides dissolve in them'), ('b', 'They are magnetic'), ('c', "They freeze above the sun's heat"), ('d', 'They turn into wood')], 'a'),
        ('What is a common drawback of these liquids?', [('a', 'They are always bright red'), ('b', 'They are often thick'), ('c', 'They cannot be stored'), ('d', 'They are too cold to touch')], 'b'),
        ('Why must each mix be checked for toxicity?', [('a', 'Toxicity depends on the components'), ('b', 'Every mix is safe by law'), ('c', 'Toxicity is the same for all mixes'), ('d', 'Only the colour matters')], 'a'),
    ],
}
