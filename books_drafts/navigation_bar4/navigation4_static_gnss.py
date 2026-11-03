"""Static GNSS Baselines: long sessions for precise distances between receivers."""
CODE = "navigation4_static_gnss"
BOOK = {
    "title": "Static GNSS Baselines",
    "subtitle": "Long sessions for precise distances between receivers",
    "chapters": [
        ("Long sessions", "A static GNSS survey keeps receivers still for a long time. The longer the session, the more data is collected. Long sessions help reduce many small errors."),
        ("Baselines between receivers", "A baseline is the vector between two receivers. It is measured with great precision by combining their data. Baselines form the links of a survey network."),
        ("The ionosphere over long lines", "The ionosphere delays signals differently at different places. Two receivers far apart may see different delays. Dual-frequency receivers help remove most of this effect."),
        ("Precise orbits", "Precise satellite orbits improve the result. Orbits are computed from networks of tracking stations. Using precise orbits reduces errors in the baseline."),
        ("The network", "Many baselines together form a network. Each baseline is checked against the others. Loops that close well show good data."),
        ("Quality checks", "Check the baseline's quality with statistics and loop closures. Repeat sessions to confirm results. A record of each check is kept with the survey."),
    ],
    "test": [
        ("What is a baseline in GNSS surveying?",
         [("a", "A painted line on a road"), ("b", "The vector between two receivers"), ("c", "A kind of aircraft"), ("d", "A measuring tape")], "b"),
        ("Why are long sessions used?",
         [("a", "To collect more data and reduce small errors"), ("b", "To make the receiver hot"), ("c", "To wait for lunch"), ("d", "To print maps")], "a"),
        ("What affects long baselines in particular?",
         [("a", "The colour of the sky"), ("b", "Tides"), ("c", "Local bird songs"), ("d", "The ionosphere delays the signals differently")], "d"),
        ("What helps remove most of the ionospheric delay?",
         [("a", "Single-frequency paper"), ("b", "A bigger tripod"), ("c", "Dual-frequency receivers"), ("d", "Paint")], "c"),
        ("What do closed loops of baselines show?",
         [("a", "Whether the data is consistent"), ("b", "The price of the receivers"), ("c", "The name of the surveyor"), ("d", "The weather forecast")], "a"),
    ],
}
