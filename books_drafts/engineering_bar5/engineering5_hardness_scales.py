"""Hardness Scales and Their Conversion: the common hardness tests, what each one measures, and why converting between them is only approximate."""
CODE = "engineering5_hardness_scales"
BOOK = {
    "title": "Hardness Scales and Their Conversion",
    "subtitle": "Rockwell, Vickers, Brinell and the limits of each",
    "chapters": [
        ("Many scales, one idea", "Hardness is how well a material resists being indented. Different scales measure it in different ways, so the scale must always be named with the number."),
        ("Rockwell", "A cone or ball is pressed in under a set load. The depth of the mark gives the Rockwell number, which is quick to read and widely used."),
        ("Vickers", "A diamond pyramid is pressed into the surface. The size of the mark gives the Vickers hardness, which works across a wide range of materials."),
        ("Brinell", "A hard ball is pressed into the surface under a set load. The diameter of the mark is measured, and the result suits coarse or uneven materials."),
        ("Microhardness", "Very small loads test tiny areas, such as a single grain or a thin surface layer. This is useful where a larger test would average over too much material."),
        ("Converting and limits", "Conversions between scales are approximate, and they depend on the material. Each scale has its own limits, so a converted number should be used with care."),
    ],
    "test": [
        ("What is hardness?", [("a", "How loud a material rings"), ("b", "How heavy a material is"), ("c", "How well a material resists being indented"), ("d", "How bright a material looks")], "c"),
        ("What does a Rockwell test measure?", [("a", "The depth of the mark from a cone or ball under a set load"), ("b", "The length of a cable"), ("c", "The colour of a paint"), ("d", "The temperature of tea")], "a"),
        ("What does a Brinell test use?", [("a", "A sharp knife"), ("b", "A magnet"), ("c", "A camera"), ("d", "A hard ball pressed in, measuring the diameter of the mark")], "d"),
        ("What is microhardness for?", [("a", "Testing whole buildings"), ("b", "Testing very small areas, such as a single grain"), ("c", "Painting walls"), ("d", "Cooking food in a lab")], "b"),
        ("Are scale conversions exact?", [("a", "Yes, they are always exactly the same"), ("b", "Only for paint"), ("c", "No, they are approximate and depend on the material"), ("d", "Only for cars")], "c"),
    ],
}
