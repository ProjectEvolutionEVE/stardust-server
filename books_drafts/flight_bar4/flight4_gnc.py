"""Guidance, Navigation and Control: the three jobs every flying craft must do, and how they fit together."""
CODE = "flight4_gnc"
BOOK = {
    "title": "Guidance, Navigation and Control",
    "subtitle": "Where to go, where we are, and how to steer",
    "chapters": [
        ("Three jobs", "Every flying craft must do three jobs. Guidance decides where to go next. Navigation works out where the craft is now. Control makes the craft move the way guidance asks."),
        ("Sensors in", "Sensors feed the craft with information. Star trackers, sun sensors, gyroscopes, accelerometers and radio links all report what is happening. No single sensor is perfect, so the computer weighs them together."),
        ("The computer in the middle", "The flight computer takes the sensor data and works out the position, the speed and the plan. It compares the plan with the goal and decides the next correction. This happens many times every second."),
        ("Actuators out", "Actuators carry out the decision. They are the thrusters, the wheels that turn the craft, and the engines. Each one gets a command from the computer and makes a small move."),
        ("Control loops", "A control loop measures the error, which is the gap between where the craft is and where it should be. It then pushes back to shrink the gap. A good loop corrects smoothly and does not overshoot."),
        ("Real flight examples", "Apollo's computer used guidance and navigation together to land on the Moon. Modern craft use the same three jobs, often with more sensors and more careful checks on each part."),
    ],
    "test": [
        ("What does guidance decide?", [("a", "The colour of the hull"), ("b", "The cook's menu"), ("c", "Where the craft should go next"), ("d", "The radio station")], "c"),
        ("What is the job of navigation?", [("a", "Turning the craft off"), ("b", "Working out where the craft is now"), ("c", "Painting the wings"), ("d", "Counting the crew")], "b"),
        ("What does an actuator do?", [("a", "Carries out the computer's command with a thruster, wheel or engine"), ("b", "Measures the sun"), ("c", "Plays music"), ("d", "Stores the data")], "a"),
        ("What is the gap that a control loop measures?", [("a", "The size of the cabin"), ("b", "The length of the day"), ("c", "The gap between two stars"), ("d", "The error between where the craft is and where it should be")], "d"),
        ("Why does the computer weigh several sensors together?", [("a", "Sensors cannot be turned on"), ("b", "It needs more paint"), ("c", "No single sensor is perfect"), ("d", "Sensors are only for show")], "c"),
    ],
}
