"""Fracture and Fatigue: stress concentration, the Griffith criterion, crack growth, fatigue cycles, fracture toughness testing and designing against failure."""
CODE = "science4_mat_fracture"
BOOK = {
    "title": "Fracture and Fatigue",
    "subtitle": "Stress, cracks, fatigue and designing against failure",
    "chapters": [
        ("Stress concentration", "Stress builds up sharply around holes, sharp corners and cracks. This concentration of stress is why a small flaw can matter so much."),
        ("The Griffith criterion", "Griffith showed that a crack grows when the energy released by its growth is enough to create the new surface. This gives a critical stress for a crack of a given size."),
        ("Crack growth", "Cracks can grow slowly under a steady load, or suddenly once they reach a critical size. The growth rate depends on the stress and on the material."),
        ("Fatigue cycles", "Fatigue is the weakening caused by repeated loading and unloading. A part can fail under stresses far below its strength for a single load."),
        ("Fracture toughness testing", "Fracture toughness measures how well a material resists crack growth. Tests use a specimen with a notch, which gives a standard value for comparison."),
        ("Designing against failure", "Engineers design against fracture and fatigue by controlling flaws, choosing tough materials and limiting stress. Inspection finds cracks before they grow to failure."),
    ],
    "test": [
        ("Why do small flaws matter a lot?",
         [("a", "They concentrate stress"), ("b", "They make a part lighter"), ("c", "They change its colour"), ("d", "They make it quieter")], "a"),
        ("What did Griffith's criterion explain?",
         [("a", "Why metals rust"), ("b", "When a crack grows, based on an energy balance"), ("c", "The colour of rust"), ("d", "The taste of steel")], "b"),
        ("What is fatigue?",
         [("a", "Feeling tired after lifting"), ("b", "A heat treatment"), ("c", "A type of paint"), ("d", "Weakening from repeated loading and unloading")], "d"),
        ("What is fracture toughness?",
         [("a", "How shiny a metal is"), ("b", "How heavy a part is"), ("c", "How well a material resists crack growth"), ("d", "How fast sound moves through it")], "c"),
        ("What is the best way engineers design against fracture and fatigue?",
         [("a", "Ignore flaws"), ("b", "Use paint only"), ("c", "Make parts as thin as possible"), ("d", "Control flaws, choose tough materials, limit stress and inspect")], "d"),
    ],
}
