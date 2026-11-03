"""Gravity Anomalies and Corrections: reading the pull of the ground beneath us."""
CODE = "navigation4_gravity_anomalies"
BOOK = {
    "title": "Gravity Anomalies and Corrections",
    "subtitle": "Reading the pull of the ground beneath us",
    "chapters": [
        ("Gravity on a model Earth", "The reference ellipsoid has a standard gravity value that changes with latitude. Measured gravity is compared with that expected value. The difference is called a gravity anomaly."),
        ("Free-air and Bouguer corrections", "The free-air correction allows for height above the reference surface. The Bouguer correction allows for the rock between the point and that surface. Both help reveal the true mass beneath the ground."),
        ("Gravity surveys", "A gravity survey measures gravity at many points. The results show where rock is denser or lighter than usual. Geologists use these maps to find hidden structures."),
        ("Use in heights", "Gravity matters for heights. Water flows downhill because of gravity, so levels depend on it. Heights referred to a surface of equal gravity are more meaningful."),
        ("Instruments", "Gravimeters measure gravity very precisely. Some are used on the ground, and some on ships and aircraft. Each instrument must be calibrated carefully."),
        ("Errors", "Errors come from instrument drift, poor heights and nearby objects. Repeating measurements and checking the drift keeps the errors small. Good records make a survey worth trusting."),
    ],
    "test": [
        ("What is a gravity anomaly?",
         [("a", "A ghost in the ground"), ("b", "The difference between measured and expected gravity"), ("c", "A broken gravimeter"), ("d", "A type of tide")], "b"),
        ("What does the free-air correction allow for?",
         [("a", "Wind"), ("b", "The colour of rock"), ("c", "The time of day"), ("d", "Height above the reference surface")], "d"),
        ("What do gravity surveys reveal?",
         [("a", "Where rock is denser or lighter than usual"), ("b", "The names of the rivers"), ("c", "The price of land"), ("d", "The best time to sail")], "a"),
        ("Why does gravity matter for heights?",
         [("a", "Gravity makes trees taller"), ("b", "Gravity changes the colour of the sky"), ("c", "Gravity is the same everywhere"), ("d", "Water and levels depend on gravity")], "d"),
        ("What is a gravimeter?",
         [("a", "A type of clock"), ("b", "A kind of boat"), ("c", "An instrument that measures gravity"), ("d", "A map projection")], "c"),
    ],
}
