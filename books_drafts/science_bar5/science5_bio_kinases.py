"""Cell Signalling Cascades and Kinases: how phosphate tags pass messages through cells, and how scaffolds, feedback and drugs shape them."""
CODE = "science5_bio_kinases"
BOOK = {
    "title": "Cell Signalling Cascades and Kinases",
    "subtitle": "How phosphate tags carry messages through a cell, and how drugs can target them",
    "chapters": [
        ("Messages inside cells", "Cells respond to signals from outside by passing messages from one protein to the next. Many of these messages are carried by a chain of chemical changes called a cascade."),
        ("Phosphorylation", "A kinase adds a phosphate group to a target protein, usually taking it from the energy molecule ATP. The added tag can switch the target protein on, switch it off, or change where it goes."),
        ("Kinase families", "Humans have hundreds of kinases, grouped into families by their shape and their targets. Members of one family often share a similar core, which is why designing a drug that hits just one can be hard."),
        ("Scaffold proteins", "Scaffold proteins hold several signalling proteins together in one place. This keeps the steps of a cascade close, so the signal passes quickly and does not leak to the wrong targets."),
        ("Signal amplification and feedback", "A cascade can amplify a small signal into a large response, because each step activates many copies of the next protein. Feedback loops return part of the response to the start, which can speed up or calm the process."),
        ("Inhibitor specificity", "Drugs that block kinases are only useful if they hit the right one. A highly specific inhibitor causes fewer unintended effects, while a broad one can disturb many pathways at once."),
    ],
    "test": [
        ("What does a kinase do?",
         [("a", "Breaks DNA"), ("b", "Adds phosphate groups to proteins"), ("c", "Makes lipids"), ("d", "Digests cells")], "b"),
        ("What do scaffold proteins do?",
         [("a", "Make bones"), ("b", "Store sugar"), ("c", "Stop all signals"), ("d", "Hold several signalling proteins together so the signal flows efficiently")], "d"),
        ("What is signal amplification?",
         [("a", "A small signal triggers a much larger response"), ("b", "Making sounds louder"), ("c", "Turning off a cell"), ("d", "Changing the cell's colour")], "a"),
        ("What is a feedback loop in a cascade?",
         [("a", "A broken wire"), ("b", "A signal that never changes"), ("c", "A signal that returns to adjust the process, so it can speed up or slow down"), ("d", "A kind of sleep")], "c"),
        ("Why does inhibitor specificity matter?",
         [("a", "It makes all kinases the same"), ("b", "It only matters in plants"), ("c", "It is irrelevant to drugs"), ("d", "A drug that hits only the intended kinase causes fewer unintended effects")], "d"),
    ],
}
