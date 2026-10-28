"""Piezoelectric actuators and micropositioning: the piezo effect, stacks, hysteresis, precision positioning, harvesting limits and drive needs."""
CODE = "engineering4_piezo"
BOOK = {
    "title": "Piezoelectric Actuators and Micropositioning",
    "subtitle": "The piezo effect, stacks and precision positioning",
    "chapters": [
        ("The piezo effect",
         "Some crystals and ceramics change shape slightly when a voltage is applied. The same materials make a small voltage when they are squeezed. This two-way link is the piezoelectric effect."),
        ("Stacks",
         "Many thin piezo layers can be stacked to give a larger movement at a usable voltage. A stack moves in tiny steps that can be very precise. The stack is a common form for precision actuators."),
        ("Hysteresis",
         "A piezo actuator does not always return to the same position for the same voltage. Its response depends on its recent history, which is called hysteresis. Designers add sensors or control methods to correct for it."),
        ("Precision positioning",
         "Piezo positioners can move by fractions of a micrometre with fast response. They are used in microscopes, optical alignment and precision machines. Their range of movement is small, so they often sit on larger stages."),
        ("Energy harvesting limits",
         "Piezo materials can turn small vibrations into electrical energy. The amount harvested is usually small, and it is limited by the material and the size of the vibration. Harvesting suits low-power sensors more than large loads."),
        ("Drive requirements",
         "Piezo actuators need a drive electronics unit that supplies a controlled voltage. The drive must suit the capacitance of the stack and the speed of movement. Engineers match the drive to the load and the precision needed."),
    ],
    "test": [
        ("What is the piezoelectric effect?", [("a", "A material changing shape slightly when a voltage is applied"), ("b", "A heater that warms rooms"), ("c", "A light that glows"), ("d", "A glue for paper")], "a"),
        ("Why are piezo layers stacked?", [("a", "To stop all movement"), ("b", "To make the stack heavier"), ("c", "To hide the layers"), ("d", "To give a larger movement at a usable voltage")], "d"),
        ("What is hysteresis in a piezo actuator?", [("a", "A type of spring"), ("b", "A position that depends on the recent history, so the same voltage may give different positions"), ("c", "A colour change"), ("d", "A loud noise")], "b"),
        ("Where are piezo positioners often used?", [("a", "In tyre pumps"), ("b", "In bread ovens"), ("c", "In microscopes and optical alignment"), ("d", "In barrels of oil")], "c"),
        ("What do piezo drives need to supply?", [("a", "A heavy weight"), ("b", "A flood of water"), ("c", "A controlled voltage that suits the stack and the speed of movement"), ("d", "A paint spray")], "c"),
    ],
}
