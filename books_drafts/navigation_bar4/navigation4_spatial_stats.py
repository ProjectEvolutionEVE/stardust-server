"""Spatial Statistics and Hot Spots: point patterns, clustering, hot-spot tests, the role of scale, and honest reporting."""
CODE = "navigation4_spatial_stats"
BOOK = {
    "title": "Spatial Statistics and Hot Spots",
    "subtitle": "Finding where things cluster, and not fooling yourself about it",
    "chapters": [
        ("Point patterns", "A point pattern shows where events happen on a map. Points may be spread evenly, pile up in clusters, or fall at random. The first step is to look at the pattern before you test it."),
        ("Clustering", "Clustering means events sit closer together than chance would suggest. A cluster can be a real problem or a harmless quirk of the data. Only a test can tell the two apart."),
        ("Hot-spot tests", "A hot-spot test compares a place with its neighbours. It asks whether high values are gathered there more than chance allows. Several standard tests do this, and each suits different data."),
        ("Scale", "Results depend on the size of the areas used. Drawing the areas differently can change where the hot spots appear. Always say which scale you used."),
        ("False alarms", "Testing many places at once makes false alarms more likely. Some hot spots will appear by chance. Correct for multiple tests, and check the result with fresh data."),
        ("Reporting", "Report the method, the scale and the uncertainty. Show the map and the numbers together. A clear report lets others check your work and decide what to do."),
    ],
    "test": [
        ("What does a point pattern show?", [("a", "The taste of the water"), ("b", "The date of each song"), ("c", "Where events happen on a map"), ("d", "The colour of the sky")], "c"),
        ("What is clustering?", [("a", "Events sitting closer together than chance suggests"), ("b", "Events spread out exactly evenly"), ("c", "A type of map projection"), ("d", "A way of printing maps")], "a"),
        ("What does a hot-spot test ask?", [("a", "How many colours a map has"), ("b", "The name of the mapmaker"), ("c", "How heavy a file is"), ("d", "Whether high values gather in one place more than chance allows")], "d"),
        ("Why do results depend on scale?", [("a", "Scale has no effect"), ("b", "The size of the areas used can change where hot spots appear"), ("c", "Only paper maps have scale"), ("d", "Scale changes the weather")], "b"),
        ("What makes false alarms more likely?", [("a", "Testing many places at once without correction"), ("b", "Using fresh data"), ("c", "Reporting the method"), ("d", "Showing the uncertainty")], "a"),
    ],
}
