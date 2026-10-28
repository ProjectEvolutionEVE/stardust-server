"""Helical Springs and Spring Design: spring rate, wire stress, fatigue, set removal, shot peening and spring selection."""
CODE = "engineering4_springs"
BOOK = {
    "title": "Helical Springs and Spring Design",
    "subtitle": "Spring rate, fatigue, peening and selection",
    "chapters": [
        ("Spring rate",
         "Spring rate is the force needed to compress a spring by one unit of length. A stiff spring has a high rate."),
        ("Wire stress",
         "Wire stress depends on the force, the coil diameter and the wire diameter. Designers keep the stress below the material limit, with a margin to spare."),
        ("Fatigue in springs",
         "Springs flex again and again, and repeated stress can start cracks. Fatigue life is a main design check for any spring."),
        ("Set removal",
         "A spring loaded beyond its limit may take a permanent set. Presetting removes the early set by loading the spring to a higher value once, before it goes into service."),
        ("Shot peening",
         "Shot peening hits the surface with small balls, which leaves a layer of compressive stress. That layer raises the fatigue life of the spring."),
        ("Spring selection",
         "Choose the material, wire size and coil shape for the load, the fatigue life and the space available. Each choice trades cost, fatigue life and size against the others."),
    ],
    "test": [
        ("What is spring rate?",
         [("a", "The force needed to compress a spring by one unit of length"), ("b", "Paint"), ("c", "Sound"), ("d", "Weather")], "a"),
        ("What can start cracks in a spring?",
         [("a", "Paint"), ("b", "Repeated stress from flexing"), ("c", "Light"), ("d", "Sound")], "b"),
        ("What does shot peening do?",
         [("a", "Melts the wire"), ("b", "Paints the coil"), ("c", "Stops the spring"), ("d", "Leaves compressive stress at the surface and raises fatigue life")], "d"),
        ("What is set in a spring?",
         [("a", "A colour"), ("b", "A sound"), ("c", "A permanent change after overloading"), ("d", "A flavour")], "c"),
        ("What guides spring selection?",
         [("a", "Material, wire size and coil shape for the load"), ("b", "Only colour"), ("c", "Only price"), ("d", "Only sound")], "a"),
    ],
}
