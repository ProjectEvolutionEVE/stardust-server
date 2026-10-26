"""The Bi-elliptic Transfer: a three-burn path that can beat the Hohmann path for very large orbit changes."""
CODE = "flight4_bielliptic"
BOOK = {
    "title": "The Bi-elliptic Transfer",
    "subtitle": "A three-burn alternative for very large moves",
    "chapters": [
        ("A third burn", "The bi-elliptic transfer uses three burns instead of two. The craft first climbs on a large ellipse that goes far past the target orbit. At the far point it burns again to bring the path down, and at a third point it makes its orbit circular."),
        ("The far apogee", "The big idea is a very distant high point. The craft goes out beyond the target, then drops back. This is why the path can save fuel when the target is very far away from the start."),
        ("When it beats Hohmann", "For circles in one plane, the bi-elliptic path needs less total speed change than the Hohmann path only when the outer orbit is about twelve or more times the inner orbit's distance. For smaller changes, the two-burn Hohmann path is better."),
        ("The time penalty", "The three-burn path takes much longer. Its ellipses are large, so each lap is long. A mission that saves fuel may need many more days or months to arrive, and the crew or the cargo must wait."),
        ("A worked ratio", "Imagine a move from an orbit at a distance of one unit to one at a distance of thirty units. The bi-elliptic path can use a far point above the outer orbit, and the sum of the three burns can be smaller than the two Hohmann burns. Mission planners check the sums for each real case, because the answer changes with the ratio."),
        ("Choosing between the two", "Planners weigh fuel, time and risk. A large fuel saving may not be worth a long trip with more chances for things to go wrong. Most real moves between nearby orbits use the simpler Hohmann path, and the bi-elliptic path is kept for the rare very large jumps."),
    ],
    "test": [
        ("How many burns does the bi-elliptic transfer use?", [("a", "Three"), ("b", "Two"), ("c", "Four"), ("d", "None")], "a"),
        ("What is the main feature of the first ellipse?", [("a", "It stays close to the start"), ("b", "It is a straight line"), ("c", "It goes far past the target orbit"), ("d", "It never leaves the planet")], "c"),
        ("Roughly when does the bi-elliptic path beat the Hohmann path for circles in one plane?", [("a", "When the orbits are the same size"), ("b", "When the craft is very small"), ("c", "Never"), ("d", "When the outer orbit is about twelve or more times the inner distance")], "d"),
        ("What is the main cost of the bi-elliptic path?", [("a", "It needs no fuel"), ("b", "It takes much longer"), ("c", "It cannot be planned"), ("d", "It only works for the Moon")], "b"),
        ("Why do planners often prefer the Hohmann path for nearby orbits?", [("a", "It is slower and cheaper"), ("b", "The bi-elliptic path is illegal"), ("c", "It is simpler, and the saving from the third burn is not worth the wait"), ("d", "The Hohmann path has no burns")], "c"),
    ],
}
