"""Plates: flexural stiffness, edge support, deflection, stiffeners and ribs, and checking thickness against a load."""
CODE = "engineering4_plate_bending"
BOOK = {
    "title": "Plates: Bending and Stiffening",
    "subtitle": "Flexural stiffness, edge support and stiffeners",
    "chapters": [
        ("What a plate is",
         "A plate is a flat piece of material that is much wider than it is thick. It bends under a load across its surface. Its bending stiffness depends strongly on its thickness."),
        ("Flexural stiffness",
         "Flexural stiffness describes how hard a plate is to bend. Stiffness rises very fast with thickness, so a small increase in thickness gives a large gain. This is why plate thickness is one of the main design choices."),
        ("Edge support",
         "How a plate is supported at its edges changes how much it bends. A plate held firmly on all sides is stiffer than one held only at a few points. Designers choose the edge support to suit the structure."),
        ("Deflection",
         "Deflection is how far a plate moves under load. Too much deflection can crack finishes, jam doors or spoil how a surface feels. Designers set a limit on deflection as well as on stress."),
        ("Stiffeners and ribs",
         "Stiffeners and ribs are strips welded or bolted onto a plate. They add stiffness without much extra weight. A thin plate with well-placed ribs can match a much thicker plain plate."),
        ("Checking thickness against a load",
         "Engineers check the plate's thickness against the load and its support. They compare the bending stress and the deflection with the allowed values. A plate that passes both checks is thick enough for its job."),
    ],
    "test": [
        ("What is a plate?", [("a", "A round bar of any length"), ("b", "A flat piece much wider than it is thick"), ("c", "A thin wire"), ("d", "A sealed tank of water")], "b"),
        ("How does thickness affect a plate's bending stiffness?", [("a", "It makes no difference"), ("b", "It makes the plate lighter and softer"), ("c", "Stiffness rises very fast with thickness"), ("d", "It reduces stiffness to zero")], "c"),
        ("What does a plate held firmly on all sides do compared with one held at a few points?", [("a", "It bends more"), ("b", "It cannot carry any load"), ("c", "It is stiffer"), ("d", "It melts")], "c"),
        ("Why is deflection limited in design?", [("a", "Too much movement can crack finishes or jam doors"), ("b", "Deflection makes plates cheaper"), ("c", "Deflection has no effect"), ("d", "Deflection changes the colour")], "a"),
        ("What do stiffeners and ribs do?", [("a", "Lift the plate off the ground"), ("b", "Remove the need for any support"), ("c", "Make the plate transparent"), ("d", "Add stiffness without much extra weight")], "d"),
    ],
}
