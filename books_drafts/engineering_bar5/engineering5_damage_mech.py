"""Continuum Damage Mechanics: describing the gradual loss of stiffness as a material fills with micro-cracks."""
CODE = "engineering5_damage_mech"
BOOK = {
    "title": "Continuum Damage Mechanics",
    "subtitle": "Describing gradual loss of stiffness as a material fills with micro-cracks",
    "chapters": [
        ("Damage as a variable",
         "Continuum damage mechanics describes the spread of tiny cracks and voids with a damage variable. The variable runs from zero for an undamaged material to one for a fully broken one."),
        ("Stiffness degradation",
         "As damage grows, the material loses stiffness. The stress for a given strain drops, even before a visible crack appears."),
        ("Damage evolution laws",
         "A damage evolution law sets how fast the damage variable grows with load or strain. It turns the idea of damage into a rule a computer can use."),
        ("Calibration from tests",
         "The laws are fitted to test data, such as the stiffness measured over repeated load cycles. A good fit gives confidence in predictions for new loading."),
        ("The link to fracture",
         "When damage reaches a critical value in a region, a crack is likely to start there. The damage model can therefore estimate where and when a crack is likely to start."),
        ("Keep it plain",
         "The damage variable is a model, not a count of each crack. It is most useful when the cracks are too many or too small to track one by one."),
    ],
    "test": [
        ("What does the damage variable run from?",
         [("a", "Zero for undamaged to one for fully broken"), ("b", "Ten to a hundred"), ("c", "Red to blue"), ("d", "Left to right")], "a"),
        ("What happens to stiffness as damage grows?",
         [("a", "Stiffness rises"), ("b", "Stiffness falls"), ("c", "Only the colour changes"), ("d", "The mass grows")], "b"),
        ("What is a damage evolution law?",
         [("a", "A tax form"), ("b", "A list of paints"), ("c", "A map of the sea"), ("d", "A rule for how fast damage grows with load or strain")], "d"),
        ("How are the damage laws usually set?",
         [("a", "By guessing"), ("b", "By fitting to test data"), ("c", "By the price of steel"), ("d", "By counting birds")], "b"),
        ("When does a damage model predict a crack?",
         [("a", "When damage reaches a critical value in a region"), ("b", "Never"), ("c", "At the first sound"), ("d", "When the paint dries")], "a"),
    ],
}
