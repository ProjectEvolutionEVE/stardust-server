"""Surface Finish and Machining Damage: how surface roughness, white layers and tool marks affect fatigue life, and how finish is measured."""
CODE = "mining5_surface_finish"
BOOK = {
    "title": "Surface Finish and Machining Damage",
    "subtitle": "The skin of a part decides how long it lasts",
    "chapters": [
        ("Surface roughness", "Every machined surface has tiny peaks and valleys. Their average height is called surface roughness, often written as Ra. A smoother surface usually costs more time to make."),
        ("Damage from machining", "Cutting and grinding can leave cracks, dents or changed layers under the surface. Heat from fast cutting can alter the metal near the surface, and these changes can be hidden from the eye."),
        ("White layers", "Hard turning and grinding can form a thin white layer on steel. It is very hard but often brittle, and it can contain small cracks. Its formation depends on heat and cooling speed during the cut."),
        ("Fatigue", "Parts that flex many times fail by fatigue, and cracks often start at the surface. Scratches, tool marks and white layers all give cracks a place to start. A good finish helps a part last longer under repeated load."),
        ("Polishing", "Polishing removes the peaks and smooths the surface. Shot peening, which puts small compressive stress at the surface, can also help against fatigue cracks."),
        ("Measuring finish", "A stylus profilometer drags a tiny tip across the surface and records the height changes. Optical methods use light to map the surface without touching it."),
    ],
    "test": [
        ("What does Ra measure?",
         [("a", "The weight of a part"), ("b", "The colour of the metal"), ("c", "The temperature of the room"), ("d", "Average surface roughness")], "d"),
        ("What is a white layer?",
         [("a", "A sheet of paper"), ("b", "A hard, often brittle layer formed by machining heat"), ("c", "A coat of white paint"), ("d", "A layer of snow")], "b"),
        ("Where do fatigue cracks often start?",
         [("a", "At the surface"), ("b", "In the air"), ("c", "Inside the packaging"), ("d", "In the handle of a cup")], "a"),
        ("What does polishing do to the surface?",
         [("a", "Adds big bumps"), ("b", "Makes the metal melt"), ("c", "Removes peaks and smooths it"), ("d", "Changes its name")], "c"),
        ("What instrument drags a tiny tip across a surface to measure it?",
         [("a", "A stylus profilometer"), ("b", "A kitchen timer"), ("c", "A rain gauge"), ("d", "A compass")], "a"),
    ],
}
