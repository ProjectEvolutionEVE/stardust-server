"""Hot Isostatic Pressing: Closing Internal Pores. Gas pressure at high temperature, pore closure, cast and printed parts, and the money side of cycle cost against scrap saved."""
CODE = "engineering5_hip"
BOOK = {
    "title": "Hot Isostatic Pressing: Closing Internal Pores",
    "subtitle": "Squeezing the hidden holes out of a part with hot gas",
    "chapters": [
        ("Holes you cannot see",
         "Castings and printed metal parts can hold tiny internal pores. The pores are often too small to see from outside, but they can start a crack under load. Hot isostatic pressing, or HIP, is one way to close them."),
        ("Heat and pressure together",
         "In a HIP furnace, a part is heated and surrounded by an inert gas, usually argon. The gas presses on the part from every side at the same time, which is what isostatic means. Heat makes the metal soft enough for the pores to close."),
        ("How pores close",
         "Under heat and pressure, the metal around a pore yields and creeps inward. The pore shrinks and closes, and the metal bonds across the old space. Good HIP cycles can close most internal pores in the part."),
        ("Cast and printed parts",
         "HIP is widely used on castings and on metal parts made by powder bed printing. Both can carry internal porosity from the process. Closing it can raise fatigue life a great deal, which matters for safety parts."),
        ("Cycle cost against scrap",
         "A HIP cycle takes time and furnace energy, so it adds cost to each batch. Often the cost is worth paying, because it saves parts that would otherwise be scrapped. The engineer compares the cycle cost with the scrap and the risk avoided."),
        ("Checking the result",
         "After HIP, parts are checked by inspection, such as X-ray or CT, and by sample tests. A cycle that looks good on paper must still be proven on the actual parts. Records of each cycle are kept for traceability."),
    ],
    "test": [
        ("What gas is commonly used in a HIP furnace?",
         [("a", "Chlorine"), ("b", "Pure oxygen"), ("c", "Steam"), ("d", "Argon")], "d"),
        ("What does isostatic mean in this process?",
         [("a", "Pressure comes from every side at the same time"), ("b", "Pressure comes from one side only"), ("c", "The part is cooled quickly"), ("d", "The part is painted")], "a"),
        ("How does HIP close an internal pore?",
         [("a", "The pore fills with paint"), ("b", "The metal around the pore yields and creeps inward under heat and pressure"), ("c", "The pore is drilled out"), ("d", "The pore is frozen solid")], "b"),
        ("Which kinds of parts often carry internal porosity that HIP can help?",
         [("a", "Paper cups"), ("b", "Glass bottles"), ("c", "Castings and printed metal parts"), ("d", "Wooden boards")], "c"),
        ("What does the engineer weigh when choosing a HIP cycle?",
         [("a", "The colour of the furnace"), ("b", "The name of the operator"), ("c", "The weather that day"), ("d", "The cycle cost against the scrap and risk it avoids")], "d"),
    ],
}
