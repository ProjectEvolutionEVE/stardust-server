"""Lagrangian Mechanics for Machines: writing the motion of a machine from its energy, with the kinetic and potential energy as the starting point."""
CODE = "engineering5_lagrange"
BOOK = {
    "title": "Lagrangian Mechanics for Machines",
    "subtitle": "Describing motion through energy, with generalised coordinates",
    "chapters": [
        ("The idea", "The Lagrange method describes a machine by its energy rather than by each force. It uses a small set of coordinates that fully describe the position of the machine. Often these are angles or distances that the machine can actually move through."),
        ("Generalised coordinates", "A generalised coordinate is any quantity that sets the position of the machine. A simple pendulum needs only one, the angle. A double pendulum needs two. Choosing good coordinates keeps the equations short."),
        ("Kinetic and potential energy", "Kinetic energy T is the energy of motion. Potential energy V is the energy stored by position, such as height or the stretch of a spring. The Lagrangian is L, which equals T minus V."),
        ("The equations of motion", "For each coordinate, the Euler-Lagrange equation says that the rate of change of the momentum conjugate to it equals the sum of the outside forces acting along it. Written out, it gives one equation for each coordinate. Solving these gives the motion."),
        ("Constraints", "A constraint, such as a rod that must stay a fixed length, can be built into the choice of coordinates. This removes the constraint force from the calculation, which is a strength of the method. Constraints that cannot be built in require extra terms."),
        ("Why engineers use it", "The method is systematic. The same recipe works for a robot arm, a rotor or a vehicle suspension. Once the energy is known, the equations follow with fewer steps and fewer mistakes than force-based methods."),
    ],
    "test": [
        ("What is the Lagrangian L equal to?", [("a", "T minus V"), ("b", "T plus V"), ("c", "T times V"), ("d", "V divided by T")], "a"),
        ("What is a generalised coordinate?", [("a", "The colour of the machine"), ("b", "The price of a part"), ("c", "A fixed measurement of the room"), ("d", "Any quantity that sets the position of the machine")], "d"),
        ("What does kinetic energy T measure?", [("a", "Energy stored by height"), ("b", "Energy of motion"), ("c", "Heat in the air"), ("d", "Electrical charge")], "b"),
        ("How many coordinates does a simple pendulum need?", [("a", "None"), ("b", "Two"), ("c", "Ten"), ("d", "One, the angle")], "d"),
        ("Why can a constraint be built into the coordinates?", [("a", "So the machine becomes heavier"), ("b", "So the energy becomes zero"), ("c", "So the constraint force is removed from the calculation"), ("d", "So the equations need no solving")], "c"),
    ],
}
