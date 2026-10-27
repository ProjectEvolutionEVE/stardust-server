"""Otto and Diesel Cycles: how piston engines compress, ignite and push, and why real ones fall short."""
CODE = 'engineering4_otto_diesel'
BOOK = {
    "title": "Otto and Diesel Cycles",
    "subtitle": "How piston engines compress, ignite and push, and why real ones fall short",
    "chapters": [
        ("Piston engines",
         "A piston engine draws in air or a fuel mixture, compresses it, burns fuel, and pushes the piston down to make work. The cycle repeats many times a minute."),
        ("Compression ratio",
         "The compression ratio is how far the gas is squeezed. A higher ratio gives a higher ideal efficiency, though there are limits to how high it can go in practice."),
        ("Knock",
         "In a petrol engine, the mixture can ignite too early under high compression. This is called knock. It wastes power and can damage the engine."),
        ("Diesel ignition",
         "A diesel engine squeezes air so hard that it becomes hot enough to ignite the fuel when it is sprayed in. It needs no spark plug."),
        ("Real against ideal",
         "Real engines lose heat, lose energy to friction and take time to complete each stroke, so they fall well short of the ideal cycle. Closing that gap is where most engine design work happens."),
        ("Fuel cost per mile",
         "Fuel cost depends on the engine's efficiency and the energy in the fuel. Better efficiency means fewer litres for the same distance."),
    ],
    "test": [
        ("What is the compression ratio?",
         [("a", "The speed of the piston"), ("b", "The weight of the engine"), ("c", "How far the gas is squeezed"), ("d", "The number of wheels")], "c"),
        ("What is knock?",
         [("a", "Early ignition under high compression, which wastes power"), ("b", "A bell"), ("c", "A tyre noise"), ("d", "A scratch in the paint")], "a"),
        ("How does a diesel engine ignite its fuel?",
         [("a", "With a spark plug"), ("b", "With a match"), ("c", "With ice"), ("d", "By the heat of compressed air")], "d"),
        ("Why do real engines fall short of the ideal cycle?",
         [("a", "They have no pistons"), ("b", "They lose heat, energy to friction and time"), ("c", "They are painted"), ("d", "They run in space")], "b"),
        ("What lowers fuel cost per mile?",
         [("a", "A heavier car"), ("b", "A bigger fuel tank"), ("c", "More braking"), ("d", "Better efficiency, which means fewer litres for the same distance")], "d"),
    ],
}
