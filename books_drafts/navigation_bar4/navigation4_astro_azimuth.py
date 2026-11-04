"""Astronomical Azimuth for Surveys: finding true north from the sky."""
CODE = "navigation4_astro_azimuth"
BOOK = {
    "title": "Astronomical Azimuth for Surveys",
    "subtitle": "Finding true north from the sky",
    "chapters": [
        ("A true bearing from a star", "An astronomical azimuth gives a true bearing from the sky. Surveyors use it to fix the direction of a line. Stars and the Sun are the usual targets."),
        ("Polaris and the Sun", "Polaris lies close to the celestial pole, so it shows north well. The Sun is also used, especially where Polaris is hard to see. Both need careful timing."),
        ("Timing", "Accurate timing is essential, because the sky moves steadily. A small time error gives a small angular error. Surveyors use precise clocks or time signals."),
        ("The reduction", "The observed bearing is reduced to a true azimuth using tables or formulas. The reduction allows for latitude, declination and the hour angle. Careful work gives a reliable azimuth."),
        ("Tying a network to true north", "The true azimuth is used to tie a survey network to true north. Other bearings are then linked to it. This fixes the orientation of the whole network."),
        ("The error budget", "Every step has an error, and the total is the error budget. Timing, pointing and the reduction all add to it. Surveyors list each error to judge the result."),
    ],
    "test": [
        ("What does an astronomical azimuth give?",
         [("a", "A ship's weight"), ("b", "A paint colour"), ("c", "The depth of a river"), ("d", "A true bearing from the sky")], "d"),
        ("Why is Polaris useful for finding north?",
         [("a", "It is the brightest star"), ("b", "It lies close to the celestial pole"), ("c", "It moves fast"), ("d", "It is a planet")], "b"),
        ("Why does a small time error matter?",
         [("a", "Clocks are pretty"), ("b", "It helps the Sun rise"), ("c", "A small time error causes an angular error"), ("d", "It stops the wind")], "c"),
        ("What does the reduction allow for?",
         [("a", "Latitude, declination and the hour angle"), ("b", "The colour of the sky"), ("c", "The speed of a car"), ("d", "The thickness of the paper")], "a"),
        ("What is the error budget?",
         [("a", "A bank account"), ("b", "A map colour"), ("c", "A survey tool"), ("d", "The list of all the errors that add up")], "d"),
    ],
}
