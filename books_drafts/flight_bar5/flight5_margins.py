"""Design Margins: the spare strength and capacity that keep a design safe when reality is worse than the plan."""
CODE = 'flight5_margins'
BOOK = {
    'title': 'Design Margins',
    'subtitle': 'Spare strength that keeps a design safe',
    'chapters': [
        ('What a margin is', 'A design margin is the extra capacity a part has beyond what it normally needs. It is the difference between the strength you have and the strength you expect to use.'),
        ('Safety factors', 'A safety factor is a multiplier applied to the expected load. A part built to carry three times its expected load has a safety factor of three. The right factor depends on how severe a failure would be.'),
        ('Derating', 'Derating means using a part below its rated limit, for example a power part that runs at half its rated power. Lower stress usually means a longer life and fewer surprises.'),
        ('Knockdown factors', 'Knockdown factors reduce the rated strength of a material to allow for flaws, temperature and wear. They are chosen from tests and experience, not guessed.'),
        ('Heritage', 'A design with a long record of safe use, called heritage, may earn a smaller margin. A new design needs more margin until it has been proven. Heritage must be real records, not memory.'),
        ('Margin on margin', 'Stacking many margins can make a design too heavy, too costly or too slow to build. A good engineer counts each margin once and checks the total. Ask whether a margin is covering a real risk or just adding fear.'),
    ],
    'test': [
        ('What is a design margin?', [('a', 'A line around a page'), ('b', 'The price of a part'), ('c', 'The extra capacity beyond what a part normally needs'), ('d', 'A fine for late work')], 'c'),
        ('What does a safety factor of three mean?', [('a', 'The part is built to carry three times its expected load'), ('b', 'The part weighs three tons'), ('c', 'The part has three colours'), ('d', 'The part needs three people')], 'a'),
        ('What is derating?', [('a', 'Painting a part black'), ('b', 'Raising the rated limit on paper'), ('c', 'Removing a part from the design'), ('d', 'Using a part below its rated limit')], 'd'),
        ('What does a heritage design have?', [('a', 'A new paint scheme'), ('b', 'A long, real record of safe use'), ('c', 'No records at all'), ('d', 'A promise from the designer')], 'b'),
        ('What is the risk of stacking many margins?', [('a', 'The design can become too heavy, costly or slow to build'), ('b', 'The design always becomes safer and cheaper'), ('c', 'Margins cancel each other out to zero'), ('d', 'Margins make tests unnecessary')], 'a'),
    ],
}
