"""Gravity and Magnetic Surveys: how small variations in the Earth’s pull and magnetism reveal what lies hidden underground."""
CODE = "science4_geo_potential_surveys"
BOOK = {
    "title": "Gravity and Magnetic Surveys",
    "subtitle": "Measuring hidden variations in gravity and magnetism",
    "chapters": [
        ("Gravity anomalies",
         "Gravity pulls a little harder over dense rock and a little less over light rock. A gravity anomaly is a small difference from the expected value. Surveys measure these differences to map what lies beneath the surface."),
        ("Magnetic anomalies",
         "Some rocks contain magnetic minerals that bend the Earth’s magnetic field locally. A magnetic anomaly is a small change from the regional field. Magnetic maps can reveal buried rock bodies, faults and old volcanic features."),
        ("Survey grids",
         "Surveys are planned on a grid of measuring points, spaced to suit the size of the target. Each point is measured carefully and its position recorded. A regular grid makes it easier to draw accurate maps from the data."),
        ("Corrections and noise",
         "Raw readings must be corrected for things that are not geology, such as elevation, the position of the Sun and the Moon, and the instrument itself. Noise from traffic, power lines and weather can hide real signals, so careful surveyors remove what they can."),
        ("Reading an anomaly map",
         "An anomaly map shows the corrected differences across the survey area. Contour lines join points of equal value. Sharp edges often mark a boundary between rock types, and round highs can hint at dense bodies."),
        ("From anomaly to drilling target",
         "An anomaly is only a clue. Before drilling, geologists test their interpretation with other data, such as rock samples and seismic lines. Drilling is expensive, so the strongest, best-checked anomaly is the one to test first."),
    ],
    "test": [
        ("What is a gravity anomaly?",
         [("a", "A change in the length of a day"), ("b", "A kind of earthquake"), ("c", "A small difference from the expected gravity value"), ("d", "A type of mineral")], "c"),
        ("What can a magnetic anomaly reveal?",
         [("a", "The price of metal"), ("b", "The speed of the wind"), ("c", "The number of stars"), ("d", "Buried rock bodies, faults and old volcanic features")], "d"),
        ("Why are surveys planned on a grid?",
         [("a", "To make the readings colder"), ("b", "To help make accurate maps from evenly spaced measurements"), ("c", "To keep the instruments off the ground"), ("d", "To stop noise from reaching the instrument")], "b"),
        ("Why must readings be corrected?",
         [("a", "Because gravity is never measured"), ("b", "To remove effects that are not geology, such as elevation"), ("c", "Because maps must be coloured"), ("d", "To make the anomaly bigger")], "b"),
        ("Why is an anomaly alone not enough to start drilling?",
         [("a", "Because drilling needs no target"), ("b", "Because anomalies never exist"), ("c", "Because it is only a clue and needs checking with other data"), ("d", "Because the ground is always solid")], "c"),
    ],
}
