"""Additive Manufacturing: how metal and polymer parts are built layer by layer, and what makes them reliable."""
CODE = "science5_mat_am"
BOOK = {
    "title": "Additive Manufacturing: Metal and Polymer Printing",
    "subtitle": "Layer fusion, powder bed processes, process defects, residual stress, post-processing and qualification",
    "chapters": [
        ("Building layer by layer", "Additive manufacturing builds a part by adding material one thin layer at a time, guided by a digital model. It can make shapes that are hard or impossible to cut or cast. Each layer must bond properly to the one beneath it."),
        ("Layer fusion and powder beds", "In powder bed processes, a thin layer of metal or polymer powder is spread across a bed. A heat source, such as a laser or electron beam, melts or sinters the areas that form the part. The bed is lowered and the next layer is spread."),
        ("Process defects", "Common defects include porosity, which leaves small gas holes, and lack of fusion, where layers fail to bond fully. Defects often start from powder quality, energy settings or gas flow. Finding them early saves time and cost."),
        ("Residual stress", "Uneven heating and cooling leaves residual stresses locked inside the part. These can warp the part during the build or later in service. Stress relief heat treatment or careful build planning can reduce them."),
        ("Post-processing", "After printing, parts often need support removal, stress relief, heat treatment, machining of critical faces and surface finishing. Post-processing can change the strength and fatigue life of the part, so it is treated as part of the process."),
        ("Qualification", "Qualification shows, with evidence, that a process reliably makes parts that meet the specification. It involves controlled builds, testing of samples and records of every setting. A printed part is trusted only when its process has been qualified."),
    ],
    "test": [
        ("What happens in layer fusion?",
         [("a", "Layers are cut away from a solid block"), ("b", "Each thin layer of powder is melted or bonded onto the one below"), ("c", "The part is moulded inside a mould"), ("d", "Liquid metal is poured into sand")], "b"),
        ("What are residual stresses in a printed metal part?",
         [("a", "Internal stresses left in the part by uneven heating and cooling"), ("b", "Stresses caused by paint on the printer"), ("c", "Stress that builds up while the part is stored"), ("d", "Friction from the build plate alone")], "a"),
        ("Why is post-processing needed?",
         [("a", "To add more layers to the part"), ("b", "To change the material's chemistry entirely"), ("c", "To make the part larger"), ("d", "To remove supports, relieve stress and finish the surfaces")], "d"),
        ("What does qualification of a process mean?",
         [("a", "Printing a single test part"), ("b", "Choosing the cheapest powder available"), ("c", "Showing with evidence that the process reliably makes parts that meet the specification"), ("d", "Giving the printer a name")], "c"),
        ("What is a common process defect in powder bed printing?",
         [("a", "Porosity, which leaves small gas holes in the part"), ("b", "Too much polish on the surface"), ("c", "Parts that are too heavy to lift"), ("d", "Colour fading in sunlight")], "a"),
    ],
}
