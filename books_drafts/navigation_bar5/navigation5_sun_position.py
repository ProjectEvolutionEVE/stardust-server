"""Computing the Sun's Position: the orbit, the equation of time, declination, algorithms, accuracy and printed tables."""
CODE = "navigation5_sun_position"
BOOK = {
    "title": "Computing the Sun's Position",
    "subtitle": "Orbit, declination, the equation of time and the tables",
    "chapters": [
        ("The orbit",
         "Earth travels around the Sun in an orbit that is close to a circle, but slightly elliptical. The Sun's apparent path across the sky follows the Earth's orbit as seen from here. Computing the Sun's position starts with the orbit."),
        ("The equation of time",
         "The clock time of solar noon varies over the year, by up to about sixteen minutes. This difference is the equation of time. Sundials and navigators both need it."),
        ("Declination",
         "Declination is the Sun's angle north or south of the celestial equator. It changes through the year, reaching about 23.4 degrees at the midsummer and midwinter points. Declination sets how high the Sun climbs at noon."),
        ("Algorithms",
         "Astronomers compute the Sun's position with formulas that depend on the date and time. Simple methods are accurate to a fraction of a degree. More careful ones are used when precision matters."),
        ("Accuracy",
         "The accuracy of a computed position depends on the method and on the data. Errors are checked by comparing results with measured positions. Good navigators know how accurate their figures are."),
        ("Tables",
         "Printed tables of the Sun's position were used for centuries before calculators existed. Almanacs listed the declination and the equation of time for each day. Tables are still a quick check on a computed value."),
    ],
    "test": [
        ("What shape is Earth's orbit around the Sun, close to?",
         [("a", "A near circle"), ("b", "A square"), ("c", "A cube"), ("d", "A straight line")], "a"),
        ("What is the equation of time?",
         [("a", "The price of sundials"), ("b", "The time light takes to reach Earth"), ("c", "The number of hours of daylight"), ("d", "How much solar noon varies from clock noon over the year")], "d"),
        ("What is declination?",
         [("a", "The Sun's speed"), ("b", "The Sun's angle north or south of the celestial equator"), ("c", "The Sun's distance from Earth"), ("d", "The colour of the Sun")], "b"),
        ("How is the Sun's position computed?",
         [("a", "By counting ships"), ("b", "By guessing"), ("c", "With formulas that depend on the date and time"), ("d", "By reading the wind")], "c"),
        ("What checks a computed figure?",
         [("a", "Comparing it with measured positions"), ("b", "Burning it"), ("c", "Ignoring it"), ("d", "Adding more digits")], "a"),
    ],
}
