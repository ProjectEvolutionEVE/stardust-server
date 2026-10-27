"""Punching Shear in Concrete Slabs: how a column can push through a flat slab, and how designers guard against it."""
CODE = "engineering5_punching"
BOOK = {
    "title": "Punching Shear in Concrete Slabs",
    "subtitle": "Shear perimeters, column loads and failure around the column",
    "chapters": [
        ("A slab under a column", "A column pushes down on a flat slab. The slab can fail by punching, a sudden shear failure in a ring around the column, rather than by bending."),
        ("Shear perimeters", "A critical shear perimeter lies a set distance from the column. The shear force is checked along this perimeter, and a larger perimeter helps resist it."),
        ("Column loads", "The larger the column load, the larger the shear that must be resisted around the column. Heavy loads need a thicker slab or more reinforcement."),
        ("Reinforcement", "Steel bars crossing the perimeter help the slab carry the load and limit cracking. Shear reinforcement is placed where the shear is highest."),
        ("Edge effects", "A column near the edge of a slab has a smaller perimeter to resist shear. Edge columns need extra care in the design."),
        ("Failure patterns", "Punching failure often shows as a cone or plug of concrete pushed through the slab. Engineers design to prevent this sudden failure."),
    ],
    "test": [
        ("What is punching shear?", [("a", "A kind of dance for builders"), ("b", "A hole cut for pipes"), ("c", "A type of paint for concrete"), ("d", "A sudden shear failure of a slab around a column")], "d"),
        ("What is the critical perimeter?", [("a", "A set distance from the column where shear is checked"), ("b", "The edge of the car park"), ("c", "The paint line on the floor"), ("d", "The top of the wall")], "a"),
        ("What does a bigger column load do?", [("a", "It makes the slab thinner"), ("b", "It cools the slab"), ("c", "It increases the shear that must be resisted"), ("d", "It removes the perimeter")], "c"),
        ("What helps a slab resist punching?", [("a", "Paint on the surface"), ("b", "More sunlight on the slab"), ("c", "A cup of tea left nearby"), ("d", "Steel reinforcement crossing the perimeter")], "d"),
        ("Why are edge columns a concern?", [("a", "They are always painted"), ("b", "They have a smaller perimeter to resist shear"), ("c", "They are heavier by design"), ("d", "They hold no load")], "b"),
    ],
}
