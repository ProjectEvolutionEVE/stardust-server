"""Protein Dynamics and Allostery: how proteins move between shapes, how a signal at one site changes another, and why drugs use this."""
CODE = "science5_bio_allostery"
BOOK = {
    "title": "Protein Dynamics and Allostery",
    "subtitle": "Proteins that move between shapes, and signals that travel from one site to another",
    "chapters": [
        ("Proteins are not still", "A protein is not a fixed object. It shifts and flexes, and it spends time in several shapes at once. Scientists describe this set of shapes as a conformational ensemble."),
        ("Conformational ensembles", "Each shape in the ensemble has its own likelihood. Changing conditions, such as binding a partner or a small molecule, can shift which shapes are most common."),
        ("Allosteric signalling", "Allostery is the process by which a change at one site on a protein alters activity at a distant site. It lets a protein act as a switch that responds to signals from far away."),
        ("NMR relaxation", "Nuclear magnetic resonance can measure how fast atomic nuclei return to their resting state after a pulse. These relaxation rates reveal how fast parts of a protein move."),
        ("Molecular dynamics", "Molecular dynamics is a computer method that simulates how atoms move over time, using the forces between them. Simulations show possible paths of motion, though the results depend on the model used."),
        ("Drug binding sites", "Allosteric sites are often different from the main active site. A drug that binds there can change how the protein works without blocking the main site, which can make drugs more selective."),
    ],
    "test": [
        ("What is a conformational ensemble?",
         [("a", "A group of cells"), ("b", "A single fixed shape"), ("c", "A set of shapes a protein can take, with different likelihoods"), ("d", "A gene cluster")], "c"),
        ("What is allosteric signalling?",
         [("a", "A change at one site that alters activity at a distant site"), ("b", "Sending a letter"), ("c", "A sound"), ("d", "Breaking a bond in water")], "a"),
        ("What does NMR relaxation reveal?",
         [("a", "Blood pressure"), ("b", "The weight of a protein"), ("c", "The colour of a sample"), ("d", "How fast nuclei return to rest, which shows how parts of a protein move")], "d"),
        ("What is molecular dynamics?",
         [("a", "A dance performance"), ("b", "A computer method that simulates how atoms move over time"), ("c", "A type of microscope"), ("d", "A way to grow crystals only")], "b"),
        ("Why do allosteric sites matter for drugs?",
         [("a", "They can be targets for drugs that change activity without blocking the main site"), ("b", "They are always the main site"), ("c", "They do not exist in proteins"), ("d", "They are only found in plants")], "a"),
    ],
}
