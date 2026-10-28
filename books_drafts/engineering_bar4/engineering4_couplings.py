"""Shaft Couplings and Keyways: keys, splines, flexible couplings, misalignment, shaft fits and fretting wear."""
CODE = "engineering4_couplings"
BOOK = {
    "title": "Shaft Couplings and Keyways",
    "subtitle": "Keys, splines, flexible couplings and fretting",
    "chapters": [
        ("Keys and keyways",
         "A key fits into a slot called a keyway, and it locks a gear or pulley to a shaft so the two turn together. The key carries torque by pushing against the sides of the slot."),
        ("Splines",
         "Splines are ridges cut into a shaft that fit matching grooves in a hub. They carry more torque than a single key, and they can slide along the shaft when needed."),
        ("Flexible couplings",
         "A flexible coupling joins two shafts and allows a small misalignment. It may use rubber, a flexible disc or a grid."),
        ("Misalignment",
         "Shafts that are not lined up cause extra loads, heat and wear in bearings and seals. Alignment checks are part of every installation."),
        ("Shaft fits",
         "The fit between a shaft and a hub can be a tight press fit or a sliding fit. The choice depends on the load and on whether the parts must be taken apart again."),
        ("Fretting wear",
         "Small rubbing movement between two tight surfaces causes fretting. It wears the metal and can start cracks. Good fits and lubrication reduce it."),
    ],
    "test": [
        ("What does a key do?",
         [("a", "Locks a gear to a shaft so it turns with it"), ("b", "Stores heat"), ("c", "Measures sound"), ("d", "Paints the shaft")], "a"),
        ("What do splines do?",
         [("a", "Melt"), ("b", "Stop all rotation"), ("c", "Carry more torque than a single key"), ("d", "Paint")], "c"),
        ("What does a flexible coupling allow?",
         [("a", "Large heat"), ("b", "Sound"), ("c", "Colour"), ("d", "Small misalignment")], "d"),
        ("What is fretting?",
         [("a", "Smooth rolling"), ("b", "Gear paint"), ("c", "Fuel"), ("d", "Small rubbing movement that wears metal")], "d"),
        ("What causes extra loads on bearings?",
         [("a", "Misalignment of shafts"), ("b", "Good alignment"), ("c", "Lubricant"), ("d", "Clean fits")], "a"),
    ],
}
