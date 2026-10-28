"""Non-Traditional Machining: EDM, Waterjet and Laser. Cutting and shaping without a cutting tool touching the part."""
CODE = 'engineering4_nontrad'
BOOK = {
    "title": "Non-Traditional Machining: EDM, Waterjet, Laser",
    "subtitle": "Cutting and shaping without a cutting tool touching the part",
    "chapters": [
        ("Machining without a cutter",
         "Non-traditional methods remove material with sparks, a high-pressure water jet, or a focused beam of light. No cutting tool presses on the part, so very hard or very delicate parts can be shaped."),
        ("Spark erosion (EDM)",
         "In electrical discharge machining, electric sparks jump between an electrode and the part, melting and blasting away tiny bits of metal. It works on hard metals that are difficult to cut with a tool, and the electrode shape sets the cut."),
        ("Abrasive waterjet",
         "Water pushed at very high pressure carries fine grit through a small nozzle. It cuts thick materials and does not heat the edge much. It suits stone, glass and metal that could be damaged by heat."),
        ("Laser cutting",
         "A focused laser beam melts, burns or vaporises the material along a line. It suits thin sheet at high speed and gives precise shapes with a narrow cut."),
        ("Choosing a process",
         "EDM fits hard conductive metals and tight internal shapes. Waterjet fits thick or heat-sensitive materials. Laser fits thin sheet where speed matters. The job decides the process."),
        ("Running costs",
         "Each method has its own costs: power and electrodes for EDM, grit and water for waterjet, and gas and power for lasers. Compare the cost per part, not only the price of the machine."),
    ],
    "test": [
        ("What makes these methods non-traditional?",
         [("a", "They do not use a cutting tool pressing on the part"), ("b", "They use paper"), ("c", "They only work on wood"), ("d", "They are done by hand")], "a"),
        ("What does EDM use to remove metal?",
         [("a", "A saw blade"), ("b", "A hot knife"), ("c", "Electric sparks"), ("d", "A drill bit")], "c"),
        ("Which process suits thick, heat-sensitive materials?",
         [("a", "A laser only"), ("b", "Abrasive waterjet"), ("c", "A paper knife"), ("d", "A spoon")], "b"),
        ("What does a laser cutter do?",
         [("a", "It sews the part"), ("b", "It prints ink"), ("c", "It bends the metal"), ("d", "It melts, burns or vaporises material along a line")], "d"),
        ("What should you compare when choosing a process?",
         [("a", "Cost per part"), ("b", "The colour of the machine"), ("c", "The name of the factory"), ("d", "The weather")], "a"),
    ],
}
