"""Residual Stress Measurement: stresses locked inside a part after it is made, and the methods that find them."""
CODE = "mining5_residual_stress"
BOOK = {
    "title": "Residual Stress Measurement",
    "subtitle": "The stress that stays locked inside a part, and how to find it",
    "chapters": [
        ("Stress that stays", "Residual stress is stress that remains inside a part with no outside load on it. It comes from uneven heating, cooling, welding, machining or plastic bending. It can help a part or harm it."),
        ("Welds and tension", "A weld cools and shrinks, and the metal near it is often left in tension. Tensile residual stress can help cracks grow, so welds are a common place to check."),
        ("Peening", "Shot peening bombards a surface with small balls. This leaves a layer of compressive residual stress near the surface, which slows fatigue cracks from starting."),
        ("Hole drilling", "In the hole drilling method, a small hole is drilled and strain gauges around it record how the surface relaxes. The strain readings give the stress near the surface."),
        ("X-ray and neutron methods", "X-ray diffraction measures stress in a shallow surface layer by how the spacing of atomic planes changes. Neutron diffraction can probe much deeper inside a part."),
        ("Designing with stress", "Engineers measure residual stress to choose the right process and to check the result. A part with the right stress pattern can last much longer."),
    ],
    "test": [
        ("What is residual stress?",
         [("a", "Stress that stays inside a part with no outside load"), ("b", "A stress that disappears at once"), ("c", "A colour on the surface"), ("d", "The weight of a box")], "a"),
        ("What stress is usually left near a weld?",
         [("a", "No stress at all"), ("b", "Magnetic stress only"), ("c", "Tensile stress"), ("d", "Water stress")], "c"),
        ("What does shot peening leave near the surface?",
         [("a", "Liquid metal"), ("b", "Compressive residual stress"), ("c", "Paper coating"), ("d", "Ice crystals")], "b"),
        ("Which method drills a small hole and reads strain around it?",
         [("a", "Hand weighing"), ("b", "Colour matching"), ("c", "Taste testing"), ("d", "Hole drilling")], "d"),
        ("Which method can probe deeply inside a part?",
         [("a", "Looking with the naked eye"), ("b", "Neutron diffraction"), ("c", "Weighing on a scale"), ("d", "Smelling the metal")], "b"),
    ],
}
