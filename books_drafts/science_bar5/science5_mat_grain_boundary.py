"""Grain Boundaries and Microstructure: how the small crystals in a metal, and the edges between them, decide its strength."""
CODE = "science5_mat_grain_boundary"
BOOK = {
    "title": "Grain Boundaries and Microstructure",
    "subtitle": "How the crystal grains inside a metal control its strength",
    "chapters": [
        ("Grains", "Most metals are made of many small crystals called grains. Each grain has its atoms in a regular pattern. The grains are packed together like tiles in a floor."),
        ("Boundaries", "The boundary is the interface between two grains. Atoms there cannot line up perfectly with both neighbours. Boundaries therefore carry extra energy."),
        ("Grain growth", "Large grains tend to grow at the expense of small ones, because this lowers the total boundary energy. Heat speeds the process. Engineers manage it to keep grain size where they want it."),
        ("Hall-Petch relation", "The Hall-Petch relation says that smaller grains usually make a metal stronger. Boundaries block the motion of dislocations, so more boundaries mean more blocking. It is one of the most useful rules in metal design."),
        ("Texture", "Texture is a preferred orientation of the crystals in a metal. It comes from how the metal was made, such as rolling or drawing. Texture changes how the metal behaves under load."),
        ("Controlling grain size", "Heat treatment and rolling are the main ways to control grain size. The right sequence gives a fine grain for strength or a coarse grain for other uses. Careful control gives predictable parts."),
    ],
    "test": [
        ("What is a grain in a metal?",
         [("a", "A seed of corn"), ("b", "A grain of sand"), ("c", "A grain of rice"), ("d", "A small crystal in the metal")], "d"),
        ("Why do grain boundaries carry extra energy?",
         [("a", "They are made of gold"), ("b", "They are hot"), ("c", "Atoms there are out of line with the crystal pattern"), ("d", "They contain light")], "c"),
        ("What is the Hall-Petch relation?",
         [("a", "Smaller grains usually make a metal stronger"), ("b", "Larger grains always make a metal stronger"), ("c", "Grain size has no effect on strength"), ("d", "Grains never affect strength")], "a"),
        ("What is texture in a metal?",
         [("a", "The smell of the metal"), ("b", "A preferred crystal orientation from how the metal was made"), ("c", "Its colour"), ("d", "Its weight")], "b"),
        ("How can engineers control grain size?",
         [("a", "By painting the metal"), ("b", "By shaking it in water"), ("c", "By heat treatment and rolling"), ("d", "By cooling it in sand")], "c"),
    ],
}
