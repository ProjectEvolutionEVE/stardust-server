"""Failure Mechanism Maps: charts that show which way a material fails, for each combination of stress and temperature."""
CODE = "engineering5_fail_maps"
BOOK = {
    "title": "Failure Mechanism Maps",
    "subtitle": "Deformation and fracture maps for choosing a material",
    "chapters": [
        ("Maps of failure", "A failure mechanism map plots which mechanism controls a material's behaviour across stress and temperature. It turns a long list of test results into one picture."),
        ("Deformation maps", "Deformation maps show the regions where a material stays elastic, creeps or flows. They help show when a part will bend or sag over time."),
        ("Fracture maps", "Fracture maps show where a material fails by brittle or ductile fracture. They help show when a part may break suddenly."),
        ("Regimes of temperature and stress", "Each region of a map is a regime where one mechanism dominates. Moving across the map can change which mechanism controls the part."),
        ("Choosing a material from its map", "A designer checks where the part will work, then picks a material that stays in a safe region for that duty. The map makes the comparison clear."),
        ("Limits of the map", "Maps are simplified, so they guide the choice but do not replace testing. Real parts can differ from the map because of their shape, surface and history."),
    ],
    "test": [
        ("What does a failure mechanism map show?", [("a", "The price of a drill"), ("b", "The colour of a lab"), ("c", "The office plan of a factory"), ("d", "Which mechanism controls behaviour across stress and temperature")], "d"),
        ("What do deformation maps show?", [("a", "Regions where a material creeps, flows or stays elastic"), ("b", "Where to park a van"), ("c", "Which shop sells paint"), ("d", "Where the tea is kept")], "a"),
        ("What is a regime on a map?", [("a", "A type of sandwich"), ("b", "A new member of staff"), ("c", "A region where one mechanism dominates"), ("d", "A way of painting walls")], "c"),
        ("How should a designer use a map?", [("a", "Pick the cheapest colour for the part"), ("b", "Ignore the temperature"), ("c", "Skip the stress check"), ("d", "Check where the part will operate and pick a material that stays in a safe region")], "d"),
        ("Why do maps not replace testing?", [("a", "Because maps are printed in colour"), ("b", "Because maps are simplified guides"), ("c", "Because maps are long to read"), ("d", "Because maps are always wrong")], "b"),
    ],
}
