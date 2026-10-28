"""Direct lithium extraction sorbents: adsorbents, ion sieves, loading, eluent, regeneration and cost."""
CODE = 'mining5_dle_sorb'
BOOK = {
    'title': 'Direct Lithium Extraction Sorbents',
    'subtitle': 'Solid materials that take lithium out of brine, then release it',
    "chapters": [
        ('Pulling lithium out', 'Direct lithium extraction uses a solid material that takes up lithium ions from brine and holds them. The loaded sorbent is then separated from the brine, and the lithium is recovered from it.'),
        ('Adsorbents', 'An adsorbent holds the target ion on its surface or within its structure. Many of these materials are inorganic.'),
        ('Ion sieves', 'Ion sieves have openings sized to fit lithium ions, so they select lithium over many other ions. Their structure favours lithium over many other ions in the brine.'),
        ('Loading and eluent', 'When the sorbent is full, it is loaded. A cleaning liquid called eluent then releases the lithium.'),
        ('Regeneration', 'The sorbent is regenerated so it can be used again. Regeneration keeps the cost down.'),
        ('Cost', 'Sorbent life, eluent use and regeneration decide whether the process pays. Each of these three costs can be lowered by better design.'),
    ],
    "test": [
        ('What does a lithium extraction sorbent do?', [('a', 'Adds salt to the brine'), ('b', 'Turns brine into gas'), ('c', 'Takes up lithium ions from brine'), ('d', 'Paints the tanks')], 'c'),
        ('What is an ion sieve?', [('a', 'A metal screen for rocks'), ('b', 'A material with openings sized to select certain ions'), ('c', 'A fan for the mine'), ('d', 'A kind of drill bit')], 'b'),
        ('What is eluent?', [('a', 'A type of fuel'), ('b', 'A gas for the lights'), ('c', 'A cleaning cloth'), ('d', 'A liquid that releases the lithium from the sorbent')], 'd'),
        ('What is regeneration?', [('a', 'Preparing the sorbent to be used again'), ('b', 'Throwing the sorbent away'), ('c', 'Painting the sorbent'), ('d', 'Burning the sorbent in a furnace')], 'a'),
        ('What decides whether the process pays?', [('a', 'The colour of the tanks'), ('b', 'The number of visitors'), ('c', 'Sorbent life, eluent use and regeneration'), ('d', 'The weather in the region')], 'c'),
    ],
}
