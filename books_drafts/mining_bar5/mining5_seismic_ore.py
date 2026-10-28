"""Seismic Imaging of Ore Systems: sending sound waves into the crust to map layers and dense sulfide zones, and the limits of the method."""
CODE = "mining5_seismic_ore"
BOOK = {
    "title": "Seismic Imaging of Ore Systems",
    "subtitle": "Sound waves that map rock layers and sulfide zones",
    "chapters": [
        ("Crust imaging", "Seismic imaging sends sound waves into the ground and records their echoes. The echoes reveal layers, faults and boundaries deep below the surface. It is one of the strongest tools for seeing the crust."),
        ("Reflection profiles", "A reflection profile is a cross-section built from many echo recordings along a line. Interpreters use it to trace layers and structures. A good profile can show features kilometres down."),
        ("Velocity contrasts", "Sound travels at different speeds in different rocks. A sharp change in acoustic impedance (rock speed times density) causes a strong echo. Geologists look for these contrasts to find boundaries and dense bodies."),
        ("Reflective sulfide zones", "Massive sulfide bodies are dense and often reflect seismic waves strongly. They can show up as bright features on a profile. Interpreters must still check these features with drilling, because other rocks can look similar."),
        ("Depth limits", "Seismic imaging has depth and resolution limits. Deep targets are harder to see clearly, and small bodies can be missed. Teams state these limits before they plan a survey."),
        ("Cost", "Seismic surveys are expensive because they need many sources, receivers and skilled processing. The cost is justified only when the target is large and the geology is complex. Careful planning keeps the cost in check."),
    ],
    "test": [
        ("What does seismic imaging do?",
         [("a", "Sends sound waves into the ground and records their echoes"), ("b", "Measures the wind speed"), ("c", "Counts birds on a field"), ("d", "Grows crystals")], "a"),
        ("What is a reflection profile?",
         [("a", "A photograph of a face"), ("b", "A map of train stations"), ("c", "A chart of prices"), ("d", "A cross-section built from many echo recordings along a line")], "d"),
        ("Why does a sharp change in acoustic impedance (speed times density) matter?",
         [("a", "It makes the rock melt"), ("b", "It changes the rock colour"), ("c", "It creates a strong echo that marks a boundary"), ("d", "It has no effect on echoes")], "c"),
        ("Why must a bright seismic feature be checked by drilling?",
         [("a", "Bright features are always gold"), ("b", "Other rocks can look similar on a profile"), ("c", "Drilling is never needed"), ("d", "Bright features are always rain")], "b"),
        ("Why is seismic surveying expensive?",
         [("a", "It needs many sources, receivers and skilled processing"), ("b", "It uses only one cheap microphone"), ("c", "It needs no staff at all"), ("d", "It is done by hand with a stick")], "a"),
    ],
}
