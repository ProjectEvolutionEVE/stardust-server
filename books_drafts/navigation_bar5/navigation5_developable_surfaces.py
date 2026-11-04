"""Developable Surfaces and Cone Constants: unrolling a cone, and what the cone constant means for a conic map."""
CODE = "navigation5_developable_surfaces"
BOOK = {
    "title": "Developable Surfaces and Cone Constants",
    "subtitle": "Unrolling a cone to make a conic map",
    "chapters": [
        ("Surfaces that unroll", "A developable surface, such as a cylinder or a cone, can be unrolled flat without tearing or stretching. A plane is developable too."),
        ("Cone unfolding", "A cone can be cut along one line and laid flat as a sector of a circle. Conic map projections use this idea."),
        ("The cone constant", "The cone constant is a number that describes how much of the full circle the flat sector takes. It depends on the standard parallels."),
        ("Standard parallels", "A conic projection is exact along its standard parallels. Between them and beyond them, the scale changes."),
        ("Scale", "In a simple conic projection, the scale is exact along the standard parallels and varies between them. Choosing the parallels with care keeps errors small across a country."),
        ("The derivation", "The cone constant can be worked out from the standard parallels using trigonometry. It is often one of the first derivations students learn in map projections."),
    ],
    "test": [
        ("Which surface can be unrolled flat without stretching?",
         [("a", "A sphere"), ("b", "A potato"), ("c", "A rubber ball"), ("d", "A cone")], "d"),
        ("What is a cone's flat form when it is unrolled?",
         [("a", "A sector of a circle"), ("b", "A square"), ("c", "A triangle"), ("d", "A cube")], "a"),
        ("What is the cone constant?",
         [("a", "The colour of the paper"), ("b", "A number describing how much of the full circle the flat shape covers"), ("c", "The price of the map"), ("d", "A date")], "b"),
        ("Along what is a conic projection exact?",
         [("a", "The poles"), ("b", "The standard parallels"), ("c", "The prime meridian only"), ("d", "The sea")], "b"),
        ("What is true of scale between the standard parallels?",
         [("a", "It is always exact"), ("b", "It is zero"), ("c", "It varies"), ("d", "It is random in size")], "c"),
    ],
}
