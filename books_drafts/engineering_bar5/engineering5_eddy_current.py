"""Eddy Current Testing: using electrical currents induced in a conductor to find cracks and measure the surface of metal parts."""
CODE = "engineering5_eddy_current"
BOOK = {
    "title": "Eddy Current Testing",
    "subtitle": "Induced currents, skin depth and finding cracks in metal",
    "chapters": [
        ("Currents in metal", "A coil carrying alternating current makes an alternating magnetic field. Near a metal part, this field induces eddy currents, which circulate inside the metal."),
        ("Coil impedance", "The coil's electrical impedance changes when the eddy currents in the part change. This change is what the instrument measures."),
        ("Skin depth", "Eddy currents flow mainly near the surface. The depth they reach falls as the frequency rises, and this depth is called the skin depth."),
        ("Probe design", "The probe's shape and size decide which region is tested and how sensitive the test is. Different probes suit different jobs."),
        ("Lift-off", "Moving the probe away from the surface changes the reading. This effect is called lift-off, and it must be controlled or allowed for."),
        ("Detecting cracks", "A crack interrupts the eddy currents, so the reading changes at that point. This change shows a crack at or near the surface, within the skin depth; cracks hidden deep below are beyond its reach."),
    ],
    "test": [
        ("What induces eddy currents?", [("a", "An alternating magnetic field from a coil"), ("b", "A dry cloth"), ("c", "A bucket of water"), ("d", "A sheet of paper")], "a"),
        ("What is skin depth?", [("a", "The thickness of a paint layer"), ("b", "The colour of the metal"), ("c", "The depth of eddy currents near the surface, which falls as frequency rises"), ("d", "The thickness of a person's skin")], "c"),
        ("What is lift-off?", [("a", "The effect of moving the probe away from the surface"), ("b", "A crane used in a workshop"), ("c", "A jump test for coils"), ("d", "A type of rocket engine")], "a"),
        ("What does a crack do to eddy currents?", [("a", "It paints them a new colour"), ("b", "It makes them louder"), ("c", "It makes them stop forever"), ("d", "It interrupts them and changes the reading")], "d"),
        ("What does coil impedance change with?", [("a", "The colour of the desk"), ("b", "The eddy currents in the part"), ("c", "The weather outside"), ("d", "The operator's coffee")], "b"),
    ],
}
