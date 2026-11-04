"""Asteroid Taxonomy from Spectra: how the colour of reflected light sorts asteroids into families and links them to meteorites."""
CODE = "science5_planet_asteroid_tax"
BOOK = {
    "title": "Asteroid Taxonomy from Spectra",
    "subtitle": "Sorting asteroids by the light they reflect, and linking them to meteorites",
    "chapters": [
        ("Reading reflected light", "Asteroids shine only by reflecting sunlight. The way an asteroid reflects light at different colours carries clues about its surface materials, so astronomers study its spectrum closely."),
        ("Spectral classes", "Asteroids with similar spectra are grouped into classes. The S-type class has stony, fairly bright surfaces, while the C-type class is dark and rich in carbon-based material."),
        ("Albedo", "Albedo is the share of light an object reflects. A bright asteroid has a high albedo and a dark one has a low albedo, and this measurement helps separate classes that look alike in colour."),
        ("Colour indices", "Colour indices compare the brightness of an asteroid through filters of different colours. They are a quick way to sort large numbers of asteroids before a full spectrum is measured."),
        ("Taxonomy systems", "Several taxonomy systems have been built over the years to group asteroids. Each one uses the spectral features and the albedo in its own way, so scientists must say which system they use."),
        ("Meteorite links", "Meteorites that fall to Earth can be matched to asteroid classes. Many ordinary stony meteorites match S-type asteroids, and some carbonaceous meteorites match the dark C-type group."),
    ],
    "test": [
        ("What do asteroids shine by?",
         [("a", "Reflecting sunlight"), ("b", "Their own light"), ("c", "Burning gas"), ("d", "Radio signals from Earth")], "a"),
        ("Which asteroid class is described as dark and carbon-rich?",
         [("a", "S-type"), ("b", "M-type"), ("c", "C-type"), ("d", "V-type")], "c"),
        ("What is albedo?",
         [("a", "The size of a crater"), ("b", "The speed of an asteroid"), ("c", "The temperature of the core"), ("d", "The share of light an object reflects")], "d"),
        ("What is the purpose of colour indices?",
         [("a", "To make asteroids change colour"), ("b", "To sort large numbers of asteroids quickly before a full spectrum is measured"), ("c", "To measure the distance to Earth"), ("d", "To count meteors in the sky")], "b"),
        ("Which asteroid class do many ordinary stony meteorites match?",
         [("a", "Comets"), ("b", "C-type"), ("c", "Gas giants"), ("d", "S-type")], "d"),
    ],
}
