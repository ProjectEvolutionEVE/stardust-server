"""Surface Integrity and Machining Damage: how machining can leave a surface that looks fine but has hidden damage that shortens fatigue life."""
CODE = "engineering5_surface_integrity"
BOOK = {
    "title": "Surface Integrity and Machining Damage",
    "subtitle": "White layers, residual stress, microcracks and fatigue life",
    "chapters": [
        ("Beyond the smooth look", "A surface can look fine and still hide damage just below it. Surface integrity looks at this hidden damage, not only at how smooth the surface feels."),
        ("White layers", "Grinding or cutting can heat a thin layer of the surface very fast. This layer, called a white layer, can be hard and brittle, and it may crack."),
        ("Residual stress", "Machining can leave stress locked in the surface. Compressive stress can help a part resist fatigue, while tensile stress can hurt it."),
        ("Microcracks", "Machining can leave tiny cracks in the surface. Microcracks are a common place for fatigue failure to start."),
        ("Roughness", "A rough surface gives fatigue cracks more places to start. Smoothing the surface is one way to improve fatigue life."),
        ("Fatigue life", "Surface damage can cut the life of a part under repeated loads. Surface finish and treatment therefore matter as much as the material for many parts."),
    ],
    "test": [
        ("What is a white layer?", [("a", "A layer of snow on the ground"), ("b", "A type of paper for drawings"), ("c", "A hard, rapidly heated surface layer from grinding or cutting"), ("d", "A painted warning sign")], "c"),
        ("What can grinding leave in the surface?", [("a", "Residual stress"), ("b", "A ring of rust"), ("c", "A shadow line"), ("d", "A printed receipt")], "a"),
        ("Why are microcracks a concern?", [("a", "They make parts shiny"), ("b", "They make parts lighter"), ("c", "They cool the parts down"), ("d", "They can start fatigue failure")], "d"),
        ("How does roughness affect fatigue?", [("a", "It changes the part's name"), ("b", "It removes the need for loads"), ("c", "Rough surfaces give fatigue cracks more places to start"), ("d", "It makes the part cooler")], "c"),
        ("What does surface damage affect?", [("a", "The price of the shop"), ("b", "The fatigue life of a part under repeated loads"), ("c", "The colour of the office"), ("d", "The weather on site")], "b"),
    ],
}
