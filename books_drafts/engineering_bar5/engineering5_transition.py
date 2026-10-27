"""Laminar-to-Turbulent Transition: how smooth flow breaks into turbulence, what speeds it up, and why early transition costs drag."""
CODE = "engineering5_transition"
BOOK = {
    "title": "Laminar-to-Turbulent Transition",
    "subtitle": "Routes to turbulence, roughness effects and the drag penalty",
    "chapters": [
        ("From smooth to chaotic", "Flow along a surface can change from smooth laminar flow to chaotic turbulent flow. This change is called transition, and where it happens matters for the whole design."),
        ("Instability routes", "There are several routes to turbulence, and the one that applies depends on the disturbances and the flow. Each route has its own signs that show up before transition."),
        ("Roughness and free stream", "Surface roughness and disturbances in the outer flow can bring transition earlier. A small bump or a turbulent outer flow can have a large effect."),
        ("Prediction", "Engineers predict transition with methods that track the growth of disturbances, combined with empirical rules from experiments."),
        ("The drag penalty", "Turbulent flow has more skin friction than laminar flow. Early transition therefore raises drag, which costs fuel or energy over the life of the vehicle."),
        ("Designing for late transition", "Smooth surfaces and careful shaping can keep the flow laminar for longer. The benefit depends on keeping the surface clean and free of damage."),
    ],
    "test": [
        ("What is transition in a flow?", [("a", "A change of paint on a surface"), ("b", "A change from laminar to turbulent flow"), ("c", "A change of job by a worker"), ("d", "A change of shoes for the test")], "b"),
        ("What can bring transition earlier?", [("a", "Cold tea on the bench"), ("b", "Bright lights in the lab"), ("c", "Surface roughness and disturbances in the outer flow"), ("d", "A long table in the lab")], "c"),
        ("Why does early transition raise drag?", [("a", "Turbulent flow has less friction than laminar flow"), ("b", "It makes the body lighter"), ("c", "It removes the air around the body"), ("d", "Turbulent flow has more skin friction than laminar flow")], "d"),
        ("What do engineers use to predict transition?", [("a", "Methods that track disturbance growth, with empirical rules"), ("b", "A coin toss"), ("c", "A dice roll"), ("d", "A calendar of test dates")], "a"),
        ("How can laminar flow be kept longer?", [("a", "Rough paint on the surface"), ("b", "Smooth surfaces and careful shaping"), ("c", "More disturbance in the flow"), ("d", "Hotter tea on the bench")], "b"),
    ],
}
