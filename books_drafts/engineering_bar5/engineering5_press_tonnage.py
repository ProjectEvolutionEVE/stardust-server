"""Press Tonnage and Forming Energy: force calculations, energy per stroke, press selection and the cost of forming per part."""
CODE = "engineering5_press_tonnage"
BOOK = {
    "title": "Press Tonnage and Forming Energy",
    "subtitle": "Choosing a press strong enough, and not one bigger than needed",
    "chapters": [
        ("The force a press must give",
         "Every forming job needs a certain force. The press must supply more than that force, with margin, or the job will stall. The force is called the tonnage, and it is the first number an engineer finds."),
        ("Force calculations",
         "The force is estimated from the area being formed and the flow stress of the metal. Friction and the shape of the part add to it. Simulation and test runs check the estimate before the press is chosen."),
        ("Energy per stroke",
         "Forming also needs energy, which is the force multiplied by the distance the press moves while it works. A mechanical press stores energy in a flywheel. Enough energy per stroke is needed, not only enough force."),
        ("Choosing the press",
         "A press that is too small cannot finish the part. A press far too large costs more to buy and run, and wastes energy. Engineers pick a press with a sensible margin above the calculated need."),
        ("Cost per formed part",
         "The cost of forming a part adds the press time, the energy, the labour and the tooling wear. A faster press that makes more parts per hour lowers the cost of each part. Engineers track cost per part, not only the cost of the press."),
        ("Checking the numbers",
         "Load cells and sensors on the press can show the real force during a run. Comparing these readings with the calculation tells the engineer whether the estimate was sound. The numbers improve with each job."),
    ],
    "test": [
        ("What is the tonnage of a press?",
         [("a", "The force it must supply to form a part"), ("b", "The number of workers"), ("c", "The weight of the floor"), ("d", "The colour of the metal")], "a"),
        ("What is forming energy per stroke?",
         [("a", "The price of the press"), ("b", "The force multiplied by the distance the press moves while working"), ("c", "The hours in a shift"), ("d", "The number of bolts")], "b"),
        ("Why is a press far too large a problem?",
         [("a", "It makes the part invisible"), ("b", "It always breaks the metal"), ("c", "It costs more to buy and run and wastes energy"), ("d", "It cannot be switched on")], "c"),
        ("What does the cost per formed part include?",
         [("a", "Only the colour of the paint"), ("b", "Only the name of the factory"), ("c", "Only the weather"), ("d", "Press time, energy, labour and tooling wear")], "d"),
        ("What do load cells on a press show?",
         [("a", "The real force during a run"), ("b", "The number of birds nearby"), ("c", "The price of the metal"), ("d", "The shape of the building")], "a"),
    ],
}
