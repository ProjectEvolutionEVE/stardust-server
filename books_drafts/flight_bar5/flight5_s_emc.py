"""Electromagnetic Interference: unwanted electrical noise, and how designers keep equipment from disturbing itself."""
CODE = "flight5_s_emc"
BOOK = {
    "title": "Electromagnetic Interference",
    "subtitle": "Unwanted electrical noise, and how to keep devices from interfering",
    "chapters": [
        ("What interference is",
         "Electrical equipment gives off electromagnetic noise, and that noise can disturb other equipment nearby. The unwanted effect is called electromagnetic interference, or EMI."),
        ("Grounding",
         "Grounding gives stray electrical currents a safe path to a common point. Good grounding keeps systems quiet and safe."),
        ("Filters",
         "A filter lets wanted signals through and blocks unwanted noise. Filters are fitted where noise enters or leaves a unit."),
        ("Testing",
         "Equipment is tested in special rooms that measure how much noise it gives off, and how well it resists noise from outside. These tests happen before flight."),
        ("Cases of trouble",
         "Some craft have suffered faults from interference that were hard to trace. Thorough design and testing find many of these problems before launch."),
        ("Design",
         "Designers keep high-power wires apart from signal wires, and they route cables with care. A good layout is cheaper than repair."),
    ],
    "test": [
        ("What does EMI stand for?",
         [("a", "Early mission ideas"), ("b", "Electromagnetic interference"), ("c", "Electric motor input"), ("d", "Energy map index")], "b"),
        ("What does grounding do?",
         [("a", "Makes things heavier"), ("b", "Adds colour to wires"), ("c", "Makes sound"), ("d", "Gives stray currents a safe path")], "d"),
        ("What is a filter's job?",
         [("a", "To block unwanted noise and pass wanted signals"), ("b", "To store fuel"), ("c", "To grow plants"), ("d", "To cool the room")], "a"),
        ("When is equipment tested for EMI?",
         [("a", "After it crashes"), ("b", "Only once it is in orbit"), ("c", "Before flight, in special rooms"), ("d", "Never")], "c"),
        ("What is a good design choice to reduce interference?",
         [("a", "Running power and signal wires side by side"), ("b", "Keeping high-power wires apart from signal wires"), ("c", "Making every wire the same colour"), ("d", "Removing all grounding")], "b"),
    ],
}
