"""Large Deflection and Geometric Nonlinearity: when a structure moves so far that its own shape changes the answer."""
CODE = "engineering5_large_deflection"
BOOK = {
    "title": "Large Deflection and Geometric Nonlinearity",
    "subtitle": "When a structure moves so far that its own shape changes the answer",
    "chapters": [
        ("Small movements and big ones",
         "Simple beam formulas assume small movements, so the shape stays close to the original. When a structure moves a lot, its geometry changes how it carries the load, and the simple formulas no longer hold."),
        ("Stiffening and softening",
         "A tensioned membrane or cable can become stiffer as it stretches, which is stiffening. A slender column can lose stiffness as it bends under load, which is softening."),
        ("Stress stiffening",
         "Axial tension in a beam or plate raises its stiffness against bending. Axial compression does the opposite, lowering the stiffness until buckling appears."),
        ("Snap-through",
         "A shallow arch or dome can suddenly flip to a new shape when the load reaches a critical value. The load can drop or jump at that point, which a straight-line analysis would never show."),
        ("Cables",
         "A cable carries load only in tension and changes shape as it loads, so its stiffness depends on how far it has already moved. Bridges and masts rely on this behaviour and must be checked with it in mind."),
        ("When linear analysis fails",
         "Linear analysis assumes the shape stays the same and the response is proportional to the load. When the change in shape is large, use a nonlinear method that updates the geometry as the structure moves."),
    ],
    "test": [
        ("What assumption does simple linear analysis make about movement?",
         [("a", "That movement is large"), ("b", "That the shape stays close to the original"), ("c", "That the structure is made of glass"), ("d", "That the load is zero")], "b"),
        ("What is snap-through?",
         [("a", "A crack in glass"), ("b", "A nut that comes loose"), ("c", "A shallow arch that flips suddenly to a new shape at a critical load"), ("d", "A slow creep test")], "c"),
        ("What does axial tension usually do to the bending stiffness of a beam?",
         [("a", "Lowers it"), ("b", "Removes it"), ("c", "Raises it"), ("d", "Makes it zero")], "c"),
        ("How does a cable carry load?",
         [("a", "In compression only"), ("b", "In bending only"), ("c", "In torsion only"), ("d", "In tension only")], "d"),
        ("What should you do when the movement is large?",
         [("a", "Ignore the change in shape"), ("b", "Use a nonlinear method that updates the geometry as the structure moves"), ("c", "Double the steel"), ("d", "Use linear analysis anyway")], "b"),
    ],
}
