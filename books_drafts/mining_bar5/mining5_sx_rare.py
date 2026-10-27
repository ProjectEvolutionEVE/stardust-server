"""Solvent extraction cascades for rare earths: mixer-settler stages, separation factors, reagents, crud, products and efficiency."""
CODE = 'mining5_sx_rare'
BOOK = {
    'title': 'Solvent Extraction Cascades for Rare Earths',
    'subtitle': 'Separating rare earth elements through many small mixing steps',
    "chapters": [
        ('Many small steps', 'Solvent extraction moves metal from one liquid into another in a series of mixer-settler stages, called a cascade. Each stage moves the metal a little further toward the wanted product.'),
        ('Stages', 'Each stage mixes the two liquids and then lets them separate. More stages give a finer separation.'),
        ('Separation factors', 'A separation factor measures how much better one rare earth goes into the solvent than another. A small difference needs many stages.'),
        ('Reagents', 'Organic extractants and diluents are chosen for selectivity and safety. Reagent losses are a major cost.'),
        ('Crud', 'Crud is a sticky layer of solids and organic matter that builds up between the liquids. It slows the separation.'),
        ('Products and efficiency', 'Each product is a pure stream of one element. Efficiency depends on the number of stages, the flow and the reagent use.'),
    ],
    "test": [
        ('What is a cascade in solvent extraction?', [('a', 'A waterfall in a mine'), ('b', 'A series of mixer-settler stages'), ('c', 'A pile of ore'), ('d', 'A line of trucks')], 'b'),
        ('What does a separation factor measure?', [('a', 'How much better one rare earth goes into the solvent than another'), ('b', 'The depth of the stage'), ('c', 'The temperature of the canteen'), ('d', 'The weight of a drum')], 'a'),
        ('What does a small separation difference need?', [('a', 'No stages at all'), ('b', 'A single bucket'), ('c', 'A colder room'), ('d', 'Many stages')], 'd'),
        ('What is crud?', [('a', 'Clean drinking water'), ('b', 'A type of ore'), ('c', 'A sticky layer of solids and organic matter at the boundary between liquids'), ('d', 'A kind of paint')], 'c'),
        ('What does efficiency depend on?', [('a', 'The colour of the cascade'), ('b', 'The name of the plant'), ('c', 'The number of visitors'), ('d', 'The number of stages, the flow and the reagent use')], 'd'),
    ],
}
