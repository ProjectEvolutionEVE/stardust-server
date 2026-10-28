"""Collaborative Robot Safety Standards: speed and separation monitoring, power and force limiting, risk assessment and safeguards."""
CODE = "engineering5_cobot_safety"
BOOK = {
    "title": "Collaborative Robot Safety Standards",
    "subtitle": "Robots that work beside people, and the rules that keep them safe",
    "chapters": [
        ("What a cobot is",
         "A collaborative robot, or cobot, is designed to work in the same space as people. Unlike a robot in a locked cage, it may share the work area with a worker. That makes safety design the heart of the job."),
        ("Speed and separation monitoring",
         "This method watches the distance between the robot and any person nearby. As a person gets closer, the robot slows, and it stops if the gap becomes too small. Sensors such as laser scanners or cameras supply the distance readings."),
        ("Power and force limiting",
         "This method keeps the energy and contact force of the robot below levels that could injure a person. The robot may be built with soft covers and limited power. The aim is that even a contact is not harmful."),
        ("Risk assessment",
         "A risk assessment lists the hazards of the robot and its task. For each hazard, the team estimates how likely and how serious harm would be. It then chooses safeguards that bring the risk down to an acceptable level."),
        ("Safeguards",
         "Safeguards include guards, light curtains, safety-rated stops and clear signs on the floor. Some are built into the robot and others are placed around it. Safeguards are chosen from the risk assessment, not guessed."),
        ("The standards",
         "The main standards for robot safety include ISO 10218, parts 1 and 2, for industrial robots and collaborative operation. The guidance once given in ISO/TS 15066 was folded into the 2025 edition of ISO 10218. These documents describe the methods and the limits that designers and users must consider. Compliance is shown through testing and records."),
    ],
    "test": [
        ("What is a collaborative robot?",
         [("a", "A robot in a locked cage only"), ("b", "A robot that paints"), ("c", "A robot designed to work alongside people in a shared space"), ("d", "A robot that calculates tax")], "c"),
        ("What does speed and separation monitoring do?",
         [("a", "Slows or stops the robot as a person gets closer"), ("b", "Counts the bolts"), ("c", "Sets the colour of the lights"), ("d", "Times the lunch break")], "a"),
        ("What does power and force limiting aim to do?",
         [("a", "Make the robot stronger"), ("b", "Make the robot heavier"), ("c", "Turn the robot off forever"), ("d", "Keep contact forces below levels that can injure a person")], "d"),
        ("What does a risk assessment do?",
         [("a", "Chooses the paint"), ("b", "Identifies hazards and decides which safeguards reduce the risk"), ("c", "Counts the crew"), ("d", "Sets the price")], "b"),
        ("Which standard covers collaborative robot operation?",
         [("a", "ISO 9001"), ("b", "ISO 14001"), ("c", "ISO 10218 (parts 1 and 2)"), ("d", "ISO 27001")], "c"),
    ],
}
