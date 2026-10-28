"""Continuous Casting: how molten metal becomes a long solid strand without a mould for each piece."""
CODE = 'mining4_continuous_casting'
BOOK = {
    "title": 'Continuous Casting',
    "subtitle": 'Moulds and strands: how molten steel becomes slabs and blooms',
    "chapters": [
        ('A strand that never stops',
         'In continuous casting, molten metal flows into an open-ended water-cooled mould. The outside cools to a solid skin while the core is still liquid. Rollers pull the strand down and out, and it is cut into lengths.'),
        ('The mould',
         'The mould is usually made of copper, because copper carries heat away quickly. Cooling water runs through channels behind it. A flux powder on top of the melt keeps the surface clean and helps lubricate the strand.'),
        ('The solid shell',
         'The shell thickens as the strand moves down, and its thickness depends on how fast it is pulled and how well it is cooled. If the shell is too thin when it leaves the mould, it can burst and spill molten metal.'),
        ('Shapes that come out',
         'Slabs are wide and flat and are later rolled into plate or sheet. Blooms and billets are smaller and square, and are rolled into bars, beams and wire. The mould shape decides which form comes out.'),
        ('Segregation and losses',
         'Some elements gather in the centre of the strand as it solidifies, which is called segregation. The ends of each length are cut off, and any cracked or faulty lengths are scrapped, so some metal is always lost.'),
        ('Quality checks',
         'Inspectors check the surface for cracks, measure the size, and test samples for chemistry and inclusions. Good casting practice keeps the yield high, which means more usable metal from each tonne of melt.'),
    ],
    "test": [
        ('What happens inside the mould in continuous casting?',
         [('a', 'The metal is sprayed into dust'), ('b', 'The metal is heated to vapour'), ('c', 'A solid skin forms while the core is still liquid'), ('d', 'Nothing; the mould is only a stand')], 'c'),
        ('Why is copper often used for the mould?',
         [('a', 'It carries heat away quickly'), ('b', 'It is very soft'), ('c', 'It is cheap to paint'), ('d', 'It never conducts heat')], 'a'),
        ('What is segregation in a cast strand?',
         [('a', 'Cutting the strand into equal lengths'), ('b', 'Painting the surface'), ('c', 'The strand splitting into two'), ('d', 'Some elements gathering in the centre as it solidifies')], 'd'),
        ('Which shape is usually rolled into plate or sheet?',
         [('a', 'A billet'), ('b', 'A slab'), ('c', 'A bloom'), ('d', 'A ball')], 'b'),
        ('What does a high yield in casting mean?',
         [('a', 'More scrap from each cast'), ('b', 'A slower pour'), ('c', 'More usable metal from each tonne of melt'), ('d', 'A thicker mould')], 'c'),
    ],
}
