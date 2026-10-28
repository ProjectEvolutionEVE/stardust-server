"""Rockburst Mechanics and Energy Release: how strain energy stored in rock can be released suddenly, and how support and design reduce the danger."""
CODE = "mining5_rb_energy"
BOOK = {
    "title": "Rockburst Mechanics and Energy Release",
    "subtitle": "Strain energy, fault slip, burst types, support and mitigation",
    "chapters": [
        ("Energy held in rock",
         "Rock under high stress holds strain energy, a bit like a bent spring. Mining removes support and changes the stress, so the energy can move. A rockburst is a sudden release of that stored energy."),
        ("Strain energy",
         "The amount of energy stored depends on the stress and the stiffness of the rock. The stored energy rises steeply as stress builds, and stiff, brittle rock tends to release it suddenly. When the rock breaks, that energy is released as seismic waves and violent movement."),
        ("Fault slip",
         "A fault is a fracture where rock has already moved. Mining can load a fault until it slips. The slip releases a large amount of energy at once, which can throw broken rock into the opening."),
        ("Burst types",
         "Strain bursts break the rock around an excavation with little warning. Fault-slip bursts come from movement on a fault. Pillar bursts occur when a rock pillar fails under high stress."),
        ("Support capacity",
         "Support such as bolts, mesh and shotcrete holds broken rock in place. Each support has a limit to the energy it can absorb. A burst larger than that limit can overwhelm the support."),
        ("Mitigation",
         "Mitigation reduces the stress or the energy that can be released. Methods include changing the mine layout, sequencing the mining, and using controlled blasts to relieve stress. Warning systems help people leave the danger zone in time."),
    ],
    "test": [
        ("What is a rockburst?",
         [("a", "A sudden release of stored strain energy in rock"), ("b", "A gentle rain of sand"), ("c", "A kind of drill bit"), ("d", "A type of lamp")], "a"),
        ("What does the amount of strain energy depend on?",
         [("a", "The stress and the stiffness of the rock"), ("b", "The colour of the rock"), ("c", "The name of the mine"), ("d", "The price of diesel")], "a"),
        ("What is fault slip?",
         [("a", "A slip on a wet floor"), ("b", "A type of drill rod"), ("c", "Movement on a fracture where rock has already moved"), ("d", "A kind of rock sample")], "c"),
        ("What limits what support can do?",
         [("a", "The colour of the bolts"), ("b", "The name of the company"), ("c", "The temperature of the office"), ("d", "The amount of energy it can absorb")], "d"),
        ("What is one way to reduce the danger of a rockburst?",
         [("a", "Mining faster in the same spot"), ("b", "Changing the layout and sequencing of the mining"), ("c", "Removing all support"), ("d", "Ignoring warning signs")], "b"),
    ],
}
