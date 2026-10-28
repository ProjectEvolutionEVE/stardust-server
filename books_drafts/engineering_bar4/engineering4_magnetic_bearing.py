"""Magnetic Bearings and Levitation: magnetic force, active position control, no-contact rotation, power losses and failure modes."""
CODE = "engineering4_magnetic_bearing"
BOOK = {
    "title": "Magnetic Bearings and Levitation",
    "subtitle": "Active control, no-contact rotation and backup bearings",
    "chapters": [
        ("Magnetic force",
         "Magnets can push or pull a rotor without touching it. A fixed arrangement of magnets cannot hold a rotor stable on its own, so some control is needed."),
        ("Active control",
         "Sensors measure the rotor's position many times a second. A controller adjusts the currents in the magnets to hold the rotor in place."),
        ("No-contact rotation",
         "With no contact, there is no friction or wear in the bearing. This allows very high speeds and a long life."),
        ("Power losses",
         "The magnets and the controller use power, and eddy currents and hysteresis can heat parts. Designers keep these losses low."),
        ("Failure modes",
         "If power or the controller fails, the rotor may drop onto backup bearings. Backup bearings are needed for a safe shutdown."),
        ("Where they are used",
         "Magnetic bearings appear in turbines, compressors and flywheels, where low friction matters. Their low friction also suits any job where clean running matters."),
    ],
    "test": [
        ("What is an advantage of magnetic bearings?",
         [("a", "No contact means no friction or wear"), ("b", "They are made of paper"), ("c", "They need no sensors"), ("d", "They are heavy by design")], "a"),
        ("Why is active control needed?",
         [("a", "Magnets are bad"), ("b", "Rotors never move"), ("c", "A fixed arrangement of magnets cannot hold a rotor stable on its own"), ("d", "Sensors are wasted")], "c"),
        ("What do the sensors in a magnetic bearing measure?",
         [("a", "Paint"), ("b", "Taste"), ("c", "Wind"), ("d", "Rotor position")], "d"),
        ("What is a risk if power fails?",
         [("a", "The rotor paints itself"), ("b", "Nothing ever happens"), ("c", "The rotor may drop onto backup bearings"), ("d", "The rotor grows")], "c"),
        ("Where are magnetic bearings used?",
         [("a", "Turbines, compressors and flywheels"), ("b", "Kitchens"), ("c", "Sofas"), ("d", "Gardens")], "a"),
    ],
}
