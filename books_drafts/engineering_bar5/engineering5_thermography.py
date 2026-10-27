"""Infrared Thermography and Emissivity Correction: reading surface temperature from heat images, and why the surface itself can mislead the camera."""
CODE = "engineering5_thermography"
BOOK = {
    "title": "Infrared Thermography and Emissivity Correction",
    "subtitle": "Reading heat images, emissivity and reflected radiation",
    "chapters": [
        ("Seeing heat", "An infrared camera turns the heat a surface gives off into a picture. Warmer areas show as different colours, so uneven heating can be seen at a glance."),
        ("Emissivity", "Emissivity is how well a surface gives off heat, from 0 to 1. Dull, dark surfaces are close to 1, and shiny metal surfaces are much lower. The camera must be told the right value."),
        ("Calibration", "The camera must be calibrated, and its emissivity setting must match the surface. Otherwise the temperatures it reads can be badly wrong."),
        ("Reflected radiation", "A shiny surface can reflect heat from other objects around the room. The camera may read that reflected heat as the surface's own, which can fool the reading."),
        ("Thermal images of parts", "A thermal picture of a warm part can show hot spots and uneven heating. Comparing the picture with a good part helps spot what is wrong."),
        ("Defect detection", "A region that heats or cools differently from its surroundings can point to a defect. Examples include a delamination, a blockage in a channel or a poor bond."),
    ],
    "test": [
        ("What is emissivity?", [("a", "How well a surface gives off heat, from 0 to 1"), ("b", "The weight of a camera"), ("c", "The colour of a paint"), ("d", "The speed of the wind")], "a"),
        ("Why do shiny surfaces cause trouble?", [("a", "They are always cold"), ("b", "They are heavy to lift"), ("c", "They reflect heat from other things, which can fool the camera"), ("d", "They give off no light at all")], "c"),
        ("What must be done before reading temperatures?", [("a", "The camera must be calibrated and emissivity set"), ("b", "The camera must be painted"), ("c", "The room must be made dark"), ("d", "The lens must be removed")], "a"),
        ("What can a thermal image show in a part?", [("a", "The music it plays"), ("b", "Hot spots and uneven heating"), ("c", "The paint brand"), ("d", "The operator's name")], "b"),
        ("What can a region that heats differently point to?", [("a", "A defect such as a delamination or blockage"), ("b", "A holiday in the sun"), ("c", "A good night's sleep"), ("d", "A new paint job")], "a"),
    ],
}
