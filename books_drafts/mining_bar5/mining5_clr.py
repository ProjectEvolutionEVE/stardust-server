"""Compositional Data and Log-Ratios: why percentages that add to a whole need special handling before any statistics are run."""
CODE = "mining5_clr"
BOOK = {
    "title": "Compositional Data and Log-Ratios",
    "subtitle": "Closed sums, centred log-ratios and the pitfalls of percentages",
    "chapters": [
        ("Parts of a whole",
         "Some data are parts of a whole, such as the percentages of minerals in a rock. They always add up to one hundred. This closed sum changes the way the numbers relate to one another."),
        ("Closed sums",
         "When one part goes up, another part must go down. This creates links between parts that do not reflect real geology. Standard statistics can then show correlations that are not there."),
        ("Centred log-ratio",
         "The centred log-ratio, often called clr, takes the logarithm of each part divided by the geometric mean of all parts. This removes the closed-sum effect so that ordinary methods can be used. Each value then compares a part with the whole."),
        ("Isometric transforms",
         "The isometric log-ratio, called ilr, creates a set of new coordinates that do not overlap. Each coordinate is independent, which suits tests that need independent values. The choice depends on the question being asked."),
        ("Statistical tests and pitfalls",
         "Zeros are a problem, because a logarithm of zero is undefined. Small replacement values or special methods are needed. Results must also be checked, since a transform can hide or create patterns if used carelessly."),
        ("Software",
         "Many statistical software packages include functions for these transforms. The steps are simple once the logic is clear. Always write down which transform was used, so others can repeat the work."),
    ],
    "test": [
        ("What is special about compositional data?",
         [("a", "They are always stored in colour"), ("b", "They are parts of a whole that add up to a fixed total"), ("c", "They always have a date"), ("d", "They can only be measured in water")], "b"),
        ("What is a closed sum problem?",
         [("a", "When one part rises, another must fall, creating false links"), ("b", "When a drill hole is sealed"), ("c", "When a file cannot be opened"), ("d", "When the sample is too cold")], "a"),
        ("What does the centred log-ratio do?",
         [("a", "It compares each part with the geometric mean of all parts"), ("b", "It adds all parts together"), ("c", "It deletes every zero"), ("d", "It sets all values to one")], "a"),
        ("What is a problem with zeros in log-ratio work?",
         [("a", "Zeros make the data too large"), ("b", "Zeros are always correct"), ("c", "A logarithm of zero is undefined, so special handling is needed"), ("d", "Zeros can only be printed in red")], "c"),
        ("Why should the transform used be written down?",
         [("a", "So the paper is heavier"), ("b", "So the colour matches the logo"), ("c", "So the data cannot be read"), ("d", "So the work can be repeated and checked by others")], "d"),
    ],
}
