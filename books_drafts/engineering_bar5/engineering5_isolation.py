"""Vibration Isolation Theory: how a flexible mount lets a machine's shaking pass less strongly into its surroundings, and how to choose the mount."""
CODE = "engineering5_isolation"
BOOK = {
    "title": "Vibration Isolation Theory",
    "subtitle": "How flexible mounts keep shaking out of the floor and the frame",
    "chapters": [
        ("The aim of isolation", "Isolation stops a machine's shaking from reaching the floor, the frame or nearby equipment. A flexible mount sits between the machine and its support. It lets the machine move a little so less force passes through."),
        ("Transmissibility", "Transmissibility is the ratio of the force or motion passed on to the support, compared with the input. A value below one means the mount is doing its job. The value depends on the ratio of the driving frequency to the natural frequency, and on damping."),
        ("The isolation region", "Isolation works only above a certain frequency. Once the driving frequency is about the square root of two times the natural frequency or more, the transmissibility falls below one. Below that range, a mount can make the shaking worse."),
        ("Choosing the mount", "A softer mount has a lower natural frequency, so it isolates better over a wider range. But a very soft mount can move too much under load or during start-up. Engineers pick a stiffness that balances these needs."),
        ("Rotating machines", "Fans, pumps and motors spin at a steady speed, so their driving frequency is known. The mount is chosen so its natural frequency is well below that speed. Starting and stopping pass through resonance and must be checked."),
        ("Damping trade-off", "More damping lowers the peak at resonance, but it reduces isolation at high frequency. Engineers pick damping to suit the expected speeds. A test on the installed machine confirms that the isolation works."),
    ],
    "test": [
        ("What does isolation stop?", [("a", "The machine from having a colour"), ("b", "The machine from being switched on"), ("c", "The sound of the operator"), ("d", "Shaking from passing into the floor and frame")], "d"),
        ("What is transmissibility?", [("a", "The number of wires in a cable"), ("b", "The ratio of the force or motion passed on to the support, compared with the input"), ("c", "The speed of a fan"), ("d", "The price of a mount")], "b"),
        ("Above what driving frequency does isolation start to work?", [("a", "Zero hertz"), ("b", "Exactly the natural frequency"), ("c", "One tenth of the natural frequency"), ("d", "About the square root of two times the natural frequency or more")], "d"),
        ("Why can a very soft mount cause trouble?", [("a", "It makes the machine lighter"), ("b", "It removes all shaking"), ("c", "It can move too much under load or during start-up"), ("d", "It changes the paint")], "c"),
        ("What is the trade-off in damping for an isolator?", [("a", "More damping lowers the resonance peak but reduces isolation at high frequency"), ("b", "More damping makes the peak higher"), ("c", "Damping has no effect"), ("d", "Damping only changes the colour")], "a"),
    ],
}
