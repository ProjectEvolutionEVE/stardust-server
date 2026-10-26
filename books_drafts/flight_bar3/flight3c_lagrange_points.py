"""Lagrange Points: five balanced parking spots where two large bodies' pulls cancel out for a small craft."""
CODE = "flight3c_lagrange_points"
BOOK = {
    "title": "Lagrange Points",
    "subtitle": "Five places where the pulls of two big bodies balance, and where some craft sit",
    "chapters": [
        ("Two pulls, one spot",
         "A small craft near two large bodies, such as the Sun and the Earth, feels a pull from each. In a few special places, the two pulls and the craft's own motion round the Sun balance out. A craft placed there can stay in step with both bodies. These places are called Lagrange points."),
        ("Five points",
         "Each pair of large bodies has five Lagrange points, usually numbered L1 to L5. Three lie in a line with the two bodies, and two form a triangle with them, one ahead of the smaller body on its orbit and one behind."),
        ("Parking for watchers",
         "The Sun-Earth point L1 lies between the two, and sun-watching spacecraft use it because they have a clear view of the Sun. The point L2 lies on the far side of the Earth from the Sun. Space telescopes use L2 for a steady, cool view of the sky."),
        ("Not quite still",
         "The balance at L1 and L2 is unstable, so a craft drifts away from it over time. It must make small corrections to stay near the point. These are like station keeping, but they are small, and they are needed regularly."),
        ("Fuel and time",
         "Staying near a Lagrange point needs far less fuel than staying in a close planet orbit, so it is a cheap place to park for years. The costs are the regular small burns and the long trip out to reach it. Those costs belong in the budget from the start."),
        ("A pilot's use",
         "A Lagrange point is a good place to wait and watch. Plan the trip there, count the small corrections, and keep the fuel budget in mind before you settle in. A parking spot that costs little to keep is still not free to reach."),
    ],
    "test": [
        ("How many Lagrange points does a pair of large bodies have?",
         [("a", "Two"), ("b", "Three"), ("c", "Five"), ("d", "Ten")], "c"),
        ("Which Lagrange point do sun-watching craft often use?",
         [("a", "L1, between the Sun and the Earth"), ("b", "L4, behind Mars"), ("c", "L5, beyond Pluto"), ("d", "The surface of the Moon")], "a"),
        ("Why does a craft near L2 need small corrections?",
         [("a", "Its engines are switched off"), ("b", "It is caught in a storm"), ("c", "The Sun is too close"), ("d", "Its balance is unstable, so it drifts")], "d"),
        ("Why are space telescopes often placed at L2?",
         [("a", "It is right next to Mars"), ("b", "It is on the far side of the Earth from the Sun"), ("c", "It is always in daylight"), ("d", "It has air to breathe")], "b"),
        ("What is the main cost of staying at a Lagrange point?",
         [("a", "A large amount of fuel every day"), ("b", "Little fuel, plus regular small burns and the trip out"), ("c", "A constant leak of air"), ("d", "Nothing at all")], "b"),
    ],
}
