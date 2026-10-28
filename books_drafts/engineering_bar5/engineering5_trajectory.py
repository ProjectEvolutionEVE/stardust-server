"""Trajectory Generation: polynomial and spline paths, velocity and jerk limits, path blending and smoothness."""
CODE = "engineering5_trajectory"
BOOK = {
    "title": "Trajectory Generation: Splines and Time Scaling",
    "subtitle": "Smooth paths, speed limits and joining moves together",
    "chapters": [
        ("Path and timing",
         "A path says where the robot must go. A trajectory adds when it must be there. Together they tell the arm the exact position, speed and acceleration at every moment of a move."),
        ("Polynomial paths",
         "A polynomial is a smooth curve described by a few numbers. A cubic polynomial can join two positions with set speeds at each end. Engineers use these curves because they are simple to compute and smooth to follow."),
        ("Velocity and jerk limits",
         "Every motor has a top speed. Jerk is the rate at which acceleration changes, and a high jerk shakes the arm and wears its parts. Good trajectories keep both speed and jerk inside their limits."),
        ("Time scaling",
         "Time scaling changes how fast a path is followed without changing its shape. A path can be run slowly for care or quickly for speed. Scaling the time is an easy way to fit a move inside the limits."),
        ("Path blending",
         "A task often has many moves in a row. Stopping fully at every point wastes time and adds shock. Path blending joins two segments with a smooth curve, so the arm flows from one to the next."),
        ("Smoothness in practice",
         "A smooth trajectory is quieter, kinder to the machine and more accurate. Engineers check the speed, acceleration and jerk plots before a motion runs. A little extra time often buys much smoother motion."),
    ],
    "test": [
        ("What is a trajectory in robotics?",
         [("a", "A type of gripper"), ("b", "A camera mount"), ("c", "A path with timing that says where the robot is at each moment"), ("d", "A brake")], "c"),
        ("What does a jerk limit control?",
         [("a", "How quickly the acceleration itself changes"), ("b", "The colour of the arm"), ("c", "The price per move"), ("d", "The number of joints")], "a"),
        ("Why are smooth polynomial or spline paths used?",
         [("a", "To make the robot louder"), ("b", "To cut paint"), ("c", "To save ink"), ("d", "To cut sudden changes that cause vibration and wear")], "d"),
        ("What is time scaling?",
         [("a", "Changing the clock on the wall"), ("b", "Changing how fast a path is followed while keeping its shape"), ("c", "Painting a timeline"), ("d", "A safety switch")], "b"),
        ("What does path blending do?",
         [("a", "Mixes paint"), ("b", "Stops the robot at every point"), ("c", "Joins two path segments smoothly without a full stop"), ("d", "Adds weight")], "c"),
    ],
}
