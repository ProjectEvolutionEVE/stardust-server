"""Monopropellant Thrusters: one liquid fuel, one catalyst, and the small engines that steer spacecraft."""
CODE = "flight5_s_monoprop"
BOOK = {
    "title": "Monopropellant Thrusters",
    "subtitle": "One liquid fuel, one catalyst, and the small engines that steer spacecraft",
    "chapters": [
        ("One fuel, no mixing",
         "A monopropellant thruster runs on a single liquid fuel. Hydrazine is the most common choice. Unlike most rocket engines, it does not need a separate oxidiser to burn."),
        ("The catalyst bed",
         "When hydrazine passes over a catalyst, usually a bed of small metal grains, it breaks down into hot gas very quickly. The hot gas rushes out of a nozzle and gives the push. No spark or igniter is needed."),
        ("Small pushes, many times",
         "These engines suit small jobs: turning a craft, correcting its path and holding it steady. Each firing is brief, and a spacecraft may fire the same thruster thousands of times over its life."),
        ("Simple and dependable",
         "The design has few moving parts, which makes it dependable. The catalyst can wear with age, so engineers test it and track its performance closely."),
        ("Handling the fuel",
         "Hydrazine is toxic. Teams handle it in protective gear, following strict steps. That care makes work at the launch site slower and more costly."),
        ("Greener choices",
         "Engineers are testing alternative fuels that are less toxic. Each one has its own trade-offs in power, storage and handling, so none is an easy swap."),
    ],
    "test": [
        ("What does a monopropellant thruster use as its fuel?",
         [("a", "A mix of two fuels and an oxidiser"), ("b", "Solid powder pellets"), ("c", "One liquid fuel that breaks down on a catalyst"), ("d", "Light from the Sun")], "c"),
        ("What does the catalyst do in this thruster?",
         [("a", "It speeds the breakdown of the fuel into hot gas"), ("b", "It cools the engine"), ("c", "It stores extra fuel"), ("d", "It sends radio signals")], "a"),
        ("What are these thrusters mainly used for on a spacecraft?",
         [("a", "Carrying heavy cargo"), ("b", "Launching from the ground"), ("c", "Lighting the cabin"), ("d", "Small steering and attitude adjustments")], "d"),
        ("Why is hydrazine a concern for ground teams?",
         [("a", "It is too cold to handle"), ("b", "It is toxic"), ("c", "It glows in the dark"), ("d", "It floats on water")], "b"),
        ("Why do engineers like the simple thruster design?",
         [("a", "It needs a strong magnet"), ("b", "It burns with a spark"), ("c", "It has few moving parts, so it is dependable"), ("d", "It never needs checking")], "c"),
    ],
}
