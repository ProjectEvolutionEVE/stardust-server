"""Grippers and End-Effector Design: grip force, finger geometry, vacuum grippers, compliance and tool changers."""
CODE = "engineering5_gripper"
BOOK = {
    "title": "Grippers and End-Effector Design",
    "subtitle": "Holding, releasing and handing over parts",
    "chapters": [
        ("What an end-effector is",
         "The end-effector is the tool at the tip of a robot arm. A gripper is the most common kind. Its job is to hold a workpiece firmly, carry it, and release it at the right place."),
        ("Grip force",
         "A gripper must press with enough force to hold the part, but not so much that it crushes it. The needed force depends on the weight, the speed of the motion and the friction between the fingers and the part. Engineers add a safety margin."),
        ("Finger geometry",
         "The shape of the fingers decides how the part sits in the grip. Fingers that match the shape of the part hold it securely. Designers also think about how easily the fingers can reach into tight spaces."),
        ("Vacuum grippers",
         "A vacuum gripper uses a cup and a pump to lower the air pressure inside, so the outside air presses the part against the cup. It suits flat, smooth parts such as sheets and boxes. A leak in the seal reduces the hold."),
        ("Compliance",
         "Compliance lets the gripper give a little when it meets a part that is slightly out of place. This makes the grip gentler and tolerates small errors in position. Soft fingers and springs are common ways to add it."),
        ("Tool changers",
         "A tool changer lets a robot swap grippers or other tools automatically. A master plate on the arm locks to a tool plate on the tool. This saves time and lets one robot do many jobs."),
    ],
    "test": [
        ("What does a gripper do?",
         [("a", "Paints the part"), ("b", "Measures its colour"), ("c", "Stores it in a box"), ("d", "Holds and releases a workpiece")], "d"),
        ("What does friction affect in a gripper?",
         [("a", "The paint finish"), ("b", "The grip force a gripper can hold without slipping"), ("c", "The cable length"), ("d", "The weight of the box")], "b"),
        ("What is a vacuum gripper's hold based on?",
         [("a", "A pressure difference between the inside of the cup and the air outside"), ("b", "Magnets only"), ("c", "Glue"), ("d", "Wind")], "a"),
        ("What is a tool changer?",
         [("a", "A paint roller"), ("b", "A timer"), ("c", "A device that lets a robot swap its tools automatically"), ("d", "A cable")], "c"),
        ("What does compliance in a gripper do?",
         [("a", "Makes it glow"), ("b", "Makes it heavy"), ("c", "Stops all motion"), ("d", "Lets parts give a little, so the grip is gentler and tolerates small misalignment")], "d"),
    ],
}
