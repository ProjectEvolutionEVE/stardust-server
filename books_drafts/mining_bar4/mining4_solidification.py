"""Solidification and Dendrites: how a metal freezes into crystals, and why the pattern matters."""
CODE = 'mining4_solidification'
BOOK = {
    "title": 'Solidification and Dendrites',
    "subtitle": 'How a metal freezes into crystals, and why the pattern matters',
    "chapters": [
        ('Freezing starts at a seed',
         'When liquid metal cools, tiny solid crystals form first, at points called nuclei. Each nucleus grows as more atoms join it from the liquid around it. Where the crystals meet, they form the grain boundaries of the finished metal.'),
        ('Tree-shaped crystals',
         'Many metals grow in branched, tree-like crystals called dendrites. The main arms point along the direction heat flows out. Side arms grow off them, and the spaces between the arms fill in last.'),
        ('Supercooling',
         'Sometimes the melt in front of a growing crystal is cooled below its freezing point, which is called constitutional supercooling. This makes the front break up into shapes and can speed the growth of side arms.'),
        ('Segregation between arms',
         'As each arm grows, it pushes some alloy elements into the liquid between the arms. The last liquid to freeze is richer in those elements, which is called microsegregation.'),
        ('Grain size',
         'Adding small particles called inoculants gives the melt many nuclei at once. More nuclei give smaller grains, and smaller grains usually make the metal stronger and tougher.'),
        ('Casting defects',
         'Shrinkage is a common defect: the metal shrinks as it freezes, and pores can form where the last liquid cannot be fed. Hot tears are cracks that open while the metal is still weak and hot. Good design and feeding of the casting prevent both.'),
    ],
    "test": [
        ('What are dendrites?',
         [('a', 'Small holes made by bubbles'), ('b', 'Paints used on moulds'), ('c', 'Tree-shaped crystals that grow as metal freezes'), ('d', 'Sheets of rolled steel')], 'c'),
        ('What is an inoculant used for?',
         [('a', 'To give the melt many nuclei and so smaller grains'), ('b', 'To melt the metal faster'), ('c', 'To colour the metal'), ('d', 'To cool the mould')], 'a'),
        ('Where does microsegregation happen?',
         [('a', 'On the outside of the mould'), ('b', 'In the furnace roof'), ('c', 'In the cooling water'), ('d', 'In the liquid left between the growing dendrite arms')], 'd'),
        ('What is shrinkage in a casting?',
         [('a', 'The metal getting bigger'), ('b', 'Pores that form when the last liquid cannot be fed'), ('c', 'A coat of rust'), ('d', 'The ladle cracking')], 'b'),
        ('Why does smaller grain size usually help a metal?',
         [('a', 'It makes the metal see-through'), ('b', 'It lowers its melting point to zero'), ('c', 'It makes the metal stronger and tougher'), ('d', 'It stops the metal conducting heat')], 'c'),
    ],
}
