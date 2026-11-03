"""Satellite altimetry: radar echoes from orbit, the sea surface, the geoid, uses for charts and limits near the coast."""
CODE = "navigation4_altimetry"
BOOK = {
    "title": "Satellite Altimetry",
    "subtitle": "Measuring the sea surface from orbit",
    "chapters": [
        ("Height from orbit", "A radar altimeter in a satellite sends pulses down to the sea and times the echoes. Knowing the satellite's orbit gives the height of the sea surface. The method covers the whole ocean."),
        ("The sea surface", "The sea surface is not flat. It bulges and dips with currents, winds and gravity. Altimetry maps these shapes over time."),
        ("The geoid", "The geoid is the shape the sea would take if it were shaped only by gravity and Earth's rotation. Height above the geoid shows the sea surface features. Knowing the geoid well is essential."),
        ("Uses for charts", "Altimetry helps map the seafloor in areas that have not been surveyed. Bumps in the sea surface can hint at undersea ridges. This helps plan ship surveys."),
        ("Limits", "Altimetry sees the sea surface, not the depth directly. Near the coast the echoes are messy. Measurements are less reliable close to land."),
        ("Working together", "Altimetry is combined with ship surveys and gravity models. Each source fills gaps left by the others. The combined maps are used in charts and research."),
    ],
    "test": [
        ("What does a radar altimeter in orbit measure?", [("a", "The time of radar echoes from the sea"), ("b", "The brightness of city lights"), ("c", "The sugar in sea water"), ("d", "The number of fish below")], "a"),
        ("What is the geoid?", [("a", "A type of sea bird"), ("b", "The shape the sea would take if shaped only by gravity and rotation"), ("c", "The highest mountain on Earth"), ("d", "A sound made by whales")], "b"),
        ("What does altimetry help map in areas not yet surveyed?", [("a", "The number of boats"), ("b", "The colour of the beaches"), ("c", "The seafloor"), ("d", "The mood of the crew")], "c"),
        ("What does a gravity bump in the sea surface hint at?", [("a", "A warm bath"), ("b", "A sunken ship"), ("c", "A rainbow above the water"), ("d", "An undersea ridge")], "d"),
        ("Where are altimetry measurements less reliable?", [("a", "Far out on the open ocean"), ("b", "Over a calm, deep sea"), ("c", "Close to the coast"), ("d", "In a dry desert")], "c"),
    ],
}
