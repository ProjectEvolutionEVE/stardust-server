"""Rendezvous and docking: phasing orbits, closing rates, approach corridors, relative navigation and safety margins."""
CODE = "navigation4_rendezvous"
BOOK = {
    "title": "Rendezvous and Docking",
    "subtitle": "Closing in on another craft in orbit",
    "chapters": [
        ("Meeting in orbit", "Rendezvous is the act of bringing two spacecraft together in orbit. It takes careful planning because both craft are moving very fast. Docking is the final join."),
        ("Phasing orbits", "Phasing orbits adjust the timing so that one craft catches up with another. A craft in a different orbit can be sped up or slowed to change its place. These changes must be planned carefully."),
        ("Closing rates", "The closing rate is how fast the two craft move toward each other. It is kept small near the target. A slow final approach gives time to correct any error."),
        ("The approach corridor", "The approach corridor is a planned path the chasing craft follows toward its target. Staying inside it keeps the craft clear of the target. Leaving the corridor calls for a correction."),
        ("Sensors and relative navigation", "Relative navigation measures the position of one craft against the other. Sensors include cameras, lidar and radar-type tools. The data guide the final approach."),
        ("Safety margins", "Safety margins leave room for errors at every stage. A close approach with little margin is risky. Good planners build in large margins."),
    ],
    "test": [
        ("What does rendezvous mean in orbit?", [("a", "Splitting one craft into two"), ("b", "Painting a craft in flight"), ("c", "Bringing two spacecraft together"), ("d", "Counting the stars")], "c"),
        ("What do phasing orbits adjust?", [("a", "The timing of one craft so it catches another"), ("b", "The colour of the craft"), ("c", "The menu for the crew"), ("d", "The name of the mission")], "a"),
        ("What is the closing rate?", [("a", "The speed of sound on the craft"), ("b", "The number of windows in a hatch"), ("c", "The price of fuel"), ("d", "How fast two craft move toward each other")], "d"),
        ("What is the approach corridor?", [("a", "A hallway inside the craft"), ("b", "A planned path the chasing craft follows toward its target"), ("c", "A list of ground stations"), ("d", "A radio channel")], "b"),
        ("Why is a slow final approach used?", [("a", "It saves paint"), ("b", "It keeps the crew awake"), ("c", "It gives time to correct any error"), ("d", "It makes the craft invisible")], "c"),
    ],
}
