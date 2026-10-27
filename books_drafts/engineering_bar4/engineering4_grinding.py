"""Grinding and abrasive finishing: wheel grit and bond, dressing, surface finish, grinding burn, coolant and the cost of a fine finish."""
CODE = "engineering4_grinding"
BOOK = {
    "title": "Grinding and Abrasive Finishing",
    "subtitle": "Grit, bond, dressing and surface finish",
    "chapters": [
        ("Many small cutters",
         "A grinding wheel is packed with hard abrasive grains held in a bond. Each grain cuts a tiny chip as the wheel turns. Together the grains remove material and leave a finish."),
        ("Grit and bond",
         "Grit size sets how coarse or fine the cut is. A coarse grit removes material fast, and a fine grit gives a smoother finish. The bond holds the grains and releases worn ones at the right rate."),
        ("Dressing the wheel",
         "Dressing trims the wheel to restore sharp grains and a true shape. A blunt or clogged wheel rubs instead of cutting. Dressing is a regular part of keeping a grinding process stable."),
        ("Surface finish",
         "Surface finish describes the small peaks and valleys left on a part. It is measured by a roughness value and chosen to suit the part's function. A bearing seat needs a finer finish than a rough casting face."),
        ("Grinding burn",
         "Heat from grinding can change the surface of steel, causing a burn. The burn can soften the surface or leave tensile stresses that crack the part later. Coolant and gentle cutting prevent it."),
        ("The cost of a fine finish",
         "A finer finish takes more passes, slower feeds and more time on the machine. It can also need finer wheels and more dressing. Designers specify the finish that the function needs and no finer."),
    ],
    "test": [
        ("What do the grains in a grinding wheel do?", [("a", "They store water"), ("b", "They hold the wheel's colour"), ("c", "Each cuts a tiny chip as the wheel turns"), ("d", "They carry electricity")], "c"),
        ("What does a coarse grit do?", [("a", "Removes material fast with a rougher cut"), ("b", "Gives the smoothest finish"), ("c", "Stops the wheel"), ("d", "Melts the part")], "a"),
        ("What is dressing a grinding wheel?", [("a", "Freezing the wheel"), ("b", "Painting the wheel"), ("c", "Wrapping the wheel in cloth"), ("d", "Trimming the wheel to restore sharp grains and a true shape")], "d"),
        ("What is grinding burn?", [("a", "A sunburn on the operator"), ("b", "Heat damage that can soften the surface of steel"), ("c", "A cool blue colour"), ("d", "A sound made by a fan")], "b"),
        ("Why does a finer finish cost more?", [("a", "It uses no tools"), ("b", "It needs no time at all"), ("c", "It needs more passes, slower feeds and more time on the machine"), ("d", "It is always cheaper")], "c"),
    ],
}
