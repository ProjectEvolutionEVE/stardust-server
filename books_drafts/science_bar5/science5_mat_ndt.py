"""Nondestructive Testing Methods: how engineers look inside a part for flaws without breaking it."""
CODE = "science5_mat_ndt"
BOOK = {
    "title": "Nondestructive Testing Methods",
    "subtitle": "Ultrasonic inspection, radiography, eddy currents, thermography, detection limits and planning",
    "chapters": [
        ("Testing without breaking", "Nondestructive testing, or NDT, checks a part for flaws without damaging it. A part that passes can go back into service. That matters for bridges, aircraft and pipelines, where breaking a sample to look inside is not an option."),
        ("Ultrasonic inspection", "Ultrasonic inspection sends high-frequency sound waves into a part. The waves bounce back from the far side and from any crack or void they meet. The timing and strength of the echoes show where a flaw sits and roughly how big it is."),
        ("Radiography and eddy currents", "Radiography passes X-rays or gamma rays through a part and records the image on film or a detector, so internal flaws show as darker or lighter areas. Eddy current testing induces electrical currents in conducting metals, and changes in those currents reveal surface and near-surface cracks."),
        ("Thermography", "Thermography uses infrared cameras to show the heat patterns on a surface. A hidden flaw can change how heat flows, which shows up as a difference in temperature. The method is quick over large areas, but it works best on flaws that affect heat flow."),
        ("Detection limits", "A detection limit is the smallest flaw a method can reliably find under given conditions. Each method has its own limit, and it depends on the material, the shape of the part and the skill of the operator. Knowing the limit tells you what a clean result really means."),
        ("Inspection planning", "Inspection planning chooses which method to use, where to look, how often to check and what level of detection is needed. A good plan balances cost, access and risk. Planning ensures that flaws are found while they are still small enough to repair safely."),
    ],
    "test": [
        ("What does nondestructive testing mean?",
         [("a", "Breaking samples to see inside them"), ("b", "Destroying a part in order to test it"), ("c", "Inspecting a part without damaging it"), ("d", "Melting a sample for chemical analysis")], "c"),
        ("What does ultrasonic inspection use?",
         [("a", "Visible light only"), ("b", "Radio signals sent through a metal part"), ("c", "Strong magnetic pulses that lift flaws out"), ("d", "High-frequency sound waves that bounce off flaws")], "d"),
        ("What is a detection limit?",
         [("a", "The smallest flaw a method can reliably find under given conditions"), ("b", "The longest time a test may run"), ("c", "The highest temperature a probe can take"), ("d", "The largest number of flaws a method can count")], "a"),
        ("What does radiography reveal?",
         [("a", "Surface colour only"), ("b", "Internal flaws, shown by X-rays or gamma rays passing through the part"), ("c", "The chemical composition of the alloy"), ("d", "The electrical resistance of the part")], "b"),
        ("Why is inspection planning important?",
         [("a", "It removes the need for any inspection"), ("b", "It makes all flaws disappear"), ("c", "It guarantees the part has zero risk"), ("d", "It decides which method to use, where to look and how often, so flaws are found in time")], "d"),
    ],
}
