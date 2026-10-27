"""Radiation Heat Transfer and View Factors: how heat crosses empty space, and why a spacecraft must radiate its waste heat."""
CODE = "engineering4_radiation_heat"
BOOK = {
    "title": "Radiation Heat Transfer and View Factors",
    "subtitle": "Emissivity, the fourth-power law, shields and radiators",
    "chapters": [
        ("Heat by radiation alone",
         "In a vacuum, heat cannot move by conduction or convection, so radiation carries it. Every warm surface gives off electromagnetic waves. The hotter the surface, the more it gives off."),
        ("Emissivity",
         "Emissivity is a number from 0 to 1 that says how well a surface radiates, compared with a perfect black body. Polished metal has low emissivity and matt black paint has high emissivity. Surfaces that radiate well also absorb well."),
        ("The Stefan-Boltzmann law",
         "The power a black body gives off per square metre rises with the fourth power of its absolute temperature. The constant is about 5.67 times ten to the minus eight watts per square metre per kelvin to the fourth. Doubling the absolute temperature gives about sixteen times the radiated power."),
        ("View factors",
         "The view factor is the share of radiation leaving one surface that lands on another. It depends on the shape of the two surfaces and the distance between them. Engineers work out view factors before they add up the heat exchanged."),
        ("Radiation shields",
         "A thin sheet placed between two hot surfaces cuts the heat passing between them. A stack of several sheets cuts it much more. Each sheet heats up and radiates again in both directions, so the net flow falls."),
        ("Radiative cooling in space",
         "A spacecraft has no air to carry heat away, so it must radiate its waste heat. Radiators face cold space and are built to have high emissivity. Their area sets how much heat the craft can reject."),
    ],
    "test": [
        ("What is emissivity?",
         [("a", "The speed of heat in air"), ("b", "A number from 0 to 1 showing how well a surface radiates"), ("c", "The mass of a radiator"), ("d", "The colour of a surface")], "b"),
        ("If the absolute temperature of a black body doubles, how does its radiated power change?",
         [("a", "It doubles"), ("b", "It rises four times"), ("c", "It rises eight times"), ("d", "It rises about sixteen times")], "d"),
        ("What does a view factor describe?",
         [("a", "How much a surface weighs"), ("b", "The share of radiation from one surface that reaches another"), ("c", "How fast air flows past it"), ("d", "The thickness of its paint")], "b"),
        ("Why do radiation shields reduce heat transfer?",
         [("a", "They block sound"), ("b", "They cool the surfaces by moving air"), ("c", "They absorb and re-radiate heat, cutting the net flow between hot surfaces"), ("d", "They turn radiation into electricity")], "c"),
        ("Why must a spacecraft radiate its waste heat?",
         [("a", "Air carries heat away in space"), ("b", "Heat cannot leave by conduction or convection in a vacuum, so it must be radiated away"), ("c", "The Sun cools the craft"), ("d", "Metal absorbs all heat")], "b"),
    ],
}
