"""Ocean Current Datasets: surface currents, model and drifter data, forecasts, their use in routing, and their limits."""
CODE = "navigation4_ocean_currents"
BOOK = {
    "title": "Ocean Current Datasets",
    "subtitle": "Where current data comes from, and how far to trust it",
    "chapters": [
        ("Surface currents", "Surface currents are the movement of the upper water of the sea. They push ships along or slow them down. A good route takes them into account."),
        ("Model data", "Ocean models calculate currents from physics and from forcing such as wind and tides. They cover large areas and give regular values. Their accuracy depends on the detail and quality of the model."),
        ("Drifter data", "Drifters are floats that move with the water near the surface. Their tracks show the real currents where they have been. They are most useful where the model has few checks."),
        ("Forecasts", "Current forecasts predict the currents ahead of a voyage. They are updated as new data arrives. Like weather forecasts, they become less certain further ahead."),
        ("Routing use", "Routing tools combine current data with wind and waves. A favourable current can save fuel and time. An adverse current can add days to a passage."),
        ("Limits and gaps", "Current data has gaps, especially in remote areas and in deep water. Models can miss small, fast currents near the coast. Always compare the data with what the crew sees."),
    ],
    "test": [
        ("What are surface currents?", [("a", "Sounds made by whales"), ("b", "Patterns of clouds"), ("c", "Movement of the upper water of the sea"), ("d", "Lines on a chart")], "c"),
        ("What do drifters do?", [("a", "They fly above the ocean"), ("b", "They measure the depth of rivers"), ("c", "They float with the water near the surface, showing real currents"), ("d", "They sail faster than ships")], "c"),
        ("What can a favourable current do for a voyage?", [("a", "Save fuel and time"), ("b", "Stop the ship"), ("c", "Change the flag"), ("d", "Remove the crew")], "a"),
        ("Where are current data often weakest?", [("a", "In every harbour"), ("b", "On every map"), ("c", "In a classroom"), ("d", "In remote areas and deep water")], "d"),
        ("What should a crew do with current data?", [("a", "Ignore the sea"), ("b", "Compare it with what they see"), ("c", "Trust it with no checks"), ("d", "Throw it away")], "b"),
    ],
}
