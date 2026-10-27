"""Limit Analysis and Plastic Collapse: how ductile structures carry load past first yield, until they collapse."""
CODE = "engineering5_limit_analysis"
BOOK = {
    "title": "Limit Analysis and Plastic Collapse",
    "subtitle": "When a structure gives way under its full load, not just when it first yields",
    "chapters": [
        ("Beyond first yield",
         "A ductile structure does not fail the moment one fibre first yields. It can keep carrying more load as plastic hinges form, until enough of them make a mechanism. The load at that point is the collapse load."),
        ("Plastic hinges",
         "A plastic hinge is a section where the whole cross-section has reached yield, so it can turn while holding its full plastic moment. A beam with enough hinges becomes a mechanism, a set of rigid pieces that can move."),
        ("Upper and lower bounds",
         "The upper bound theorem says any possible mechanism gives a load at or above the true collapse load, so the lowest such load is the best estimate from above. The lower bound theorem says a safe stress field, which balances the loads and nowhere exceeds yield, gives a load at or below collapse."),
        ("Collapse of beams and frames",
         "For a beam, count the hinges needed to make a mechanism, then balance the work of the loads against the work absorbed at the hinges. Frames work the same way, and each possible sway or joint rotation must be checked. The lowest result is the one that governs."),
        ("Shakedown",
         "A structure under repeated loads may settle into purely elastic behaviour after early yielding. This is shakedown. If the loads cycle beyond that limit, the structure can fail by alternating plasticity or by ratchetting, where the deformation grows with each cycle."),
        ("Safety in ductile design",
         "Ductile steel gives warning through large deflections before it breaks, which is why plastic design is trusted. Engineers still apply factors of safety and check that hinges have enough rotation capacity to form as assumed."),
    ],
    "test": [
        ("What is a plastic hinge?",
         [("a", "A pivot bolt"), ("b", "A section where the full cross-section has yielded, so it can rotate at the plastic moment"), ("c", "A welded joint"), ("d", "A spring for vibration")], "b"),
        ("What does the upper bound theorem give?",
         [("a", "A load always below the true collapse load"), ("b", "Nothing useful"), ("c", "A load at or above the true collapse load"), ("d", "A load equal to zero")], "c"),
        ("Which best describes shakedown?",
         [("a", "Failure after a single load"), ("b", "A structure settles into elastic behaviour after early yielding under repeated loads"), ("c", "Shaking in an earthquake"), ("d", "Cracking from heat")], "b"),
        ("What does a mechanism in a beam mean?",
         [("a", "Enough hinges that the beam becomes rigid pieces able to move"), ("b", "A new steel grade"), ("c", "A gear train"), ("d", "A bolted connection")], "a"),
        ("Why is ductile steel preferred for plastic design?",
         [("a", "It never deforms"), ("b", "It is cheaper to paint"), ("c", "It gives warning through large deflections before it breaks"), ("d", "It has no yield point")], "c"),
    ],
}
