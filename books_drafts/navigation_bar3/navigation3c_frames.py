"""Frames of Reference: Ship Axes and World Axes. Which way is forward, and how to turn one set of directions into another."""
CODE = "navigation3c_frames"
BOOK = {
    "title": "Frames of Reference: Ship Axes and World Axes",
    "subtitle": "Which way is forward, which way is up, and how to turn one set of directions into another",
    "chapters": [
        ("Measuring from somewhere",
         "A direction means nothing until you say what it is measured from. A frame of reference is a set of three axes and a starting point. Every position and every push is stated in one frame or another."),
        ("The craft's own axes",
         "The ship frame, also called the body frame, is fixed to the craft. Its axes point forward, to one side, and up or down. Sensors report in these axes, because that is how they are bolted on."),
        ("A fixed frame",
         "A fixed frame does not turn with the craft. In space, navigators use axes fixed against the distant stars, which hardly move during a short flight. Positions are easiest to add up in a frame like that."),
        ("Turning between frames",
         "To compare the two, the navigator turns the readings through the craft's attitude, its angle in space. The turn changes the numbers, though the push itself has not changed. A mistake in that turn is a common source of wrong answers."),
        ("Local frames near the ground",
         "Near a planet, a local frame has one axis pointing straight up from the surface, and the others pointing north and east, or along the track. Charts, maps and landing sites are easiest to state in a frame like that."),
        ("Always name the frame",
         "State your frame as well as your numbers. A position given without its frame can mean something very different. A navigator's log should name the frame in every entry."),
    ],
    "test": [
        ("What is a frame of reference?",
         [("a", "A picture on the wall"), ("b", "A set of three axes and a starting point"), ("c", "A kind of engine"), ("d", "A type of sensor")], "b"),
        ("Which frame is fixed to the craft and turns with it?",
         [("a", "The fixed frame"), ("b", "The local frame"), ("c", "The ship frame, also called the body frame"), ("d", "The Earth's core")], "c"),
        ("Why do navigators often use axes fixed against the distant stars?",
         [("a", "Because stars are very bright"), ("b", "Because the stars barely shift in a short flight, so the axes stay steady"), ("c", "Because stars steer the craft"), ("d", "Because stars carry the radio signal")], "b"),
        ("What must be done before comparing ship-frame readings with a fixed frame?",
         [("a", "Paint the hull"), ("b", "Double the fuel"), ("c", "Switch off the sensors"), ("d", "Turn the readings through the craft's attitude")], "d"),
        ("Why should every log entry name its frame?",
         [("a", "Because a position without its frame can mean something very different"), ("b", "Because the frame is always the same"), ("c", "Because the law requires a colour code"), ("d", "Because it makes the page longer")], "a"),
    ],
}
