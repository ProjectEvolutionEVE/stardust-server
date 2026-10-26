"""Wiring and Connectors: cables, plugs and insulation, and why small wiring faults can matter a great deal."""
CODE = "flight5_s_cable"
BOOK = {
    "title": "Wiring and Connectors",
    "subtitle": "Cables, plugs and insulation, and why small faults matter",
    "chapters": [
        ("The harness",
         "A craft's wires are bundled into harnesses that carry power and signals to every system. A single harness can contain thousands of wires."),
        ("Shielding",
         "A metal braid or foil wrapped around a wire keeps outside noise from disturbing the signal inside it. Shielding matters most on signals that must be kept clean."),
        ("Insulation",
         "Insulation keeps wires from touching each other or the frame. When it cracks, electricity can jump where it should not."),
        ("Arcing",
         "An arc is a spark that jumps across a gap. Arcs can start fires and damage nearby equipment, so engineers design wiring to avoid them."),
        ("Apollo 13",
         "On Apollo 13 in 1970, a fault in the wiring of an oxygen tank led to an explosion that crippled the spacecraft. The crew came home safely, and the wiring lesson stayed with every later team."),
        ("Care",
         "Wires are bent, tied and checked with care. Gentle handling and clear labels make repairs and inspections quicker and safer."),
    ],
    "test": [
        ("What is a harness?",
         [("a", "A bundle of wires"), ("b", "A kind of parachute"), ("c", "A type of fuel"), ("d", "A camera")], "a"),
        ("What does shielding do for a wire?",
         [("a", "Makes it heavier"), ("b", "Makes it glow"), ("c", "Keeps outside noise from disturbing the signal"), ("d", "Makes it colder")], "c"),
        ("What is insulation for?",
         [("a", "Carrying more power"), ("b", "Making wires shiny"), ("c", "Adding heat"), ("d", "Stopping wires touching where they should not")], "d"),
        ("What is arcing?",
         [("a", "A bend in a wire"), ("b", "A spark jumping across a gap"), ("c", "A type of radio"), ("d", "A glowing lamp")], "b"),
        ("What role did wiring play in the Apollo 13 emergency?",
         [("a", "A fault in an oxygen tank's wiring led to an explosion"), ("b", "A wire rang a bell"), ("c", "The lunar lander stuck to a wire"), ("d", "The crew used wires as rope")], "a"),
    ],
}
