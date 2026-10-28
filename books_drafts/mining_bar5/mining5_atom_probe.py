"""Atom Probe Tomography: pulling single atoms off a sharp tip to rebuild a three-dimensional map of a metal's atoms."""
CODE = "mining5_atom_probe"
BOOK = {
    "title": "Atom Probe Tomography",
    "subtitle": "Peeling a metal one atom at a time to map it in three dimensions",
    "chapters": [
        ("A needle-sharp sample", "Atom probe tomography needs a sample shaped as a needle with a tip only tens of nanometres across. The tip is made by electropolishing or with a focused ion beam."),
        ("Field evaporation", "The tip is cooled and placed under a very high electric field, often with short voltage or laser pulses. Atoms are pulled off the surface one at a time. This is called field evaporation."),
        ("Timing the flight", "Each ion flies to a detector and its flight time shows its mass. This identifies the element. Because the detector also records where each ion lands, the surface can be traced back to its origin."),
        ("Three-dimensional maps", "Software rebuilds the atoms in three dimensions, one layer after another. The result shows where each element sits, to near atomic resolution."),
        ("Solute clusters", "The method shows tiny clusters of added atoms, such as small groups of copper or magnesium. These clusters strongly affect hardness and are hard to see in other ways."),
        ("Limits", "The sample volume is very small, so the result describes only a tiny region. Preparation takes skill, and some materials break in the tip during the test."),
    ],
    "test": [
        ("What shape must an atom probe sample have?",
         [("a", "A flat coin"), ("b", "A hollow ball"), ("c", "A sharp needle tip"), ("d", "A long wire loop")], "c"),
        ("What is field evaporation?",
         [("a", "Pulling single atoms off the tip with a strong electric field"), ("b", "Boiling water off a sample"), ("c", "Painting atoms onto a board"), ("d", "Cooling the room")], "a"),
        ("How is the element of each ion identified?",
         [("a", "By its colour"), ("b", "By its taste"), ("c", "By its sound"), ("d", "By its flight time to the detector")], "d"),
        ("What do solute clusters affect?",
         [("a", "Colour of paper"), ("b", "Hardness"), ("c", "Shape of a cloud"), ("d", "Taste of water")], "b"),
        ("What is a main limit of this method?",
         [("a", "It examines the whole planet"), ("b", "It works in the dark only"), ("c", "It needs no preparation"), ("d", "It examines only a very small sample volume")], "d"),
    ],
}
