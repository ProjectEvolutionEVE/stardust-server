"""The Principle of Least Action and Lagrangian Mechanics: a different, powerful way to describe how things move, and when it is the simpler path."""
CODE = "science4_phys_lagrangian"
BOOK = {
    "title": "The Principle of Least Action and Lagrangian Mechanics",
    "subtitle": "A powerful way to describe motion, from energy rather than force",
    "chapters": [
        ("Least action",
         "The principle of least action says a system moves along the path that makes its action a minimum, or more precisely a stationary value. The action is the time integral of the Lagrangian, which is kinetic energy minus potential energy. The principle gives the same results as Newton’s laws."),
        ("Generalised coordinates",
         "Generalised coordinates are any set of variables that fix the position of a system. They can be angles, distances along a track, or combinations of both. Choosing good coordinates can make a hard problem much simpler."),
        ("Euler-Lagrange equations",
         "Applying the principle of least action gives the Euler-Lagrange equations. For each coordinate, they link the change in the Lagrangian with respect to that coordinate to the rate of change of its momentum. Solving them gives the motion of the system."),
        ("Symmetries",
         "Noether’s theorem shows that every continuous symmetry of a system gives a conserved quantity. A system that looks the same under shifts in time gives conserved energy, and one that looks the same under shifts in space gives conserved momentum. This link is one of the deepest in physics."),
        ("Pendulum and orbit examples",
         "A simple pendulum can be solved neatly using the angle as the coordinate, with energy as the starting point. Orbits in a central force field are also easy to describe this way. The method works well when constraints are present."),
        ("When Newton is simpler",
         "For a single particle in a simple force, Newton’s second law is often the quickest route. The Lagrangian method shines when there are constraints, many coupled parts, or a need for clean symmetry arguments. Good physicists choose the method that fits the problem."),
    ],
    "test": [
        ("What does the principle of least action describe?",
         [("a", "A system never moves"), ("b", "A system always moves in a circle"), ("c", "A system moves along the path that makes its action stationary"), ("d", "A system loses all its energy")], "c"),
        ("How is the Lagrangian defined?",
         [("a", "Kinetic energy plus potential energy only"), ("b", "Mass times the square of the speed"), ("c", "Force times distance"), ("d", "Kinetic energy minus potential energy")], "d"),
        ("What does Noether’s theorem link?",
         [("a", "Continuous symmetries and conserved quantities"), ("b", "Colours and sounds"), ("c", "Mass and volume"), ("d", "Temperature and pressure")], "a"),
        ("What is a set of generalised coordinates?",
         [("a", "A grid painted on a floor"), ("b", "Any variables that fix the position of the system"), ("c", "Only straight-line distances"), ("d", "A list of prices")], "b"),
        ("When is Newton’s method often the quickest route?",
         [("a", "For a single particle in a simple force"), ("b", "Only for systems with many constraints"), ("c", "Only for light"), ("d", "Never")], "a"),
    ],
}
