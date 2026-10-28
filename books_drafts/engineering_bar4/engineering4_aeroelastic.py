"""Aeroelasticity: how air forces and structure couple, flutter and divergence, stiffness margins and wind-tunnel tests."""
CODE = "engineering4_aeroelastic"
BOOK = {
    "title": "Aeroelasticity: Flutter and Divergence",
    "subtitle": "Air forces, structure, flutter speed and divergence",
    "chapters": [
        ("Air and structure together",
         "Aerodynamic forces push on a wing, and the wing bends and twists under them. Those movements change the air forces again. This two-way coupling is aeroelasticity."),
        ("Flutter",
         "Flutter is a self-feeding oscillation, where bending and twisting combine with air forces to grow. Above a certain flutter speed, the oscillation grows and can destroy the structure."),
        ("Divergence",
         "Divergence is a static twist that grows without limit once the aerodynamic twisting force beats the structure's stiffness. It is a sudden loss of stiffness, not a vibration."),
        ("Stiffness margins",
         "Designers keep a margin between the flight speed and the flutter and divergence speeds. Stiffer structures and well-placed mass raise these speeds."),
        ("Wind-tunnel tests",
         "Wing models are tested in wind tunnels to find the flutter speed before flight. Flight tests then confirm the margin."),
        ("Why it matters",
         "Flutter has caused serious failures in aviation history, so the check is part of every aircraft design. Engineers treat the check as essential, not optional."),
    ],
    "test": [
        ("What does aeroelasticity study?",
         [("a", "Only paint"), ("b", "How air forces and structure affect each other"), ("c", "Cooking"), ("d", "Fuel tanks only")], "b"),
        ("What is flutter?",
         [("a", "A static twist"), ("b", "Engine noise"), ("c", "A self-feeding oscillation that grows with air forces"), ("d", "A colour change")], "c"),
        ("What is divergence?",
         [("a", "A static twist that grows without limit once it beats the stiffness"), ("b", "Engine heat"), ("c", "A fault in the paint"), ("d", "A landing")], "a"),
        ("What raises the flutter speed?",
         [("a", "Less stiffness"), ("b", "Less testing"), ("c", "Higher fuel load"), ("d", "A stiffer structure and well-placed mass")], "d"),
        ("What do wind-tunnel tests of wing models find?",
         [("a", "The colour of the wing"), ("b", "The flutter speed before flight"), ("c", "The fuel use"), ("d", "The crew size")], "b"),
    ],
}
