"""Fracture Toughness Testing: how engineers measure how easily a crack runs through a material, and how to trust the number."""
CODE = 'mining5_kic'
BOOK = {
    "title": 'Fracture Toughness Testing',
    "subtitle": 'Measuring how easily a crack runs through a material',
    "chapters": [
        ('What toughness means', 'Fracture toughness measures how well a material resists a crack that is already there. A material with high toughness can take a crack without breaking suddenly. Engineers use it to choose safe materials.'),
        ('K-IC', 'K-IC is the plane-strain fracture toughness, a standard number found by testing a cracked specimen. The test is done under strict rules set by standards bodies. Each result is only valid if the test was done right.'),
        ('Specimen size', 'The specimen must be thick enough and large enough. If it is too small, the result depends on the size and not on the material. Standards give minimum sizes for a valid answer.'),
        ('Plane strain', 'Plane strain is the condition where the crack is held back in the thick middle of a part. It gives the lowest and most cautious toughness value. Thin parts can behave differently, so the test is chosen to match the use.'),
        ('The J-integral', 'For tougher materials that bend before they break, the J-integral is used instead. It measures the energy release around the crack tip. Its results need their own test rules.'),
        ('Standards and use', 'Standards set how to prepare, load and read each test. The toughness number is then used in design and in inspection rules. Any number used in a design must come from a valid test.'),
    ],
    "test": [
        ('What does fracture toughness measure?', [('a', 'How shiny a metal is'), ('b', 'How light a bar is'), ('c', 'How well a material resists a crack that is already there'), ('d', 'How cold the room is')], 'c'),
        ('What does K-IC stand for?', [('a', 'A kind of kitchen knife'), ('b', 'A computer code'), ('c', 'A brand of paint'), ('d', 'The plane-strain fracture toughness')], 'd'),
        ('Why must the specimen be big enough?', [('a', 'A small specimen gives a result that depends on size, not the material'), ('b', 'Bigger specimens are cheaper'), ('c', 'Small specimens are always stronger'), ('d', 'Size has no effect at all')], 'a'),
        ('When is plane strain present?', [('a', 'On the surface of a sheet of paper'), ('b', 'In the thick middle of a part, where the crack is held back'), ('c', 'Inside a glass of water'), ('d', 'In the open air')], 'b'),
        ('When is the J-integral used?', [('a', 'For brittle glass only'), ('b', 'For sugar cubes'), ('c', 'For tougher materials that bend before they break'), ('d', 'For paper cups')], 'c'),
    ],
}
