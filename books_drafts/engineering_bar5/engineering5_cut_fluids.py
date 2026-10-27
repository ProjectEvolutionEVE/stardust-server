"""Cutting Fluid Chemistry and Health: lubricity, cooling, biocides, fluid life, operator exposure limits and the money side of fluid recycling."""
CODE = "engineering5_cut_fluids"
BOOK = {
    "title": "Cutting Fluid Chemistry and Health",
    "subtitle": "Keeping tools cool and clean while keeping people safe",
    "chapters": [
        ("What the fluid does",
         "Cutting fluid cools the tool and the work, and it lubricates the cut. Less friction means less heat and longer tool life. A good fluid also carries chips away from the cutting zone."),
        ("Lubricity and cooling",
         "Lubricity is how well the fluid reduces friction at the tool face. Cooling is how well it carries heat away. Oil-based fluids lubricate best; water-based fluids cool best. Most fluids balance the two."),
        ("Biocides",
         "Water-based fluids can grow bacteria and fungi, which cause smell and skin problems. Biocides are added to keep them under control. The right biocide and its level are checked regularly."),
        ("Fluid life",
         "Fluid life is how long a fluid stays useful before it must be changed. Chips, tramp oil and bacteria shorten it. Keeping the sump clean and the concentration right makes the fluid last longer."),
        ("Operator exposure",
         "Workers can breathe mist and touch the fluid for hours each day. Exposure limits set how much mist is allowed in the air. Good ventilation and guards help meet those limits; gloves protect the skin."),
        ("The money side",
         "Buying fresh fluid and disposing of old fluid cost real money. Recycling and filtering can extend fluid life and cut both costs. Engineers compare the cost of recycling with the cost of new fluid and disposal."),
    ],
    "test": [
        ("What does cutting fluid do?",
         [("a", "It cools the tool and work and lubricates the cut"), ("b", "It paints the part"), ("c", "It welds the chips together"), ("d", "It makes the metal harder to cut")], "a"),
        ("Which kind of fluid is usually best at lubricating?",
         [("a", "Plain air"), ("b", "Oil-based fluids"), ("c", "Dry sand"), ("d", "Frozen water")], "b"),
        ("Why are biocides added to water-based fluids?",
         [("a", "To make the fluid sweeter"), ("b", "To make the fluid heavier"), ("c", "To keep bacteria and fungi under control"), ("d", "To change the metal's colour")], "c"),
        ("What shortens fluid life?",
         [("a", "Clean filters and right concentration"), ("b", "Cool storage rooms"), ("c", "Regular checks"), ("d", "Chips, tramp oil and bacteria")], "d"),
        ("What do exposure limits control?",
         [("a", "How much mist workers may breathe in the air"), ("b", "How many fluid drums are stored"), ("c", "How fast the spindle turns"), ("d", "How bright the lights are")], "a"),
    ],
}
