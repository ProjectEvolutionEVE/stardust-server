"""Buckling as an Eigenvalue Problem: finding the loads at which a structure can first buckle."""
CODE = "engineering5_eigen_buckling"
BOOK = {
    "title": "Buckling as an Eigenvalue Problem",
    "subtitle": "Finding the loads at which a structure can first buckle",
    "chapters": [
        ("The buckling question",
         "Buckling asks at what load a structure can stay bent in a new shape, not just straight. The answer comes from checking when the stiffness of the structure becomes zero in some direction."),
        ("The eigenvalue formulation",
         "The buckling loads are the eigenvalues of an equation that combines the stiffness matrix with a geometric stiffness matrix. Each eigenvalue is a load multiplier, and the smallest one is the first buckling load."),
        ("Mode shapes",
         "Each eigenvector is a mode shape, the pattern in which the structure would buckle. The lowest mode is usually the one that governs the design first."),
        ("Geometric stiffness",
         "The geometric stiffness matrix captures how existing axial load changes the bending stiffness. Compression lowers it, and tension raises it."),
        ("Linear buckling analysis",
         "Software can run this as a quick check of the critical load in a single solve, without tracing the whole load path. It gives the answer for a perfect structure."),
        ("Its limits",
         "Linear buckling ignores imperfections and the nonlinear behaviour after buckling. It is an upper estimate, so the real strength may be lower and needs further checks."),
    ],
    "test": [
        ("What is the buckling question?",
         [("a", "What colour the structure is"), ("b", "At what load a structure can take a new bent shape"), ("c", "How much a bolt costs"), ("d", "How long the paint lasts")], "b"),
        ("What is each eigenvalue in a buckling analysis?",
         [("a", "A load multiplier"), ("b", "A paint colour"), ("c", "A steel grade"), ("d", "A date")], "a"),
        ("What does a mode shape show?",
         [("a", "The menu of a shop"), ("b", "Sound levels"), ("c", "The pattern in which the structure would buckle"), ("d", "The price")], "c"),
        ("What does compression do to bending stiffness in the geometric stiffness?",
         [("a", "Raises it"), ("b", "Lowers it"), ("c", "Leaves it unchanged always"), ("d", "Makes it infinite")], "b"),
        ("What is a limit of linear buckling analysis?",
         [("a", "It is too slow"), ("b", "It ignores imperfections and nonlinear behaviour after buckling"), ("c", "It needs no computer"), ("d", "It gives colours")], "b"),
    ],
}
