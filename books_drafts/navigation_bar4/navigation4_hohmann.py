"""The Hohmann transfer: moving between circular orbits with two burns along an elliptical path, with delta-v, timing and phase angle."""
CODE = "navigation4_hohmann"
BOOK = {
    "title": "The Hohmann Transfer",
    "subtitle": "Two burns and an ellipse",
    "chapters": [
        ("Changing orbits with two burns", "Moving a spacecraft from one circular orbit to another can be done with two engine burns. The Hohmann transfer uses an elliptical path that touches both orbits. It is one of the most efficient simple methods."),
        ("The transfer ellipse", "The transfer ellipse starts at the lower orbit and ends at the higher one. The first burn raises the far side of the ellipse. The second burn makes the new orbit circular."),
        ("Delta-v", "Delta-v is the change in speed that each burn provides. The two burns together give the total cost of the transfer. The fuel needed depends on this total."),
        ("Timing", "The spacecraft and its target must be in the right place when the second burn arrives. The timing depends on the orbits involved. Missing the window means waiting for the next one."),
        ("The phase angle", "The phase angle is the position of the target when the first burn starts. It must be right for the transfer to meet the target. Planners calculate it carefully."),
        ("Limits", "The Hohmann transfer is slow, since it takes half an orbit of the transfer ellipse. It assumes simple circular orbits and instant burns. Real missions adjust it for these limits."),
    ],
    "test": [
        ("How many burns does a basic Hohmann transfer use?", [("a", "Two"), ("b", "One"), ("c", "Three"), ("d", "Ten")], "a"),
        ("What shape is the transfer path?", [("a", "A straight line to the Sun"), ("b", "A spiral that never ends"), ("c", "A square loop"), ("d", "An ellipse touching both orbits")], "d"),
        ("What is delta-v?", [("a", "The distance to the Moon"), ("b", "The change in speed given by a burn"), ("c", "The number of crew aboard"), ("d", "The colour of the engine")], "b"),
        ("What is the phase angle?", [("a", "The angle of the solar panels"), ("b", "The tilt of the launch pad"), ("c", "The position of the target at the start of the first burn"), ("d", "The angle of the fuel tank")], "c"),
        ("What is a real limit of the simple Hohmann transfer?", [("a", "It works only near the Moon"), ("b", "It assumes circular orbits and instant burns"), ("c", "It needs no fuel at all"), ("d", "It can be flown only at night")], "b"),
    ],
}
