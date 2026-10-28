"""Cryogenics: Making and Holding Very Cold Liquids. Liquefying gases, and keeping them cold in well-insulated tanks."""
CODE = 'engineering4_cryogenics'
BOOK = {
    "title": "Cryogenics: Making and Holding Very Cold Liquids",
    "subtitle": "Cooling gases to liquid, and keeping them cold in well-insulated tanks",
    "chapters": [
        ("Liquefaction",
         "Gases such as nitrogen and oxygen are cooled until they condense into liquids. This takes compressors, heat exchangers and expansion steps working together."),
        ("Vacuum insulation",
         "A vacuum gap between two walls stops heat from crossing easily. Vacuum flasks use the same idea, and large tanks use it too."),
        ("Boil-off",
         "Some liquid always boils off as heat leaks in. The boil-off rate is a key measure of how well a tank is insulated."),
        ("Handling cryogens safely",
         "Very cold liquids can freeze skin and make some materials brittle. Use insulated gloves, eye protection and well-ventilated rooms."),
        ("Pressure and venting",
         "Boiling gas raises the pressure in a sealed tank. Tanks need relief valves and must never be sealed completely."),
        ("The cost of keeping liquids cold",
         "Keeping a liquid cold costs energy, and some product is lost each day to boil-off. Good insulation and tank design reduce both costs."),
    ],
    "test": [
        ("What is liquefaction?",
         [("a", "Cooling a gas until it becomes a liquid"), ("b", "Melting ice"), ("c", "Painting a tank"), ("d", "Drawing a wire")], "a"),
        ("What does a vacuum gap do in a tank wall?",
         [("a", "Lets heat through"), ("b", "Adds weight"), ("c", "Makes sound"), ("d", "Stops heat from crossing")], "d"),
        ("What is boil-off?",
         [("a", "Freezing"), ("b", "Painting"), ("c", "Liquid that boils off as heat leaks in"), ("d", "Cutting")], "c"),
        ("Why should a tank never be sealed completely?",
         [("a", "It is too heavy"), ("b", "Boiling gas can raise pressure, so it needs a relief valve"), ("c", "It looks nicer"), ("d", "It would freeze the sky")], "b"),
        ("What is a risk of very cold liquids?",
         [("a", "They can freeze skin and make materials brittle"), ("b", "They make music"), ("c", "They help plants grow"), ("d", "They taste sweet")], "a"),
    ],
}
