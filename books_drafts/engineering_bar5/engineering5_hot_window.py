"""Hot Working Temperature Windows: recrystallisation windows, flow stress against temperature, cracking limits and choosing forging and rolling temperatures."""
CODE = "engineering5_hot_window"
BOOK = {
    "title": "Hot Working Temperature Windows",
    "subtitle": "Choosing the heat that lets metal be shaped without cracking",
    "chapters": [
        ("Shaping hot metal",
         "Hot working shapes metal at a temperature high enough that it softens. Forging and rolling are common examples. The right temperature makes the work easier and the grain structure better."),
        ("Recrystallisation",
         "When metal is hot and deformed, new grains form in place of the strained ones. This is recrystallisation. Working above the recrystallisation temperature keeps the grains fine and the metal sound."),
        ("Flow stress against temperature",
         "Flow stress is the force per area needed to keep the metal deforming. It drops as the temperature rises, so the metal is easier to shape. Engineers read the curve to set the force the press must deliver."),
        ("Cracking limits",
         "Too cold, and the metal cracks under the work. Too hot, and it can burn or form a brittle layer at the grain boundaries. Every alloy has a window between those two limits."),
        ("Choosing forging temperatures",
         "The forging or rolling temperature is picked from the window for the alloy. The engineer leaves margin for the heat lost as the part moves to the press. Measuring the actual temperature at the part is part of good practice."),
        ("Keeping the window",
         "Parts that cool too much during handling must be reheated, or the window is lost. Furnace time and handling speed are planned together. Staying inside the window saves energy, tooling and scrap."),
    ],
    "test": [
        ("What is hot working?",
         [("a", "Painting metal while it is cold"), ("b", "Storing metal in ice"), ("c", "Cutting paper with metal"), ("d", "Shaping metal at a temperature high enough that it softens")], "d"),
        ("What is recrystallisation?",
         [("a", "New grains forming in place of strained ones when hot"), ("b", "The metal melting completely"), ("c", "The metal turning into glass"), ("d", "Paint drying on the metal")], "a"),
        ("What happens to flow stress as temperature rises?",
         [("a", "It rises sharply to infinity"), ("b", "It drops, so the metal is easier to shape"), ("c", "It stays exactly the same"), ("d", "It turns into electricity")], "b"),
        ("What happens if the work is too cold?",
         [("a", "The metal becomes lighter"), ("b", "The metal turns blue"), ("c", "The metal can crack under the work"), ("d", "Nothing happens at all")], "c"),
        ("Why is a margin left for heat loss?",
         [("a", "The press needs warm oil"), ("b", "The part must grow larger"), ("c", "The margin is painted on"), ("d", "The part cools as it moves to the press, and must stay in the window")], "d"),
    ],
}
