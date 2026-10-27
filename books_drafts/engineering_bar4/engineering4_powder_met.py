"""Powder metallurgy and sintering: powder making, pressing, sintering, porosity control, gears and bearings, and high-volume economics."""
CODE = "engineering4_powder_met"
BOOK = {
    "title": "Powder Metallurgy and Sintering",
    "subtitle": "Pressing, sintering and high-volume parts",
    "chapters": [
        ("Making parts from powder",
         "Powder metallurgy makes parts by pressing metal powder into a shape and heating it. The powder is not melted into a casting. The method gives accurate parts with little waste."),
        ("Pressing",
         "The powder is pressed in a hardened die to form a green compact. The compact holds its shape but is weak until it is heated. Press design and powder choice set the density of the part."),
        ("Sintering",
         "Sintering heats the compact below its melting point, so the particles bond at their contacts. The part shrinks a little and gains strength. Furnace atmosphere and time must be controlled."),
        ("Porosity control",
         "Some porosity is left between the particles after sintering. Porosity lowers strength but can hold oil in bearings. Engineers control the pressing and sintering to set the porosity they need."),
        ("Gears and bearings",
         "Gears and bearings are often made this way because the porous structure can hold lubricant, and the shapes come out close to final size. Complex shapes can be made in one press. The method suits many small parts."),
        ("Economics of high volume",
         "The dies are costly, but the cost per part falls sharply when many parts are made. Powder metallurgy suits high-volume runs of the same part. Low volume work is often better made another way."),
    ],
    "test": [
        ("What is a green compact?", [("a", "A fully finished gear"), ("b", "A green paint tin"), ("c", "A pressed powder shape before sintering"), ("d", "A type of furnace")], "c"),
        ("What does sintering do?", [("a", "Cools the part to ice"), ("b", "Melts the powder into a liquid"), ("c", "Heats the compact below melting so the particles bond"), ("d", "Paints the part")], "c"),
        ("Why are some porous parts useful for bearings?", [("a", "The pores can hold lubricant"), ("b", "The pores make the part heavier"), ("c", "Pores have no use"), ("d", "Pores melt the bearing")], "a"),
        ("When does powder metallurgy make the most economic sense?", [("a", "Only for paint"), ("b", "For one-off art pieces"), ("c", "Only for very large castings"), ("d", "For high-volume runs of the same part")], "d"),
        ("What happens to the part as it is sintered?", [("a", "It grows large and weak"), ("b", "It shrinks a little and gains strength"), ("c", "It turns to liquid"), ("d", "It loses all its shape")], "b"),
    ],
}
