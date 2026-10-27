"""Drone Magnetics and Gradiometry: flying magnetic sensors over ground to map buried rock, and the care that makes the data useful."""
CODE = "mining5_drone_mag"
BOOK = {
    "title": "Drone Magnetics and Gradiometry",
    "subtitle": "Mapping buried rock from the air with magnetic sensors",
    "chapters": [
        ("Sensor noise", "Every magnetic sensor picks up some noise from its own electronics and from the drone. Teams measure the noise before each survey. Noise that is too high hides the real signal."),
        ("Flight lines", "A survey is flown along parallel flight lines at a set height and spacing. The lines must be close enough to resolve the targets. Careful planning sets the spacing for the size of the feature."),
        ("Magnetic gradients", "A gradiometer uses two sensors to measure how fast the magnetic field changes over a short distance. Gradients sharpen edges and show buried features more clearly. They help locate contacts between rock types."),
        ("Processing", "Raw magnetic data is corrected for the drone's own magnetism, for the time of day and for the flight path. Processing removes noise and turns the readings into a map. Each step is recorded so it can be repeated."),
        ("Costs", "Drone surveys cost much less than crewed aircraft surveys over small areas. They are limited by battery life and by flight rules. The cost must be weighed against the size of the area."),
        ("Mapping", "The processed data is turned into maps that show magnetic patterns across the ground. Geologists interpret these patterns with other data such as rock samples. A combined map is a stronger guide for drilling."),
    ],
    "test": [
        ("What does a gradiometer measure?",
         [("a", "How fast the magnetic field changes over a short distance"), ("b", "The temperature of the drone"), ("c", "The speed of the wind"), ("d", "The colour of the ground")], "a"),
        ("Why are flight lines spaced carefully?",
         [("a", "To make the drone look good"), ("b", "To use up the battery quickly"), ("c", "To avoid all magnetism"), ("d", "To resolve the targets at the size being searched for")], "d"),
        ("Why is sensor noise measured before a survey?",
         [("a", "Noise makes the ground warmer"), ("b", "Noise is never a problem"), ("c", "Noise that is too high can hide the real signal"), ("d", "Noise cancels out gold")], "c"),
        ("What must processing correct for?",
         [("a", "The number of birds nearby"), ("b", "The drone's own magnetism, the time of day and the flight path"), ("c", "The price of fuel"), ("d", "The name of the pilot")], "b"),
        ("What limits a drone survey?",
         [("a", "Battery life and flight rules"), ("b", "The taste of the ground"), ("c", "The number of trees in town"), ("d", "The weather on Mars")], "a"),
    ],
}
