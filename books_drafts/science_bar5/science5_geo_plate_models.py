"""Numerical Modelling of Plate Dynamics: governing equations, plate boundary forces, subduction and model checking."""
CODE = "science5_geo_plate_models"
BOOK = {
    "title": "Numerical Modelling of Plate Dynamics",
    "subtitle": "Computing how the Earth's plates move, and checking the answers",
    "chapters": [
        ("What the model tries to do", "Plate models use computers to simulate how the rigid plates of the outer shell move over the hot, slowly flowing mantle below. No model copies the Earth exactly. Each one is a set of equations solved on a grid of points."),
        ("Governing equations for mantle flow", "The main equations describe how the mantle flows as a very viscous fluid, driven by heat and density differences. They balance forces against the rate of movement and the transport of heat. Solving them needs numerical methods such as finite element or finite difference schemes."),
        ("Plate boundary forces", "Models must include forces at plate boundaries, where plates pull apart, push together or slide past one another. The pull of sinking slabs is often a major driver of plate motion. The strength chosen for each boundary shapes the result."),
        ("Computing subduction", "Subduction models simulate an oceanic plate sinking into the mantle beneath another plate. The sinking slab is cooler and denser, so it pulls the plate along. Getting the bending and strength of the slab right is one of the hardest parts."),
        ("Benchmarking models", "Benchmarking compares different codes on the same simple test problem with known answers. It shows whether a code is doing its sums correctly. Benchmark problems are shared so that results can be checked across research groups."),
        ("Comparing models with observations", "Model results are compared with measured plate velocities, earthquake patterns and seismic images. A good match builds confidence, but many different settings can fit the same data. Simulations are useful for testing ideas, not for proving them alone."),
    ],
    "test": [
        ("What are numerical plate models?",
         [("a", "Computer simulations that solve equations on a grid to study plate motion"), ("b", "Paper maps of coastlines"), ("c", "Lab measurements of rock colour"), ("d", "Descriptions of weather")], "a"),
        ("How is the mantle usually treated in flow equations?",
         [("a", "As a gas"), ("b", "As a very viscous fluid"), ("c", "As a solid with no flow"), ("d", "As pure water")], "b"),
        ("What is a subduction model?",
         [("a", "A model of a glacier"), ("b", "A model of a river delta"), ("c", "A model of wind"), ("d", "A model of an oceanic plate sinking beneath another plate")], "d"),
        ("What is benchmarking in model testing?",
         [("a", "Measuring the length of a ruler"), ("b", "Choosing a colour scheme"), ("c", "Comparing codes on a simple test problem with known answers"), ("d", "Pricing the computer time")], "c"),
        ("Why is a good match between a model and observations not proof on its own?",
         [("a", "Because the observations are always wrong"), ("b", "Because computers cannot count"), ("c", "Because plates never move"), ("d", "Because many different settings can fit the same data")], "d"),
    ],
}
