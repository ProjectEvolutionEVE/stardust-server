"""Fusing Geochemical and Geophysical Data: combining different kinds of measurements into one honest picture of the ground."""
CODE = "mining5_fusion"
BOOK = {
    "title": "Fusing Geochemical and Geophysical Data",
    "subtitle": "Joint inversion, multivariate maps and avoiding false patterns",
    "chapters": [
        ("Many measurements, one ground",
         "Geochemistry measures what the rock contains, and geophysics measures how it responds to fields and waves. Each one sees part of the story. Fusing them gives a fuller picture than either alone."),
        ("Joint inversion",
         "A joint inversion fits one model to several data sets at once. It forces the model to explain the magnetic, gravity and electrical data together. A structure seen in one data set must also be consistent with the others."),
        ("Cross-correlation",
         "Cross-correlation checks whether two maps change together. A strong match suggests a shared cause, such as a rock contact. A weak match is also information, because it tells you the two maps show different things."),
        ("Multivariate maps",
         "Several maps can be combined into one using methods such as principal component analysis or clustering. Each group of similar places gets one colour. Such maps make patterns easy to see, but they hide which input did what."),
        ("Feature selection and overfitting",
         "Adding more variables does not always help. Too many inputs let a model fit the random noise in the data, which is called overfitting. A model that fits the noise will fail on new ground. Choosing a few meaningful inputs keeps the model honest."),
        ("Presentation",
         "A good presentation shows the uncertainty as well as the best map. It states which data went in and which were left out. Readers can then judge how far the picture can be trusted."),
    ],
    "test": [
        ("What does joint inversion do?",
         [("a", "It paints maps in one colour"), ("b", "It removes all the data"), ("c", "It counts drill holes"), ("d", "It fits one model to several data sets at once")], "d"),
        ("What does a strong cross-correlation between two maps suggest?",
         [("a", "The maps are printed on the same paper"), ("b", "A shared cause, such as a rock contact"), ("c", "That one of the maps is wrong"), ("d", "That the survey is finished")], "b"),
        ("What is overfitting?",
         [("a", "A model that fits the random noise and fails on new ground"), ("b", "A model that is too simple to fit anything"), ("c", "A map that is too small to read"), ("d", "A drill that goes too deep")], "a"),
        ("What does a multivariate map do?",
         [("a", "It combines several inputs into one map with groups of similar places"), ("b", "It measures the weight of the ore"), ("c", "It replaces the drill"), ("d", "It records the weather")], "a"),
        ("What should a good presentation of fused data show?",
         [("a", "Only the single best map, with nothing else"), ("b", "Only the colours used"), ("c", "The uncertainty, and which data went in or were left out"), ("d", "Only the name of the software")], "c"),
    ],
}
