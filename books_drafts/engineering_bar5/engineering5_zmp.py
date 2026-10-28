"""Legged Robot Balance and Zero-Moment Point: centre of pressure, support polygons, balance control, gait generation and recovery from falls."""
CODE = "engineering5_zmp"
BOOK = {
    "title": "Legged Robot Balance and Zero-Moment Point",
    "subtitle": "Keeping a walking machine on its feet",
    "chapters": [
        ("The balance problem",
         "A walking robot is stable only while its weight and motion keep it from tipping over. Every step changes where its support is. Balance control keeps the robot's centre of mass over its feet as it moves."),
        ("Centre of pressure",
         "The centre of pressure is the point on the ground where the forces from the feet act overall. On flat ground with the feet flat, it is the same as the zero-moment point. Watching where the centre of pressure lies tells the controller how the robot is leaning."),
        ("Support polygons",
         "The support polygon is the area enclosed by the contact points of the feet on the ground. A robot stands securely while its balance point stays inside this area. Standing on one foot gives a small polygon and makes balance harder."),
        ("Balance control",
         "Balance control uses sensors to watch the robot's lean and motion. It moves the feet, hips and arms to keep the balance point inside the support polygon. Fast, small corrections keep a walking robot upright on uneven ground."),
        ("Gait generation",
         "Gait generation plans the sequence of foot motions that makes a walk. The plan sets when each foot lifts, where it lands and how the body moves between steps. A good gait looks natural and keeps the robot stable."),
        ("Recovery from falls",
         "Robots fall sometimes, so recovery must be designed in. A fall recovery plan aims to bring the robot's balance back into a safe state. Sometimes the safest choice is to lower the robot to the ground in a controlled way."),
    ],
    "test": [
        ("What is the zero-moment point?",
         [("a", "The point on the ground where the net tipping moment is zero"), ("b", "The start line"), ("c", "A brake setting"), ("d", "A camera point")], "a"),
        ("What is a support polygon?",
         [("a", "A painted square"), ("b", "A sports field"), ("c", "The area enclosed by the contact points of the feet on the ground"), ("d", "A menu")], "c"),
        ("When is a legged robot stable in the simple model?",
         [("a", "When it is painted"), ("b", "When the zero-moment point lies inside the support polygon"), ("c", "When it is cold"), ("d", "When it is tall")], "b"),
        ("What does gait generation produce?",
         [("a", "Paint patterns"), ("b", "Lunch times"), ("c", "Sounds"), ("d", "A planned sequence of foot motions for walking")], "d"),
        ("What must recovery from a fall aim to do?",
         [("a", "Bring the robot's balance back into a safe state"), ("b", "Paint it"), ("c", "Count the steps"), ("d", "Turn up the volume")], "a"),
    ],
}
