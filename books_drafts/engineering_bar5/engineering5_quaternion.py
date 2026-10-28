"""Rotations, Quaternions and Attitude Math: how a body's orientation in space is described, why quaternions are used, and the trap of gimbal lock."""
CODE = "engineering5_quaternion"
BOOK = {
    "title": "Rotations, Quaternions and Attitude Math",
    "subtitle": "Describing which way a body points, and doing it without getting stuck",
    "chapters": [
        ("Attitude", "Attitude means the orientation of a body in space. A satellite, an aircraft and a camera gimbal all need to know their attitude. Engineers describe it with rotation matrices, Euler angles or quaternions."),
        ("Euler angles", "Euler angles give the orientation as three turns, one after another, about three axes. They are easy to picture. They have one serious weakness, which is gimbal lock."),
        ("Gimbal lock", "When the middle angle reaches 90 degrees, two of the three turning axes line up. One degree of freedom is lost, and the other two turns cancel each other out. The calculation then becomes unstable near that position."),
        ("Quaternions", "A quaternion is a set of four numbers, with a unit length, that describes a rotation. It has no gimbal lock. Combining two rotations is simple multiplication, and it avoids the trigonometry of matrices."),
        ("Smooth interpolation", "To turn smoothly from one orientation to another, engineers use spherical linear interpolation, called slerp. It moves along the shortest path at a steady rate. Euler angles can take a longer, uneven path."),
        ("Using them in practice", "Most flight and game software stores attitude as a quaternion and shows it as Euler angles. Small errors build up over time, so the quaternion is normalised again after each step. This keeps the orientation valid."),
    ],
    "test": [
        ("What does attitude mean?", [("a", "The mood of the crew"), ("b", "The speed of a motor"), ("c", "The weight of a part"), ("d", "The orientation of a body in space")], "d"),
        ("What is gimbal lock?", [("a", "A lock that holds a door shut"), ("b", "Loss of a degree of freedom when two turning axes line up"), ("c", "A fault in the battery"), ("d", "A method of painting metal")], "b"),
        ("How many numbers does a quaternion use to describe a rotation?", [("a", "One"), ("b", "Two"), ("c", "Three"), ("d", "Four")], "d"),
        ("What is slerp used for?", [("a", "Cutting metal sheets"), ("b", "Counting packets of data"), ("c", "Smooth interpolation between two orientations"), ("d", "Charging batteries")], "c"),
        ("Why is a quaternion normalised after each step?", [("a", "To keep it a valid rotation as small errors build up"), ("b", "To change its colour"), ("c", "To make it heavier"), ("d", "To stop it being stored")], "a"),
    ],
}
