"""Antibiotic Resistance Mechanisms: how bacteria change their targets, pump drugs out and break drugs down, and how that spread is tracked."""
CODE = "science5_bio_resistance"
BOOK = {
    "title": "Antibiotic Resistance Mechanisms",
    "subtitle": "How bacteria survive antibiotics, and how scientists track the spread",
    "chapters": [
        ("Evolution in action", "Antibiotics kill or slow bacteria, but some bacteria survive by chance. Those survivors can pass their traits on, so resistance can spread through a population."),
        ("Target modification", "Some bacteria change the molecule that a drug aims at. The changed target binds the drug less well, so the drug has less effect on the cell."),
        ("Efflux pumps", "An efflux pump is a protein that pumps a drug out of the cell. By keeping the drug level low, the pump lets the bacterium survive exposure."),
        ("Enzymatic inactivation", "Some bacteria make enzymes that chemically break or modify a drug, so it stops working. Beta-lactamase enzymes are a well-known example of this kind of defence."),
        ("How resistance evolves", "Resistance evolves through selection. Bacteria that carry a resistance trait survive treatment and multiply, so the trait becomes more common in the population."),
        ("Surveillance of resistance", "Surveillance tracks which resistances are spreading and where. This information guides treatment choices, infection control and public policy."),
    ],
    "test": [
        ("What is target modification in resistance?",
         [("a", "Changing the colour of a drug"), ("b", "Breaking a drug into smaller pieces"), ("c", "Adding a drug to a cell"), ("d", "Changing the drug's target so the drug binds less well")], "d"),
        ("What is an efflux pump?",
         [("a", "A water tap"), ("b", "A protein that pumps a drug out of the cell"), ("c", "A kind of spacecraft"), ("d", "A type of virus")], "b"),
        ("What is enzymatic inactivation?",
         [("a", "Making enzymes stronger"), ("b", "Turning enzymes into sugar"), ("c", "An enzyme chemically breaks or modifies a drug so it stops working"), ("d", "Stopping all enzymes in the body")], "c"),
        ("How does resistance evolve?",
         [("a", "By selection: resistant bacteria survive treatment and multiply"), ("b", "By the bacteria choosing it"), ("c", "By the weather"), ("d", "By the Moon")], "a"),
        ("What does surveillance of resistance do?",
         [("a", "Stops all bacteria"), ("b", "Tracks which resistances are spreading, to guide treatment and policy"), ("c", "Makes new planets"), ("d", "Counts stars")], "b"),
    ],
}
