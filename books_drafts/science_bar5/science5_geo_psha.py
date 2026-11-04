"""Probabilistic Seismic Hazard Analysis. How scientists estimate the chance of strong shaking at a site over time."""
CODE = "science5_geo_psha"
BOOK = {
    "title": "Probabilistic Seismic Hazard Analysis",
    "subtitle": "Estimating how often strong shaking is likely at a site",
    "chapters": [
        ("Asking how likely shaking is",
         "Probabilistic seismic hazard analysis asks how likely it is that the ground at a site will shake above a given level within a set time. It combines what we know about faults, earthquakes and ground motion into one answer."),
        ("Source models",
         "A source model maps the faults and zones that can produce earthquakes near the site. Each source has a size range and a location, and the model shows where future earthquakes are most likely to start."),
        ("Recurrence rates",
         "Recurrence rates describe how often earthquakes of a given size happen. The Gutenberg-Richter relation links the number of small and large earthquakes, so that a rate for small events can be extended to large ones."),
        ("Ground motion prediction",
         "Ground motion prediction equations estimate how strong shaking will be at a site, given an earthquake's size and distance and the local soil. These equations carry large scatter, and the models must include that scatter."),
        ("Hazard curves",
         "A hazard curve plots the annual chance of exceeding each shaking level at a site. Reading the curve at a chosen probability gives the design level used for buildings and dams."),
        ("Logic trees and communication",
         "Logic trees show the range of models and parameters used, each branch with a weight. Good communication of hazard explains what the numbers mean, and it does not turn a probability into a promise."),
    ],
    "test": [
        ("What does probabilistic seismic hazard analysis estimate?",
         [("a", "The colour of the sky above a city"), ("b", "The chance of strong shaking at a site within a set time"), ("c", "The exact day of the next earthquake"), ("d", "The number of trees in a park")], "b"),
        ("What does a source model show?",
         [("a", "The faults and zones that can produce earthquakes near a site"), ("b", "The flow of rivers"), ("c", "The path of storms"), ("d", "The growth of forests")], "a"),
        ("What does the Gutenberg-Richter relation link?",
         [("a", "The number of small and large earthquakes"), ("b", "The height of mountains and rainfall"), ("c", "Ocean salt and cloud cover"), ("d", "Animal numbers and seasons")], "a"),
        ("What does a hazard curve plot?",
         [("a", "The colour of soil layers"), ("b", "The annual chance of exceeding each shaking level"), ("c", "The speed of ships"), ("d", "The temperature of the sea")], "b"),
        ("What is the purpose of a logic tree?",
         [("a", "To grow plants in pots"), ("b", "To record birth dates"), ("c", "To name new stars"), ("d", "To show the range of models and parameters, each with a weight")], "d"),
    ],
}
