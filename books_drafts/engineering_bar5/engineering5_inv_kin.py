"""Inverse Kinematics and Redundancy: closed-form solutions, numerical solvers, redundant arms and joint limit handling."""
CODE = "engineering5_inv_kin"
BOOK = {
    "title": "Inverse Kinematics and Redundancy",
    "subtitle": "Finding joint angles for a wanted tip position",
    "chapters": [
        ("The reverse problem",
         "Inverse kinematics starts from a wanted tip position and asks which joint angles will reach it. It is the reverse of forward kinematics. Most real tasks are planned this way, because people specify where the tool should go."),
        ("Closed-form solutions",
         "For some arm designs, a direct formula gives all the joint angles at once. These closed-form solutions are fast and exact. Many common industrial arms have one, but not all do."),
        ("Numerical solvers",
         "When no direct formula exists, a numerical solver starts from a guess and improves it step by step. Each step uses the Jacobian to move closer to the target. Solvers can be slow, and they may settle on a poor answer if the guess is bad."),
        ("Redundant arms",
         "A redundant arm has more joints than the task needs. It can reach the same tip position in many different ways. The extra freedom lets the arm avoid obstacles, stay clear of its limits and keep a good posture."),
        ("Joint limit handling",
         "A solution is useless if it asks a joint to go beyond its limits. Solvers check each answer and steer away from limits when they can. Some methods score each posture and prefer those that keep joints near the middle of their range."),
        ("Choosing a method",
         "Engineers pick the method that matches the arm and the task. A closed-form answer suits a simple, fixed arm, while a solver suits a complex or redundant one. Testing the solution on the real arm is always the last step."),
    ],
    "test": [
        ("What does inverse kinematics find?",
         [("a", "The tip position from the joints"), ("b", "The joint angles that reach a wanted tip position"), ("c", "The weight of the arm"), ("d", "The colour of the motors")], "b"),
        ("What is a redundant arm?",
         [("a", "An arm that is broken"), ("b", "An arm with no joints"), ("c", "An arm that is painted twice"), ("d", "An arm with more joints than the task needs")], "d"),
        ("What is a numerical solver?",
         [("a", "A calculator for money"), ("b", "A paint mixer"), ("c", "An iterative method that repeatedly improves a guess for the joint angles"), ("d", "A safety light")], "c"),
        ("Why must joint limits be handled in inverse kinematics?",
         [("a", "So the solution stays within what the joints can physically reach"), ("b", "So the arm changes colour"), ("c", "So the arm is heavier"), ("d", "So the price is lower")], "a"),
        ("What is a closed-form solution?",
         [("a", "A guess"), ("b", "A direct formula that gives the joint angles without iteration"), ("c", "A paint process"), ("d", "A type of fuse")], "b"),
    ],
}
