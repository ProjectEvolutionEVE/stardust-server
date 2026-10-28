"""Diffusion Bonding of Metals: joining two metal surfaces in the solid state, with no melting and no filler metal."""
CODE = "engineering5_diffusion_bond"
BOOK = {
    "title": "Diffusion Bonding of Metals",
    "subtitle": "Joining metal in the solid state, with no filler",
    "chapters": [
        ("Joining without melting", "Diffusion bonding joins two surfaces by pressing them together at high temperature, below the melting point. Atoms move across the join over time. The result is one continuous piece of metal."),
        ("Surface preparation", "The surfaces must be very clean and smooth. Oxide layers and dirt block atoms from crossing the boundary, so the bond fails if the surface is not prepared well."),
        ("Pressure and temperature", "Pressure brings the surfaces into close contact, and temperature speeds up atomic movement. Both must be controlled, because too little of either gives a weak joint."),
        ("Interface diffusion", "Over time, atoms move across the interface between the two pieces. The boundary fades, and the joint gains strength as the grains of metal grow across it."),
        ("No filler", "No filler metal is added, so the joint is made of the parent metals themselves. This can keep the joint's properties close to those of the base metal."),
        ("Where it is used", "The method suits parts where a normal weld would distort the metal or weaken it. It is slower and needs careful control of the furnace and the press."),
    ],
    "test": [
        ("What does diffusion bonding avoid?", [("a", "Cleaning the surfaces"), ("b", "Melting the metal"), ("c", "Applying pressure"), ("d", "Inspecting the finished joint")], "b"),
        ("Why must the surfaces be clean?", [("a", "So they look nice"), ("b", "Because oxides and dirt block atoms from crossing the join"), ("c", "So the parts are heavier"), ("d", "So the colour stays the same")], "b"),
        ("What joins the two pieces?", [("a", "A glue layer"), ("b", "A filler metal"), ("c", "Atoms moving across the interface"), ("d", "Mechanical screws")], "c"),
        ("Why is pressure used?", [("a", "To bring the surfaces into close contact"), ("b", "To melt the metal"), ("c", "To cool the joint"), ("d", "To make the metal magnetic")], "a"),
        ("What does a diffusion bond use instead of filler?", [("a", "The parent metals themselves"), ("b", "A layer of plastic"), ("c", "A sheet of wood"), ("d", "A coat of paint")], "a"),
    ],
}
