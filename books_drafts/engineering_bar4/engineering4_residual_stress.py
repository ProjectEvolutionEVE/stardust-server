"""Residual stress: locked-in forces from machining, welding and quenching, measurement by hole drilling, relief by heat and fatigue effects."""
CODE = "engineering4_residual_stress"
BOOK = {
    "title": "Residual Stress: Locked-In Forces",
    "subtitle": "Stress left behind by making a part",
    "chapters": [
        ("Stress with no load",
         "Residual stress is stress that remains in a part with no external load on it. It is locked in by the way the part was made. It can help or harm the part, depending on where it sits."),
        ("Sources of residual stress",
         "Machining, welding and quenching all leave residual stress. Uneven heating or cooling makes one region shrink against another. Plastic deformation during forming can also leave stress behind."),
        ("Measuring by hole drilling",
         "The hole drilling method drills a small hole and measures the strain released around it. The released strain shows the stress that was in the surface. It is a common method for measuring residual stress near the surface."),
        ("Relief by heat",
         "Heating a part to a suitable temperature lets the material relax and lowers residual stress. This is called stress relief. The heat must be chosen so that the part keeps its required properties."),
        ("Effects on fatigue",
         "Compressive residual stress near a surface can slow fatigue cracks from starting. Tensile residual stress can speed them up. Engineers take residual stress into account when they predict fatigue life."),
        ("Designing with residual stress",
         "Designers plan the process order so that helpful compressive stress is kept and harmful tensile stress is removed. Testing after the process confirms the result. A part is safer when its locked-in forces are known."),
    ],
    "test": [
        ("What is residual stress?", [("a", "Stress from a load that is removed completely"), ("b", "Stress that remains in a part with no external load on it"), ("c", "A type of paint"), ("d", "The weight of a box")], "b"),
        ("Which processes can leave residual stress?", [("a", "Only packing"), ("b", "Only painting"), ("c", "Machining, welding and quenching"), ("d", "Only shipping")], "c"),
        ("How does the hole drilling method work?", [("a", "It paints a hole in the surface"), ("b", "It fills a hole with water"), ("c", "It drills a small hole and measures the strain released around it"), ("d", "It cuts the part in half")], "c"),
        ("What is stress relief by heat?", [("a", "Heating a part so the material relaxes and residual stress falls"), ("b", "Freezing a part to make it hard"), ("c", "Adding paint to a part"), ("d", "Making the part heavier")], "a"),
        ("What does compressive residual stress near a surface do for fatigue?", [("a", "It melts the surface"), ("b", "It always speeds up cracks"), ("c", "It has no effect at all"), ("d", "It can slow fatigue cracks from starting")], "d"),
    ],
}
