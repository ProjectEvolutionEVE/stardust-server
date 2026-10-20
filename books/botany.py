"""Botany & Hydroponics (10-20). Real plant science, plus the Starship's greenhouse and water plant (rule 28)."""
CODE = "botany"
BOOK = {
    "title": "Botany & Hydroponics",
    "subtitle": "Growing plants without soil, aboard the Starship",
    "chapters": [
        ("What a plant needs",
         "A plant needs light, water, carbon dioxide, nutrients and the right temperature. Give it those and it grows."),
        ("Photosynthesis",
         "Leaves are green because of chlorophyll. Chlorophyll catches light, and the plant uses that energy to turn "
         "carbon dioxide and water into sugar, its food. Oxygen is left over and goes into the air."),
        ("Roots and nutrients",
         "Roots drink water and take up dissolved minerals. The big three are nitrogen (N), phosphorus (P) and "
         "potassium (K). Roots also need oxygen, which is why plants drown in stale, still water."),
        ("Hydroponics: no soil needed",
         "Soil only holds water and nutrients for the roots. In hydroponics the roots sit in water with the nutrients "
         "already mixed in, kept moving or bubbled with air so the roots can breathe. It uses far less water than a field, "
         "because the water is reused."),
        ("Light",
         "Indoors, plants grow under lamps. Most plants also need darkness every day, so growers run their lights on a "
         "timer."),
        ("The Starship's greenhouse",
         "The Starship carries a large self-sustaining greenhouse, full of plants and fragrant flowers. Its water comes "
         "from the ship's water generation plant, which makes its own H2O, so the greenhouse never runs dry. Greenhouse "
         "work is one of the early careers aboard."),
    ],
    "test": [
        ("What makes leaves green?",
         [("a", "Chlorophyll"), ("b", "Iron"), ("c", "Salt"), ("d", "Paint")], "a"),
        ("In photosynthesis, what is left over and goes into the air?",
         [("a", "Carbon dioxide"), ("b", "Oxygen"), ("c", "Nitrogen"), ("d", "Smoke")], "b"),
        ("What are the big three plant nutrients?",
         [("a", "Gold, silver, copper"), ("b", "Nitrogen, phosphorus, potassium"), ("c", "Sugar, salt, water"), ("d", "Iron, nickel, carbon")], "b"),
        ("What does hydroponics grow plants without?",
         [("a", "Water"), ("b", "Light"), ("c", "Soil"), ("d", "Nutrients")], "c"),
        ("Why does the Starship's greenhouse never run dry?",
         [("a", "It is watered from debris ice"), ("b", "The water generation plant makes its own H2O"), ("c", "Water is bought every day"), ("d", "Plants need no water")], "b"),
    ],
}
