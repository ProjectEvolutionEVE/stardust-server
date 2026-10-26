"""Medicine, bar 3 (Senior Doctor), part B: Hazards and Controls at Work. Spotting hazards, judging risk, the order of controls, lockout and tagout, and reporting near misses."""
CODE = "medicine3b_hazards"
BOOK = {
    "title": "Hazards and Controls at Work",
    "subtitle": "Spotting hazards, judging risk, and the order of controls that keeps a workplace safe",
    "chapters": [
        ("What a hazard is",
         "A hazard is anything that could cause harm, such as a moving part, a sharp edge, a heavy load, a hot surface or a toxic chemical. Risk is the chance that harm happens, together with how serious it could be. Safe work begins by finding hazards before they cause harm."),
        ("Judging risk",
         "A simple way to judge risk asks two questions: how likely is harm, and how serious would it be? A slippery floor may be a likely but minor hazard, while a fall from height is less likely but very serious. Both need attention, and the serious ones come first."),
        ("The order of controls",
         "Safety experts use a hierarchy of controls. The best option is to remove the hazard completely. Next comes replacing it with something safer, then engineering controls such as guards. After those come rules and training, and last of all personal protective equipment such as gloves and helmets."),
        ("Lockout and tagout",
         "Before work on a machine that could move or release energy, its power is cut off and locked, and a tag explains why. This is called lockout and tagout. It means no one can switch the machine back on while someone is working on it."),
        ("Near misses",
         "A near miss is an event that could have caused harm but did not. Reporting near misses lets a team fix a problem before someone is hurt. A culture where people report without blame is one of the strongest safety tools a team has."),
        ("Safety pays",
         "Accidents cost money in treatment, lost work, repairs and lost trust. Investing in guards, training and clear procedures usually costs far less than the injuries they prevent. A safety budget is a form of smart saving."),
    ],
    "test": [
        ("What is a hazard?",
         [("a", "Anything that could cause harm"), ("b", "A type of food"), ("c", "A ship's name"), ("d", "A kind of money")], "a"),
        ("Which control is the best in the hierarchy?",
         [("a", "Gloves"), ("b", "Rules and training"), ("c", "A warning sign"), ("d", "Removing the hazard completely")], "d"),
        ("What is lockout and tagout?",
         [("a", "A sign for dinner"), ("b", "A sleep plan"), ("c", "Cutting off and locking a machine's power during work on it, with a tag saying why"), ("d", "A way to lock food")], "c"),
        ("What is a near miss?",
         [("a", "A safe landing"), ("b", "An event that could have caused harm but did not"), ("c", "A type of hazard only"), ("d", "A lost cargo")], "b"),
        ("Why does reporting near misses help?",
         [("a", "It makes reports longer"), ("b", "It stops all work"), ("c", "It removes the need for training"), ("d", "It lets a team fix a problem before someone is hurt")], "d"),
    ],
}
