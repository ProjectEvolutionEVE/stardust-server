"""The wind triangle: airspeed, ground speed, drift, heading correction, the vector diagram and the flight computer."""
CODE = "navigation4_wind_triangle"
BOOK = {
    "title": "The Wind Triangle",
    "subtitle": "Airspeed, wind and the track over the ground",
    "chapters": [
        ("Air moves too", "A craft flies through air that may itself be moving. The wind changes the path over the ground. Pilots must allow for it to arrive where they intend."),
        ("Airspeed and ground speed", "Airspeed is the speed relative to the air. Ground speed is the speed over the ground, and it includes the effect of the wind. The difference between them is the wind's effect."),
        ("Drift", "Drift is the sideways push of the wind that moves the craft off course. The heading must be changed to correct it. The amount depends on the wind's strength and angle."),
        ("Heading correction", "A heading correction turns the craft into the wind so that it tracks the desired course. The correction is worked out before the flight. It can be refined on the way."),
        ("The vector diagram", "The wind triangle is a diagram of three vectors: airspeed, wind and ground track. Solving it gives the heading and ground speed. It is a clear way to see the wind's effect."),
        ("The flight computer", "A flight computer is a hand tool that solves the wind triangle quickly. Modern navigation computers do the same automatically. Learning the triangle still helps pilots understand the result."),
    ],
    "test": [
        ("What is airspeed?", [("a", "The speed relative to the air"), ("b", "The speed over the ground only"), ("c", "The speed of the wind alone"), ("d", "The speed of sound in the cabin")], "a"),
        ("What is drift?", [("a", "The number of wings"), ("b", "A kind of cloud"), ("c", "The sound of the engines"), ("d", "A sideways push by the wind that moves the craft off course")], "d"),
        ("What does a heading correction do?", [("a", "Changes the colour of the wing"), ("b", "Turns the craft to keep the desired ground track"), ("c", "Makes the wind stop"), ("d", "Lowers the flaps")], "b"),
        ("What are the three sides of the wind triangle?", [("a", "Height, depth and width"), ("b", "Fuel, cargo and crew"), ("c", "Airspeed, wind and ground track"), ("d", "Engines, wings and tail")], "c"),
        ("What does a flight computer do?", [("a", "Solves the wind triangle quickly"), ("b", "Cooks meals in flight"), ("c", "Paints the wing"), ("d", "Plays music for passengers")], "a"),
    ],
}
