"""The Hall-Petch Relation: why finer grains make a metal stronger, and where that trend stops."""
CODE = 'mining5_hall_petch'
BOOK = {
    "title": 'The Hall-Petch Relation',
    "subtitle": 'Why finer grains make a metal stronger, and where that stops',
    "chapters": [
        ('Grains in metal', 'Most metals are made of many tiny crystals called grains. The boundaries between grains change how the metal deforms. Grain size is one of the main levers a metallurgist can pull.'),
        ('Dislocation pile-ups', 'Deformation happens when dislocations, line-like defects, move through the crystal. A grain boundary stops them, so they pile up against it. The pile-up pushes back and makes the metal harder to deform.'),
        ('The relation', 'The Hall-Petch relation says the yield strength rises as the grain size falls, roughly with the inverse square root of the grain diameter. Halving the grain size gives a clear gain in strength. The rule was found separately by Hall and by Petch.'),
        ('Fine grains', 'Fine-grained metals are stronger and often tougher at low temperature. Processes such as controlled rolling and heat treatment are used to make fine grains. Each process must be tested to confirm the result.'),
        ('Limits', 'The trend does not go on forever. Very fine grains can slide past each other, and strength can level off or fall. Metal at very high temperature also behaves differently from metal at room temperature.'),
        ('Measurement', 'Grain size is measured under a microscope by counting or comparing grains. Standard charts and methods make results comparable. Good measurement is the base for any strength promise.'),
    ],
    "test": [
        ('What are the crystals in a metal called?', [('a', 'Bubbles'), ('b', 'Sheets'), ('c', 'Grains'), ('d', 'Ribbons')], 'c'),
        ('What stops dislocations and makes them pile up?', [('a', 'Paint layers'), ('b', 'Water drops'), ('c', 'Paper sheets'), ('d', 'Grain boundaries')], 'd'),
        ('What does the Hall-Petch relation say about grain size and strength?', [('a', 'Finer grains give higher yield strength'), ('b', 'Coarser grains are always stronger'), ('c', 'Grain size has no effect'), ('d', 'Strength depends only on colour')], 'a'),
        ('Which processes make fine grains?', [('a', 'Painting and polishing'), ('b', 'Controlled rolling and heat treatment'), ('c', 'Sugar coating'), ('d', 'Freezing in ice')], 'b'),
        ('Why does the trend stop for very fine grains?', [('a', 'Metal turns into water'), ('b', 'Light cannot pass through'), ('c', 'The grains can slide past each other, so strength levels off or falls'), ('d', 'Grains always grow larger')], 'c'),
    ],
}
