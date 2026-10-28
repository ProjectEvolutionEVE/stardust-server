"""Photoelasticity and Stress Freezing: seeing stress as coloured fringes in clear plastic models."""
CODE = "engineering5_photoelastic"
BOOK = {
    "title": "Photoelasticity and Stress Freezing",
    "subtitle": "Seeing stress as coloured fringes in clear plastic models",
    "chapters": [
        ("Light through stressed plastic",
         "Some clear plastics become birefringent under stress, which means they split light into two rays that travel at different speeds. Seen between polarisers, the stress shows up as fringes."),
        ("Isochromatic fringes",
         "Isochromatic fringes are lines of equal difference between the principal stresses. Their colour order gives the size of that stress difference."),
        ("Isoclinic fringes",
         "Isoclinic fringes are dark lines that show the direction of the principal stresses. They help read which way the stress runs."),
        ("Stress freezing",
         "A model is heated, loaded, and then cooled slowly while still under load. The stress becomes locked in, so the model can be cut and studied later."),
        ("Interpreting fringe patterns",
         "Fringes crowd together where stress is high, and their order rises with the stress. Reading them needs a careful count from a known edge where the stress is zero."),
        ("Where it fits",
         "Photoelasticity gives a clear, visual way to see stress flow around holes and notches. It is used less now that computer methods are common, but its pictures still help explain how stress behaves."),
    ],
    "test": [
        ("What does birefringence do to light?",
         [("a", "Stops it"), ("b", "Paints it"), ("c", "Makes it louder"), ("d", "Splits it into two rays that travel at different speeds")], "d"),
        ("What do isochromatic fringes show?",
         [("a", "Lines of equal difference between the principal stresses"), ("b", "Prices"), ("c", "Paint layers"), ("d", "Weather")], "a"),
        ("What do isoclinic fringes show?",
         [("a", "Heat"), ("b", "Dates"), ("c", "The direction of the principal stresses"), ("d", "Costs")], "c"),
        ("What is stress freezing?",
         [("a", "Ice on a model"), ("b", "Stress locked in by cooling a loaded model slowly"), ("c", "Freezing a camera"), ("d", "Cold paint")], "b"),
        ("Where do the fringes crowd together?",
         [("a", "Where stress is high"), ("b", "Where stress is zero"), ("c", "Nowhere"), ("d", "At the edges only")], "a"),
    ],
}
