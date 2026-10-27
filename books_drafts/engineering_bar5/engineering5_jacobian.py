"""The Jacobian: joint-to-tip velocity and force mapping, singularities and manipulability for robot arms."""
CODE = "engineering5_jacobian"
BOOK = {
    "title": "The Jacobian: Velocities and Forces in Robots",
    "subtitle": "How joint speeds become tip speeds, and how forces map back",
    "chapters": [
        ("What the Jacobian is",
         "The Jacobian is a table of numbers that links the speeds of the joints to the speed of the tip. It changes as the arm moves, because the arm's shape changes. Each position of the arm has its own Jacobian."),
        ("Joint speed to tip speed",
         "If you know how fast each joint turns, the Jacobian tells you how fast the tip moves. Controllers use this to plan smooth moves in straight lines or curves. It turns a plan in joint space into a plan in the world."),
        ("Static force mapping",
         "When the tip pushes on something and the arm holds still, the joints must provide torques. The Jacobian's transpose maps the tip force into those joint torques. Engineers use this to check that the motors can hold a load."),
        ("Singularities",
         "A singularity is a pose where the Jacobian loses rank. At such a pose the arm cannot move the tip in some direction, however fast the joints turn. Near a singularity, small motions can require very large joint speeds."),
        ("Manipulability",
         "Manipulability is a measure of how easily the arm can move its tip in many directions from its current pose. A high value means the arm is well placed for the task. A low value warns that the arm is close to a singularity."),
        ("Using the Jacobian in practice",
         "Software checks the Jacobian throughout a motion and warns when the arm nears a singularity. Engineers use it to choose a good home pose and to size motors. It is one of the most useful tools in robot design."),
    ],
    "test": [
        ("What does the Jacobian relate?",
         [("a", "Joint speeds to the speed of the tip"), ("b", "Colour to light"), ("c", "Cost to time"), ("d", "Weight to paint")], "a"),
        ("What is a singularity?",
         [("a", "A famous robot"), ("b", "A fast motor"), ("c", "A pose where the arm loses the ability to move the tip in some direction"), ("d", "A type of gripper")], "c"),
        ("How are joint torques related to a force at the tip?",
         [("a", "They are unrelated"), ("b", "Through the transpose of the Jacobian"), ("c", "Through the price of steel"), ("d", "By the colour of the arm")], "b"),
        ("What does manipulability measure?",
         [("a", "The price of the robot"), ("b", "The noise level"), ("c", "The colour of the arm"), ("d", "How easily the arm can move its tip in many directions")], "d"),
        ("What is static force mapping useful for?",
         [("a", "Finding the joint torques needed to hold a force at the tip"), ("b", "Choosing paint"), ("c", "Counting bolts"), ("d", "Setting the clock")], "a"),
    ],
}
