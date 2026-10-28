"""Viscoelasticity and Time-Dependent Response: how plastics stretch, sag and relax over time under steady load."""
CODE = "engineering5_viscoelastic"
BOOK = {
    "title": "Viscoelasticity and Time-Dependent Response",
    "subtitle": "How plastics stretch, sag and relax over time under steady load",
    "chapters": [
        ("Materials with memory",
         "Polymers respond to load partly like springs and partly like thick liquids. Their response depends on how long the load acts, not just on its size."),
        ("Creep and relaxation",
         "Under a steady load, a polymer slowly stretches further, which is creep. Under a steady stretch, the force falls over time, which is relaxation."),
        ("Maxwell and Kelvin models",
         "The Maxwell model puts a spring and a dashpot in series, and suits relaxation. The Kelvin model puts them in parallel, and suits creep and its recovery."),
        ("Time-temperature superposition",
         "Warmer polymers behave as if time runs faster. Test data taken at several temperatures can be shifted together into a single curve that covers a long range of times."),
        ("Design with plastics",
         "Designs must allow for creep, for the loss of force from relaxation, and for changing temperature. A part that fits well when new may loosen after months of service."),
        ("Check the time scale",
         "Use data for the real temperature and the real time of service. A short test cannot tell you everything that happens over years."),
    ],
    "test": [
        ("What does creep mean?",
         [("a", "A fast crack"), ("b", "A slow stretch under steady load"), ("c", "A paint process"), ("d", "A bright colour")], "b"),
        ("What does relaxation mean?",
         [("a", "Force drops over time under a steady stretch"), ("b", "Force rises for ever"), ("c", "Colour fades"), ("d", "Metal melts")], "a"),
        ("Which model puts a spring and a dashpot in series?",
         [("a", "Kelvin"), ("b", "Newton"), ("c", "Maxwell"), ("d", "Hooke")], "c"),
        ("What does time-temperature superposition do?",
         [("a", "Shifts data taken at several temperatures into one curve over a wide range of times"), ("b", "Heats the plastic"), ("c", "Paints it"), ("d", "Counts time")], "a"),
        ("Why might a plastic part fit when new but loosen later?",
         [("a", "Metal rust only"), ("b", "Paint"), ("c", "Creep and relaxation over time"), ("d", "Sunlight only")], "c"),
    ],
}
