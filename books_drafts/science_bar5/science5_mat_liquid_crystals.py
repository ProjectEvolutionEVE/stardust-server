"""Liquid Crystals and Soft Matter: materials that flow like liquids yet keep molecular order, and how that order is measured."""
CODE = "science5_mat_liquid_crystals"
BOOK = {
    "title": "Liquid Crystals and Soft Matter",
    "subtitle": "Materials that flow but keep a hidden order",
    "chapters": [
        ("Between liquid and solid", "A liquid crystal flows like a liquid but keeps some order in how its molecules point. It sits between a plain liquid and a solid crystal. This middle state is called a mesophase."),
        ("Mesophases", "Liquid crystals come in several phases. In the nematic phase, molecules point roughly the same way but lack positional order. Smectic and cholesteric phases show other kinds of order."),
        ("Order parameters", "An order parameter is a number that measures how ordered the molecules are. It is zero in the disordered liquid and rises as order grows. It helps scientists describe each phase."),
        ("Director fields", "The director is the average direction of the molecules at a point. A director field maps that direction throughout the material. Changing the field changes how light passes through."),
        ("Displays", "Liquid crystal displays use a voltage to change the molecular direction in each pixel. The change alters how much light passes through. Thin layers and polarisers make the image."),
        ("Colloids and soft matter", "Soft matter includes colloids, gels and polymers. Colloidal crystals form from tiny particles suspended in liquid. They are studied with light scattering and microscopy."),
    ],
    "test": [
        ("What is a liquid crystal?",
         [("a", "Solid glass"), ("b", "A state between liquid and solid, with some molecular order"), ("c", "A gas"), ("d", "A metal")], "b"),
        ("What does a director field describe?",
         [("a", "The taste of a liquid"), ("b", "The colour of a light"), ("c", "The weight of a sample"), ("d", "The average direction of molecules at each point")], "d"),
        ("What do liquid crystal displays use to change the light?",
         [("a", "Sound waves"), ("b", "Heat alone"), ("c", "A voltage that changes molecular direction and so the light"), ("d", "Magnets alone")], "c"),
        ("What is a mesophase?",
         [("a", "A phase of matter with partial order"), ("b", "A type of soup"), ("c", "A kind of rock"), ("d", "A metal alloy")], "a"),
        ("What is an order parameter?",
         [("a", "A kind of clock"), ("b", "A number that measures how ordered the molecules are"), ("c", "A menu"), ("d", "A cooking rule")], "b"),
    ],
}
