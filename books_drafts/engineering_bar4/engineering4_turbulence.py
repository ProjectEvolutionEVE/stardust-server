"""Turbulence and Its Modelling: chaotic eddies, averaged equations, and how far a model can be trusted."""
CODE = 'engineering4_turbulence'
BOOK = {
    "title": "Turbulence and Its Modelling",
    "subtitle": "Chaotic eddies, averaged equations, and how far a model can be trusted",
    "chapters": [
        ("Eddies",
         "Turbulent flow is full of swirling eddies of many sizes. They mix heat, momentum and material far faster than smooth flow does."),
        ("Reynolds averaging",
         "Engineers split the flow into an average part and a fluctuating part. Averaging gives equations that can be solved in practice, along with extra terms that need modelling."),
        ("Turbulence models",
         "A turbulence model supplies the terms that averaging leaves out. Different models suit different flows, and none is perfect for every case."),
        ("The energy cascade",
         "Energy enters the flow at the large eddies and passes down to smaller and smaller ones, where it finally turns into heat. This is the energy cascade."),
        ("When a model can be trusted",
         "A model is trusted only where it has been checked against measurements of similar flows. Using it far outside that range is risky."),
        ("Why it matters",
         "Turbulence sets the drag, mixing and heat transfer in most real flows. Good models save testing time and money."),
    ],
    "test": [
        ("What is an eddy?",
         [("a", "A stone"), ("b", "A painted line"), ("c", "A swirling motion in turbulent flow"), ("d", "A ship's sail")], "c"),
        ("What does Reynolds averaging split the flow into?",
         [("a", "An average part and a fluctuating part"), ("b", "Red and blue parts"), ("c", "Hot and cold parts"), ("d", "Fast and slow lanes")], "a"),
        ("What does a turbulence model do?",
         [("a", "Paints the flow"), ("b", "Stops the flow"), ("c", "Cuts the eddies out"), ("d", "Supplies the terms that averaging leaves out")], "d"),
        ("What is the energy cascade?",
         [("a", "Energy passing from large eddies down to small ones, where it turns into heat"), ("b", "A waterfall"), ("c", "A shower"), ("d", "A paint job")], "a"),
        ("When can a turbulence model be trusted?",
         [("a", "Everywhere"), ("b", "Only in the paint shop"), ("c", "Where it has been checked against measurements for similar flows"), ("d", "When the sun is out")], "c"),
    ],
}
