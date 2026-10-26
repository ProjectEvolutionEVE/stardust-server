"""The Inner Worlds Compared: Mercury, Venus, Earth and Mars side by side, and the debris rings in the game."""
CODE = 'science3a_inner_worlds'
BOOK = {
    "title": 'The Inner Worlds Compared',
    "subtitle": 'Mercury, Venus, Earth and Mars side by side, and the debris rings in the game',
    "chapters": [
        ("Four rocky worlds",
         "Mercury, Venus, Earth and Mars are the four rocky planets closest to the Sun. Each is made mostly of rock and metal, unlike the gas giants farther out."),
        ("Size",
         "Mercury is about 4,900 kilometres across, Mars about 6,800, Venus about 12,100 and Earth about 12,700. Venus and Earth are nearly the same width, Mars is about half of Earth's width, and Mercury is the smallest."),
        ("Distance and year",
         "Their average distances from the Sun are about 0.39, 0.72, 1.00 and 1.52 astronomical units. Their years last about 88, 225, 365 and 687 Earth days. The closer a planet is, the faster it goes around the Sun."),
        ("Moons",
         "Mercury and Venus have no moons. Earth has one large Moon, and Mars has two small ones, Phobos and Deimos."),
        ("Air and heat",
         "Venus has a very thick carbon dioxide air. Earth's air is mostly nitrogen with about a fifth oxygen. Mars has a thin carbon dioxide air, and Mercury has almost none."),
        ("The rings in the game",
         "The solar map marks the old orbits of these four worlds at their real distances. The game's story says all four were destroyed, and the cause is not known. Their remains now circle the Sun in four broad rings of debris."),
    ],
    "test": [
        ("Which of the four inner planets is the smallest?",
         [('a', 'Mars'), ('b', 'Venus'), ('c', 'Earth'), ('d', 'Mercury')], 'd'),
        ("Which two inner planets have no moons?",
         [('a', 'Mars and Earth'), ('b', 'Mercury and Venus'), ('c', 'Earth and Venus'), ('d', 'Mercury and Mars')], 'b'),
        ("About how far is Earth from the Sun, on average, in astronomical units?",
         [('a', '0.39'), ('b', '0.72'), ('c', '1.00'), ('d', '1.52')], 'c'),
        ("Which inner planet has a year of about 687 Earth days?",
         [('a', 'Mercury'), ('b', 'Venus'), ('c', 'Earth'), ('d', 'Mars')], 'd'),
        ("What does the solar map in the game mark?",
         [('a', 'The paths of comets'), ('b', 'The old orbits of the four destroyed inner planets'), ('c', 'The sites of future mines only'), ('d', 'Where the gas giants will form')], 'b'),
    ],
}
