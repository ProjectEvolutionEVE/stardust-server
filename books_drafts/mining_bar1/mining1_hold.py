"""Fitting the Hold: what fits in the starter hold, and how much room each piece really takes up."""
CODE = 'mining1_hold'
BOOK = {
    "title": 'Fitting the Hold',
    "subtitle": 'What fits in the starter hold, and how much room each piece takes',
    "chapters": [
        ('The starter hold',
         'The starter hold is a box measuring 1.6 by 1.2 by 1.0 metres. That gives it 1.92 cubic metres of room for everything you carry. Every piece you take aboard has to fit inside that space.'),
        ('Shape: will it fit at all?',
         'A piece comes aboard only if its shape fits, turned any way you like. Its longest side must fit the hold\'s longest side, 1.6 metres, its middle side the middle, 1.2 metres, and its shortest side the shortest, 1.0 metre. A piece too long for the hold stays out, however much room is left.'),
        ('Room: its box, not its rock',
         'Room is counted by the piece\'s box: the box that holds the piece along its three main directions. A piece uses the room of its whole box, length times width times height, not just the rock inside. A piece is taken only if the boxes already aboard, plus its own box, still fit in 1.92 cubic metres.'),
        ('Why irregular rocks waste space',
         'A rock is not a box, so the box around it has empty corners. In the game, a piece\'s own volume is about half of its box, which means each piece takes about twice the room the rock itself fills. The hold counts the box, so every piece pays this cost, whatever its shape.'),
        ('What happens while you collect',
         'When you collect, the game takes the nearest piece that fits both tests, its shape and its box. Any piece that does not fit is skipped and left in the field, and the others are still taken. When nothing else fits, the game says the hold is full.'),
        ('Choosing what to carry',
         'Because room is limited, pick the pieces worth the space. A small, valuable piece can be worth more room than a large, light one. When you unload at the Starship, your hold moves into your own space in the Starship\'s cargo hold, which also has a fixed size.'),
    ],
    "test": [
        ('How big is the starter hold?',
         [('a', '1.6 by 1.2 by 1.0 metres'), ('b', '2 by 2 by 2 metres'), ('c', '1.0 by 1.0 by 1.0 metres'), ('d', '16 by 12 by 10 metres')], 'a'),
        ('When does a piece come aboard?',
         [('a', 'When it is gold'), ('b', 'When its shape fits the hold turned any way, and its box fits the room left'), ('c', 'Always'), ('d', 'When it is the biggest piece in the field')], 'b'),
        ('What counts as the room a piece takes up?',
         [('a', 'Its weight'), ('b', 'Its colour'), ('c', 'The volume of its box, along its three main directions'), ('d', 'Its price')], 'c'),
        ('Why does an irregular rock waste room in the hold?',
         [('a', 'It is always too heavy'), ('b', 'Rocks cannot be carried'), ('c', 'It is made of gold'), ('d', 'Its box has empty corners around the rock')], 'd'),
        ('What happens to a piece that is too long for the hold, even when there is room?',
         [('a', 'It is loaded anyway'), ('b', 'It is cut in half'), ('c', 'It is skipped and left in the field'), ('d', 'It is sold at once')], 'c'),
    ],
}
