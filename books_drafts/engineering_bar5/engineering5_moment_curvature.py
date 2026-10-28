"""Moment-Curvature and Section Ductility: how a cross-section bends past yield, and how far it can rotate."""
CODE = "engineering5_moment_curvature"
BOOK = {
    "title": "Moment-Curvature and Section Ductility",
    "subtitle": "How a cross-section bends past yield, and how far it can rotate",
    "chapters": [
        ("Bending a section",
         "The bending moment is the turning effect on a section, and curvature is how sharply the section bends. Plotting one against the other shows the section's behaviour from elastic bending up to failure."),
        ("Behaviour past yield",
         "Once the outer fibres yield, the moment still rises, but more slowly, as yielding spreads inward. The curve bends over and approaches the plastic moment, the strength of a fully yielded section."),
        ("Curvature limits",
         "A section can bend only so far before the concrete crushes or the steel fractures. The curvature at that point is its limit, and designers keep the demands on the section below it."),
        ("Steel and concrete together",
         "In reinforced concrete, the steel yields and carries the tension, while the concrete carries the compression. Their interaction sets the shape of the moment-curvature curve and the point where the section fails."),
        ("Rotation capacity and ductility demand",
         "The rotation a hinge can give before failure is its rotation capacity. The rotation a structure needs in an earthquake or an overload is the ductility demand, and the capacity must exceed the demand."),
        ("Why it matters",
         "A section with good ductility gives warning before it fails. Checking the moment-curvature curve shows whether a design has that margin, and where it does not, the design needs changing."),
    ],
    "test": [
        ("What does a moment-curvature curve plot?",
         [("a", "Bending moment against curvature"), ("b", "Colour against weight"), ("c", "Cost against time"), ("d", "Stress against temperature")], "a"),
        ("What happens to the moment as yielding spreads through a section?",
         [("a", "It drops to zero at once"), ("b", "It stays exactly the same from the first yield"), ("c", "It keeps rising, more slowly, toward the plastic moment"), ("d", "It doubles at once")], "c"),
        ("What is rotation capacity?",
         [("a", "The number of turns on a bolt"), ("b", "The rotation a hinge can give before failure"), ("c", "The speed of a crane"), ("d", "The angle of a roof")], "b"),
        ("What must exceed the ductility demand?",
         [("a", "The rotation capacity"), ("b", "The price of the job"), ("c", "The number of floors"), ("d", "The thickness of the paint")], "a"),
        ("In reinforced concrete, which material carries the tension in the section?",
         [("a", "Concrete"), ("b", "Water"), ("c", "Steel"), ("d", "Air")], "c"),
    ],
}
