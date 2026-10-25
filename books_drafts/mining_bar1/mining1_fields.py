"""Reading a Debris Field: the four field sizes, how many pieces each holds, and how far you can spot them."""
CODE = 'mining1_fields'
BOOK = {
    "title": 'Reading a Debris Field',
    "subtitle": 'Field sizes, piece counts, and how far away you can spot them',
    "chapters": [
        ('What a field is',
         'A debris field is a cloud of broken rock and ore, drifting together in one place. Each field has a size, and the size tells you what to expect: how many pieces there are and how big they are. It does not tell you what any one piece holds. That is worked out piece by piece.'),
        ('Four sizes',
         'There are four field sizes: large, medium, small and tiny. A large field holds 400 to 1,200 pieces, a medium one 60 to 250, a small one 10 to 20, and a tiny one 8 to 20. Medium fields are the most common, at about 35 in every 100.'),
        ('How big the pieces are',
         'Each piece has a scale in metres, and its box is about 1.7 times that scale on each side. Large fields have scales from 0.05 to 4.0. Medium fields run from 0.06 to 2.0, small fields from 0.12 to 1.2, and tiny fields from 0.04 to 0.35.'),
        ('Mostly small pieces',
         'The pieces are not spread evenly. Their sizes are chosen so that small fragments are far more common than big ones. Even a large field is mostly small pieces, with a minority of boulders. Expect many small rocks for every big one.'),
        ('How far you can spot a field',
         'Your scanner picks up a field from a distance that depends on its size. A large field shows up from about 1,100 metres away, a medium one from 600 metres, a small one from 260 metres, and a tiny one from 160 metres. Bigger fields can be found from farther off.'),
        ('Reading a field before you go',
         'A big field holds more pieces, so it holds more of every kind, rare ones too, even though any single piece is less likely to be rare. A tiny field has few pieces and is quick to clear. Use the size as a guide, not a promise: the pieces inside are still a roll.'),
    ],
    "test": [
        ('How many pieces can a large field hold?',
         [('a', '8 to 20'), ('b', '60 to 250'), ('c', '400 to 1,200'), ('d', 'More than 10,000')], 'c'),
        ('Which field size is the most common?',
         [('a', 'Large'), ('b', 'Medium'), ('c', 'Small'), ('d', 'Tiny')], 'b'),
        ('What does a piece\'s scale tell you?',
         [('a', 'Its size, in metres'), ('b', 'Its colour'), ('c', 'Its price'), ('d', 'Which rarity band it is in')], 'a'),
        ('What do most of the pieces in a field look like?',
         [('a', 'Boulders as big as the field'), ('b', 'Pieces all the same size'), ('c', 'Only gold'), ('d', 'Small fragments, with a few big ones')], 'd'),
        ('Which field can your scanner pick up from the farthest away?',
         [('a', 'Tiny'), ('b', 'Small'), ('c', 'Medium'), ('d', 'Large')], 'd'),
    ],
}
