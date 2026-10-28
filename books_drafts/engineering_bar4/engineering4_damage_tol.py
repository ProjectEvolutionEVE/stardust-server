"""Damage Tolerance and Inspection Intervals: assumed flaws, fail-safe and safe-life design, crack growth and the records behind each interval."""
CODE = "engineering4_damage_tol"
BOOK = {
    "title": "Damage Tolerance and Inspection Intervals",
    "subtitle": "Assumed flaws, fail-safe and safe-life design, and inspection planning",
    "chapters": [
        ("Assuming flaws exist",
         "Damage tolerance design assumes small flaws may already be in a part, from making it or from use. The design must then show those flaws will not grow to a dangerous size before they are found."),
        ("Fail-safe and safe-life",
         "A fail-safe design keeps the structure safe even when one part fails. A safe-life design limits how long a part is used before it is replaced."),
        ("Crack growth",
         "Cracks grow under repeated loads, a little with each cycle. The rate depends on the load, the material and the size of the crack."),
        ("Planning inspections",
         "Inspection intervals are set so that a crack would be found before it reaches a critical size. Inspections use methods such as visual checks and ultrasound."),
        ("Records",
         "Each interval rests on records of loads, flights or hours, and test results. Keeping good records is part of the safety case."),
        ("Changing the schedule",
         "If new data show a crack growing faster than expected, the interval is shortened. Good records make that change possible without guessing."),
    ],
    "test": [
        ("What does damage tolerance design assume?",
         [("a", "No flaws exist"), ("b", "Small flaws may already exist"), ("c", "Only new parts are used"), ("d", "Cracks never grow")], "b"),
        ("What does a fail-safe design do?",
         [("a", "Keeps the structure safe even when one part fails"), ("b", "Stops all inspections"), ("c", "Removes the need for records"), ("d", "Uses no materials")], "a"),
        ("What does a safe-life design limit?",
         [("a", "The colour of the part"), ("b", "The number of crew"), ("c", "The paint"), ("d", "How long the part is used before replacement")], "d"),
        ("What sets an inspection interval?",
         [("a", "The weather"), ("b", "The price of the part"), ("c", "Making sure a crack is found before it becomes critical"), ("d", "The colour of the report")], "c"),
        ("Why are records important in this work?",
         [("a", "They support the intervals and show the loads and hours used"), ("b", "They replace the part"), ("c", "They change the metal"), ("d", "They stop cracks forming")], "a"),
    ],
}
