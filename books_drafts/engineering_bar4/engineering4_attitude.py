"""Attitude Control: pointing a craft, reaction wheels, momentum dumping, thrusters and the sensors that measure attitude."""
CODE = "engineering4_attitude"
BOOK = {
    "title": "Attitude Control: Reaction Wheels and Thrusters",
    "subtitle": "Pointing, wheels, thrusters and sensors",
    "chapters": [
        ("Pointing",
         "Attitude is the orientation of a craft in space. Many craft must point an antenna, a camera or a sensor at a target, and hold it steady."),
        ("Reaction wheels",
         "A reaction wheel is a spinning flywheel. Speeding it up turns the craft the other way, and slowing it turns the craft back. Small turns need no fuel."),
        ("Momentum storage and dumping",
         "A wheel can store only so much spin. When it builds up too much, the craft must dump the momentum, often with thrusters or magnetic torquers."),
        ("Thrusters",
         "Thrusters push the craft to turn or to move. They use propellant, so their use is counted and saved for jobs the wheels cannot do."),
        ("Sensors",
         "Star trackers, sun sensors and gyroscopes measure attitude. The controller compares the measured attitude with the target and corrects the difference."),
        ("Trade-offs",
         "Wheels are precise and save propellant, but their momentum must be dumped. Thrusters are simple and powerful, but they use fuel."),
    ],
    "test": [
        ("What is attitude?",
         [("a", "The orientation of a craft in space"), ("b", "Engine noise"), ("c", "The fuel level"), ("d", "The crew mood")], "a"),
        ("How does a reaction wheel turn a craft?",
         [("a", "By melting"), ("b", "By leaking gas"), ("c", "By sound"), ("d", "By speeding up or slowing its spin")], "d"),
        ("Why must momentum be dumped?",
         [("a", "Thrusters are needed for paint"), ("b", "The Sun is near"), ("c", "A wheel can store only so much spin"), ("d", "Wheels melt")], "c"),
        ("What is a drawback of thrusters?",
         [("a", "They use propellant"), ("b", "They are silent"), ("c", "They cannot push"), ("d", "They need no sensors")], "a"),
        ("What do star trackers and sun sensors measure?",
         [("a", "Paint"), ("b", "Attitude"), ("c", "Music"), ("d", "Cake")], "b"),
    ],
}
