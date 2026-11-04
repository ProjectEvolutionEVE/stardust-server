"""Magnetic Materials: why some metals become magnets, and how hard and soft magnets are used."""
CODE = "science4_mat_magnetic"
BOOK = {
    "title": "Magnetic Materials",
    "subtitle": "Why some metals become magnets, and how we use them",
    "chapters": [
        ("Magnetism in atoms", "Magnetism comes from the spins and orbits of electrons in atoms. In most materials these effects cancel out. In iron, cobalt and nickel, the spins line up across small regions, which gives a strong magnetic effect."),
        ("Ferromagnetism and domains", "Inside a ferromagnet, neighbouring atoms line up in small regions called domains. Each domain points one way, and the domains can be turned by a magnetic field. When most domains line up, the whole piece becomes a strong magnet."),
        ("Hysteresis loops", "If you magnetise a material and then reverse the field, it does not return along the same path. The plot of magnetisation against field is a hysteresis loop. The area inside the loop shows the energy lost each time the field cycles."),
        ("Hard and soft magnets", "Hard magnets, such as neodymium alloys, keep their magnetism strongly and are hard to demagnetise. Soft magnets, such as silicon steel, are easy to magnetise and demagnetise. Each type suits a different job."),
        ("Recording and motors", "Magnetic recording stores data by flipping tiny domains in a thin film, with hard materials keeping the bits stable. Electric motors use magnets to push and pull against coils. Soft materials guide the magnetic flux inside the motor."),
        ("Choosing a magnet", "Engineers pick a magnet by its strength, its stability when hot, its cost and its resistance to demagnetising. Rare earth magnets are very strong but can lose strength at high temperatures. Choosing well means balancing these trade-offs."),
    ],
    "test": [
        ("What are magnetic domains?",
         [("a", "Regions of the Earth's core"), ("b", "Small regions where atomic magnets point the same way"), ("c", "Types of electric wire"), ("d", "Cracks in a magnet")], "b"),
        ("What is a hysteresis loop?",
         [("a", "A plot showing magnetisation lags behind the field as it cycles"), ("b", "A coil of copper wire"), ("c", "A kind of battery"), ("d", "The shape of a compass needle")], "a"),
        ("Which of these is a typical hard magnet?",
         [("a", "Copper"), ("b", "Aluminium foil"), ("c", "Glass"), ("d", "Neodymium alloy")], "d"),
        ("Why are soft magnets used inside motors?",
         [("a", "They are very heavy"), ("b", "They never conduct electricity"), ("c", "They are easy to magnetise and demagnetise, and they guide the field"), ("d", "They glow in the dark")], "c"),
        ("Which metals are the classic ferromagnets?",
         [("a", "Iron, cobalt and nickel"), ("b", "Gold, silver and copper"), ("c", "Lead and tin"), ("d", "Zinc and carbon")], "a"),
    ],
}
