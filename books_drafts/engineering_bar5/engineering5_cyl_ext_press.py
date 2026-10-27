"""Cylinder Buckling Under External Pressure: how a tube collapses when the pressure is on the outside."""
CODE = "engineering5_cyl_ext_press"
BOOK = {
    "title": "Cylinder Buckling Under External Pressure",
    "subtitle": "How a tube collapses when the pressure is on the outside",
    "chapters": [
        ("Pressure from outside",
         "A tube under outside pressure is squeezed inward. Unlike a tube with pressure inside, which is stretched, outside pressure can make the wall buckle and flatten."),
        ("Ovality",
         "A tube that is not perfectly round, which is called ovality, collapses at a lower pressure. Even small out-of-round shapes weaken it noticeably."),
        ("Ring stiffeners",
         "Rings fixed around the outside divide a long tube into shorter sections and raise the pressure it can take. They work by stiffening the wall against inward movement."),
        ("The critical pressure",
         "For a perfect long tube, the classic elastic buckling pressure depends on the wall thickness, the radius, and the material's stiffness and Poisson's ratio. Real tubes fall below this value because of imperfections."),
        ("Test rigs",
         "Engineers test tubes in pressure chambers to find the real collapse pressure. The results are used to check the formulas and to set safety margins."),
        ("Using the results",
         "A design should allow for imperfections and for scatter in test results. Check that the chosen wall and stiffeners give a clear margin above the working pressure."),
    ],
    "test": [
        ("What does outside pressure tend to do to a tube wall?",
         [("a", "Stretch it outward"), ("b", "Squeeze it inward so the wall may buckle"), ("c", "Heat it"), ("d", "Paint it")], "b"),
        ("What does ovality do to the collapse pressure?",
         [("a", "Raises it"), ("b", "Has no effect"), ("c", "Lowers it"), ("d", "Doubles it")], "c"),
        ("What do ring stiffeners do?",
         [("a", "Make the tube heavier with no benefit"), ("b", "Divide the tube into shorter sections and resist inward movement"), ("c", "Let the tube bend freely"), ("d", "Melt the wall")], "b"),
        ("What must real tube designs allow for?",
         [("a", "Nothing, the formula is always exact"), ("b", "Only the colour"), ("c", "The number of bolts"), ("d", "Imperfections and scatter in test results")], "d"),
        ("Why do engineers use test rigs for tubes?",
         [("a", "To test the paint"), ("b", "To find the real collapse pressure and check the formulas"), ("c", "To measure the weather"), ("d", "To count welds")], "b"),
    ],
}
