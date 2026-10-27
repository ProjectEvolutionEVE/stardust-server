"""Laser Powder Bed Process Parameters: energy density, scan strategies, layer thickness, keyhole and lack-of-fusion defects, and parameter development."""
CODE = "engineering5_laser_am_params"
BOOK = {
    "title": "Laser Powder Bed Process Parameters",
    "subtitle": "The settings that decide whether a printed metal part is sound",
    "chapters": [
        ("Many settings, one result",
         "In laser powder bed fusion, a laser melts thin layers of metal powder, one layer after another. Many settings affect the result, including laser power, speed, layer thickness and scan pattern. Each must be chosen with care."),
        ("Energy density",
         "Energy density is roughly the laser energy put into a unit volume of powder. Too little energy leaves unmelted powder. Too much makes the melt pool deep and unstable. The right energy density sits in a window between the two."),
        ("Scan strategies",
         "The scan strategy is the path the laser takes across each layer. Changing the path changes how heat builds up and how stress forms. Good strategies spread heat evenly across the part."),
        ("Layer thickness",
         "Thin layers give finer detail and better density, but they take longer to build. Thick layers build faster but risk gaps and rough surfaces. The layer thickness is one of the main trade-offs in the process."),
        ("Defects to know",
         "Keyhole porosity forms when too much energy drives a deep, narrow melt pool that traps gas. Lack-of-fusion porosity forms when the melt does not fully join the layer below. Both show up as pores that can start cracks."),
        ("Developing the parameters",
         "Each new alloy and machine needs its own parameters, found by building test cubes and checking their density. Teams test a range of settings and pick the one that gives a sound part at a sensible build time. Records of the settings are kept with every build."),
    ],
    "test": [
        ("What does the laser do in laser powder bed fusion?",
         [("a", "It cools the bed with ice"), ("b", "It melts thin layers of metal powder"), ("c", "It cuts paper"), ("d", "It paints the bed")], "b"),
        ("What happens if the energy density is too low?",
         [("a", "The part gets too shiny"), ("b", "The part gets heavier on purpose"), ("c", "Unmelted powder is left in the part"), ("d", "Nothing happens")], "c"),
        ("What do thin layers give compared with thick ones?",
         [("a", "Faster builds with no other effect"), ("b", "Thicker walls with no gaps"), ("c", "No difference at all"), ("d", "Finer detail and better density, but slower builds")], "d"),
        ("What causes keyhole porosity?",
         [("a", "Too much energy, which drives a deep narrow melt pool that traps gas"), ("b", "Too little light in the room"), ("c", "Using a blue powder"), ("d", "Cooling the part slowly")], "a"),
        ("How are the parameters for a new alloy found?",
         [("a", "By guessing once and never checking"), ("b", "By building test cubes and checking their density across a range of settings"), ("c", "By copying a different machine without tests"), ("d", "By choosing the colour of the powder")], "b"),
    ],
}
