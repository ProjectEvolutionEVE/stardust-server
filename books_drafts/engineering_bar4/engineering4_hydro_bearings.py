"""Hydrodynamic and Hydrostatic Bearings: the oil wedge, pressurised pads, film thickness, load capacity and power loss."""
CODE = "engineering4_hydro_bearings"
BOOK = {
    "title": "Hydrodynamic and Hydrostatic Bearings",
    "subtitle": "Oil wedges, pressurised pads and film thickness",
    "chapters": [
        ("The oil wedge",
         "In a hydrodynamic bearing, a turning shaft drags oil into a narrowing gap. The oil forms a wedge that lifts the shaft and carries the load."),
        ("Pressurised pads",
         "In a hydrostatic bearing, an external pump forces oil into pockets under the load. The bearing works even at rest and at very low speed."),
        ("Film thickness",
         "The film thickness depends on speed, oil viscosity and load. A thin film raises the risk of contact, so designers keep the film thick enough."),
        ("Load capacity",
         "A bearing's load capacity depends on the film, the bearing area and the pressure. In a hydrodynamic bearing, the capacity rises with speed, because a faster shaft builds a stronger wedge."),
        ("Power used",
         "Shearing the oil uses power, and that power becomes heat. A thinner oil reduces the loss but also thins the film."),
        ("Choosing a bearing type",
         "Choose hydrodynamic for steady, high-speed running, and hydrostatic for start-stop or slow duty. Check the load and speed against each type's limits before choosing."),
    ],
    "test": [
        ("How does a hydrodynamic bearing lift its load?",
         [("a", "An oil wedge forms as the shaft drags oil into a narrowing gap"), ("b", "Magnets"), ("c", "Air balloons"), ("d", "Springs only")], "a"),
        ("What does a hydrostatic bearing use?",
         [("a", "Sunlight"), ("b", "A rope"), ("c", "Paint"), ("d", "An external pump forcing oil into pockets")], "d"),
        ("Why is a thin film a risk?",
         [("a", "Colour changes"), ("b", "Sound drops"), ("c", "Contact risk rises"), ("d", "The shaft gets lighter")], "c"),
        ("What does shearing oil produce?",
         [("a", "Gold"), ("b", "Heat"), ("c", "Light"), ("d", "Music")], "b"),
        ("Which bearing suits steady, high-speed running?",
         [("a", "Hydrodynamic"), ("b", "Hydrostatic only"), ("c", "Neither"), ("d", "Both, always")], "a"),
    ],
}
