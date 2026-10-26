"""Case Study: Voyager 2's Grand Tour. A rare alignment, four giant planets and gravity to speed the way."""
CODE = 'flight4_voyager2'
BOOK = {
    "title": "Case Study: Voyager 2's Grand Tour",
    "subtitle": "A rare alignment, four giant planets and gravity to speed the way",
    "chapters": [
        ("A rare alignment",
         "Voyager 2 launched in 1977, during a rare alignment of the outer planets. Such lineups come only about once every 175 years, so the trip could visit four giant planets using their gravity."),
        ("Jupiter and Saturn",
         "The probe flew past Jupiter in 1979 and Saturn in 1981. Each close pass bent the path and sped the craft on toward its next target."),
        ("Uranus",
         "In 1986 Voyager 2 became the only spacecraft to visit Uranus. It revealed the planet's pale blue colour, its faint rings and several new moons."),
        ("Neptune",
         "In 1989 it reached Neptune, the last of the giant planets on its route. It found powerful winds and a large dark spot, and it studied the moon Triton closely."),
        ("The long reach",
         "Voyager 2 has been sending data from far beyond the planets for decades. Its radio signal takes many hours to reach Earth, because the craft is so far away."),
        ("The lesson",
         "Voyager 2 shows the power of planning, patience and gravity assists. A rare alignment opened a route that could not be repeated soon, and careful design made the most of it."),
    ],
    "test": [
        ("When did Voyager 2 launch?",
         [("a", "1969"), ("b", "1977"), ("c", "2003"), ("d", "1986")], "b"),
        ("How many giant planets did it visit?",
         [("a", "Two"), ("b", "Four"), ("c", "One"), ("d", "Eight")], "b"),
        ("Which planet did it visit in 1986?",
         [("a", "Neptune"), ("b", "Mars"), ("c", "Uranus"), ("d", "Venus")], "c"),
        ("What did it reach in 1989?",
         [("a", "Neptune"), ("b", "The Sun"), ("c", "Mars"), ("d", "Saturn")], "a"),
        ("What helped speed the craft on from one planet to the next?",
         [("a", "Gravity assists"), ("b", "Sails"), ("c", "Magnets"), ("d", "Wind")], "a"),
    ],
}
