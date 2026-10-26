"""Casting: patterns, moulds and shrinkage, and how molten metal takes a shape and then gets smaller."""
CODE = 'engineering3b_casting'
BOOK = {
    "title": 'Casting: Patterns, Moulds and Shrinkage',
    "subtitle": 'From a pattern to a finished part: how molten metal takes a shape, and why it comes out smaller',
    "chapters": [
        ('A pattern makes the mould',
         'Casting starts with a pattern, a copy of the part, often made of wood, plastic or metal. The pattern is pressed into damp sand, or another mould material, and then lifted out, leaving a hollow shape. Molten metal is poured into that hollow, and it takes the shape of the part.'),
        ('Cores make the holes',
         'A part with a hollow inside, such as an engine block, needs a core: a shaped piece of sand set into the mould to leave the empty space. The core must stay in place while the metal flows around it. After the metal cools, the sand is knocked out and the hollow is left behind.'),
        ('Metal shrinks as it cools',
         'Most metals take up less space as they cool from liquid to solid, and they shrink a little more as they cool to room temperature. Foundry workers make the pattern a little larger than the finished size to allow for this, which is called shrink allowance. Each metal has its own allowance, because steel shrinks more than aluminium.'),
        ('Dies for many parts',
         'Die casting forces molten metal, often zinc, aluminium or magnesium, into a steel die under high pressure. It makes many identical parts quickly, with smooth surfaces and close sizes. The dies cost a lot to make, so die casting pays only when many parts are needed.'),
        ('Lost wax for fine detail',
         'Investment casting, also called lost wax, starts with a wax copy of the part. The wax is coated in a ceramic shell, then melted out, leaving a precise cavity for the metal. Jewellery and jet engine blades are often made this way.'),
        ('Check the casting',
         'A casting can hide bubbles, cracks and cold shuts, where two streams of metal failed to fuse. Check it by eye, by dye penetrant or by X-ray. A flaw found early costs far less than one found after the part has been fitted into a machine.'),
    ],
    "test": [
        ('What is a pattern in casting?',
         [('a', 'A copy of the part that is pressed into the mould material to make the hollow'), ('b', 'A type of welding torch'), ('c', 'The final polished part'), ('d', 'A tool for drilling holes')], 'a'),
        ('Why does a casting need a core?',
         [('a', 'To stop the metal from melting'), ('b', 'To hold the mould together with glue'), ('c', 'To leave a hollow space inside the part'), ('d', 'To turn the metal into a gas')], 'c'),
        ('Why is a pattern made a little larger than the finished size?',
         [('a', 'Because metal gets heavier as it cools'), ('b', 'Because the sand takes up room'), ('c', 'So the part can be sanded smooth afterwards'), ('d', 'To allow for the metal shrinking as it cools')], 'd'),
        ('Which process forces molten metal into a steel die under high pressure?',
         [('a', 'Sand casting'), ('b', 'Die casting'), ('c', 'Forging'), ('d', 'Brazing')], 'b'),
        ('What is the lost wax method also called?',
         [('a', 'Forging'), ('b', 'Die casting'), ('c', 'Investment casting'), ('d', 'Soldering')], 'c'),
    ],
}
