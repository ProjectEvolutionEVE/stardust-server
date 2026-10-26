"""Ballistic Capture: entering orbit around a moon or planet without a large braking burn, by using a weak region of gravity."""
CODE = "flight4_ballistic_capture"
BOOK = {
    "title": "Ballistic Capture",
    "subtitle": "Falling into orbit without a big braking burn",
    "chapters": [
        ("Braking is costly", "To stop near a planet, a craft must lose a great deal of speed. The usual way is a large braking burn, and that burn can need a lot of fuel. Ballistic capture is a way to get into orbit with much less."),
        ("A weak region", "Around a body such as the Moon there is a region where the pulls of the Moon and the Sun are close to balanced. A craft that enters it slowly can stay there for a time. Planners call this a weak stability region."),
        ("Falling into orbit", "A craft on the right path drifts into this region and is caught by the Moon's pull. It settles into an orbit with only a small burn, or sometimes no burn at all, because the natural paths did most of the work."),
        ("Weak stability", "The capture is weak. The orbit is easy to lose, and small changes can send the craft back out. So planners check the path with care and often correct it soon after arrival."),
        ("Moon and Mars examples", "Hiten used this kind of capture to enter lunar orbit in 1991. Planners have also studied the same idea for Mars. The results show that a slow arrival can save much fuel for the same mission."),
        ("Planning and risk", "The trade is time against fuel and risk. A ballistic capture arrives slowly and can be fragile, so it suits missions that can wait. Planners make a backup plan for each capture."),
    ],
    "test": [
        ("What is the main idea of ballistic capture?", [("a", "Painting the craft"), ("b", "Flying without any gravity"), ("c", "Getting into orbit with much less braking fuel"), ("d", "Using a big engine at full power all the time")], "c"),
        ("What is a weak stability region?", [("a", "A type of spacesuit"), ("b", "A storm on Mars"), ("c", "A launch pad"), ("d", "An area where the pulls of two bodies are close to balanced")], "d"),
        ("What does the capture need, in the best case?", [("a", "A burn larger than the whole craft"), ("b", "Only a small burn or none at all"), ("c", "Ten years of waiting at once"), ("d", "No path at all")], "b"),
        ("What is a weakness of this kind of capture?", [("a", "The orbit is easy to lose"), ("b", "It makes the craft heavier"), ("c", "It cannot be planned"), ("d", "It only works on Earth")], "a"),
        ("What is the trade for a mission using this method?", [("a", "More fuel and no time loss"), ("b", "No change at all"), ("c", "Less fuel, but a slower arrival and a fragile orbit"), ("d", "A faster arrival with no risk")], "c"),
    ],
}
