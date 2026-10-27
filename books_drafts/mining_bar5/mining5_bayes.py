"""Bayesian Targeting Under Uncertainty: how to combine prior knowledge with new evidence to rank drilling targets."""
CODE = "mining5_bayes"
BOOK = {
    "title": "Bayesian Targeting Under Uncertainty",
    "subtitle": "Updating what you think as new evidence arrives",
    "chapters": [
        ("Prior odds", "A prior is what you believe before new evidence arrives. Prior odds say how likely a target is based on what is already known. A good prior is written down so it can be checked later."),
        ("Evidence weights", "Each piece of evidence changes the odds by a certain weight. A strong magnetic anomaly might raise the odds a lot, while a weak one changes little. Weights should come from data, not hope."),
        ("Posterior maps", "The posterior is the updated belief after the evidence is combined with the prior. A posterior map shows the odds across an area. Teams use it to rank where to look next."),
        ("Updating with drilling", "Each drill hole gives new evidence that updates the posterior. A hole that finds ore raises the odds nearby, and a barren hole lowers them. The map gets sharper as holes are drilled."),
        ("Calibration", "Calibration checks whether the stated odds match what actually happens. A well calibrated model is right about as often as it claims. Poor calibration means the model needs changing."),
        ("Decisions", "Good decisions weigh the odds against the cost of drilling. A target with a high chance of success but a huge cost may not be worth it. The method helps teams make clear, reasoned choices."),
    ],
    "test": [
        ("What is a prior?",
         [("a", "A type of drill bit"), ("b", "A kind of rock"), ("c", "What you believe before new evidence arrives"), ("d", "A mountain top")], "c"),
        ("What does an evidence weight do?",
         [("a", "It weighs the rock in grams"), ("b", "It changes the odds by a certain amount"), ("c", "It cuts the drill"), ("d", "It paints the map")], "b"),
        ("What is a posterior?",
         [("a", "The updated belief after evidence is combined with the prior"), ("b", "A kind of back door"), ("c", "A sample of soil"), ("d", "A type of truck")], "a"),
        ("What happens to the odds after a barren drill hole?",
         [("a", "They go up by a lot every time"), ("b", "They never change"), ("c", "They turn into gold"), ("d", "They go down nearby")], "d"),
        ("What does calibration check?",
         [("a", "The shape of a spanner"), ("b", "The price of a flight"), ("c", "Whether stated odds match what actually happens"), ("d", "The number of birds on a fence")], "c"),
    ],
}
