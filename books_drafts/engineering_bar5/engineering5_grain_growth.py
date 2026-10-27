"""Grain Growth and Recrystallisation: how new grains form in cold-worked metal, and how they coarsen."""
CODE = "engineering5_grain_growth"
BOOK = {
    "title": "Grain Growth and Recrystallisation",
    "subtitle": "How new grains form in cold-worked metal, and how they coarsen",
    "chapters": [
        ("Cold work stores energy",
         "Bending or rolling a metal cold stores energy in its defects. That stored energy drives change when the metal is heated."),
        ("Recrystallisation",
         "New, strain-free grains form and grow into the cold-worked metal, replacing the deformed structure. The temperature needed depends on the metal and on how much cold work it has had."),
        ("Grain growth laws",
         "After recrystallisation, larger grains tend to grow at the expense of smaller ones, which lowers the total boundary energy. Growth slows as the grains get bigger."),
        ("Zener pinning",
         "Tiny particles along grain boundaries can pin them in place and slow or stop growth. This is Zener pinning, and it depends on the size and amount of the particles."),
        ("Annealing schedules",
         "An annealing schedule sets the temperature, time and cooling rate needed for the grain size and softness wanted. Too hot or too long coarsens the grains and weakens the metal."),
        ("Control in practice",
         "The right grain size gives the right strength and toughness. Measuring the grain size after annealing confirms that the schedule worked."),
    ],
    "test": [
        ("What drives change when cold-worked metal is heated?",
         [("a", "The sun"), ("b", "Paint"), ("c", "A price rise"), ("d", "Stored energy in its defects")], "d"),
        ("What is recrystallisation?",
         [("a", "Rain"), ("b", "New strain-free grains growing into the deformed metal"), ("c", "Sales"), ("d", "A paint process")], "b"),
        ("What does Zener pinning do?",
         [("a", "Freezes water"), ("b", "Paints the metal"), ("c", "Particles pin grain boundaries and slow growth"), ("d", "Adds weight")], "c"),
        ("What does an annealing schedule set?",
         [("a", "Only the colour"), ("b", "Only the price"), ("c", "Only the weight"), ("d", "Temperature, time and cooling rate")], "d"),
        ("What happens if grains coarsen too much?",
         [("a", "The metal weakens"), ("b", "The metal always gets stronger"), ("c", "Nothing"), ("d", "It turns to glass")], "a"),
    ],
}
