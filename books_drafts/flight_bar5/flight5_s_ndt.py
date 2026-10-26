"""Non-destructive Testing: looking inside metal and finding flaws without breaking the part."""
CODE = "flight5_s_ndt"
BOOK = {
    "title": "Non-destructive Testing",
    "subtitle": "Looking inside metal without breaking it",
    "chapters": [
        ("Why not cut it open",
         "Engineers need to check parts without damaging them. Non-destructive testing, or NDT, finds flaws while the part stays whole and usable."),
        ("X-ray",
         "X-rays pass through metal and show patches where there is a gap or a crack. Trained inspectors read the pictures and decide what they mean."),
        ("Ultrasound",
         "High-frequency sound waves travel into the metal and bounce back from flaws. The timing of the echo shows how deep a flaw lies."),
        ("Dye penetrant",
         "A coloured or glowing liquid soaks into cracks that reach the surface. After the excess is wiped away, a developer draws the dye out, so the crack shows."),
        ("Eddy current",
         "A coil carrying electric current induces swirling currents in the metal. Changes in those currents reveal cracks and changes in thickness, especially near the surface."),
        ("Reading results",
         "Every test needs training and judgement. An inspector must decide whether a flaw is harmless, needs watching, or means the part must be replaced."),
    ],
    "test": [
        ("What does NDT stand for?",
         [("a", "New design tools"), ("b", "Night data transfer"), ("c", "Non-destructive testing"), ("d", "Nuclear data test")], "c"),
        ("Which method uses sound waves?",
         [("a", "Ultrasound"), ("b", "Dye penetrant"), ("c", "X-ray"), ("d", "Eddy current")], "a"),
        ("What does dye penetrant reveal?",
         [("a", "Hidden cavities deep inside"), ("b", "Radio signals"), ("c", "Heat levels"), ("d", "Cracks that reach the surface")], "d"),
        ("What is needed to read NDT results well?",
         [("a", "A stopwatch"), ("b", "Training and judgement"), ("c", "A bright lamp only"), ("d", "Luck")], "b"),
        ("Why is NDT so valuable?",
         [("a", "It cuts parts open to look inside"), ("b", "It destroys the part to test it"), ("c", "It finds flaws while the part stays usable"), ("d", "It replaces all other inspection")], "c"),
    ],
}
