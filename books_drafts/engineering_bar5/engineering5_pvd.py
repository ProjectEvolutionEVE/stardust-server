"""Physical Vapour Deposition: Sputtering and Evaporation. Sputtering targets, evaporation, film thickness control, adhesion and tool coatings."""
CODE = "engineering5_pvd"
BOOK = {
    "title": "Physical Vapour Deposition: Sputtering and Evaporation",
    "subtitle": "Coating a surface with metal atoms in a vacuum",
    "chapters": [
        ("Coating without a chemical reaction",
         "Physical vapour deposition, or PVD, moves a coating material from a source to the part in a vacuum. Unlike CVD, the coating is usually the same material as the source, with no chemical reaction in between."),
        ("Evaporation",
         "In evaporation, the source material is heated until it gives off vapour. The vapour travels across the vacuum and condenses on the cooler part. It is a simple way to lay down a thin metal film."),
        ("Sputtering and targets",
         "In sputtering, ions hit a solid target and knock atoms off its surface. Those atoms land on the part and build up a film. The target is the solid block of coating material that the ions strike."),
        ("Film thickness",
         "Thickness is controlled by time, source power and the distance to the part. Sensors can measure the film as it grows. Careful control keeps each coating within its tolerance."),
        ("Adhesion",
         "A film must stick to the part. Cleaning the surface well and sometimes heating or bombarding it before coating improves adhesion. A film that peels has failed, however good it looked."),
        ("Tool coatings",
         "PVD coatings such as titanium nitride are used on cutting tools and wear parts. A thin hard layer can extend tool life a great deal. The cost of coating is weighed against the longer life and fewer tool changes."),
    ],
    "test": [
        ("What is a key difference between PVD and CVD?",
         [("a", "PVD uses no vacuum"), ("b", "PVD usually moves the source material with no chemical reaction"), ("c", "PVD only coats paper"), ("d", "PVD works only on water")], "b"),
        ("How does evaporation make a film?",
         [("a", "The part is soaked in paint"), ("b", "The part is frozen"), ("c", "A heated source gives off vapour that condenses on the cooler part"), ("d", "The part is hammered flat")], "c"),
        ("What is a sputtering target?",
         [("a", "A paper marker on the floor"), ("b", "The part being coated"), ("c", "The vacuum pump"), ("d", "The solid block of coating material that ions strike")], "d"),
        ("What controls film thickness?",
         [("a", "Time, source power and distance to the part"), ("b", "The name of the operator"), ("c", "The colour of the room"), ("d", "The day of the week")], "a"),
        ("Why does a film need good adhesion?",
         [("a", "Films with good adhesion are always heavier"), ("b", "A film that peels has failed to do its job"), ("c", "Adhesion makes the film invisible"), ("d", "Adhesion has no effect")], "b"),
    ],
}
