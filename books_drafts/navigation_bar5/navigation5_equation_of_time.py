"""The Equation of Time: the solar-day variation, eccentricity, obliquity, sundials, navigation and printed tables."""
CODE = "navigation5_equation_of_time"
BOOK = {
    "title": "The Equation of Time",
    "subtitle": "Why the solar day is not always the same length",
    "chapters": [
        ("Solar-day variation",
         "The solar day is the time from one solar noon to the next. It is not constant through the year. The equation of time measures how much it varies."),
        ("Eccentricity",
         "Earth's orbit is slightly elliptical, so Earth moves faster when it is nearer the Sun. This changes the apparent length of the solar day across the year. Eccentricity is one of the two main causes."),
        ("Obliquity",
         "The tilt of Earth's axis, about 23.4 degrees, is the other main cause. The tilt makes the Sun's apparent motion along the equator uneven. Together with eccentricity, the tilt produces the equation of time."),
        ("Sundials",
         "A sundial shows apparent solar time, which runs ahead of or behind clock time. Makers used tables of the equation of time to correct their readings. Some dials carry a special scale for this purpose."),
        ("Navigation",
         "Navigators use the equation of time to convert observed solar time into mean time. Accurate time is needed to find longitude. An error in the correction causes an error in position."),
        ("Tables",
         "Almanacs print the equation of time for every day of the year. Users look up the value and add or subtract it. Tables make the correction simple and quick."),
    ],
    "test": [
        ("What is a solar day?",
         [("a", "The time between two stars rising"), ("b", "The time from one solar noon to the next"), ("c", "The length of a year"), ("d", "The time the Moon takes to orbit")], "b"),
        ("What causes the variation from eccentricity?",
         [("a", "The colour of Earth"), ("b", "The shape of the Moon"), ("c", "Rainfall"), ("d", "Earth's orbit being slightly elliptical")], "d"),
        ("About what size is Earth's axial tilt?",
         [("a", "About 23.4 degrees"), ("b", "About 90 degrees"), ("c", "About 45 days"), ("d", "About 3 degrees")], "a"),
        ("What do sundials need the equation of time for?",
         [("a", "To show the year"), ("b", "To show the stars"), ("c", "To correct apparent solar time to clock time"), ("d", "To show the rain")], "c"),
        ("What do almanacs print for every day of the year?",
         [("a", "Recipes"), ("b", "The equation of time"), ("c", "Ship names"), ("d", "The price of ships")], "b"),
    ],
}
