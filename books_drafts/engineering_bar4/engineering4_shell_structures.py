"""Thin shells and domes: membrane action, dome forms, shell buckling, concrete shells and testing of shell models."""
CODE = "engineering4_shell_structures"
BOOK = {
    "title": "Thin Shells and Domes",
    "subtitle": "Membrane action, dome forms and shell buckling",
    "chapters": [
        ("Why curves carry load",
         "A curved thin shell can carry load across its surface, much as a flat sheet cannot. The curve spreads the force through the material in its own plane. This membrane action lets a shell be very thin for its span."),
        ("Membrane action",
         "In membrane action, the shell carries load mainly by pulling and squeezing in its own surface. Bending is kept small in the ideal case. Engineers check where this simple action breaks down, such as at edges and supports."),
        ("Dome forms",
         "Domes are built in shapes such as spherical, elliptical and parabolic forms. Each form spreads load in its own way. The best shape depends on the span, the loads and how the dome is supported."),
        ("Shell buckling",
         "A thin shell under compression can buckle suddenly, even though the material is not overstressed. A small imperfection can lower the buckling load a lot. Designers allow for imperfections and keep a margin against buckling."),
        ("Concrete shells",
         "Concrete shells can be cast as thin curved sheets, often with ribs at the edges. The shape carries most of the load, so the shell can be far lighter than a flat slab. Formwork and placing the concrete need careful control."),
        ("Testing shell models",
         "Engineers build small models of shells and load them to see how they behave. Tests reveal buckling and edge effects that may be hard to predict. The results help confirm the design before the full shell is built."),
    ],
    "test": [
        ("What is membrane action in a shell?", [("a", "Carrying load on a separate frame"), ("b", "Carrying load by bending the shell like a bar"), ("c", "Carrying load by painting it"), ("d", "Carrying load mainly by pulling and squeezing in the shell's own surface")], "d"),
        ("Why can a curved shell be so thin?", [("a", "Because thin shells never carry load"), ("b", "Because the curve spreads the force within its surface"), ("c", "Because the shell is made of glass only"), ("d", "Because gravity is weaker")], "b"),
        ("What is shell buckling?", [("a", "A type of door on a dome"), ("b", "Painting a shell in stripes"), ("c", "Sudden failure of a thin shell under compression, often from a small imperfection"), ("d", "Slow melting of the surface")], "c"),
        ("What does a concrete shell often rely on for its strength?", [("a", "Having no shape at all"), ("b", "Being filled with water"), ("c", "Its curved shape carrying most of the load"), ("d", "Being made of wood only")], "c"),
        ("Why do engineers test small shell models?", [("a", "To reveal buckling and edge effects that are hard to predict"), ("b", "To choose the colour of the dome"), ("c", "To avoid all calculation"), ("d", "To make the shell heavier")], "a"),
    ],
}
