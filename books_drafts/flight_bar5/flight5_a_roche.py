"""The Roche Limit and Rings: why some bodies break up when they come close, and how rings form."""
CODE = 'flight5_a_roche'
BOOK = {
    "title": 'The Roche Limit and Rings',
    "subtitle": 'Why some bodies break up, and how rings form',
    "chapters": [
        ('Breakup distance',
         'A body held together only by its own gravity can be pulled apart if it comes too close to a larger body. The distance at which this happens is the Roche limit. It depends on the density of the two bodies.'),
        ('Why rings form',
         'Material inside the Roche limit cannot clump into one moon, because the tides keep pulling it apart. It instead spreads into a ring of small pieces, each following its own orbit around the planet.'),
        ("Saturn's rings",
         'Saturn has bright, broad rings made of countless pieces of ice and rock. They lie inside the region where a large moon could not hold together. The rings are a striking example of this limit at work.'),
        ('Comet Shoemaker-Levy 9',
         'In 1992 a comet passed very close to Jupiter and was broken into many pieces by the tidal pull. In 1994 the fragments struck Jupiter, leaving dark marks that could be seen for months. It was a rare, real example of tidal breakup.'),
        ('Moons and rings',
         'Many moons of the giant planets keep their rings close by, or sweep material into them. Some small moons help shape the edges of rings. The interplay of moons and rings is one of the richest topics in planetary science.'),
        ('Formulas in words',
         "For a fluid body of similar density, the breakup distance is roughly two and a half times the planet's radius. Denser bodies can survive closer in. The exact number depends on the material."),
    ],
    "test": [
        ('What is the Roche limit?',
         [('a', 'The highest speed a rocket can reach'), ('b', 'The distance inside which a body held by its own gravity can be torn apart'), ('c', 'The length of a day on the Moon'), ('d', 'The depth of a crater')], 'b'),
        ('Why does material inside the Roche limit often spread into a ring?',
         [('a', 'Because it is made of glass'), ('b', 'Because it is hot'), ('c', 'Because the tides keep it from clumping into one moon'), ('d', 'Because it is far from the planet')], 'c'),
        ('What broke up in the 1992 event at Jupiter?',
         [('a', "Saturn's rings"), ('b', 'The Sun'), ('c', 'A space station'), ('d', 'Comet Shoemaker-Levy 9')], 'd'),
        ('What does the Roche limit depend on?',
         [('a', 'The density of the two bodies'), ('b', 'The colour of the planet'), ('c', 'The number of rings'), ('d', 'The date of the year')], 'a'),
        ("What are Saturn's rings mostly made of?",
         [('a', 'Countless pieces of ice and rock'), ('b', 'Pure gold'), ('c', 'Glass sheets'), ('d', 'Liquid water in a single layer')], 'a'),
    ],
}
