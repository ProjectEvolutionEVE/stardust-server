"""Special Relativity in Practice: time dilation, length contraction and spacetime diagrams, with real experiments that confirm them."""
CODE = "science4_phys_special_rel"
BOOK = {
    "title": "Special Relativity in Practice",
    "subtitle": "Time, length and energy when objects move near the speed of light",
    "chapters": [
        ("Time dilation",
         "A moving clock runs slow compared with a clock at rest. The effect is small at everyday speeds and grows as speed approaches the speed of light. Time dilation is a measured fact, not just a theory."),
        ("Length contraction",
         "A moving object is measured to be shorter along its direction of motion. Like time dilation, the effect becomes large only at very high speeds. Observers in different frames agree on physics but may disagree about lengths and times."),
        ("Spacetime diagrams",
         "A spacetime diagram plots time against position, so each event is a point. Lines show how objects move through space and time. Such diagrams make it easier to see why two observers can disagree about simultaneous events."),
        ("Muon experiments",
         "Muons created high in the atmosphere live only a short time in their own frame. Many still reach the ground because their time runs slow as they move fast. Measuring their arrival rate confirms time dilation."),
        ("Relativistic energy",
         "The total energy of a moving particle grows without limit as its speed nears the speed of light. The famous relation E equals mc squared gives the rest energy. Speeding up a particle takes more and more energy."),
        ("Consequences for particle accelerators",
         "Particle accelerators must include relativity in their design. Fast particles carry far more energy and momentum than their speed alone suggests, while their rest mass stays the same, and their paths and timing must be calculated with that in mind. Without relativity, the machines would not work as built."),
    ],
    "test": [
        ("What happens to a moving clock compared with one at rest?",
         [("a", "It runs slow"), ("b", "It runs faster"), ("c", "It stops at once"), ("d", "It keeps the same time")], "a"),
        ("What is length contraction?",
         [("a", "Objects grow when they move"), ("b", "A moving object is measured shorter along its direction of motion"), ("c", "Rulers melt in the sun"), ("d", "Objects change colour")], "b"),
        ("Why do muons from the upper atmosphere still reach the ground?",
         [("a", "Because their time runs slow as they move fast"), ("b", "Because they do not decay at all"), ("c", "Because the ground pulls them up"), ("d", "Because they are heavy")], "a"),
        ("What is the rest energy relation?",
         [("a", "E equals m times v"), ("b", "E equals m divided by c"), ("c", "E equals m c squared"), ("d", "E equals zero")], "c"),
        ("What does a spacetime diagram plot?",
         [("a", "Colour against sound"), ("b", "Weight against height"), ("c", "Time against position"), ("d", "Price against sales")], "c"),
    ],
}
