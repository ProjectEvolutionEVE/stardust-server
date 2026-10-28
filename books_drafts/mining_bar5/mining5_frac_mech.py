"""Fracture Mechanics in Rock: how cracks grow, why some grow faster than others, and how rock toughness is measured in the lab."""
CODE = "mining5_frac_mech"
BOOK = {
    "title": "Fracture Mechanics in Rock",
    "subtitle": "Stress intensity, toughness, crack growth, joints and design",
    "chapters": [
        ("Cracks and their tips",
         "Fracture mechanics studies how cracks behave. The stress at the tip of a crack is far higher than the stress in the surrounding rock. That tip is where a crack grows."),
        ("Stress intensity",
         "The stress intensity factor is a number that describes the stress near a crack tip. It depends on the load, the crack length and its shape. When it reaches a critical value, the crack starts to move."),
        ("Fracture toughness",
         "Fracture toughness is the critical value at which a crack runs. Tough rock resists cracking more than brittle rock. It is measured in the laboratory on notched samples under controlled loads."),
        ("Crack growth",
         "A crack may grow slowly under a steady load, especially in wet or chemically active conditions. Growth rate is often linked to the stress intensity by a simple law. Knowing the rate helps set how long a slope or pillar can be trusted."),
        ("Joints",
         "Joints are natural cracks in rock, usually with little or no sideways movement across them. They are weak planes along which a block can slide or open. Mapping joints shows where a rock mass is likely to fail."),
        ("Design",
         "Fracture mechanics helps engineers choose blast designs, support patterns and slope angles. It is used together with the strength and stress of the rock. A design that ignores cracks is likely to be too optimistic."),
    ],
    "test": [
        ("Where is the stress highest near a crack?",
         [("a", "Far away in the sky"), ("b", "At the crack tip"), ("c", "Inside the drill bit"), ("d", "At the office door")], "b"),
        ("What does the stress intensity factor describe?",
         [("a", "The stress near a crack tip, which decides whether it moves"), ("b", "The price of the ore"), ("c", "The depth of the water table"), ("d", "The number of joints mapped")], "a"),
        ("What is fracture toughness?",
         [("a", "The critical value at which a crack runs"), ("b", "The colour of a fracture"), ("c", "The weight of a sample"), ("d", "The age of a drill hole")], "a"),
        ("What can make a crack grow slowly under steady load?",
         [("a", "Dry, cold air only"), ("b", "Zero stress at all times"), ("c", "Wet or chemically active conditions"), ("d", "Lying still in a box")], "c"),
        ("Why is mapping joints useful?",
         [("a", "It replaces all drilling"), ("b", "It proves the rock is perfect"), ("c", "It makes the rock heavier"), ("d", "It shows where a rock mass is likely to fail")], "d"),
    ],
}
