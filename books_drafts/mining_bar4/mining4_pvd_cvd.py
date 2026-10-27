"""Vapour Deposition: PVD and CVD, the two main ways of laying a very thin film of material on a surface."""
CODE = 'mining4_pvd_cvd'
BOOK = {
    "title": 'Vapour Deposition: PVD and CVD',
    "subtitle": 'Laying thin films on a surface, in a vacuum or from a gas',
    "chapters": [
        ('Thin films',
         'A thin film is a layer of material only a few atoms to a few microns thick. Thin films change how a surface looks, wears, conducts electricity or reflects light. Vapour deposition is the main way to make them.'),
        ('Physical vapour deposition',
         'In PVD, a solid source is turned into vapour inside a vacuum chamber, either by evaporation or by sputtering, where ions knock atoms off a target. The vapour travels in a straight line and settles on the part.'),
        ('Chemical vapour deposition',
         'In CVD, gases react on a heated surface and leave a solid film behind. The reaction makes the film, so the gases must be chosen with care. CVD can coat complex shapes more evenly than a straight-line process.'),
        ('Tool coatings',
         "Cutting tools are often coated with very hard films, such as titanium nitride. The coating lets the tool run hotter and last longer. The film is only a few microns, but it changes the tool's life."),
        ('Vacuum systems',
         'PVD needs a good vacuum so the vapour does not hit stray gas atoms. Pumps, gauges and seals must be kept clean. A leak or dirty chamber spoils the film.'),
        ('Film quality',
         'Makers judge a film by its thickness, its evenness, how well it sticks to the base, and how free it is of pores. Each check is done with the right test, and the process is tuned until the film meets the spec.'),
    ],
    "test": [
        ('What is a thin film in this context?',
         [('a', 'A block of metal several centimetres thick'), ('b', 'A sheet of paper'), ('c', 'A layer only a few atoms to a few microns thick'), ('d', 'A liquid drop')], 'c'),
        ('What does PVD usually need to work well?',
         [('a', 'A good vacuum'), ('b', 'Open air full of stray gas'), ('c', 'A deep ocean'), ('d', 'A bath of cold water')], 'a'),
        ('In CVD, how is the film formed?',
         [('a', 'By freezing a liquid'), ('b', 'By pressing powder'), ('c', 'By spraying paint'), ('d', 'By gases reacting on a heated surface')], 'd'),
        ('Which coating is often put on cutting tools?',
         [('a', 'Sugar syrup'), ('b', 'Titanium nitride'), ('c', 'Wood varnish'), ('d', 'Cooking oil')], 'b'),
        ("Which of these judges a film's quality?",
         [('a', 'The colour of the vacuum pump'), ('b', 'How many people watch the chamber'), ('c', 'Its thickness, evenness and adhesion'), ('d', 'The weight of the operator')], 'c'),
    ],
}
