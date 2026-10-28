"""High-Entropy Alloys: metals mixed from five or more main elements in near-equal amounts."""
CODE = 'mining4_hea'
BOOK = {
    "title": 'High-Entropy Alloys',
    "subtitle": 'Five or more main elements, mixed in nearly equal amounts',
    "chapters": [
        ('A different kind of alloy',
         'Most alloys have one main metal with small amounts of others added. High-entropy alloys mix five or more main elements in nearly equal amounts. The mix itself is the design.'),
        ('Mixing and entropy',
         'Many elements mixed together give the atoms many possible arrangements. Scientists call this configurational entropy. Designers have used the idea to guide which mixes to try, though it is one part of a wider picture.'),
        ('Distortion in the lattice',
         'Atoms of different sizes sit in the same crystal, which strains the lattice. The strain can make it harder for dislocations to move, and that can raise strength.'),
        ('Strength and toughness',
         'Some high-entropy alloys stay strong and tough at very low temperatures. This makes them interesting for special uses, though each mix must be tested for its own behaviour.'),
        ('Testing a new alloy',
         'Making a new alloy means melting, casting, heat treating and then testing its strength, toughness and corrosion. Many mixes fail in one of these tests, so the search takes patience.'),
        ('The cost of many elements',
         'Using five or more elements means buying several metals, and some are costly or hard to supply. The cost and supply of each element is a real limit on where these alloys can be used.'),
    ],
    "test": [
        ('How many main elements does a high-entropy alloy usually have?',
         [('a', 'One'), ('b', 'Two'), ('c', 'Five or more'), ('d', 'Exactly three')], 'c'),
        ('What is configurational entropy in these alloys?',
         [('a', 'The number of possible arrangements of atoms in the mix'), ('b', 'The weight of the furnace'), ('c', 'The price of a metal'), ('d', 'The colour of the surface')], 'a'),
        ('What does lattice distortion from mixed atom sizes do?',
         [('a', 'It melts the alloy at room temperature'), ('b', 'It removes all strength'), ('c', 'It makes the alloy transparent'), ('d', 'It can make dislocations harder to move, which can raise strength')], 'd'),
        ('Why is cost a limit on high-entropy alloys?',
         [('a', 'They are sold only as paint'), ('b', 'Several elements must be bought, and some are costly or hard to supply'), ('c', 'They cannot be tested'), ('d', 'They weigh nothing')], 'b'),
        ('What steps are used to test a new alloy?',
         [('a', 'Reading it aloud'), ('b', 'Freezing it in a bag'), ('c', 'Melting, casting, heat treating and testing its properties'), ('d', 'Counting its colours')], 'c'),
    ],
}
