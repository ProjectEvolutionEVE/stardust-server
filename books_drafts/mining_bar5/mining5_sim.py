"""Conditional Simulation of Ore Bodies: building many equally likely versions of an ore body that all match the drill data."""
CODE = "mining5_sim"
BOOK = {
    "title": "Conditional Simulation of Ore Bodies",
    "subtitle": "Realisations, conditioning data, variograms and managing risk",
    "chapters": [
        ("Many possible deposits",
         "Drill holes sample only a tiny part of an ore body. Many different deposits could fit the same holes. Conditional simulation creates many of these possible deposits, each one honest to the data."),
        ("Realisations",
         "Each simulated version is called a realisation. All realisations match the measured data where it was measured. Between the holes they differ, and that spread shows how uncertain the true deposit is."),
        ("Conditioning data",
         "The simulation is conditioned on the drill data, so the samples are reproduced exactly at their locations. The data are the anchor that keeps every realisation close to what is known. More good data gives tighter results."),
        ("Variograms",
         "A variogram describes how similar two samples are as the distance between them grows. It shows how far grade continues before it changes. The variogram tells the simulation how smooth or patchy the ore should look."),
        ("Multiple outcomes and risk",
         "Running a whole set of realisations gives a range of outcomes for tonnes, grade and profit. Planners can look at the good and bad ends of that range. Risk is clearer when many outcomes are compared than when a single model is used."),
        ("Choosing a model",
         "No single realisation is the answer. A good team chooses the models that cover the range of geology, checks them against new data, and keeps the assumptions visible. The model is a tool for decisions, not a prophecy."),
    ],
    "test": [
        ("Why do many different deposits fit the same drill holes?",
         [("a", "Because drill holes sample only a tiny part of the ore body"), ("b", "Because drill holes are always perfect"), ("c", "Because ore does not exist"), ("d", "Because gold is the same everywhere")], "a"),
        ("What is a realisation?",
         [("a", "A final bill for drilling"), ("b", "A type of drill bit"), ("c", "One simulated version of the ore body that matches the data"), ("d", "A safety alarm")], "c"),
        ("What does a variogram describe?",
         [("a", "The colour of the ore"), ("b", "The price per tonne"), ("c", "The number of miners"), ("d", "How similar samples are as the distance between them grows")], "d"),
        ("Why is a set of realisations useful?",
         [("a", "It removes the need for any data"), ("b", "It gives a range of outcomes, so the risk can be seen"), ("c", "It always gives one correct answer"), ("d", "It makes drilling unnecessary")], "b"),
        ("What is a good way to use a simulation?",
         [("a", "Use it as a tool for decisions and keep its assumptions visible"), ("b", "Treat one realisation as the final truth"), ("c", "Ignore all uncertainty"), ("d", "Hide the assumptions from the team")], "a"),
    ],
}
