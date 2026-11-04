"""Ecosystem Modelling and Energy Budgets: simple models of how energy and matter move through an ecosystem."""
CODE = "science5_bio_ecosys_models"
BOOK = {
    "title": "Ecosystem Modelling and Energy Budgets",
    "subtitle": "Simple pictures of how energy flows through living systems",
    "chapters": [
        ("Models as simple pictures", "A model is a simplified version of a system. It leaves out much detail so the main pattern is easier to see. Good models are useful because they can be tested."),
        ("Compartments", "A compartment model divides an ecosystem into pools, such as plants, herbivores, predators and soil. Each pool stores energy or matter. Arrows show how material moves from one pool to another."),
        ("Energy flux", "Energy flows through an ecosystem in one direction, from sunlight to plants and then to animals. Only part of the energy passes up each step. A common rule of thumb is that roughly ten percent moves to the next level."),
        ("Parameters", "Parameters are the numbers that set how fast each flow happens. A model is only as good as the values chosen for its parameters. Scientists measure these values in the field or the lab."),
        ("Sensitivity analysis", "A sensitivity analysis tests how much the results change when one number changes. It shows which parts of a model matter most. It also shows where more measurement is needed."),
        ("Evaluating a model", "A model should be checked against real data. If it cannot match what is observed, it needs to be changed. Tipping points, where a small change flips the system, are one of the hardest things to predict."),
    ],
    "test": [
        ("What is a model in ecology?",
         [("a", "A toy car"), ("b", "A simplified picture of a system"), ("c", "A rock sample"), ("d", "A bird's nest")], "b"),
        ("In a compartment model, what are the compartments?",
         [("a", "Rooms in a laboratory"), ("b", "Shipping crates"), ("c", "Folders on a hard drive"), ("d", "Pools such as plants, herbivores and soil that store energy or matter")], "d"),
        ("Roughly how much energy passes from one food level to the next?",
         [("a", "About 100 percent"), ("b", "About 50 percent"), ("c", "About 10 percent"), ("d", "About 90 percent")], "c"),
        ("What does a sensitivity analysis test?",
         [("a", "How much the results change when one number changes"), ("b", "The colour of the model"), ("c", "The price of food"), ("d", "The speed of a computer")], "a"),
        ("Why should a model be checked against real data?",
         [("a", "So it can be painted"), ("b", "So it can be sold"), ("c", "So it becomes longer"), ("d", "So we know whether it predicts real systems well")], "d"),
    ],
}
