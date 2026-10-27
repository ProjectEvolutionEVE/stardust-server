"""Ellingham Diagrams: a chart that shows which metal oxides break apart at which temperatures, and why."""
CODE = 'mining4_ellingham'
BOOK = {
    "title": 'Ellingham Diagrams: Why Oxides Break',
    "subtitle": 'Free energy against temperature, and which reductant works',
    "chapters": [
        ('What the chart shows',
         'An Ellingham diagram plots how the free energy of forming an oxide changes with temperature. Each metal has its own line. The lower a line sits, the more stable its oxide is at that temperature.'),
        ('Reading the lines',
         'To remove oxygen from an oxide, a reductant must form a more stable oxide than the metal you want. On the chart, its line must lie below the line of the oxide being reduced.'),
        ('Carbon as a reductant',
         "Carbon's line slopes downward as temperature rises. At high temperature it lies below many metal oxides, so carbon can reduce them. This is why carbon has been used for smelting for a very long time."),
        ('Oxide stability',
         'Oxides of metals like gold sit high on the chart and break apart easily. Oxides of metals like aluminium and magnesium sit low and are very stable. The chart shows this ranking at a glance.'),
        ('Reading the diagram',
         'A crossing point between two lines marks a temperature where one reductant starts to work better than another. Engineers use these crossings to choose the reductant and the furnace temperature.'),
        ('Limits of the diagram',
         'The diagram shows what is possible, not how fast it happens. It assumes standard conditions and does not show rates or the effect of impurities. Real plants test the process before they build.'),
    ],
    "test": [
        ('What does an Ellingham diagram plot?',
         [('a', 'The colour of metals'), ('b', 'The weight of furnaces against cost'), ('c', 'The free energy of forming an oxide against temperature'), ('d', 'The speed of sound in steel')], 'c'),
        ('What does a lower line on the chart mean?',
         [('a', 'A more stable oxide at that temperature'), ('b', 'A less stable oxide'), ('c', 'A metal that melts at room temperature'), ('d', 'A gas leak')], 'a'),
        ('Why does carbon become useful as a reductant at high temperature?',
         [('a', 'It turns into ice'), ('b', 'It is always the coldest element'), ('c', 'It never reacts'), ('d', 'Its line sinks below many metal oxides at high temperature')], 'd'),
        ('What does the diagram not show?',
         [('a', 'The free energy of oxides'), ('b', 'How fast the reaction happens'), ('c', 'The ranking of oxide stability'), ('d', 'The temperatures at which lines cross')], 'b'),
        ('What does a crossing point between two lines mark?',
         [('a', 'A broken chart'), ('b', 'The price of gold'), ('c', 'A temperature where one reductant starts to work better than another'), ('d', 'The end of the furnace')], 'c'),
    ],
}
