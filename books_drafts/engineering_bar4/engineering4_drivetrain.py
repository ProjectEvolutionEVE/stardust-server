"""Drivetrains and Differentials: gear ratios, torque split, limited-slip units, drivetrain efficiency and the cost of a gearbox."""
CODE = "engineering4_drivetrain"
BOOK = {
    "title": "Drivetrains and Differentials",
    "subtitle": "Gear ratios, torque split and limited-slip units",
    "chapters": [
        ("Gear ratios",
         "A gear ratio sets how much torque is multiplied and how much speed is reduced. A high ratio gives more torque at low speed."),
        ("Torque split",
         "An open differential sends equal torque to both wheels, so the slower wheel limits the drive. A limited-slip unit sends more torque to the wheel that has more grip."),
        ("Drivetrain efficiency",
         "Each gear mesh and bearing loses some power as heat. Efficient designs keep those losses small."),
        ("Limited-slip units",
         "Limited-slip units use friction plates, clutches or gears to restrain the difference in speed between the wheels. They help traction on slippery ground."),
        ("The cost of the gearbox",
         "Gearboxes add weight, cost and maintenance. Designers choose the fewest gears that give the range the vehicle needs."),
        ("Matching to use",
         "The drivetrain should suit the way the vehicle is used. A vehicle that climbs hills needs different ratios from one that cruises on a flat road."),
    ],
    "test": [
        ("What does a higher gear ratio give?",
         [("a", "More torque at lower speed"), ("b", "More colour"), ("c", "Silence"), ("d", "Lighter wheels")], "a"),
        ("What does an open differential do with the torque?",
         [("a", "Stops the car"), ("b", "Paints it"), ("c", "Sends all of it to one wheel"), ("d", "Sends equal torque to both wheels")], "d"),
        ("What does a limited-slip unit do?",
         [("a", "Makes noise"), ("b", "Restrains the speed difference between the wheels"), ("c", "Melts"), ("d", "Steers")], "b"),
        ("What do gear meshes and bearings lose?",
         [("a", "Gold"), ("b", "Light"), ("c", "Paint"), ("d", "Power as heat")], "d"),
        ("What should a gearbox design aim for?",
         [("a", "The fewest gears that give the range needed"), ("b", "The most gears possible"), ("c", "Heavy gears"), ("d", "Paint")], "a"),
    ],
}
