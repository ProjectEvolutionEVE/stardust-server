"""Offshore Jacket Structures and Fatigue: wave loads, jacket frames, joint fatigue, corrosion allowances and inspection plans."""
CODE = "engineering5_offshore_jacket"
BOOK = {
    "title": "Offshore Jacket Structures and Fatigue",
    "subtitle": "Waves, joints, corrosion and the inspection plan",
    "chapters": [
        ("What a jacket is",
         "A jacket is a steel frame of tubes that stands on the seabed and holds up a platform above the waves. Its legs and braces are welded together at joints. The whole frame must carry its own weight and the loads from wind, waves and current."),
        ("Wave loads",
         "Waves push on the frame again and again, and the size of each push depends on the wave height and period. Engineers design for rare, very large storms and also for the everyday waves that come round constantly. Both kinds of load shape the final frame."),
        ("Joint fatigue",
         "Fatigue is damage that builds up when a metal part is loaded and unloaded many times. Cracks often start at the welded joints, where stress is concentrated. A joint can fail well below the load it could carry once, if the cycles keep coming."),
        ("Corrosion allowance",
         "Seawater rusts steel, so designers add a corrosion allowance, which is extra thickness that is lost to rust over the design life. Coatings and protective anodes add further defence. Each of these choices costs money and must be checked."),
        ("Inspection planning",
         "Operators inspect the jacket on a planned schedule, often with divers and remote underwater vehicles. The plan targets the joints most likely to crack. A good plan balances the cost of each inspection against the risk of missing a defect."),
        ("The money side",
         "Inspection, repair and downtime are all costs, and a platform that stops producing loses income each day. Engineers weigh the price of stronger steel, more frequent checks and early repair against the cost of a failure. Clear records make these decisions easier to defend."),
    ],
    "test": [
        ("What is the frame of an offshore jacket made from?",
         [("a", "Wood beams"), ("b", "Glass panels"), ("c", "Steel tubes welded at joints"), ("d", "Stacked stone blocks")], "c"),
        ("What is fatigue?",
         [("a", "Damage that builds up from repeated loading"), ("b", "Rust on the surface only"), ("c", "A fall in the price of steel"), ("d", "The weight of the platform")], "a"),
        ("Where do fatigue cracks often start?",
         [("a", "At the top of the platform deck"), ("b", "At the welded joints, where stress is concentrated"), ("c", "In the paint"), ("d", "In the cables on the crane")], "b"),
        ("What is a corrosion allowance?",
         [("a", "A payment to the seabed owner"), ("b", "A discount on coatings"), ("c", "Extra thickness lost to rust over the design life"), ("d", "A limit on how many divers may enter the water")], "c"),
        ("What does a good inspection plan balance?",
         [("a", "The colour of the platform against its height"), ("b", "The cost of each inspection against the risk of missing a defect"), ("c", "The number of crew against the number of cranes"), ("d", "The price of fuel against the price of paint")], "b"),
    ],
}
