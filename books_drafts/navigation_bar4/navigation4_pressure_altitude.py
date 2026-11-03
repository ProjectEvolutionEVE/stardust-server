"""Pressure altitude and altimeter settings: the standard atmosphere, QNH, QFE, transition altitude, errors and safety."""
CODE = "navigation4_pressure_altitude"
BOOK = {
    "title": "Pressure Altitude and Altimeter Settings",
    "subtitle": "Which number the altimeter should show",
    "chapters": [
        ("The standard atmosphere", "The standard atmosphere is an agreed model of pressure, temperature and height. Pressure falls with height in a known way. Altimeters are built around this model."),
        ("QNH", "QNH is the altimeter setting that makes the altimeter read height above mean sea level at a place. Pilots set it on the ground to match local conditions. It is used at low levels."),
        ("QFE", "QFE is the altimeter setting that makes the altimeter read zero on the ground at an airfield. It shows height above the airfield. It is used less often than QNH."),
        ("Transition altitude", "The transition altitude is the height above which all aircraft set the standard pressure. This keeps aircraft working from the same reference. Pilots change their setting at this level."),
        ("Errors", "Altimeter readings are affected by air that differs from the standard atmosphere. Weather changes the real air away from the standard. Pilots must allow for these differences."),
        ("Safety", "Wrong settings can cause an aircraft to fly too low or to misjudge its height. Clear procedures and checks reduce that risk. Crews confirm settings aloud."),
    ],
    "test": [
        ("What is the standard atmosphere?", [("a", "A weather forecast for a single day"), ("b", "An agreed model of pressure, temperature and height"), ("c", "A list of airport names"), ("d", "A type of cloud")], "b"),
        ("What does QNH give on the altimeter?", [("a", "Height above a hillside"), ("b", "The speed of the wind"), ("c", "Height above mean sea level at the place"), ("d", "The number of passengers")], "c"),
        ("What does QFE make the altimeter read on the ground at an airfield?", [("a", "The price of landing"), ("b", "A random number"), ("c", "The number of runways"), ("d", "Zero")], "d"),
        ("What is the transition altitude?", [("a", "The highest point on a runway"), ("b", "The height above which all aircraft set standard pressure"), ("c", "The height where the wind stops"), ("d", "The altitude of a hot-air balloon")], "b"),
        ("Why must pilots allow for errors in altimeter readings?", [("a", "Air that is not standard changes what the altimeter shows"), ("b", "Altimeters are always perfectly accurate"), ("c", "Altimeters work only at night"), ("d", "Altimeters work only over water")], "a"),
    ],
}
