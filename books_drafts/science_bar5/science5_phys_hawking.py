"""Black Hole Thermodynamics and Hawking Radiation: horizon area and entropy, black hole temperature, evaporation, and the information puzzle."""
CODE = 'science5_phys_hawking'
BOOK = {
    "title": 'Black Hole Thermodynamics and Hawking Radiation',
    "subtitle": 'Black holes that have temperature, entropy and slow evaporation',
    "chapters": [
        ('Area and entropy',
         "In the 1970s, Jacob Bekenstein showed that a black hole's entropy is proportional to the area of its event horizon. Entropy is a measure of hidden information about a system. A bigger horizon hides more of it."),
        ('A temperature',
         "Stephen Hawking showed that black holes emit radiation with a temperature. The temperature is set by the mass: a larger black hole is colder. A black hole of the Sun's mass would be far colder than the cosmic background radiation."),
        ('Evaporation',
         'Because a black hole radiates, it slowly loses mass and shrinks. For a black hole with the mass of a star, the process is far too slow to see. Tiny black holes would evaporate faster and end in a burst.'),
        ('The information puzzle',
         'Hawking radiation appears to be thermal, meaning its pattern carries no detail about what fell in. If the black hole fully evaporates, that detail seems lost. This clashes with quantum mechanics, which says information is never destroyed.'),
        ('Analogue experiments',
         'Physicists have built laboratory systems, such as sound waves in flowing fluids, that behave like a horizon. These analogues test the basic ideas of horizon radiation, though they do not show real black holes evaporating.'),
        ('Limits of the theory',
         "Hawking's calculation uses a semiclassical picture, where gravity is classical and matter is quantum. A full theory of quantum gravity would be needed to settle the information puzzle. Many proposals exist, but none has been confirmed."),
    ],
    "test": [
        ("What is a black hole's entropy proportional to?",
         [('a', 'The colour of its light'), ('b', 'The speed of nearby stars'), ('c', 'The number of planets nearby'), ('d', 'The area of its event horizon')], 'd'),
        ('What does Hawking show about the temperature of a black hole?',
         [('a', 'Larger black holes are hotter'), ('b', 'All black holes are exactly the same temperature'), ('c', 'Black holes have no temperature at all'), ('d', 'Larger black holes are colder')], 'd'),
        ('What happens to a black hole as it emits Hawking radiation?',
         [('a', 'It grows by a large amount'), ('b', 'It turns into a star'), ('c', 'It slowly loses mass and shrinks'), ('d', 'It stops moving in space')], 'c'),
        ('What is the information puzzle?',
         [('a', 'How to read a newspaper'), ('b', 'Whether information is lost when a black hole evaporates'), ('c', 'How many stars are in a galaxy'), ('d', 'Why the Moon has craters')], 'b'),
        ('What do analogue experiments do?',
         [('a', 'Make a real black hole in a lab'), ('b', 'Turn water into gold'), ('c', 'Test the ideas of horizon radiation in a lab system'), ('d', 'Create a new planet')], 'c'),
    ],
}
