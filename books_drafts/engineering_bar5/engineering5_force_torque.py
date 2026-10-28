"""Force-Torque Sensing and Compliance Control: strain-based sensors, calibration, contact forces, compliance control and safety limits."""
CODE = "engineering5_force_torque"
BOOK = {
    "title": "Force-Torque Sensing and Compliance Control",
    "subtitle": "Feeling a push, and yielding to it",
    "chapters": [
        ("Feeling force",
         "A force-torque sensor lets a robot feel the forces and twists acting on its tool. It is usually placed between the wrist and the tool. With it, a robot can tell how hard it is pushing, and in which direction."),
        ("Strain-based sensors",
         "Most of these sensors use strain gauges bonded to a metal body. Under load, the body deforms by a tiny amount, and the gauges change their electrical resistance. The changes are turned into force and torque values."),
        ("Calibration",
         "Each sensor must be calibrated so its readings match known forces and torques. Engineers hang known weights and apply known twists, then record the sensor's response. Without this step the readings would be wrong."),
        ("Contact forces",
         "When a tool touches a surface, a contact force appears, pushing back on the tool. The robot must handle this force carefully. A tool that pushes too hard can damage the work or itself."),
        ("Compliance control",
         "Compliance control lets the robot give way to contact forces, rather than pushing rigidly. The robot moves in a way that keeps the force near a target value. This is how robots can polish a surface or insert a part smoothly."),
        ("Safety limits",
         "Force limits must be set so that contact with people or objects stays gentle enough to avoid harm. The controller stops or backs off when a limit is reached. Safety limits are checked and tested before any robot works near people."),
    ],
    "test": [
        ("How do strain-based force sensors work?",
         [("a", "By weighing with a scale"), ("b", "Strain gauges measure a tiny deformation of a metal body under load"), ("c", "By sound"), ("d", "By light")], "b"),
        ("Why calibrate a force-torque sensor?",
         [("a", "To paint it"), ("b", "To make it hotter"), ("c", "To change its name"), ("d", "To map its readings to known forces and torques")], "d"),
        ("What is compliance control?",
         [("a", "Obeying a paint code"), ("b", "Following a price list"), ("c", "Letting the robot yield to contact forces instead of pushing rigidly"), ("d", "Turning off the power")], "c"),
        ("Why set safety limits on contact force?",
         [("a", "So contact with people or objects stays gentle enough to avoid harm"), ("b", "To make the robot faster"), ("c", "To cut the cost of cable"), ("d", "To lower the paint bill")], "a"),
        ("What is a contact force?",
         [("a", "A type of paint"), ("b", "The push or pull that arises when the tool touches something"), ("c", "A cable colour"), ("d", "The speed of a motor")], "b"),
    ],
}
