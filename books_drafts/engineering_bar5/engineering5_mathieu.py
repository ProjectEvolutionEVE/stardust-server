"""Parametric Resonance and the Mathieu Equation: how a system can grow large swings when its stiffness is varied in time, and how to avoid the unstable zones."""
CODE = "engineering5_mathieu"
BOOK = {
    "title": "Parametric Resonance and the Mathieu Equation",
    "subtitle": "Swings that grow when stiffness changes in time, and how to stay out of trouble",
    "chapters": [
        ("A different kind of resonance", "Ordinary resonance happens when a force pushes at the natural frequency. Parametric resonance is different: the stiffness itself changes in time. The system can then gain energy and grow large swings even with no direct push."),
        ("The Mathieu equation", "A common model is the Mathieu equation, a second-order equation whose stiffness varies as a cosine in time. It is named after the French mathematician Emile Mathieu, who studied it in the 1860s. It describes many real machines."),
        ("Unstable zones", "The Mathieu equation has regions of settings where the motion grows without limit, called instability zones. Outside them the motion stays bounded. Engineers plot these zones to see which speeds and stiffness levels are safe."),
        ("Rotating machines", "A rotor on a shaft with unequal stiffness in two directions sees a stiffness that varies twice per turn. This can cause growing vibration at certain speeds. Designers check the operating speed against the unstable zones."),
        ("The role of damping", "Damping lowers the size of the unstable zones. Enough damping can keep the system stable even when the stiffness varies. Too little damping leaves the system open to growth."),
        ("Design advice", "Engineers avoid running a machine inside a known unstable zone. They change the natural frequencies, add damping or change the stiffness pattern. Tests confirm that the chosen design stays out of trouble."),
    ],
    "test": [
        ("How does parametric resonance differ from ordinary resonance?", [("a", "It needs no energy at all"), ("b", "It only occurs in fluids"), ("c", "It only happens at zero speed"), ("d", "The stiffness itself changes in time")], "d"),
        ("What is the Mathieu equation a model of?", [("a", "A chemical reaction in a tank"), ("b", "The flow of water in a pipe"), ("c", "A second-order system with stiffness that varies as a cosine in time"), ("d", "The colour of a surface")], "c"),
        ("What are instability zones?", [("a", "Settings where the motion grows without limit"), ("b", "Places where the paint peels"), ("c", "Sections of road that are wet"), ("d", "Storage areas for spare parts")], "a"),
        ("What does damping do to the unstable zones?", [("a", "Makes them bigger"), ("b", "Moves them to the sea floor"), ("c", "Has no effect ever"), ("d", "Lowers their size")], "d"),
        ("What is good design advice for a machine near an unstable zone?", [("a", "Run it at the zone speed to test it"), ("b", "Avoid running inside the zone by changing frequencies or adding damping"), ("c", "Remove all damping"), ("d", "Double the speed without checking")], "b"),
    ],
}
