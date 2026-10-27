"""Soil mechanics and foundations: soil types, effective stress, bearing capacity, settlement and site investigation."""
CODE = "engineering4_soil"
BOOK = {
    "title": "Soil Mechanics and Foundations",
    "subtitle": "Effective stress, bearing capacity and settlement",
    "chapters": [
        ("Soil is not one material",
         "Soils range from loose sand and soft clay to dense gravel and rock fragments. Each type drains, squeezes and holds water differently. A foundation designer must know which kind of soil is under the building."),
        ("Effective stress",
         "The load on soil is shared between the soil grains and the water in its pores. Only the part carried by the grains, the effective stress, makes the soil stronger or weaker. Water pressure in the pores can reduce this and make the ground fail."),
        ("Bearing capacity",
         "Bearing capacity is the load a soil can carry under a footing before it fails. It depends on the soil's strength, the footing's size and the depth it sits at. Designers keep the working load well below this limit."),
        ("Settlement",
         "Settlement is the slow sinking of a foundation as the soil squeezes. Clay can settle over years as water leaves its pores. Uneven settlement cracks walls and can tilt a building, so designers limit it as well as the failure load."),
        ("Footing design",
         "Footings spread a column or wall load over a wider area of soil. Pad footings, strip footings and rafts are chosen by the load and the soil. The footing depth also has to suit frost, roots and any future digging."),
        ("Site investigation",
         "Engineers find out what lies underground by boring holes, taking samples and testing them. Field tests and lab tests give the strength and stiffness numbers the design needs. Cutting this step short is a common cause of costly foundation problems."),
    ],
    "test": [
        ("What is effective stress?", [("a", "The total weight of the building"), ("b", "The colour of the soil"), ("c", "The part of the load carried by the soil grains"), ("d", "The depth of the water table only")], "c"),
        ("What is bearing capacity?", [("a", "How many people a soil can hold"), ("b", "The speed of a drill"), ("c", "The load a soil can carry under a footing before it fails"), ("d", "How hot the ground gets")], "c"),
        ("What is settlement?", [("a", "A foundation slowly sinking as the soil squeezes"), ("b", "Soil being added on top"), ("c", "Water boiling in the ground"), ("d", "A type of rock")], "a"),
        ("Why does uneven settlement matter?", [("a", "It only affects gardens"), ("b", "It makes the soil warmer"), ("c", "It never causes any damage"), ("d", "It cracks walls and can tilt a building")], "d"),
        ("How is the ground under a site usually found out?", [("a", "By guessing from the weather"), ("b", "By boring holes, taking samples and testing them"), ("c", "By reading the paint colour"), ("d", "By skipping the survey")], "b"),
    ],
}
