"""Subsea Pipelines and Free Spans: seabed pipes, free span vibration, buckling, thermal expansion and burial."""
CODE = "engineering5_subsea_pipe"
BOOK = {
    "title": "Subsea Pipelines and Free Spans",
    "subtitle": "Pipes on the seabed, vibration, buckling and burial",
    "chapters": [
        ("Laying a pipe on the seabed",
         "A subsea pipeline carries oil, gas or water along the bottom of the sea. It is laid in long sections, joined on a vessel, and lowered to the seabed. Its route is chosen with care to avoid rough ground where it could be damaged."),
        ("Free spans",
         "Uneven seabed can leave a length of pipe hanging unsupported, which is called a free span. Current flowing past the pipe can make a free span vibrate. Engineers measure the span length and the flow to check that the vibration stays within safe limits."),
        ("Buckling",
         "Hot oil in a pipe makes the steel want to grow longer. Because the pipe is held by the seabed, that growth pushes against the soil and can cause the pipe to buckle sideways or upward. Designers limit this by controlling temperature and by setting the pipe's route."),
        ("Thermal expansion",
         "Steel expands when it gets hotter and shrinks when it cools. In a long pipe the change in length can be large, so the design must allow for it. Expansion loops, anchors and burial all help the pipe handle the movement."),
        ("Burial",
         "Burying a pipe in a trench protects it from fishing gear, anchors and currents. Burial also holds the pipe down and steadies it against buckling. The trench and the backfill are chosen to suit the soil."),
        ("Keeping the pipe safe",
         "Operators survey pipelines with sensors and inspection vehicles to find spans, exposed sections and damage. Each finding is ranked by risk and fixed in a planned order. Records of every survey help the operator decide when to act."),
    ],
    "test": [
        ("What does a subsea pipeline carry?",
         [("a", "Oil, gas or water along the seabed"), ("b", "Sand for the beaches"), ("c", "Electricity for towns"), ("d", "Air for divers")], "a"),
        ("What is a free span?",
         [("a", "A type of valve"), ("b", "A test for steel strength"), ("c", "A part of a pipe hanging unsupported over uneven seabed"), ("d", "A fishing net")], "c"),
        ("What can cause a pipe to buckle?",
         [("a", "Cold seawater alone"), ("b", "Heat that makes the steel expand against the seabed"), ("c", "Too much paint"), ("d", "Light from the surface")], "b"),
        ("What does burying a pipe protect it from?",
         [("a", "Fishing gear, anchors and currents"), ("b", "Sunlight"), ("c", "Being too heavy"), ("d", "Radio signals")], "a"),
        ("Why are survey records kept?",
         [("a", "To decorate the control room"), ("b", "To help the operator rank risks and plan repairs"), ("c", "To replace the crew"), ("d", "To count fish")], "b"),
    ],
}
