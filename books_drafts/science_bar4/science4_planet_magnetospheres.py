"""Planetary Magnetospheres: dynamo generation, the magnetopause, radiation belts, auroras, magnetic shielding and comparing planets."""
CODE = "science4_planet_magnetospheres"
BOOK = {
    "title": "Planetary Magnetospheres",
    "subtitle": "Dynamos, boundaries, belts and auroras",
    "chapters": [
        ("Dynamo fields", "A planet's magnetic field can be made by a dynamo, the motion of an electrically conducting fluid inside the planet. Earth's field comes from the flowing liquid iron of its outer core."),
        ("The magnetopause", "The magnetopause is the boundary where a planet's magnetic field pushes back against the solar wind. Outside it, the solar wind flows past. Inside it, the planet's own field rules."),
        ("Radiation belts", "Charged particles can become trapped by magnetic fields, forming belts around a planet. Earth's Van Allen belts are the best-known example."),
        ("Auroras", "Charged particles that follow magnetic field lines into the upper atmosphere produce auroras. On Earth, the auroras appear mostly near the poles."),
        ("Magnetic shielding", "A strong magnetic field shields a planet's surface from much of the solar wind and cosmic rays. Planets without strong fields tend to lose more of their atmospheres."),
        ("Comparing planets", "Mercury, Earth, Jupiter, Saturn, Uranus and Neptune all have magnetic fields. Venus has no global field, and Mars has only weak remnants. Comparing fields means looking at their strength and their tilt."),
    ],
    "test": [
        ("What is a dynamo in a planet?",
         [("a", "An engine for spacecraft"), ("b", "A kind of volcano"), ("c", "A ring of ice"), ("d", "Moving conducting fluid that generates a magnetic field")], "d"),
        ("What is the magnetopause?",
         [("a", "The boundary where a planet's field pushes back against the solar wind"), ("b", "A ring around a comet"), ("c", "The surface of the Sun"), ("d", "A cloud over the poles")], "a"),
        ("What are the Van Allen belts?",
         [("a", "Clouds of dust"), ("b", "Rings of ice around Jupiter"), ("c", "Regions where charged particles are trapped by Earth's magnetic field"), ("d", "Layers of rock")], "c"),
        ("Where do auroras mostly appear on Earth?",
         [("a", "On the equator"), ("b", "Near the poles"), ("c", "In deserts"), ("d", "Under the oceans")], "b"),
        ("Which planet has no global magnetic field today?",
         [("a", "Earth"), ("b", "Jupiter"), ("c", "Mercury"), ("d", "Venus")], "d"),
    ],
}
