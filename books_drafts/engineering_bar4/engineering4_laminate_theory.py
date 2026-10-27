"""Laminate theory: ply stiffness, stacking sequence, warping, quasi-isotropic layups, coupon testing and laminate design rules."""
CODE = "engineering4_laminate_theory"
BOOK = {
    "title": "Laminate Theory: Stacking Plies",
    "subtitle": "Ply stiffness, stacking sequence and layup rules",
    "chapters": [
        ("Plies and laminates",
         "A ply is one thin layer of fibre and resin. A laminate is a stack of plies bonded together. Each ply is stiff along its own fibre direction and much weaker across it."),
        ("Stacking sequence",
         "The order and angle of the plies in a stack is called the stacking sequence. Changing the sequence changes how the laminate bends and stretches. Designers choose the sequence to suit the loads on the part."),
        ("Warping",
         "A laminate with plies at mixed angles can warp after it cools from curing. The plies shrink by different amounts and pull against each other. Symmetric stacking helps keep a flat part flat."),
        ("Quasi-isotropic layups",
         "A quasi-isotropic layup uses several ply angles so the laminate has similar stiffness in all in-plane directions. It is a good general choice when the loads are not known in advance. It is not the strongest choice for a single known load."),
        ("Coupon testing",
         "A coupon is a small test piece cut from the laminate. Engineers pull, bend and compress coupons to measure the properties of a layup. Coupon results feed into the design of the full part."),
        ("Design rules for laminates",
         "Designers follow rules such as using enough plies at each angle and avoiding large groups of plies at one angle. These rules limit cracking between layers and reduce the risk of sudden failure. Rules guide the design, but each part still needs checking."),
    ],
    "test": [
        ("What is a ply?", [("a", "A paint coat"), ("b", "A metal bolt"), ("c", "A single thin layer of fibre and resin"), ("d", "A type of door")], "c"),
        ("What is the stacking sequence?", [("a", "The order and angle of the plies in a stack"), ("b", "The colour pattern of the surface"), ("c", "The number of workers on the line"), ("d", "The date of manufacture")], "a"),
        ("Why can a laminate with mixed ply angles warp after curing?", [("a", "The fibres are magnetic"), ("b", "Warping comes from paint"), ("c", "Laminates never cool"), ("d", "The plies shrink by different amounts and pull against each other")], "d"),
        ("What does a quasi-isotropic layup give?", [("a", "A layer that is only stiff across the fibres"), ("b", "Similar stiffness in all in-plane directions"), ("c", "A part that cannot be tested"), ("d", "A laminate with no plies")], "b"),
        ("What is a coupon in laminate testing?", [("a", "A type of mould"), ("b", "A discount on the resin"), ("c", "A small test piece cut from the laminate"), ("d", "A safety sign")], "c"),
    ],
}
