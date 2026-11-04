"""Chromatography: Separating Mixtures: how chromatography separates the parts of a mixture, and how analysts check that a method works."""
CODE = "science4_chem_chromatography"
BOOK = {
    "title": "Chromatography: Separating Mixtures",
    "subtitle": "Separating a mixture by how each part moves through a column",
    "chapters": [
        ("Partition and retention",
         "In chromatography, a mixture is carried by a moving phase past a stationary phase. Each component partitions between the two phases, and components that stick more strongly take longer to pass through. The time a component takes to exit is its retention time."),
        ("Gas and liquid chromatography",
         "In gas chromatography, the moving phase is an inert gas and the sample must be able to vaporise. In liquid chromatography, a liquid carries the sample through a column. Each method suits different kinds of compounds."),
        ("Column choice",
         "The column holds the stationary phase and decides how well the components separate. Length, packing and chemistry all matter. Choosing a column that suits the sample is one of the most important decisions in the method."),
        ("Detectors",
         "A detector senses the components as they leave the column. Common types respond to light absorption, to ionisation, or to heat conductivity. The detector choice affects how sensitive and specific the analysis is."),
        ("Calibration curves",
         "A calibration curve plots the detector response against known amounts of a standard. An unknown sample’s response is then read off the curve to give its amount. A straight-line calibration is easiest to trust."),
        ("Method validation",
         "A method is validated by checking its accuracy, precision, range and limits of detection. These checks show that the method gives reliable results for its intended use. Validation is the proof that a method can be trusted."),
    ],
    "test": [
        ("What decides how long a component takes to leave a column?",
         [("a", "The colour of the column"), ("b", "The weight of the flask"), ("c", "The age of the lab"), ("d", "Its retention, from how strongly it partitions into the stationary phase")], "d"),
        ("In gas chromatography, what carries the sample?",
         [("a", "Sand"), ("b", "Liquid metal"), ("c", "An inert gas"), ("d", "Ice")], "c"),
        ("What is a calibration curve used for?",
         [("a", "To measure the weight of the column"), ("b", "To heat the sample"), ("c", "To paint the detector"), ("d", "To read the amount of an unknown from its detector response")], "d"),
        ("What does a detector do?",
         [("a", "It senses the components as they leave the column"), ("b", "It makes the column longer"), ("c", "It cools the room"), ("d", "It stores the sample")], "a"),
        ("What does method validation check?",
         [("a", "Accuracy, precision, range and limits of detection"), ("b", "The colour of the lab coat"), ("c", "The number of chairs"), ("d", "The temperature of the sun")], "a"),
    ],
}
