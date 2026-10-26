"""Case Study: Beagle 2. A small British lander, lost on arrival, and found years later partly opened."""
CODE = 'flight4_beagle2'
BOOK = {
    "title": "Case Study: Beagle 2",
    "subtitle": "A small lander, a silent landing and a picture from orbit",
    "chapters": [
        ("A small British lander",
         "Beagle 2 was a small British lander carried to Mars by ESA's Mars Express orbiter in 2003. It was built to search for signs of life, with a compact set of instruments."),
        ("Lost on Mars",
         "Its landing was planned for Christmas Day 2003. No signal came back. The team waited for a message that never arrived, and the lander was declared lost."),
        ("Found in 2015",
         "Years later, images from a NASA orbiter showed the lander on the surface. Its solar panels were only partly open, which may have blocked its antennas."),
        ("What went wrong",
         "Experts think the landing systems or the solar panels did not open fully. The lander may have landed hard, or its antennas may not have faced Earth. Nobody can be certain now."),
        ("Lessons",
         "Beagle 2 shows how a small mission can be undone by a few parts that do not fully open. Testing the whole sequence of steps, not only the single parts, matters a great deal."),
        ("Why we remember it",
         "The lander is remembered as a brave, small project. It showed that a team can build a whole lander on a tight budget, and it taught hard lessons for later missions."),
    ],
    "test": [
        ("Which country built Beagle 2?",
         [("a", "Britain"), ("b", "Japan"), ("c", "Russia"), ("d", "Brazil")], "a"),
        ("Which orbiter carried Beagle 2 to Mars?",
         [("a", "Apollo"), ("b", "Voyager"), ("c", "Mars Express"), ("d", "Skylab")], "c"),
        ("What date was its planned landing?",
         [("a", "1 January"), ("b", "Christmas Day 2003"), ("c", "4 July"), ("d", "31 October")], "b"),
        ("Where was the lander found in 2015?",
         [("a", "On the Moon"), ("b", "In images from a NASA orbiter"), ("c", "In a museum"), ("d", "At sea")], "b"),
        ("What might have blocked its antennas?",
         [("a", "Solar panels that were not fully open"), ("b", "Snow"), ("c", "Dust bags"), ("d", "Cake")], "a"),
    ],
}
