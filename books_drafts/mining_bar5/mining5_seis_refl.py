"""Seismic Reflection in Hard Rock: sending sound waves into the ground and reading the echoes to draw deep structures."""
CODE = "mining5_seis_refl"
BOOK = {
    "title": "Seismic Reflection in Hard Rock",
    "subtitle": "Sources, geophones, processing and the hard limits of crystalline rock",
    "chapters": [
        ("Sound into the ground",
         "A seismic survey starts with a source that sends a sound wave into the ground. Sources include vibrating trucks, weight drops and small explosives. Each one makes a short pulse that travels down and back up."),
        ("Source and geophone",
         "Geophones are sensors laid on the surface in a line. They record the echoes that bounce back from layers and boundaries below. A long line of geophones gives a wide view of the ground beneath."),
        ("Processing",
         "Raw records are noisy, so they are cleaned, filtered and sorted. Then many traces are stacked together, which makes the real echoes stand out. Speed estimates turn the echo times into depths."),
        ("Migration",
         "An echo does not come from straight below the sensor when layers are tilted. Migration is a calculation that moves each echo to where the reflector really sits. Without it, dipping layers look like they are in the wrong place."),
        ("Hard rock challenges",
         "Crystalline rock such as granite and gneiss has few sharp layers, so the echoes are weak. Broken and scattered rock adds noise. These problems make deep hard rock images harder to read than images of soft sedimentary basins."),
        ("Costs",
         "A reflection survey costs a lot because it needs crews, sources, many sensors and a lot of computing time. Teams decide whether the picture is worth the cost by asking what decision it will support. A survey is only useful if its answer changes what is done next."),
    ],
    "test": [
        ("What does a geophone do in a seismic survey?",
         [("a", "It records echoes that bounce back from layers below"), ("b", "It digs the hole"), ("c", "It cools the ground"), ("d", "It counts the trucks")], "a"),
        ("What is stacking used for?",
         [("a", "To paint the map"), ("b", "To make the ground warmer"), ("c", "To make real echoes stand out from the noise"), ("d", "To cut the cable")], "c"),
        ("What does migration correct?",
         [("a", "The colour of the report"), ("b", "The speed of the crew"), ("c", "The price of explosives"), ("d", "The position of echoes from tilted layers")], "d"),
        ("Why are hard rock images difficult?",
         [("a", "Because hard rock is always wet"), ("b", "Because crystalline rock has few sharp layers, so echoes are weak"), ("c", "Because hard rock makes no sound"), ("d", "Because geophones cannot be placed on rock")], "b"),
        ("What decides whether a seismic survey is worth its cost?",
         [("a", "Whether the picture changes what is done next"), ("b", "Whether the crew likes the work"), ("c", "Whether the survey has a long name"), ("d", "Whether it is done at night")], "a"),
    ],
}
