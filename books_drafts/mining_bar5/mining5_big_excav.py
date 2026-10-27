"""Stability of large underground excavations: span, support, arching, monitoring, failure cases and design."""
CODE = 'mining5_big_excav'
BOOK = {
    'title': 'Stability of Large Excavations',
    'subtitle': 'Keeping a wide opening standing for the whole life of the mine',
    "chapters": [
        ('The span', 'The span is the width of an open excavation. Wider spans carry more risk of roof failure.'),
        ('Support', 'Rock bolts, mesh and shotcrete hold the rock in place and share the load. The right support depends on the rock and the shape of the opening.'),
        ('Arching', 'Rock above an opening can form an arch that carries its own weight, if the rock stays locked together. Cracks and water break that arch.'),
        ('Monitoring', 'Engineers measure movement in the roof and walls. If the movement speeds up, they act before the opening fails.'),
        ('Failure cases', 'Past collapses show that most failures begin with small cracks or water that were missed. Regular inspection finds these early.'),
        ('Design', 'Designers choose the shape, size and support of an opening so it stays stable for its whole life. Changing the plan later is much more costly.'),
    ],
    "test": [
        ('What is the span of an excavation?', [('a', 'Its depth below the surface'), ('b', 'The number of workers inside'), ('c', 'The age of the mine'), ('d', 'Its width')], 'd'),
        ('What do rock bolts and shotcrete do?', [('a', 'Hold the rock in place and share the load'), ('b', 'Light the tunnels'), ('c', 'Carry the ore to the mill'), ('d', 'Cool the air')], 'a'),
        ('What is arching in rock?', [('a', 'Rock turning into water'), ('b', 'A shape cut for a shaft'), ('c', 'Rock forming an arch that carries its own weight'), ('d', 'A type of rock drill')], 'c'),
        ('What do past collapses often start with?', [('a', 'Very bright lights'), ('b', 'Small cracks or water that were missed'), ('c', 'A shift change'), ('d', 'A stop for lunch')], 'b'),
        ('What does good design aim for?', [('a', 'An opening that is as narrow as possible'), ('b', 'An opening that stays stable for its whole life'), ('c', 'An opening with no support at all'), ('d', 'An opening that is never inspected')], 'b'),
    ],
}
