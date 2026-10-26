"""Spin Gravity: how a slowly turning craft can push people toward a floor, the trade of radius and spin rate, and the side effects to manage."""
CODE = "flight4_artificial_gravity"
BOOK = {
    "title": "Spin Gravity",
    "subtitle": "Making weight by turning, and the costs of doing it",
    "chapters": [
        ("The centrifugal feel", "When something turns, it pushes outward on whatever holds it in the circle. A spinning craft can push its crew toward the outer floor in the same way. The feeling is like weight, though it is not true gravity."),
        ("Radius and rate", "The feel depends on two things: the distance from the centre and the spin rate. A larger radius lets the craft spin more slowly and still give a comfortable feel. A small radius needs faster spin, and that is harder on the body."),
        ("Coriolis effects", "Moving inside a spinning craft causes odd forces. Turning the head can make the room seem to tilt or swing. These Coriolis effects are the main cause of discomfort in spin systems."),
        ("Nausea limits", "Studies suggest that spin rates above about two turns per minute are hard for many people to adapt to. A larger radius keeps the rate low, so designers aim for a big spinning ring."),
        ("Von Braun and Kubrick", "In the 1950s, the rocket engineer Wernher von Braun described a large spinning wheel for a space station. The film 2001 later showed a spinning ship with a rotating section, and both ideas shaped how people imagine artificial gravity."),
        ("Real studies", "Researchers have tested short-radius centrifuges on people for many years, to study how the body adapts. The results help designers choose the radius and the rate for future spinning craft. No large spinning station has flown yet."),
    ],
    "test": [
        ("What causes the feeling of weight in a spinning craft?", [("a", "A magnet in the floor"), ("b", "Outward push from the spin on whatever holds people in the circle"), ("c", "Heavy paint"), ("d", "The crew holding hands")], "b"),
        ("What must a designer do to keep the spin rate low?", [("a", "Use a larger radius"), ("b", "Use a smaller radius"), ("c", "Stop the craft from turning"), ("d", "Paint the walls")], "a"),
        ("What causes the odd feeling when turning the head in a spinning room?", [("a", "Hunger"), ("b", "A bad radio"), ("c", "Too much sunlight"), ("d", "Coriolis effects")], "d"),
        ("About what spin rate do studies suggest is hard for many people?", [("a", "Below one turn per hundred years"), ("b", "Exactly ten turns per second only"), ("c", "Above about two turns per minute"), ("d", "Any rate is easy")], "c"),
        ("Which person described a large spinning wheel for a space station in the 1950s?", [("a", "Isaac Newton"), ("b", "Wernher von Braun"), ("c", "Marie Curie"), ("d", "Johannes Gutenberg")], "b"),
    ],
}
