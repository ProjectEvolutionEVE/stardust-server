"""Boundary Layers and Drag: the thin layer of slow fluid next to a surface, and why it matters."""
CODE = 'engineering4_boundary'
BOOK = {
    "title": "Boundary Layers and Drag",
    "subtitle": "The thin layer of slow air or water next to a surface, and why it matters",
    "chapters": [
        ("Laminar and turbulent layers",
         "A boundary layer is the thin layer of fluid close to a surface. It starts out smooth, which is called laminar, and it can become turbulent further along the surface."),
        ("Skin friction",
         "Friction between the fluid and the surface makes up part of the drag. The shape of the boundary layer sets how much skin friction there is."),
        ("Separation",
         "If the flow slows too much against a rising pressure, it can leave the surface. This is separation. It adds a large drag and a wake behind the object."),
        ("Drag reduction",
         "Smooth surfaces, streamlined shapes and controlled transitions all reduce drag. Designers aim to keep the flow attached to the surface."),
        ("Surface roughness",
         "A rough surface can make the boundary layer turbulent sooner, and that raises skin friction. Smooth finishes reduce it."),
        ("Why it matters",
         "Drag costs fuel and energy on ships, cars, aircraft and pipes. Small reductions add up over the life of a machine."),
    ],
    "test": [
        ("What is a boundary layer?",
         [("a", "A fence"), ("b", "A border on a map"), ("c", "A thin layer of fluid near a surface"), ("d", "A shelf")], "c"),
        ("What does skin friction do?",
         [("a", "Adds part of the drag"), ("b", "Lights a bulb"), ("c", "Cools paint"), ("d", "Makes sound")], "a"),
        ("What is separation?",
         [("a", "A sheet being cut"), ("b", "A box being sealed"), ("c", "A paint job"), ("d", "When flow leaves the surface, adding a large drag and a wake")], "d"),
        ("What reduces drag?",
         [("a", "Rough surfaces"), ("b", "Smooth surfaces and streamlined shapes"), ("c", "Bumpy paint"), ("d", "More wind")], "b"),
        ("What does a rough surface often do to the boundary layer?",
         [("a", "Makes it turbulent sooner, raising skin friction"), ("b", "Removes all friction"), ("c", "Makes it dry"), ("d", "Cools it to ice")], "a"),
    ],
}
