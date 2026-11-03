"""Eclipses and Navigation: eclipse timing, star visibility, historical use, time checks, predictions and the shadow path on the ground."""
CODE = "navigation5_eclipse_navigation"
BOOK = {
    "title": "Eclipses and Navigation",
    "subtitle": "Timing, time checks and the Sun's shadow",
    "chapters": [
        ("Eclipse timing",
         "An eclipse happens when one body casts its shadow on another. Eclipses occur at predictable times, which makes them useful for checking clocks. Observers recorded their exact timing."),
        ("Star visibility",
         "During a total solar eclipse the sky darkens, and bright stars and planets can be seen. Observers can use this to check star positions. Eclipses are an unusual chance to see the sky in daylight."),
        ("Historical use",
         "Ancient astronomers used eclipses to fix dates and to compare places. Observers in different places timed the same eclipse, and the difference in times gave their longitudes. The method was used long before reliable clocks at sea."),
        ("Time checks",
         "An eclipse observation gives a time check at a known moment. If the timing matched the predicted hour, a clock could be corrected. Accurate time mattered greatly for finding longitude."),
        ("Predictions",
         "Astronomers predict eclipses by computing the orbits of the Earth and the Moon. Good predictions need good data and careful calculation. Predicted eclipses are published well in advance."),
        ("The Sun's shadow",
         "During a total solar eclipse the Moon's shadow falls on a narrow path across Earth. Outside that path the eclipse is only partial. The path of the shadow is worked out in advance."),
    ],
    "test": [
        ("When does an eclipse happen?",
         [("a", "When the wind changes"), ("b", "When the tides turn"), ("c", "When one body casts a shadow on another"), ("d", "When a comet passes")], "c"),
        ("What can observers see during a total solar eclipse?",
         [("a", "The ocean floor"), ("b", "Bright stars and planets"), ("c", "The far side of the Moon"), ("d", "Fish in the sea")], "b"),
        ("Why were eclipse timings useful to observers in different places?",
         [("a", "They gave longitude by comparing times"), ("b", "They gave the price of ships"), ("c", "They counted the crew"), ("d", "They made maps look nicer")], "a"),
        ("What does a time check from an eclipse do?",
         [("a", "It makes the wind stronger"), ("b", "It sinks ships"), ("c", "It hides the stars"), ("d", "It lets a clock be corrected at a known moment")], "d"),
        ("Why is the path of a total solar eclipse narrow on Earth?",
         [("a", "Because the Earth is small"), ("b", "Because the sea is narrow"), ("c", "Because the Moon's shadow falls on a narrow strip of ground"), ("d", "Because the Sun is small")], "c"),
    ],
}
