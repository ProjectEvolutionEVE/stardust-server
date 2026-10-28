"""Rock Mechanics and the Hoek-Brown Criterion: why a whole rock mass is weaker than a small piece of rock, and how engineers allow for it."""
CODE = "engineering5_rock_mech"
BOOK = {
    "title": "Rock Mechanics and the Hoek-Brown Criterion",
    "subtitle": "Joints, rock ratings and support for tunnels and slopes",
    "chapters": [
        ("Joints in rock", "A rock mass is full of joints, cracks and bedding planes. These weak lines mean the whole mass is weaker than a small, solid piece taken from it. Engineers must allow for the joints, not only the rock itself."),
        ("Intact rock strength", "A small sample of rock tested in a laboratory gives the strength of the intact rock. This is only a starting point, because real ground has joints and weathering that the sample does not show."),
        ("Rating the rock mass", "Engineers rate a rock mass by how blocky it is and how weathered its joints are. The Geological Strength Index, or GSI, is one such rating, from very poor to very good."),
        ("The Hoek-Brown criterion", "The Hoek-Brown criterion is an empirical rule. It uses the intact rock strength and the rating to estimate the strength of the whole rock mass. It is widely used in tunnel and slope design."),
        ("Support design", "Rock bolts, mesh and sprayed concrete, called shotcrete, hold the rock around an excavation in place. The rock rating helps decide how much support is needed and where."),
        ("Tunnel stability", "Good rock needs less support, and poor rock may need much more. The rating therefore drives both the safety of the tunnel and the cost of building it."),
    ],
    "test": [
        ("What does the Hoek-Brown criterion estimate?", [("a", "The colour of the rock"), ("b", "The strength of a whole rock mass"), ("c", "The weight of a drill"), ("d", "The speed of a rock slide")], "b"),
        ("What are joints in rock?", [("a", "Cracks, fractures and bedding planes"), ("b", "Minerals found in a laboratory"), ("c", "Steel bars placed in a tunnel"), ("d", "Layers of rain water")], "a"),
        ("What is the Geological Strength Index?", [("a", "A type of rock drill"), ("b", "The depth of a tunnel"), ("c", "A rating of how blocky and weathered a rock mass is"), ("d", "The price of rock per tonne")], "c"),
        ("Why do tunnels need support?", [("a", "To make the rock hotter"), ("b", "To stop the rock being tested"), ("c", "To lengthen the tunnel"), ("d", "To hold the rock around an opening stable")], "d"),
        ("Why does a well-rated rock need less support?", [("a", "The whole mass is stronger, so less holding is needed"), ("b", "It is heavier, so it stays in place"), ("c", "It has no joints at all"), ("d", "It has no weight to carry")], "a"),
    ],
}
