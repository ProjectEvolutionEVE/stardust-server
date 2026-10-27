"""Geometallurgy: Predicting Behaviour in Advance: linking ore variation to how it will process, so plants can be planned before mining starts."""
CODE = "mining5_geomet"
BOOK = {
    "title": "Geometallurgy: Predicting Behaviour in Advance",
    "subtitle": "Knowing how ore will process before it is mined",
    "chapters": [
        ("Ore variability", "Ore in one deposit is never perfectly uniform. Its hardness, mineral mix and grain size can change from place to place. These changes affect how the ore processes."),
        ("Comminution tests", "Comminution tests measure how easily ore is crushed and ground. Teams use the results to size mills and predict energy use. Samples from many parts of the deposit are tested."),
        ("Recovery maps", "A recovery map shows how much metal a plant is likely to recover from each part of the deposit. It is built from test results and mineral data. The map helps planners avoid poor-recovery zones."),
        ("Block models", "A block model divides the deposit into blocks, each with estimated grades and properties. Geometallurgical properties are added to the blocks. The model guides the mine plan."),
        ("Plant planning", "Plant planning uses the block model to match ore types to the right processing steps. It helps set capacity, reagent use and waste handling. A plan built this way avoids surprises after the plant starts."),
        ("Feedback", "Operating data from the plant is compared with the predictions. Differences are used to improve the models. Feedback keeps the predictions honest as the mine goes on."),
    ],
    "test": [
        ("What does a comminution test measure?",
         [("a", "The colour of the ore"), ("b", "How easily ore is crushed and ground"), ("c", "The weight of a truck"), ("d", "The sound of a bell")], "b"),
        ("What does a recovery map show?",
         [("a", "How much metal a plant is likely to recover from each part of the deposit"), ("b", "A route for buses"), ("c", "The price of food"), ("d", "The shape of the sky")], "a"),
        ("What is a block model?",
         [("a", "A toy made of wood"), ("b", "A type of wall"), ("c", "A car engine"), ("d", "A model dividing the deposit into blocks with estimated properties")], "d"),
        ("Why are samples taken from many parts of a deposit?",
         [("a", "Because all ore is the same"), ("b", "Because samples are free to lose"), ("c", "Because ore varies from place to place"), ("d", "Because the deposit must be counted by hand")], "c"),
        ("What does feedback from the plant do?",
         [("a", "It stops all mining"), ("b", "It improves the models by comparing predictions with real results"), ("c", "It erases the block model"), ("d", "It changes the weather")], "b"),
    ],
}
