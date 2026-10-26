"""Inertial Navigation: Counting Every Push. Accelerometers and gyroscopes track a craft from the inside, and small errors grow over time."""
CODE = "navigation3c_inertial"
BOOK = {
    "title": "Inertial Navigation: Counting Every Push",
    "subtitle": "Accelerometers and gyroscopes that track a craft from inside, and why small errors grow",
    "chapters": [
        ("Sensing from inside",
         "An inertial navigation unit needs no view of the outside. It carries accelerometers, which sense every push on the craft, and gyroscopes, which sense every turn. Nothing outside has to be seen or heard."),
        ("From push to speed to place",
         "Adding up the acceleration readings over time, which navigators call integrating, gives the change in speed. Adding up the speeds over time gives the change in position. Starting from a known place and speed, the unit keeps a running total."),
        ("Turning the pushes",
         "A push is measured in the craft's own axes, so it must be turned into the outside frame before it is added up. The gyroscopes supply the turn, so the unit always knows which way each push pointed."),
        ("Where the drift comes from",
         "The sums are never perfect. A tiny steady error in an accelerometer, added up over time, grows into a large position error. A constant error in acceleration gives a position error that grows with the square of the time elapsed."),
        ("Fixes from outside",
         "Real units are corrected from outside whenever they can be, using a star view, a radio fix or a known landmark. Between fixes the unit carries the position alone. It is the best sensor for short spans and the weakest for long ones."),
        ("Self-contained, and therefore limited",
         "Because it needs nothing from outside, an inertial unit still works in the dark, under cloud, or inside a hull where no signal reaches. That is why craft carry them. Its weakness is time: left alone, it wanders."),
    ],
    "test": [
        ("What do accelerometers sense?",
         [("a", "The colour of the stars"), ("b", "Every push on the craft"), ("c", "The speed of light"), ("d", "The Sun's warmth")], "b"),
        ("What does adding up acceleration readings over time give you?",
         [("a", "The change in speed"), ("b", "The number of crew"), ("c", "The fuel price"), ("d", "The weight of the cargo")], "a"),
        ("What is the main weakness of inertial navigation on its own?",
         [("a", "It cannot work in the dark"), ("b", "It needs a star view every second"), ("c", "Small errors grow over time"), ("d", "It sends signals that others can hear")], "c"),
        ("What do gyroscopes supply to an inertial unit?",
         [("a", "The turn of the craft, so each push can be turned into outside axes"), ("b", "The name of the next port"), ("c", "The air pressure in the hold"), ("d", "The radio channel")], "a"),
        ("Why are inertial units corrected from outside whenever possible?",
         [("a", "They never have any error"), ("b", "Their running sums drift, and a fix resets them"), ("c", "The law requires it"), ("d", "They cannot measure pushes")], "b"),
    ],
}
