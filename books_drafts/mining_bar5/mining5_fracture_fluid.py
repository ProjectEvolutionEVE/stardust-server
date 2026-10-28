"""Fluid Flow in Fractured Crust: how water moves through cracks in rock, and how pressure cycles can pump it to where ore forms."""
CODE = "mining5_fracture_fluid"
BOOK = {
    "title": "Fluid Flow in Fractured Crust",
    "subtitle": "Water moving through cracks, and the pumping that brings metal up",
    "chapters": [
        ("Permeability", "Permeability is how easily a fluid moves through rock. Solid rock has low permeability, but cracks and pores raise it. A small change in cracks can change flow many times over."),
        ("Fracture networks", "Rock is often cut by a network of fractures of many sizes. The network decides where fluid can go. Geologists map fracture patterns in the field and in drill core."),
        ("Fault valves", "A fault can act like a valve. Pressure builds until the fault slips, which opens a path and lets fluid rush up. Then the path seals again. This cycle is called fault-valve behaviour."),
        ("Pressure cycling", "Repeated pressure build-up and release can pump fluid through rock again and again. Each cycle carries dissolved metal toward a place where it can settle. The process is slow but powerful over long periods."),
        ("Hydrothermal pumping", "Hydrothermal pumping combines heat, pressure and fracture flow to move fluid over large distances. Hot fluid rises, cools, and leaves metal behind. The pumping helps build large ore systems."),
        ("Field tests", "Field tests measure permeability and flow with pumping tests and tracers. Teams compare the results with models of the fracture network. A model that fails a field test must be changed."),
    ],
    "test": [
        ("What is permeability?",
         [("a", "How hard a rock is to scratch"), ("b", "How old a rock is"), ("c", "How bright a rock looks"), ("d", "How easily a fluid moves through rock")], "d"),
        ("How can a fault act like a valve?",
         [("a", "It stores sound"), ("b", "It turns rock into water"), ("c", "It opens to let fluid through when pressure builds and slips"), ("d", "It grows trees")], "c"),
        ("What does pressure cycling do?",
         [("a", "It freezes all the rock solid"), ("b", "It repeatedly pumps fluid through rock"), ("c", "It removes all cracks at once"), ("d", "It has no effect at all")], "b"),
        ("What helps a fracture network carry fluid?",
         [("a", "Its pattern and openings"), ("b", "Its colour only"), ("c", "Its smell"), ("d", "Its shape in the sky")], "a"),
        ("How do field tests help a model?",
         [("a", "They prove any model is right"), ("b", "They make models unnecessary"), ("c", "They only measure the weather"), ("d", "A model that fails a field test must be changed")], "d"),
    ],
}
