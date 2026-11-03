"""Terrain-referenced navigation: matching radar altimeter height profiles to a stored terrain height map."""
CODE = "navigation4_terrain_reference"
BOOK = {
    "title": "Terrain-Referenced Navigation",
    "subtitle": "Matching the ground below to a stored map",
    "chapters": [
        ("Matching the ground", "Terrain-referenced navigation compares the height of the ground below with a stored map of heights. A radar altimeter measures the height beneath the craft. The match gives a position fix."),
        ("The terrain height map", "The stored map gives the ground height at many points on a grid. The map must be accurate and up to date. Its quality sets the limit on the fix."),
        ("The radar altimeter", "A radar altimeter sends a radio pulse down and times its return. This gives the height above the ground. Taken along a path, these readings form a height profile."),
        ("Profile matching", "The measured profile is slid along the map to find the best fit. The place where the profile matches best gives the position. Many matches over time refine the answer."),
        ("Terrain shape", "Hills and valleys give a distinct profile, which makes matching easy. Flat ground gives a flat profile, which is hard to match. The best terrain is rugged and varied."),
        ("Limits", "Over flat country the method can fail or give an uncertain fix. Water and forest can also confuse the signal. A navigator should combine it with other aids."),
    ],
    "test": [
        ("What does terrain-referenced navigation compare?", [("a", "Two satellite clocks"), ("b", "The measured ground height with a stored height map"), ("c", "The speed of two cars"), ("d", "The colour of two maps")], "b"),
        ("What instrument measures the height below the craft?", [("a", "A kitchen timer"), ("b", "A barometer in a jar"), ("c", "A pocket torch"), ("d", "A radar altimeter")], "d"),
        ("What is profile matching?", [("a", "Sliding the measured height profile along the map to find the best fit"), ("b", "Painting the map onto the ground"), ("c", "Counting birds on the terrain"), ("d", "Turning the map into a song")], "a"),
        ("Why is flat ground hard for this method?", [("a", "Flat ground is too bright for radar"), ("b", "Flat ground has no gravity"), ("c", "A flat profile gives little to match"), ("d", "Flat ground always has tall trees")], "c"),
        ("Which terrain suits this method best?", [("a", "Open calm water"), ("b", "A perfectly flat salt plain"), ("c", "Rugged, varied ground"), ("d", "A smooth, empty car park")], "c"),
    ],
}
