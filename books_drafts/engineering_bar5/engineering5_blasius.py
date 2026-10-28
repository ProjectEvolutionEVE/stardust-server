"""The Blasius Boundary Layer Solution: the classic result for laminar flow over a flat plate, and what it tells us about friction and thickness."""
CODE = "engineering5_blasius"
BOOK = {
    "title": "The Blasius Boundary Layer Solution",
    "subtitle": "Similarity, thickness and friction for laminar flow over a flat plate",
    "chapters": [
        ("A thin layer near a wall", "A boundary layer is the thin region near a surface where the flow slows from full speed to zero at the wall. Most of the friction on a body happens inside this layer."),
        ("Similarity", "For laminar flow over a flat plate, the velocity profile keeps the same shape at each point along the plate once it is scaled by one variable. This is the idea of similarity."),
        ("The equations", "The boundary layer equations simplify the full flow equations. Blasius solved the resulting equation, and the solution is still a standard reference."),
        ("Thickness measures", "Displacement thickness and momentum thickness measure how much the slowed layer affects the outer flow and the momentum passing through it."),
        ("Skin friction", "The friction on the plate falls as the flow runs further along the plate. The fall follows a known scaling with distance from the leading edge."),
        ("Checking against data", "The Blasius solution is checked against measurements in laminar flow, where it matches well. It shows the limit of what the simple model can do."),
    ],
    "test": [
        ("What is a boundary layer?", [("a", "A layer of paint on a surface"), ("b", "The thin region near a surface where the flow slows to zero at the wall"), ("c", "A sheet of ice on a pond"), ("d", "A roof tile")], "b"),
        ("What is the Blasius solution used for?", [("a", "The price of a plate"), ("b", "A type of paint"), ("c", "Laminar boundary layer flow over a flat plate"), ("d", "Cooking rice")], "c"),
        ("What is similarity in this context?", [("a", "The velocity profile keeps the same shape when scaled by one variable"), ("b", "Two things that look alike in colour"), ("c", "A type of test rig"), ("d", "A rule of sales")], "a"),
        ("What does displacement thickness measure?", [("a", "The price of paint"), ("b", "The number of staff"), ("c", "The weight of a plate"), ("d", "How far the outer flow is pushed out by the slowed layer")], "d"),
        ("How does skin friction change along a plate?", [("a", "It rises forever"), ("b", "It falls as the flow runs further along the plate"), ("c", "It stays at zero"), ("d", "It turns into a solid")], "b"),
    ],
}
