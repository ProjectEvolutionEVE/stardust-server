"""Lunar Distances: finding Greenwich time at sea from the Moon's angle, before accurate clocks."""
CODE = "navigation4_lunar_distance"
BOOK = {
    "title": "Lunar Distances",
    "subtitle": "Finding time at sea before the chronometer",
    "chapters": [
        ("The method before the chronometer", "Before accurate clocks were carried at sea, navigators had a problem. They could not easily know the time at Greenwich. The lunar distance method offered a way to find it using the Moon."),
        ("The Moon's angle from stars", "The Moon moves steadily against the background of the stars. Navigators measured the angle between the Moon and a star or the Sun. That angle changes in a known way through the day."),
        ("Clearing the distance", "Clearing the distance means correcting the measured angle for altitude, refraction and other effects. The corrected distance is then compared with predicted values in the almanac. The match gives the time at Greenwich."),
        ("Parallax corrections", "The Moon is close enough that its apparent position depends on where you observe it from. This is parallax, and the correction is worked out from the observed altitudes. Applying it is a necessary step."),
        ("Predicted distance tables", "Almanacs printed predicted lunar distances for each hour of Greenwich time. Navigators interpolated between them. A careful interpolation gives a better time."),
        ("Accuracy", "The method takes time and care, and small errors in measurement change the result. Once reliable chronometers became widely available, the lunar method fell out of common use. It remains a fine example of careful navigation."),
    ],
    "test": [
        ("What problem did lunar distances help solve?",
         [("a", "Finding the speed of the ship"), ("b", "Measuring the depth of the sea"), ("c", "Telling the colour of the sky"), ("d", "Finding the time at Greenwich without a clock")], "d"),
        ("What is measured in the lunar distance method?",
         [("a", "The Moon's weight"), ("b", "The angle between the Moon and a star or the Sun"), ("c", "The temperature of the sea"), ("d", "The distance to the Earth's core")], "b"),
        ("What is meant by clearing the distance?",
         [("a", "Correcting the measured angle before comparing it with tables"), ("b", "Removing clouds from the sky"), ("c", "Cleaning the sextant mirrors"), ("d", "Sailing in a straight line")], "a"),
        ("Why must the Moon's distance get a parallax correction?",
         [("a", "Because the Moon is hot"), ("b", "Because the Moon gives no light"), ("c", "Because the Moon is close enough that its apparent position depends on the observer"), ("d", "Because the Moon moves only at night")], "c"),
        ("Where did navigators find predicted distances?",
         [("a", "In the almanac"), ("b", "In the ship's log only"), ("c", "In the cook's notes"), ("d", "In the rigging")], "a"),
    ],
}
