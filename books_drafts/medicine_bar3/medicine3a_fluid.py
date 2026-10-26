"""Medicine, bar 3 (Senior Doctor), part A: Fluid Balance. How the body gains and loses water and salt, and what thirst and hormones do about it."""
CODE = "medicine3a_fluid"
BOOK = {
    "title": "Fluid Balance: Water and Salt",
    "subtitle": "How the body gains and loses water, and why thirst and salt matter",
    "chapters": [
        ("Water in, water out",
         "Water makes up a large part of the body. It is held inside cells, in the fluid between them, and in the blood. Water comes in from food and drink, and leaves in urine, sweat, breath and the gut. A steady balance keeps the body working well."),
        ("Salt and water go together",
         "Water tends to follow salt across the membranes in the body. The amount of salt therefore strongly influences how much water the body holds. Keeping the two in step is one of the kidneys' main tasks."),
        ("Thirst",
         "Thirst is the body's signal that it needs water. It rises when the blood becomes more concentrated or when fluid is lost. For most healthy adults, drinking when thirsty works well, but thirst can lag behind need during heavy effort or heat."),
        ("Hormones that hold water",
         "A hormone released by the pituitary gland tells the kidneys to take back more water when the body is short of it. Another hormone, from the adrenal glands, helps the kidneys hold on to salt. Together they keep the fluid balance near its set point."),
        ("Losing fluid fast",
         "Heavy sweating, vomiting or diarrhoea can lose water and salts faster than the body can replace them. The body then conserves water, thirst rises and the blood becomes more concentrated. Steady intake matches losses better than one large amount taken at once."),
        ("Water on a long voyage",
         "A crew far from help must plan its water as carefully as its food. The Starship has a water generation plant, so water is an endless supply aboard, as the ship's story describes. A crew still watches salt, activity and the signs of dehydration."),
    ],
    "test": [
        ("Where is most of the body's water held?",
         [("a", "In the bones only"), ("b", "In the teeth"), ("c", "In the hair"), ("d", "Inside cells, between cells and in the blood")], "d"),
        ("Which hormone tells the kidneys to take back more water?",
         [("a", "A hormone released by the pituitary gland"), ("b", "Glucose"), ("c", "Vitamin C"), ("d", "Bile")], "a"),
        ("What does thirst signal?",
         [("a", "That the body has too much salt"), ("b", "That the heart has stopped"), ("c", "That the body needs water"), ("d", "That the body is full")], "c"),
        ("Why does water tend to follow salt in the body?",
         [("a", "Salt makes water freeze"), ("b", "Water follows salt across membranes, so the amount of salt affects how much water is held"), ("c", "Salt holds the bones together"), ("d", "Salt turns water into air")], "b"),
        ("Which situation makes the body lose water and salts faster?",
         [("a", "Sleeping in a cool room"), ("b", "Heavy sweating or vomiting"), ("c", "Reading a book"), ("d", "Standing still for an hour")], "b"),
    ],
}
