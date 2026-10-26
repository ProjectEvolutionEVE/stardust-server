"""Space Tethers: a long line between two craft can hold a steady pose, push or pull, and move momentum."""
CODE = 'flight4_tethers'
BOOK = {
    "title": "Space Tethers",
    "subtitle": "Gravity gradient, electric tethers and the risks of a long line",
    "chapters": [
        ("A line in space",
         "A tether is a long, strong cable joined between two objects in orbit. The line can be kilometres long, and it can carry forces between the two ends."),
        ("Gravity gradient",
         "The pull of gravity is a little stronger on the lower end of a long object. This keeps a tether pointing toward Earth, with no engine needed. Engineers use the effect to hold some satellites in a steady position."),
        ("Electric tethers",
         "A conducting tether moving through Earth's magnetic field can carry an electric current along its length. That current can produce a force that slows a craft or raises its orbit, using electricity rather than fuel. Such tethers are still being studied."),
        ("A broken line",
         "NASA and Italy flew the Tethered Satellite System in 1992 and again in 1996. The first flight got stuck partway out. In 1996 the line broke, and the satellite drifted away, so the trial ended early."),
        ("Momentum trade",
         "A tether can move momentum from one object to another. One craft speeds up while the other slows, and the total stays balanced. Momentum is moved, not created, which is why the trade costs nothing."),
        ("Hazards",
         "A tether is long and thin, so tiny debris can cut it. Designers add extra strands and guard systems to slow the damage. A tether that breaks can leave debris that is itself a hazard."),
    ],
    "test": [
        ("What keeps a long tether pointing toward Earth?",
         [("a", "Solar wind"), ("b", "Gravity gradient"), ("c", "Magnets on the Moon"), ("d", "Burnt fuel")], "b"),
        ("What does an electrodynamic tether use to push or pull?",
         [("a", "Electric current moving through a magnetic field"), ("b", "Sound waves"), ("c", "Cold gas"), ("d", "Paper sails")], "a"),
        ("What happened on the 1996 tether flight?",
         [("a", "It reached the Moon"), ("b", "It was never launched"), ("c", "The line broke"), ("d", "It docked with Mir")], "c"),
        ("What does a tether do with momentum?",
         [("a", "It destroys it"), ("b", "It moves it from one object to another"), ("c", "It creates it from nothing"), ("d", "It stores it in the Sun")], "b"),
        ("What is the main hazard for a long, thin tether?",
         [("a", "Rain"), ("b", "Tiny debris that can cut it"), ("c", "Warm air"), ("d", "Quiet noise")], "b"),
    ],
}
