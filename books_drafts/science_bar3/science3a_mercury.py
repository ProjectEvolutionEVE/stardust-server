"""Mercury as It Was: the smallest planet, real data before its loss in the game's story."""
CODE = 'science3a_mercury'
BOOK = {
    "title": 'Mercury as It Was',
    "subtitle": 'The smallest planet, and what real data says about it',
    "chapters": [
        ("The smallest planet",
         "Mercury is the smallest planet, about 4,900 kilometres across, a little over a third of Earth's width. It is still larger than Earth's Moon."),
        ("Closest to the Sun",
         "Mercury orbits closest to the Sun, at an average distance of about 0.39 astronomical units, or roughly 58 million kilometres. Sunlight there is several times stronger than at Earth."),
        ("A short year",
         "Mercury goes around the Sun in about 88 Earth days, the shortest year of any planet. Its day, from one sunrise to the next, is much longer than its year."),
        ("A huge iron core",
         "For its size, Mercury is very dense, second only to Earth. Its iron core is so large that it fills most of the planet's radius, with only a thin rocky mantle and crust around it."),
        ("Hot days, cold nights",
         "The surface can reach about 430 degrees Celsius in the day and fall to about minus 180 at night. Mercury has almost no air to hold the heat, so the swing is enormous."),
        ("Mercury in the game",
         "The Mercury ring on the solar map marks where the planet used to orbit, at its real average distance. The game's story says it was destroyed, and its remains now lie in the debris fields."),
    ],
    "test": [
        ("Which planet is the smallest?",
         [('a', 'Mars'), ('b', 'Venus'), ('c', 'Mercury'), ('d', 'Earth')], 'c'),
        ("About how many Earth days long is Mercury's year?",
         [('a', 'About 25'), ('b', 'About 88'), ('c', 'About 365'), ('d', 'About 687')], 'b'),
        ("Why does Mercury's surface temperature swing so widely?",
         [('a', 'It has almost no air to hold the heat'), ('b', 'It is covered in ice'), ('c', 'It has a thick cloud layer'), ('d', 'It has two large moons')], 'a'),
        ("Mercury is very dense for its size. Which planet is denser?",
         [('a', 'Mars'), ('b', 'Jupiter'), ('c', 'Earth'), ('d', 'Saturn')], 'c'),
        ("Which mission first mapped Mercury, with flybys in 1974 and 1975?",
         [('a', 'Mariner 10'), ('b', 'Voyager 1'), ('c', 'Apollo 11'), ('d', 'Galileo')], 'a'),
    ],
}
