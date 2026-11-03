"""Population Ecology and Growth Models: exponential growth, logistic growth, carrying capacity, predator-prey cycles, sampling populations and life tables."""
CODE = "science4_bio_pop_ecology"
BOOK = {
    "title": "Population Ecology and Growth Models",
    "subtitle": "Growth curves, carrying capacity and cycles",
    "chapters": [
        ("Exponential growth", "When a population has plenty of food and space, it can grow exponentially. Each generation adds a fixed fraction to the population before it, so the numbers climb faster and faster."),
        ("Logistic growth", "Logistic growth slows as the population nears the limit set by its resources. The growth curve takes the shape of a stretched S."),
        ("Carrying capacity", "Carrying capacity is the largest population an environment can support over the long run. It depends on food, water, shelter and other limits."),
        ("Predator-prey cycles", "Predators and prey often rise and fall in cycles. When prey are plentiful, predators increase. Then the predators eat more prey, and the prey numbers drop."),
        ("Sampling populations", "Ecologists estimate population size by sampling part of an area and scaling up the result. A good sampling design avoids bias toward easy-to-find places."),
        ("Life tables", "A life table lists the survival and reproduction of individuals at each stage of life. It helps ecologists predict how a population will change over time."),
    ],
    "test": [
        ("What is exponential growth?",
         [("a", "Growth that never changes"), ("b", "Growth where each generation adds a fixed fraction of the population"), ("c", "A flat line on a graph"), ("d", "A population that shrinks")], "b"),
        ("What shape does logistic growth make on a graph?",
         [("a", "A straight line"), ("b", "A circle"), ("c", "An S shape"), ("d", "A square")], "c"),
        ("What is carrying capacity?",
         [("a", "The largest population an environment can support over the long run"), ("b", "The number of predators"), ("c", "A kind of boat"), ("d", "The size of one animal")], "a"),
        ("What happens in predator-prey cycles?",
         [("a", "Predators never change"), ("b", "Prey stay the same forever"), ("c", "Predator numbers rise when prey are plentiful, then fall as prey drop"), ("d", "Both disappear at once")], "c"),
        ("What is a life table?",
         [("a", "A kitchen tool"), ("b", "A record of survival and reproduction at each life stage"), ("c", "A map of rivers"), ("d", "A pile of dead leaves")], "b"),
    ],
}
