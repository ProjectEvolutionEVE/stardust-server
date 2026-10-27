"""Nanocrystalline Metals: metals with very small grains, how strength rises as grains shrink, and the limits of that gain."""
CODE = "mining5_nano_crys"
BOOK = {
    "title": "Nanocrystalline Metals",
    "subtitle": "Very fine grains, great strength, and the price of staying small",
    "chapters": [
        ("What a grain is", "A metal is made of many tiny crystal grains, each with its atoms in neat order. The boundaries between grains block the movement of defects. Smaller grains mean more boundaries."),
        ("The Hall-Petch effect", "For most metals, strength rises as the grain size falls. This is called the Hall-Petch relation. Grains below about a hundred nanometres give very high strength."),
        ("Making fine grains", "Nanocrystalline metals can be made by electrodeposition, by ball milling powder, or by heavily deforming metal. Each route has its own limits on purity and size of the sample."),
        ("Grain boundaries matter", "In very small grains, boundaries take up a large share of the metal. Their behaviour then decides many properties, including how the metal bends and how it corrodes."),
        ("Stability", "Fine grains want to grow larger over time, especially when heated. This grain growth can undo the strength. Makers add small amounts of other elements to hold the grains in place."),
        ("The limits", "Very fine grained metals can be less ductile, meaning they stretch less before breaking. Samples are often small and expensive to make. These limits decide where the material is useful."),
    ],
    "test": [
        ("What usually happens to strength as grain size falls?",
         [("a", "It falls to zero"), ("b", "It stays the same always"), ("c", "It turns to gas"), ("d", "It rises")], "d"),
        ("What is the name of the rule linking grain size and strength?",
         [("a", "Ohm law"), ("b", "Hall-Petch relation"), ("c", "Boyle law"), ("d", "Snell law")], "b"),
        ("What tends to happen to fine grains when they are heated?",
         [("a", "They grow larger"), ("b", "They vanish into air"), ("c", "They turn to glass"), ("d", "They become perfectly round")], "a"),
        ("What is one limit of very fine grained metals?",
         [("a", "They never conduct heat"), ("b", "They float on water"), ("c", "They can be less ductile"), ("d", "They are always pure gold")], "c"),
        ("Roughly how small are grains in the nanocrystalline range?",
         [("a", "Below about a hundred nanometres"), ("b", "Several metres across"), ("c", "About the size of a car"), ("d", "About the size of a planet")], "a"),
    ],
}
