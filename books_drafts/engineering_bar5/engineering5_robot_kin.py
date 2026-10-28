"""Robot Kinematics: Denavit-Hartenberg parameters, link frames, transformation matrices, forward kinematics and joint limits."""
CODE = "engineering5_robot_kin"
BOOK = {
    "title": "Robot Kinematics: Denavit-Hartenberg Parameters",
    "subtitle": "Link frames, transforms and where the arm's tip ends up",
    "chapters": [
        ("Links and joints",
         "A robot arm is a chain of rigid links joined by joints. Each joint turns or slides, and each link carries the next one. Kinematics is the study of how these motions place the tip of the arm in space, without asking what forces cause them."),
        ("Link frames",
         "Engineers attach a coordinate frame to each link. A frame is a small set of three axes that marks a point and a direction. Once every link has a frame, the position of each one can be described in a common way."),
        ("Denavit-Hartenberg parameters",
         "The Denavit-Hartenberg convention describes each link with four numbers. Two describe the link's length and twist, and two describe the offset and the joint's angle. With these four numbers for every joint, the whole arm can be written down in one standard form."),
        ("Transformation matrices",
         "A transformation matrix packs a position and an orientation into one grid of numbers. Multiplying the matrices in order moves you from the base of the arm out to the tip. Each matrix is simple, and the chain of them describes the whole arm."),
        ("Forward kinematics",
         "Forward kinematics takes the joint angles and works out where the tip ends up. It is a direct calculation, with one answer for each set of joint angles. Controllers use it to check where the arm is right now."),
        ("Joint limits",
         "Every joint can turn only so far before it hits a stop or strains its parts. Joint limits are the smallest and largest angles the joint may safely reach. Good software keeps every planned motion inside these limits."),
    ],
    "test": [
        ("How many parameters does the standard Denavit-Hartenberg convention use for each link?",
         [("a", "Two"), ("b", "Three"), ("c", "Five"), ("d", "Four")], "d"),
        ("What does forward kinematics calculate?",
         [("a", "The joint angles needed for a target"), ("b", "The tip position from the joint angles"), ("c", "The motor voltage"), ("d", "The weight of the arm")], "b"),
        ("What is a transformation matrix used for?",
         [("a", "Describing the position and orientation of one frame relative to another"), ("b", "Storing photographs"), ("c", "Measuring sound"), ("d", "Paying the crew")], "a"),
        ("What are joint limits?",
         [("a", "Speed limits for the crew"), ("b", "Price limits for parts"), ("c", "The smallest and largest angles a joint can safely reach"), ("d", "The weight limit of the room")], "c"),
        ("What is a link frame?",
         [("a", "A sheet of metal"), ("b", "A picture on the wall"), ("c", "A window in the cab"), ("d", "A coordinate frame attached to each link")], "d"),
    ],
}
