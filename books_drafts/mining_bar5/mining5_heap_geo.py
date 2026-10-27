"""Heap leach pad geotechnics: stacking, settlement, liner stress, slope stability, monitoring and failure cases."""
CODE = 'mining5_heap_geo'
BOOK = {
    'title': 'Heap Leach Pads and Geotechnics',
    'subtitle': 'Stacking ore in large piles and keeping them stable',
    "chapters": [
        ('The heap', 'Heap leaching stacks crushed ore in large piles on a lined pad. A solution slowly dissolves the metal as it trickles through.'),
        ('Stacking', 'Ore is stacked in layers called lifts. Each lift is placed and compacted to a design height and slope.'),
        ('Settlement', 'Heaps settle as they are loaded and as the ore breaks down. Settlement can crack pipes and liners.'),
        ('Liner stress', 'The liner under the heap carries the full weight. Its stress must be checked so that it does not tear.'),
        ('Slope and monitoring', 'The slopes are checked for stability. Pressure cells and surveys track movement over time.'),
        ('Failure cases', 'Past heap failures often came from weak layers, water build-up or steep slopes. Each lesson is now built into the design rules.'),
    ],
    "test": [
        ('What is heap leaching?', [('a', 'Melting ore in a furnace'), ('b', 'Dissolving metal from ore stacked in piles on a lined pad'), ('c', 'Sorting ore by hand'), ('d', 'Washing sand in a river')], 'b'),
        ('Why do heaps settle?', [('a', 'The heap is painted'), ('b', 'The lights are switched on'), ('c', 'Loading and the breakdown of the ore'), ('d', 'The trucks are parked nearby')], 'c'),
        ('What must be checked under a heap?', [('a', 'The price of the lunch'), ('b', 'The number of radios'), ('c', 'The colour of the stacker'), ('d', 'The stress on the liner')], 'd'),
        ('What can settlement crack?', [('a', 'Pipes and liners'), ('b', 'Windows in the office'), ('c', 'Road signs'), ('d', 'Tree trunks')], 'a'),
        ('What did past heap failures often come from?', [('a', 'Too much sunlight'), ('b', 'Weak layers, water build-up or steep slopes'), ('c', 'Too many lunch breaks'), ('d', 'A surplus of ore')], 'b'),
    ],
}
