"""Grid North and Convergence: why a map's north is not quite the true north."""
CODE = "navigation4_grid_convergence"
BOOK = {
    "title": "Grid North and Convergence",
    "subtitle": "Why the map's north is not the true north",
    "chapters": [
        ("Three norths", "A map can show several north directions. True north points toward the geographic pole. Grid north points along the grid lines of the map. Magnetic north points toward the magnetic pole."),
        ("Grid north versus true north", "Grid north and true north agree only on the central meridian. Elsewhere the grid lines turn relative to true north. That difference is the convergence."),
        ("The convergence angle", "The convergence angle is the angle between grid north and true north at a point. It is zero on the central meridian. Surveyors calculate it for each point they measure."),
        ("Growth away from the centre", "The convergence grows as you move away from the central meridian. It also changes with latitude. Large survey areas need that change accounted for."),
        ("Correcting bearings", "To change a bearing from true to grid, you apply the convergence. The sign depends on which side of the central meridian you are. Check the sign with a simple sketch."),
        ("Grid to true, and checking", "Converting grid to true is the reverse of the correction. A simple sketch helps check the sign. A second check with software confirms the answer."),
    ],
    "test": [
        ("Which north is the direction to the geographic pole?",
         [("a", "Grid north"), ("b", "Magnetic north"), ("c", "True north"), ("d", "Solar north")], "c"),
        ("Where do grid north and true north agree?",
         [("a", "On the equator"), ("b", "At the Moon"), ("c", "At sea only"), ("d", "On the central meridian")], "d"),
        ("What is the convergence angle?",
         [("a", "The angle between grid north and true north"), ("b", "The angle of a ship's roll"), ("c", "The tilt of a satellite"), ("d", "The angle of a tide")], "a"),
        ("How does convergence change as you move away from the central meridian?",
         [("a", "It grows"), ("b", "It shrinks to zero"), ("c", "It stays the same"), ("d", "It flips every minute")], "a"),
        ("What is the reverse of applying convergence?",
         [("a", "Converting a colour"), ("b", "Converting grid to true"), ("c", "Measuring a height"), ("d", "Counting satellites")], "b"),
    ],
}
