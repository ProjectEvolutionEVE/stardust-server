"""Heat Pipes and Two-Phase Cooling: moving heat along a sealed tube by boiling at one end and condensing at the other."""
CODE = 'engineering4_heat_pipes'
BOOK = {
    "title": "Heat Pipes and Two-Phase Cooling",
    "subtitle": "Moving heat along a sealed tube by boiling at one end and condensing at the other",
    "chapters": [
        ("Evaporation and condensation",
         "A heat pipe is a sealed tube holding a small amount of working fluid. Heat boils the fluid at the hot end, the vapour travels to the cool end, and it condenses there, giving up its heat."),
        ("Wick types",
         "A wick returns the liquid to the hot end by capillary action. Wicks can be grooves, mesh or sintered powder, each with its own strengths."),
        ("Operating limits",
         "Heat pipes have limits, including a maximum heat flow, a dry-out point when the wick runs out of liquid, and a usable temperature range."),
        ("Where heat pipes are used",
         "Heat pipes cool laptops, electronics and spacecraft, among other things. They move heat with very little drop in temperature."),
        ("Gravity and orientation",
         "Some heat pipes rely on gravity to return the liquid, while wicked ones work in any direction. Orientation matters when the pipe is designed."),
        ("Why they help",
         "Heat pipes spread heat well and need no pump. Their simple, quiet operation makes them useful in tight spaces."),
    ],
    "test": [
        ("What happens at the hot end of a heat pipe?",
         [("a", "The fluid freezes"), ("b", "The tube cracks"), ("c", "The fluid boils"), ("d", "The tube is painted")], "c"),
        ("What does a wick do?",
         [("a", "Returns liquid to the hot end by capillary action"), ("b", "Holds paint"), ("c", "Cools the sun"), ("d", "Stores air")], "a"),
        ("What is dry-out?",
         [("a", "A wet floor"), ("b", "A rain shower"), ("c", "A sauna"), ("d", "When the wick runs out of liquid and the pipe stops working well")], "d"),
        ("Where are heat pipes used?",
         [("a", "Only in houses"), ("b", "In electronics and spacecraft, among other places"), ("c", "In shoe shops"), ("d", "In bakeries")], "b"),
        ("What does a heat pipe need to move heat?",
         [("a", "A pump"), ("b", "A battery"), ("c", "No pump, using boiling and condensing"), ("d", "A motor")], "c"),
    ],
}
