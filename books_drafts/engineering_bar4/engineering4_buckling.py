"""Buckling: how slender parts give way suddenly under compression, and how to design a margin against it."""
CODE = "engineering4_buckling"
BOOK = {
    "title": "Buckling: When Slender Parts Give Way",
    "subtitle": "Euler buckling, end conditions and designing a margin",
    "chapters": [
        ("Squeezed and sudden",
         "A long, thin column can carry a load in compression. At a certain load it bends sideways, and it does so suddenly, even though the material itself is not yet at its limit. This is buckling, and it is a different failure from crushing."),
        ("The Euler load",
         "Leonhard Euler worked out the load at which a slender column buckles. It rises with the stiffness of the material and the size of the column's cross section. It falls fast as the column gets longer."),
        ("Effective length",
         "The effective length depends on how the ends are held. A column fixed at both ends is much stiffer than one free at the top. Engineers use an effective length factor to show how the ends change the result."),
        ("Slenderness ratio",
         "The slenderness ratio compares the column's length with how wide its cross section is spread. A high ratio means a thin, long part that will buckle at a lower load. Short, thick parts are far less likely to buckle."),
        ("Local wall buckling",
         "Thin walls can wrinkle locally, even when the whole column does not bend. This happens in thin tubes and box sections. Stiffening ribs and thicker walls keep the walls from wrinkling early."),
        ("Designing with a margin",
         "Buckling gives little warning, so designers keep a safety margin well below the buckling load. They also check imperfections, since a slightly bent column buckles earlier. A margin is the cheap way to avoid a sudden collapse."),
    ],
    "test": [
        ("What is buckling?", [("a", "Sudden sideways bending of a slender part under compression"), ("b", "Slow melting of a metal"), ("c", "Rust on the surface"), ("d", "A colour change in paint")], "a"),
        ("What does a higher slenderness ratio mean?", [("a", "A short, thick part"), ("b", "A part with no ends"), ("c", "A part that cannot be loaded"), ("d", "A long, thin part that is more likely to buckle")], "d"),
        ("How does fixing both ends compare with leaving one end free?", [("a", "Both give the same result"), ("b", "Fixing both ends makes the column stiffer against buckling"), ("c", "Free ends make the column stronger"), ("d", "End fixings have no effect")], "b"),
        ("Why do designers keep a margin below the buckling load?", [("a", "Margins make the part heavier for no reason"), ("b", "Buckling only happens in water"), ("c", "Buckling gives little warning and an imperfect column buckles earlier"), ("d", "Buckling is harmless")], "c"),
        ("What helps keep thin walls from wrinkling locally?", [("a", "Thinner walls"), ("b", "Removing all supports"), ("c", "Stiffening ribs and thicker walls"), ("d", "A brighter colour")], "c"),
    ],
}
