"""Habitability Models and Stellar Flares: how flares from small red stars affect the air and surface of nearby planets."""
CODE = "science5_planet_habitability"
BOOK = {
    "title": "Habitability Models and Stellar Flares",
    "subtitle": "How the flares of red dwarf stars shape the chances for life on nearby planets",
    "chapters": [
        ("What habitable means", "A habitable planet is one where liquid water could exist on the surface for a long time. Scientists judge this from the planet's distance from its star, its air and its energy supply."),
        ("Flare frequency", "Small red dwarf stars can flare often and strongly, releasing bursts of light and charged particles. How often those flares happen changes how much a nearby planet is exposed."),
        ("Atmospheric erosion", "Stellar winds and high-energy light can strip gas from a planet's upper air. A planet that loses too much of its atmosphere may end up with thin air and little water."),
        ("Ultraviolet radiation", "Ultraviolet light from a flare can break apart molecules in the air and on the surface. Some of the molecules needed for life are sensitive to that damage, so the amount of ultraviolet light matters."),
        ("Habitability indices", "Habitability indices combine several measures, such as size, temperature and energy, into a single score. A high score is a useful guide, but it is not proof that life exists."),
        ("Model uncertainty", "Models of flares, air loss and surface chemistry all depend on assumptions that are not yet fully tested. Scientists try to show how much each assumption changes the final answer."),
    ],
    "test": [
        ("What does habitable mean for a planet?",
         [("a", "It is covered in ice all year"), ("b", "Liquid water could exist on the surface for a long time"), ("c", "It has no star"), ("d", "It is larger than Jupiter")], "b"),
        ("What can flares from red dwarf stars release?",
         [("a", "Pure sound"), ("b", "Solid rock"), ("c", "Cold air"), ("d", "Bursts of light and charged particles")], "d"),
        ("What can happen to a planet's air when stellar winds and high-energy light strike it?",
         [("a", "It turns into rock"), ("b", "It doubles in size"), ("c", "It can be stripped away"), ("d", "It cools to absolute zero")], "c"),
        ("What is a habitability index?",
         [("a", "A single score that combines several measures"), ("b", "A list of planet names"), ("c", "A type of telescope"), ("d", "A sports rating")], "a"),
        ("Why do habitability models carry uncertainty?",
         [("a", "They always give the same result"), ("b", "They ignore all stars"), ("c", "Their assumptions are not yet fully tested"), ("d", "They are never checked against data")], "c"),
    ],
}
