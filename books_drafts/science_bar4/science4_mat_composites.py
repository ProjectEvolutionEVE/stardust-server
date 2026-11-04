"""Composite Materials and Fibres: how strong fibres and a binding matrix share the load."""
CODE = "science4_mat_composites"
BOOK = {
    "title": "Composite Materials and Fibres",
    "subtitle": "Strong fibres in a matrix, and how the two work together",
    "chapters": [
        ("What a composite is", "A composite joins two or more materials that keep their own identities. In most composites, long fibres sit inside a matrix, a binder that holds them in place. The result can be far stronger than either part on its own."),
        ("The jobs of fibre and matrix", "The fibres carry most of the load, because they are stiff and strong along their length. The matrix spreads the load between fibres, protects them from damage and keeps them in shape. Good design gives each part a clear job."),
        ("The rule of mixtures", "For fibres lined up in one direction, a simple rule gives a first estimate of stiffness. It adds the fibre share of the volume times the fibre stiffness to the matrix share times the matrix stiffness. Real parts still need tests to confirm the numbers."),
        ("Carbon and glass fibres", "Carbon fibres are very stiff and light, and they are used in aircraft, racing cars and sports gear. Glass fibres cost less and are tougher, so they are common in boats, pipes and wind turbine blades. Each fibre suits a different budget and job."),
        ("Laminates and the interface", "A laminate stacks thin layers, called plies, with the fibres turned in different directions. The bond between fibre and matrix, the interface, decides how well the load passes between them. A weak interface lets the fibres pull out, and a strong one holds them firmly."),
        ("Testing composites", "Engineers test composites in tension, bending and shear, and they scan parts with ultrasound to find hidden gaps. Damage inside a composite can be hard to see, so testing is part of every serious design. Test results go back into the design."),
    ],
    "test": [
        ("In a fibre-reinforced composite, which part usually carries most of the load?",
         [("a", "The matrix"), ("b", "The fibres"), ("c", "The surface coating"), ("d", "The mould")], "b"),
        ("What does the rule of mixtures give a first estimate of?",
         [("a", "The colour of the composite"), ("b", "The price per kilogram"), ("c", "The number of plies in a laminate"), ("d", "The stiffness of a part with aligned fibres")], "d"),
        ("Which fibre is generally tougher and cheaper, and suited to boats and pipes?",
         [("a", "Glass fibre"), ("b", "Carbon fibre"), ("c", "Gold wire"), ("d", "Rubber thread")], "a"),
        ("What is a ply?",
         [("a", "A type of resin hardener"), ("b", "A tool for cutting fibres"), ("c", "A thin layer in a laminate"), ("d", "A test for porosity")], "c"),
        ("Why does a weak fibre-matrix interface matter?",
         [("a", "It makes the part lighter"), ("b", "It changes the colour of the part"), ("c", "It stops ultrasound scans working"), ("d", "The fibres can pull out, and the load does not pass across")], "d"),
    ],
}
