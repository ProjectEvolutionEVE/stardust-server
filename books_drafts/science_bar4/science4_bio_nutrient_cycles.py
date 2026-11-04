"""Nutrient Cycling in Ecosystems: the nitrogen cycle, the phosphorus cycle, decomposition, mineralisation, nutrient limitation and ecosystem budgets."""
CODE = "science4_bio_nutrient_cycles"
BOOK = {
    "title": "Nutrient Cycling in Ecosystems",
    "subtitle": "Nitrogen, phosphorus, decomposition and nutrient budgets",
    "chapters": [
        ("The nitrogen cycle", "Nitrogen moves between the air, the soil, the water and living things. Bacteria fix nitrogen gas into forms that plants can use."),
        ("The phosphorus cycle", "Phosphorus moves slowly through rock, soil, water and living things. It has no major gas phase, so its cycle is much slower than the nitrogen cycle."),
        ("Decomposition", "Decomposers such as fungi and bacteria break down dead matter. This releases nutrients back into the soil and water, where living things can use them again."),
        ("Mineralisation", "Mineralisation is the release of inorganic nutrients from organic matter. It makes those nutrients available for plants to take up again."),
        ("Nutrient limitation", "A nutrient is limiting when its supply is lowest compared with what organisms need. Adding that nutrient often boosts growth."),
        ("Ecosystem budgets", "Ecologists track how much of each nutrient enters, moves through and leaves an ecosystem. These budgets show where nutrients are gained or lost."),
    ],
    "test": [
        ("What do nitrogen-fixing bacteria do?",
         [("a", "Make rocks"), ("b", "Make oil"), ("c", "Destroy the air"), ("d", "Convert nitrogen gas into forms plants can use")], "d"),
        ("Why is the phosphorus cycle slower than the nitrogen cycle?",
         [("a", "Phosphorus is a gas"), ("b", "Phosphorus has no major gas phase"), ("c", "Phosphorus is in the air"), ("d", "Phosphorus is a liquid")], "b"),
        ("What do decomposers do?",
         [("a", "Break down dead matter and release nutrients"), ("b", "Make new planets"), ("c", "Sell soil"), ("d", "Light up forests")], "a"),
        ("What is mineralisation?",
         [("a", "Mining for gold"), ("b", "Making glass"), ("c", "Releasing inorganic nutrients from organic matter"), ("d", "Turning rock into metal")], "c"),
        ("What is a limiting nutrient?",
         [("a", "The nutrient that is most plentiful"), ("b", "A nutrient that stops rain"), ("c", "The nutrient whose supply is lowest compared with need"), ("d", "A nutrient found only in the Sun")], "c"),
    ],
}
