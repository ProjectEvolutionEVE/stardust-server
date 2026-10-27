"""Rotor Balancing and Critical Speeds: unbalance, critical speeds, balancing methods, rotor dynamics and running past a critical speed."""
CODE = "engineering4_rotor"
BOOK = {
    "title": "Rotor Balancing and Critical Speeds",
    "subtitle": "Unbalance, critical speeds and safe running",
    "chapters": [
        ("Unbalance",
         "A rotor is unbalanced when its mass is not spread evenly about its axis. The heavy spot pulls outward as the rotor spins, and that causes vibration."),
        ("Critical speeds",
         "A critical speed is a speed at which the rotor's vibration matches its natural frequency. The vibration can then grow sharply."),
        ("Balancing methods",
         "Balancing adds or removes small masses in set planes, so the rotor spins true. It is done on a balancing machine that measures the vibration."),
        ("Rotor dynamics",
         "Rotor dynamics studies how the shaft, bearings and supports move together at speed. Stiffer supports raise the critical speeds, and damping reduces the peak."),
        ("Running past a critical speed",
         "Many rotors run safely above a critical speed. They pass through it quickly during start-up or shut-down, and that needs careful, quick acceleration."),
        ("Monitoring",
         "Vibration sensors show when a rotor is near a critical speed or out of balance, so operators can act early. Trends in the readings show wear before it becomes a fault."),
    ],
    "test": [
        ("What causes unbalance in a rotor?",
         [("a", "Mass not spread evenly about the axis"), ("b", "Paint"), ("c", "Colour"), ("d", "Sound")], "a"),
        ("What is a critical speed?",
         [("a", "The speed of paint"), ("b", "The speed of sound"), ("c", "Zero speed"), ("d", "A speed where vibration matches the natural frequency and can grow")], "d"),
        ("What does balancing do?",
         [("a", "Adds fuel"), ("b", "Adds or removes small masses in set planes"), ("c", "Changes colour"), ("d", "Makes sound")], "b"),
        ("What do stiffer supports do?",
         [("a", "Lower the rotor's weight"), ("b", "Paint the bearings"), ("c", "Stop all vibration"), ("d", "Raise the critical speeds")], "d"),
        ("Why do vibration sensors help?",
         [("a", "They show when a rotor is near a critical speed or out of balance"), ("b", "They paint the rotor"), ("c", "They add heat"), ("d", "They stop the rotor")], "a"),
    ],
}
