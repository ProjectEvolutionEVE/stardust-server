"""Beam Stiffness and the I-Beam: why shape and depth matter more than the amount of metal."""
CODE = 'engineering3a_beam_stiffness'
BOOK = {
    "title": 'Beam Stiffness and the I-Beam',
    "subtitle": 'Why a deep, shaped beam resists bending better than a heavy solid bar',
    "chapters": [
        ('Strong is not the same as stiff',
         'A beam can be strong enough not to break and still bend too much to be useful. Stiffness is how much a beam resists bending, and it depends on the material, the length and the shape. A shelf that does not snap can still sag badly.'),
        ('Length counts most',
         'For a simple beam with a load in the middle, the sag grows with the cube of the length. Double the span and the sag becomes eight times larger. Shorten a beam a little and it becomes much stiffer.'),
        ('Shape and the second moment of area',
         'Stiffness also depends on the second moment of area, which measures how the cross section is spread about its centre. Material far from the centre counts for far more than material close to it. For a rectangle, the figure rises with the cube of its depth.'),
        ('Why an I-beam is shaped that way',
         'An I-beam puts most of its material into two flanges, at the top and bottom, and joins them with a thin web. The flanges carry the bending, and the web keeps them apart. The result is a large stiffness for the weight, which is why steel frames use I-beams so widely.'),
        ('Depth beats width',
         'If you double the depth of a rectangular beam, its stiffness rises about eight times. Doubling its width only doubles it. That is why a beam is usually set on its edge rather than laid flat.'),
        ('Check the bend before you build',
         'Work out how far a beam will sag before you build it. Compare that figure with the limit the part must meet, such as the gap to the next part. A beam that bends too much can jam a door, crack a brittle fitting or throw a sensor out of line.'),
    ],
    "test": [
        ('What is stiffness?',
         [('a', 'How bright a part is'), ('b', 'How much a part resists bending'), ('c', 'How much a part weighs'), ('d', 'How fast a part can spin')], 'b'),
        ('A simple beam with a central load has its span doubled. How much more does it sag?',
         [('a', 'Twice as much'), ('b', 'Four times as much'), ('c', 'Eight times as much'), ('d', 'The same amount')], 'c'),
        ('What does the second moment of area measure?',
         [('a', 'How heavy the beam is per metre'), ('b', 'How the cross section is spread about its centre'), ('c', 'How long the beam can be'), ('d', 'How hot the beam gets')], 'b'),
        ('Why does an I-beam have flanges at the top and bottom?',
         [('a', 'To carry most of the bending, with the web keeping them apart'), ('b', 'To make the beam float'), ('c', 'To hold paint'), ('d', 'To make the beam easier to bend')], 'a'),
        ('If you double the depth of a rectangular beam and keep its width, how does its stiffness change?',
         [('a', 'It stays the same'), ('b', 'It doubles'), ('c', 'It goes down by half'), ('d', 'It rises about eight times')], 'd'),
    ],
}
