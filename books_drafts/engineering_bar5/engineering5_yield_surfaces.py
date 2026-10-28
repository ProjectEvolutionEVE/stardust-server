"""Plastic Flow Rules and Yield Surfaces: describing where a metal starts to yield under any combination of stresses."""
CODE = "engineering5_yield_surfaces"
BOOK = {
    "title": "Plastic Flow Rules and Yield Surfaces",
    "subtitle": "Describing where a metal starts to yield under any combination of stresses",
    "chapters": [
        ("Yield in many directions",
         "A metal yields when its combined stress reaches a limit. A yield surface is the set of stress combinations that just reach that limit."),
        ("Von Mises and Tresca",
         "The von Mises surface is a smooth cylinder in stress space, and the Tresca surface has straight edges that form a hexagon in cross-section. Both fit many metals, and von Mises is usually the closer match."),
        ("Flow rules",
         "A flow rule says the direction in which plastic strain grows, usually perpendicular to the yield surface. It links the stress to the rate of plastic flow."),
        ("Hardening models",
         "As a metal yields, its yield surface may grow, which is hardening. Isotropic hardening makes the surface grow evenly, while kinematic hardening makes it move."),
        ("Strain rate sensitivity",
         "The yield stress of many metals rises with how fast they are strained. This must be included for impacts and for high-speed forming."),
        ("Fitting to test data",
         "Models are fitted to tensile and other test data, then checked against a different test. A good model matches both the load path and the rate used in the real part."),
    ],
    "test": [
        ("What is a yield surface?",
         [("a", "A paint layer"), ("b", "A road"), ("c", "A price table"), ("d", "The set of stress combinations that just reach yield")], "d"),
        ("What is the shape of the Tresca surface in cross-section?",
         [("a", "A star"), ("b", "A hexagon"), ("c", "A square"), ("d", "A spiral")], "b"),
        ("What does a flow rule give?",
         [("a", "The direction in which plastic strain grows"), ("b", "The price"), ("c", "The colour of the metal"), ("d", "The day of the week")], "a"),
        ("What does isotropic hardening do?",
         [("a", "Turns the metal to glass"), ("b", "Melts the metal"), ("c", "Makes the yield surface grow evenly"), ("d", "Cracks the surface")], "c"),
        ("Why include strain rate sensitivity?",
         [("a", "Because yield stress rises with strain rate"), ("b", "Because metals never flow"), ("c", "Because paint is wet"), ("d", "Because prices fall")], "a"),
    ],
}
