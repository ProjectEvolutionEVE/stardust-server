"""Lidar and Radar for Navigation: measuring distance and speed with light and radio, and where each one struggles."""
CODE = "flight5_s_lidar"
BOOK = {
    "title": "Lidar and Radar for Navigation",
    "subtitle": "Measuring distance and speed with light and radio",
    "chapters": [
        ("Radar",
         "Radar sends out radio waves and times the echoes that bounce back. The timing gives the distance, and the change in an echo's frequency gives the speed."),
        ("Lidar",
         "Lidar uses short pulses of laser light instead of radio. It builds a fine picture of nearby shapes and distances."),
        ("Range and speed",
         "Both methods measure range by timing echoes. The Doppler effect, the change in pitch of a returning wave, gives speed toward or away from the sensor."),
        ("Docking",
         "Some docking systems use lidar to find the exact position and angle of the other craft as it closes in. A slow, careful approach keeps contact gentle."),
        ("Landing",
         "Landing craft use radar and lidar to measure height and sideways motion close to the surface. These readings guide the final part of the descent."),
        ("Weather limits",
         "Fog, dust and rain can scatter light, and heavy rain can weaken radio signals. Engineers plan for these limits and use more than one kind of sensor."),
    ],
    "test": [
        ("What does radar use?",
         [("a", "Radio waves"), ("b", "Sound"), ("c", "Sand"), ("d", "Fire")], "a"),
        ("What does lidar use to measure?",
         [("a", "Radio only"), ("b", "A rubber ball"), ("c", "Pulses of laser light"), ("d", "Heat from the Sun")], "c"),
        ("What does the timing of an echo tell you?",
         [("a", "Colour"), ("b", "Weight"), ("c", "Taste"), ("d", "Distance")], "d"),
        ("What is docking?",
         [("a", "Storing cargo"), ("b", "Joining two craft together"), ("c", "Cooking food"), ("d", "Painting a hull")], "b"),
        ("What can weaken lidar and radar readings?",
         [("a", "Heavy fog, dust or rain"), ("b", "Clear skies"), ("c", "Silence"), ("d", "Sunny days")], "a"),
    ],
}
