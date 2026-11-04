"""Entry, Descent and Landing: how a spacecraft survives the heat, slows down and sets down safely on another world."""
CODE = "science5_planet_edl"
BOOK = {
    "title": "Entry, Descent and Landing",
    "subtitle": "Surviving the heat, slowing down and touching down safely on another world",
    "chapters": [
        ("The hardest minutes", "Entry, descent and landing is the most dangerous part of many planetary missions. In a matter of minutes, a spacecraft must slow from very high speed to a gentle touchdown."),
        ("Entry heating", "Entering an atmosphere at high speed heats the front of the craft to extreme temperatures. A heat shield made of tough material protects the craft, often by slowly burning away, a process called ablation."),
        ("Parachute systems", "Parachutes slow a craft after the first and most intense braking. Large parachutes must open at supersonic speeds, which makes their design one of the hardest engineering problems."),
        ("Retro-propulsion", "Rockets fired against the direction of motion slow a craft during the last part of descent. Engineers use this retro-propulsion to reach a near-stop just above the ground."),
        ("Landing hazards", "Rocks, slopes and loose sand can damage a lander or tip it over. Engineers plan the landing to avoid those hazards, using the best maps available before touchdown."),
        ("Navigation and site selection", "Terrain-relative navigation lets a craft compare what it sees with a map and steer toward a safe spot. Landing site selection weighs science goals against the risks found in the maps."),
    ],
    "test": [
        ("What is the main purpose of a heat shield on entry?",
         [("a", "To make the craft shine"), ("b", "To provide food"), ("c", "To protect the craft from extreme heat as it enters an atmosphere"), ("d", "To power the engines")], "c"),
        ("What is ablation?",
         [("a", "A type of paint"), ("b", "A type of parachute"), ("c", "A kind of rocket fuel"), ("d", "A slow burning away of a heat shield's surface to carry off heat")], "d"),
        ("What does retro-propulsion do?",
         [("a", "Fires rockets to speed the craft up"), ("b", "Fires rockets against the direction of motion to slow the craft"), ("c", "Turns off the engines"), ("d", "Lights the landing site")], "b"),
        ("What makes large parachutes hard to design?",
         [("a", "They must open at supersonic speeds"), ("b", "They must be made of glass"), ("c", "They must float forever"), ("d", "They must be painted gold")], "a"),
        ("What helps a craft choose a safe landing spot?",
         [("a", "Landing on the top of the tallest rock"), ("b", "Picking the spot at random"), ("c", "Landing in the darkest crater"), ("d", "Landing site selection that weighs science goals against the risks in the maps")], "d"),
    ],
}
