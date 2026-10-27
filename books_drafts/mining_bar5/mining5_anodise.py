"""Anodising and Oxide Films: growing a porous oxide layer on aluminium by electrolysis, sealing it, and colouring it."""
CODE = "mining5_anodise"
BOOK = {
    "title": "Anodising and Oxide Films",
    "subtitle": "Growing a tough oxide skin on aluminium",
    "chapters": [
        ("What anodising does", "Anodising makes aluminium form a thick oxide layer on its surface. The part is made the anode in an acid bath, and an electric current grows the oxide in a controlled way."),
        ("A porous layer", "The oxide that grows is porous, full of tiny pores in a regular pattern. This is a strong, hard layer that is still bonded to the metal below."),
        ("Sealing", "Porous oxide is sealed by immersing the part in hot water or a sealing solution. The pores close up, which blocks corrosion and holds dye in place."),
        ("Colour", "Dyes can soak into the pores before sealing, giving the surface a colour. The oxide itself is clear, so the colour shows through the layer."),
        ("Thickness", "Thickness is measured in micrometres and depends on the time, current and bath. Thicker layers protect better, but they can be less flexible."),
        ("Protection", "The sealed oxide protects aluminium from corrosion in air and in many damp places. Phone cases, window frames and cooking pans often carry anodised finishes."),
    ],
    "test": [
        ("What is made the anode in anodising?",
         [("a", "The aluminium part"), ("b", "The water bath"), ("c", "The air"), ("d", "The worker")], "a"),
        ("What kind of oxide layer forms during anodising?",
         [("a", "A glass sheet"), ("b", "A sheet of metal foil"), ("c", "A porous layer"), ("d", "A block of ice")], "c"),
        ("How are the pores in anodised aluminium closed?",
         [("a", "By sanding them"), ("b", "By sealing in hot water or a sealing solution"), ("c", "By freezing them"), ("d", "By sprinkling sugar")], "b"),
        ("In what unit is anodised layer thickness usually measured?",
         [("a", "Litres"), ("b", "Kilograms"), ("c", "Degrees"), ("d", "Micrometres")], "d"),
        ("Why is sealing important?",
         [("a", "It makes the metal heavier"), ("b", "It blocks corrosion and holds colour in place"), ("c", "It melts the part"), ("d", "It removes the oxide")], "b"),
    ],
}
