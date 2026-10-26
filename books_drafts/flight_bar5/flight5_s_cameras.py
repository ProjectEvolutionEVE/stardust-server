"""Cameras on Spacecraft: how a camera turns light into pictures, and why those pictures matter for navigation and science."""
CODE = "flight5_s_cameras"
BOOK = {
    "title": "Cameras on Spacecraft",
    "subtitle": "Taking pictures from space, and what makes them work",
    "chapters": [
        ("Optics",
         "A camera's lens gathers light and focuses it onto a sensor. Spacecraft cameras use long lenses or mirrors to see far-off targets clearly."),
        ("Sensors",
         "A digital sensor turns light into numbers. Each pixel records how much light reached it, and the sensor's size affects detail and noise."),
        ("Exposure",
         "Exposure is how long and how brightly the sensor is lit. Scenes in space can be very bright in sunlight and very dark in shadow, so exposure must be chosen with care."),
        ("Compression",
         "Pictures are compressed to fit limited radio links back to Earth. Stronger compression saves time, but it can lose detail."),
        ("Navigation images",
         "Some craft use cameras to find their position by recognising stars or landmarks. Those images guide steering as well as science."),
        ("Apollo photography",
         "Apollo astronauts carried Hasselblad cameras to the Moon. Their photographs remain some of the best records of the missions."),
    ],
    "test": [
        ("What does a camera's lens do?",
         [("a", "Stores pictures"), ("b", "Cools the sensor"), ("c", "Gathers light and focuses it onto a sensor"), ("d", "Sends radio signals")], "c"),
        ("What does a digital sensor do?",
         [("a", "Burns film"), ("b", "Turns light into numbers"), ("c", "Makes sound"), ("d", "Adds fuel")], "b"),
        ("What is exposure?",
         [("a", "The size of a lens"), ("b", "The weight of a camera"), ("c", "The colour of its case"), ("d", "How long and how brightly the sensor is lit")], "d"),
        ("Why are space pictures compressed?",
         [("a", "To fit limited radio links to Earth"), ("b", "To make them colder"), ("c", "To add noise"), ("d", "To make the files heavier")], "a"),
        ("What cameras did Apollo astronauts take to the Moon?",
         [("a", "Boxes of film only"), ("b", "Hasselblad cameras"), ("c", "Mobile phones"), ("d", "Wooden cameras")], "b"),
    ],
}
