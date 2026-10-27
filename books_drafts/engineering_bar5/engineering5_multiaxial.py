"""Multiaxial Fatigue Criteria: judging fatigue when stresses act in more than one direction at once."""
CODE = "engineering5_multiaxial"
BOOK = {
    "title": "Multiaxial Fatigue Criteria",
    "subtitle": "Judging fatigue when stresses act in more than one direction at once",
    "chapters": [
        ("Stress in many directions",
         "Real parts rarely see one simple stress. Bending, twisting and pressure often act together, and a test in a single direction does not cover this."),
        ("Critical plane methods",
         "Critical plane methods check every plane through a point and find the one where damage is worst. They suit many real loads."),
        ("The Crossland criterion",
         "Crossland's criterion combines the amplitude of the shear stress with the hydrostatic stress. It is a simple rule for fatigue under combined loads."),
        ("The Dang Van criterion",
         "Dang Van uses the shear stress and the hydrostatic stress at a small scale to decide whether fatigue will start. It is often used for high-cycle fatigue."),
        ("Rotating shafts",
         "A rotating shaft carries bending and twisting that change with each turn. Multiaxial criteria help check that it will last under this combined cycling."),
        ("Choosing a criterion",
         "No single criterion fits every material and load. Pick one that has been checked against tests similar to your part."),
    ],
    "test": [
        ("Why is a test in one direction sometimes not enough?",
         [("a", "The paint is wet"), ("b", "The steel is cold"), ("c", "Real parts often see stresses in more than one direction"), ("d", "Parts are always still")], "c"),
        ("What do critical plane methods check?",
         [("a", "Every plane through a point, to find the worst one"), ("b", "Only the top plane"), ("c", "The colour"), ("d", "The price")], "a"),
        ("What does the Crossland criterion combine?",
         [("a", "Colour with weight"), ("b", "Price with time"), ("c", "Length with paint"), ("d", "Shear stress amplitude with hydrostatic stress")], "d"),
        ("Which criterion is often used for high-cycle fatigue?",
         [("a", "Price list"), ("b", "Dang Van"), ("c", "Nothing"), ("d", "Paint")], "b"),
        ("What is the right way to choose a criterion?",
         [("a", "The cheapest one"), ("b", "One checked against tests similar to your part"), ("c", "The shortest name"), ("d", "The newest one ever")], "b"),
    ],
}
