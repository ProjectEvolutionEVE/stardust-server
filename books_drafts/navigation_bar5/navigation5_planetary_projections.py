"""Projections for Planetary Maps: datums, standards and names for worlds other than Earth."""
CODE = "navigation5_planetary_projections"
BOOK = {
    "title": "Projections for Planetary Maps",
    "subtitle": "Mapping Mars and the Moon with shared standards",
    "chapters": [
        ("Other worlds, other maps", "Planets and moons are mapped with the same ideas used on Earth, but each body has its own shape and reference. A datum sets the reference shape and the origin."),
        ("Mars and the Moon", "Mars and the Moon each have their own coordinate systems and reference shapes. Mapmakers choose a projection that suits the region they map."),
        ("Standards", "The International Astronomical Union publishes standard rotation and coordinate values for planets and moons. Using the same values lets scientists compare maps."),
        ("Naming", "The IAU approves names for features on planets and moons. Many names honour scientists, explorers and other historical figures."),
        ("Uses", "Planetary maps help plan landings, guide rovers and plan science. A good map records its datum so that later users can match it to other maps."),
        ("Care", "The exact shape of many small bodies is less well known than Earth's. Mapmakers state the uncertainty, and every record names the datum used."),
    ],
    "test": [
        ("What does a datum set?",
         [("a", "The colour of a map"), ("b", "The reference shape and origin"), ("c", "The number of planets"), ("d", "The paper size")], "b"),
        ("Which two bodies have their own map systems discussed here?",
         [("a", "Venus and Saturn"), ("b", "Jupiter and Neptune"), ("c", "Pluto and the Sun"), ("d", "Mars and the Moon")], "d"),
        ("Which body publishes standard planetary coordinate values?",
         [("a", "The World Health Organization"), ("b", "The International Astronomical Union"), ("c", "The World Bank"), ("d", "The Red Cross")], "b"),
        ("Who approves names for features on planets and moons?",
         [("a", "The IAU"), ("b", "The mission cook"), ("c", "The paper maker"), ("d", "Nobody, names are random")], "a"),
        ("Why should a planetary map record its datum?",
         [("a", "To look fancy"), ("b", "To make the map heavier"), ("c", "So later users can match it to other maps"), ("d", "To hide the shape")], "c"),
    ],
}
