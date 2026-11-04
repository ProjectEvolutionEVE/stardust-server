"""The Cell Cycle and Checkpoints: how cyclins, kinases and checkpoints keep cell division orderly and safe."""
CODE = "science5_bio_cell_cycle"
BOOK = {
    "title": "The Cell Cycle and Checkpoints",
    "subtitle": "How cells grow, copy their DNA and divide, with safety checks along the way",
    "chapters": [
        ("A cycle of growth and division", "Cells grow, copy their DNA and divide in a repeating cycle. The cycle has clear phases, and each one prepares the cell for the next."),
        ("Cyclins and CDKs", "Cyclins rise and fall in a set rhythm. Each cyclin partners with a cyclin-dependent kinase, and together they drive the cell forward through its phases."),
        ("G1/S and G2/M transitions", "The G1/S transition commits the cell to copying its DNA. The G2/M transition commits it to dividing. Each transition is a switch that is hard to reverse once it is thrown."),
        ("DNA damage checkpoints", "If DNA is damaged, checkpoints pause the cycle so the damage can be repaired. If the damage is too severe, the cell may be directed to die instead of dividing."),
        ("The spindle checkpoint", "The spindle assembly checkpoint checks that every chromosome is attached correctly to the spindle fibres before they are pulled apart. This check prevents chromosomes from being split unevenly."),
        ("Oscillators and cycle errors", "The cycle works like a clock built from interlinked switches. When checkpoints fail or are overridden, cells may gain or lose chromosomes, which can lead to uncontrolled growth."),
    ],
    "test": [
        ("What do cyclins do?",
         [("a", "Partner with cyclin-dependent kinases to drive the cell forward through the cycle"), ("b", "Make cells blue"), ("c", "Destroy DNA"), ("d", "Stop protein making")], "a"),
        ("What does the G1/S transition do?",
         [("a", "Ends the cell's life"), ("b", "Turns a cell into a neuron"), ("c", "Commits the cell to copying its DNA"), ("d", "Splits the cell in two at once")], "c"),
        ("What is the job of a DNA damage checkpoint?",
         [("a", "To ignore broken DNA"), ("b", "To pause the cycle so damaged DNA can be repaired"), ("c", "To speed up cell division regardless"), ("d", "To make the DNA longer")], "b"),
        ("What does the spindle assembly checkpoint check?",
         [("a", "The colour of the cell"), ("b", "The weather"), ("c", "The temperature of the room"), ("d", "Whether chromosomes are attached correctly to spindle fibres before separation")], "d"),
        ("What can happen when cell cycle errors are not corrected?",
         [("a", "Cells always get better"), ("b", "Nothing ever happens"), ("c", "Cells may gain abnormal numbers of chromosomes or uncontrolled growth"), ("d", "The cell grows wings")], "c"),
    ],
}
