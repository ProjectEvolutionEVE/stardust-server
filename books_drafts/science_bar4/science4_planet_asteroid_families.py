"""Asteroid Belt Families and Gaps: asteroid families, Kirkwood gaps, collisional families, Vesta and Ceres, resonances, and sampling the population."""
CODE = "science4_planet_asteroid_families"
BOOK = {
    "title": "Asteroid Belt Families and Gaps",
    "subtitle": "Families, gaps and surveys of the asteroid belt",
    "chapters": [
        ("The asteroid belt", "The asteroid belt lies between Mars and Jupiter. It holds millions of rocky bodies, and their total mass is less than that of the Moon."),
        ("Asteroid families", "Asteroids that share similar orbits and similar composition often come from the same parent body. Such a group is called a family."),
        ("Kirkwood gaps", "The Kirkwood gaps are narrow regions of the belt with very few asteroids. They lie where an orbit would be locked in a strong resonance with Jupiter."),
        ("Collisional families", "A collision can shatter an asteroid and leave a family of fragments on similar orbits. Scientists identify family members using their orbits and their colours."),
        ("Vesta and Ceres", "Vesta is a large asteroid, brighter than most, with a basaltic surface. Ceres is the largest object in the belt and is classed as a dwarf planet."),
        ("Sampling the population", "Astronomers estimate the total population by surveying part of the sky and scaling up the results. Careful statistics are needed, because surveys see some objects far better than others."),
    ],
    "test": [
        ("Where is the asteroid belt located?",
         [("a", "Between Mars and Jupiter"), ("b", "Beyond Neptune"), ("c", "Inside the orbit of Mercury"), ("d", "Around Earth")], "a"),
        ("What are Kirkwood gaps?",
         [("a", "Holes in the Moon"), ("b", "Narrow regions with very few asteroids, linked to resonance with Jupiter"), ("c", "Rivers on Ceres"), ("d", "Gaps between the rings of planets")], "b"),
        ("What is an asteroid family?",
         [("a", "A group of planets"), ("b", "A pile of comets"), ("c", "A group of asteroids with similar orbits, often from one broken parent body"), ("d", "A set of moons around Ceres")], "c"),
        ("Which is the largest object in the asteroid belt?",
         [("a", "Vesta"), ("b", "Pallas"), ("c", "Hygiea"), ("d", "Ceres")], "d"),
        ("What type of rock is Vesta thought to have on its surface?",
         [("a", "Ice"), ("b", "Basalt"), ("c", "Gold"), ("d", "Salt")], "b"),
    ],
}
