"""The Hohmann Transfer: the classic two-burn path between two circular orbits, and why it is so useful."""
CODE = "flight4_hohmann"
BOOK = {
    "title": "The Hohmann Transfer",
    "subtitle": "The classic two-burn path between orbits",
    "chapters": [
        ("Moving between orbits", "A craft in one circular orbit cannot simply move to a bigger circle. It must change its speed, and the change must be done in the right places. Walter Hohmann, a German engineer, described the most economical two-burn way to do this in 1925."),
        ("The transfer ellipse", "The path is half an ellipse. Its low point touches the inner orbit and its high point touches the outer orbit. A craft that flies this half ellipse coasts from one orbit to the other with no engine running in between."),
        ("The two burns", "The first burn happens at the low point and raises the high point of the new ellipse up to the outer orbit. The second burn happens at the high point and makes the path circular at the new height. Each burn pushes in the direction the craft is already moving."),
        ("Transfer time", "The trip takes half the time of a full lap of the transfer ellipse. Going from low Earth orbit to the Moon's distance takes several days along a path of this kind. The longer the journey, the longer the coast between burns."),
        ("Why it is cheapest for circles", "For a move between two circular orbits in the same plane, the Hohmann path needs the least total change in speed when the outer orbit is less than about twelve times the inner orbit's distance. That saving is why it is taught first."),
        ("Limits and real uses", "Real burns take time and are never instant, and the orbits are rarely perfect circles in one plane. Still, the Hohmann transfer is the starting plan for many missions, from moving satellites up to the high orbit used for communications to planning trips to other planets."),
    ],
    "test": [
        ("How many burns does a basic Hohmann transfer use?", [("a", "One"), ("b", "Three"), ("c", "Two"), ("d", "Ten")], "c"),
        ("Where does the first burn happen?", [("a", "At the low point of the transfer ellipse"), ("b", "At the high point of the transfer ellipse"), ("c", "Far outside the Solar System"), ("d", "Halfway along the transfer")], "a"),
        ("How long does the coast on a Hohmann transfer last compared with a full lap of the ellipse?", [("a", "The same time"), ("b", "Twice as long"), ("c", "A quarter of the time"), ("d", "Half the time")], "d"),
        ("For circular orbits in one plane, what does the Hohmann path usually give?", [("a", "The most total speed change"), ("b", "The least total speed change for most ratios of orbit size"), ("c", "No speed change at all"), ("d", "A path that never reaches the outer orbit")], "b"),
        ("Which is a limit of the Hohmann plan?", [("a", "It only works around the Sun"), ("b", "It needs no engine"), ("c", "Real burns are never instant"), ("d", "It cannot move a craft to a bigger orbit")], "c"),
    ],
}
