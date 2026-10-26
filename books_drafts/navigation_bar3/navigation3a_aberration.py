"""Aberration: starlight appears to lean toward the way you move, because your own motion changes the view."""
CODE = 'navigation3a_aberration'
BOOK = {
    "title": 'Aberration: Starlight Leans',
    "subtitle": 'How your own motion shifts the stars in the sky',
    "chapters": [
        ('Rain on a moving window',
         'Imagine rain falling straight down. Walk across the street, and the rain seems to slant toward you. The rain has not changed direction. Your motion has changed how it looks, and starlight behaves the same way.'),
        ('The effect on starlight',
         "Earth moves round the Sun at about 30 kilometres a second. Light from a distant star reaches a telescope while the telescope is moving, so the star appears a little away from its true place, pulled toward the direction of Earth's motion."),
        ('Found by Bradley',
         'In the 1720s the English astronomer James Bradley noticed that stars shifted through the year in a small circle. He first looked for stellar parallax, but found this different effect. His explanation, aberration, was an early clue that light has a finite speed.'),
        ('How large it is',
         'The largest shift is about 20.5 arcseconds. That is tiny, about the width of a coin seen from several kilometres away. Small as it is, it must be included in any precise position, or a telescope aims a little wrong.'),
        ('The ship in motion',
         "A craft moving at speed sees starlight shifted in the same way, and a moving craft must correct its star sights for this. The faster the craft, the larger the shift. A navigator who ignores the craft's motion gets the star's place wrong."),
        ('Keeping the sum correct',
         'Good navigators list each correction separately: light time, aberration, precession and parallax. Each one is small on its own, but together they decide whether the fix lands where you think it does.'),
    ],
    "test": [
        ('What causes aberration of starlight?',
         [('a', "The observer's own motion relative to the light"), ('b', 'Clouds in the atmosphere'), ('c', 'The colour of the star'), ('d', 'The age of the Moon')], 'a'),
        ('Roughly how fast does Earth move round the Sun?',
         [('a', 'About 30 metres a second'), ('b', 'About 300 kilometres an hour'), ('c', 'About 30 kilometres a second'), ('d', 'It does not move')], 'c'),
        ('Who first noticed the effect of aberration in the 1720s?',
         [('a', 'Isaac Newton'), ('b', 'James Bradley'), ('c', 'Ole Rømer'), ('d', 'Johannes Kepler')], 'b'),
        ('What is the largest shift of a star from aberration?',
         [('a', 'About 20.5 degrees'), ('b', 'About 20.5 kilometres'), ('c', 'About 2,000 degrees'), ('d', 'About 20.5 arcseconds')], 'd'),
        ('Why must a moving craft correct its star sights?',
         [('a', 'Because its own motion shifts the apparent place of each star'), ('b', 'Because stars move faster at night'), ('c', 'Because the hull blocks light'), ('d', 'Because the sextant gets heavier')], 'a'),
    ],
}
