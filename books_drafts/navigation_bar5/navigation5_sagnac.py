"""The Sagnac Effect in Rotating Frames: the rotating Earth, the time difference around a loop, ring lasers, ranging corrections and measurement."""
CODE = "navigation5_sagnac"
BOOK = {
    "title": "The Sagnac Effect in Rotating Frames",
    "subtitle": "How rotation shows up in light travelling around a loop, and why navigation must allow for it",
    "chapters": [
        ("The rotating Earth", "The Earth turns, and so does any frame fixed to it. Measurements made on the turning Earth can show effects that depend on the rotation. The Sagnac effect is one of these."),
        ("The time difference around a loop", "Send two light beams around a loop in opposite directions. On a turning loop the beams take slightly different times to come back. That difference is the Sagnac effect."),
        ("Ring lasers", "A ring laser gyroscope uses this effect to sense rotation. Two laser beams travel the loop in opposite directions. The difference in their frequencies shows how fast the loop is turning."),
        ("The correction in ranging", "Satellite ranging must account for the Sagnac effect. Signals travel through a frame that is turning with the Earth. Ignoring the effect would leave an error in the calculated position."),
        ("Navigation consequences", "Navigation systems that ignore the Sagnac effect can make mistakes in position and time. The correction is part of standard processing. Inertial navigators also rely on it."),
        ("Measuring it", "Michelson and Gale measured the effect in 1925 using a large loop of pipes laid around a field. Modern ring lasers measure it with great precision. The results agree with the theory."),
    ],
    "test": [
        ("What does the Sagnac effect depend on?", [("a", "The colour of the light"), ("b", "The length of a song"), ("c", "The price of the laser"), ("d", "The rotation of the loop")], "d"),
        ("In a ring laser gyroscope, what does the difference in frequency show?", [("a", "How fast the loop turns"), ("b", "The paint"), ("c", "The date"), ("d", "The weight")], "a"),
        ("Why must satellite ranging include the Sagnac correction?", [("a", "Satellites are painted"), ("b", "It removes the need for antennas"), ("c", "Signals travel in a turning frame, so ignoring it leaves errors"), ("d", "It lowers the cost of fuel")], "c"),
        ("Who measured the effect in 1925?", [("a", "Galileo and Kepler"), ("b", "Michelson and Gale"), ("c", "Newton and Halley"), ("d", "Tycho and Copernicus")], "b"),
        ("What happens when two light beams go round a turning loop in opposite directions?", [("a", "They take slightly different times to come back"), ("b", "They always return at the same instant"), ("c", "They never return"), ("d", "They stop")], "a"),
    ],
}
