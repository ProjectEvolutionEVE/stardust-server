"""Failure Modes Before They Happen: list every part, ask how each could fail, and rank what to fix first."""
CODE = "flight3c_failure_modes"
BOOK = {
    "title": "Failure Modes Before They Happen",
    "subtitle": "Listing every part, asking how each could fail, and ranking what to fix first",
    "chapters": [
        ("Ask how it breaks",
         "Engineers often use a method called failure mode and effects analysis. For each part, they ask how it could fail, what the failure would do, and how likely it is. The method turns a vague worry into a written plan."),
        ("List every part",
         "The team lists each part of a system, from a valve to a wire to a sensor. A single part can fail in more than one way. A valve may stick open, stick shut, or leak. Each way of failing gets its own line."),
        ("Score the risk",
         "Each failure is scored for how serious it would be, how often it might happen, and how hard it would be to notice in time. Multiplying the three scores gives a ranking. The ranking shows what to fix first."),
        ("Find the hidden ones",
         "The hardest failures are the ones that give no warning, such as a sensor that quietly reads wrong. A good analysis asks what could stay hidden, and then adds a way to check for it. A hidden fault is the one most likely to surprise you."),
        ("Fix the cause",
         "A warning light is useful, but the best fix removes the cause or adds a second way to see the problem. Finding a flaw on the ground is far cheaper than repairing it far from home. Early checks save money later."),
        ("A pilot's use",
         "Pilots use the same habit when they walk round their craft and ask what could go wrong on this flight. Keep a short list of the top few risks, and check those first every time. A short, honest list beats a long one nobody reads."),
    ],
    "test": [
        ("What does failure mode and effects analysis ask for each part?",
         [("a", "What colour it is"), ("b", "How it could fail, what that would do, and how likely it is"), ("c", "Who made it"), ("d", "How heavy its box is")], "b"),
        ("Why is each part listed with several ways it could fail?",
         [("a", "Parts never fail"), ("b", "It makes the list longer for fun"), ("c", "A part can fail in more than one way, such as sticking open or shut"), ("d", "Only one failure is ever possible")], "c"),
        ("Which three things are scored for each failure?",
         [("a", "Colour, shape and weight"), ("b", "Seriousness, how often it might happen, and how hard it is to notice"), ("c", "Cost, crew and distance from the Sun"), ("d", "Speed, time and fuel")], "b"),
        ("Which failures are the hardest to catch?",
         [("a", "The ones with loud alarms"), ("b", "Failures on the sunny side"), ("c", "Failures the pilot already knows about"), ("d", "The ones that give no warning, such as a quietly wrong sensor")], "d"),
        ("Why is fixing a flaw on the ground cheaper than fixing it in orbit?",
         [("a", "Repairs far from home need more fuel, time and risk"), ("b", "Ground work is faster by magic"), ("c", "Orbit has no air"), ("d", "Ground parts are always free")], "a"),
    ],
}
