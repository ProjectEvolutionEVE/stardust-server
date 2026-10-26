"""Technical Drawings: views, dimensions and scale, and how an engineering drawing shows a part exactly."""
CODE = 'engineering2_drawings'
BOOK = {
    "title": 'Technical Drawings: Views, Dimensions and Scale',
    "subtitle": 'How an engineering drawing shows a part from every side, with exact sizes',
    "chapters": [
        ('One part, several views',
         "A part is drawn from several sides, called views, usually front, top and side. Each view shows what the others cannot. "
         "Orthographic views are lined up, so a point seen in one view can be found in the next."),
        ('First and third angle',
         "Drawings use one of two layouts: first angle projection, common in Europe, or third angle projection, common in North America. "
         "A small symbol on the drawing shows which one is used. Misreading the layout can build a part backwards."),
        ('Lines carry meaning',
         "A solid line shows a visible edge. A dashed line shows a hidden edge behind a surface. A centre line, a thin chain of long and "
         "short dashes, marks the middle of holes and round parts. Each line type has its own meaning."),
        ('Section views',
         "A section view cuts through the part, as if it were sliced, and shows what lies inside, such as the wall of a tube or the bore "
         "of a hole. The cut is marked on the outside view, and the cut surface is shaded with hatching."),
        ('Dimensions and tolerances',
         "Each size is written with a dimension line, an arrow at each end, and its number above the line, in one unit. Give each "
         "dimension once, where it is most useful, because a repeated dimension invites mistakes. Tolerances are written with the size."),
        ('Scale',
         "A drawing is often smaller or larger than the real part. A scale of 1:2 means the drawing is half size, and 2:1 means double "
         "size. Always check the scale, and read the dimension written on the drawing rather than measuring the paper by eye."),
    ],
    "test": [
        ("What is a section view?",
         [('a', 'A view of the part from above only'), ('b', 'A photograph of the part'), ('c', 'A view cut through the part, to show what is inside'), ('d', 'A list of the part weights')], 'c'),
        ("What do dashed lines show on a drawing?",
         [('a', 'Hidden edges behind a surface'), ('b', 'The outer edges'), ('c', 'Dimensions'), ('d', 'Paint')], 'a'),
        ("What does a drawing at scale 1:2 mean?",
         [('a', 'Twice the real size'), ('b', 'Half the real size'), ('c', 'The same size'), ('d', 'Four times the real size')], 'b'),
        ("What does a centre line mark?",
         [('a', 'The price of the part'), ('b', 'The weight of the part'), ('c', 'The colour of the part'), ('d', 'The middle of holes and round parts')], 'd'),
        ("Why must you know whether a drawing uses first or third angle projection?",
         [('a', 'A part can be built backwards if the layout is misread'), ('b', 'It changes the colour of the part'), ('c', 'It changes the weight of the part'), ('d', 'It has no effect at all')], 'a'),
    ],
}
