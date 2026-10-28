"""Planetary Gear Trains: sun, planet and ring gears, ratios, load sharing between planets, compact gearboxes and efficiency."""
CODE = "engineering4_planetary"
BOOK = {
    "title": "Planetary Gear Trains",
    "subtitle": "Sun, planets, ring and load sharing",
    "chapters": [
        ("The parts",
         "A planetary gear train has a central sun gear, several planet gears that orbit it, and a ring gear with internal teeth around them. The planets are held on a carrier."),
        ("Ratios",
         "The ratio depends on which part is held, which is driven and which gives the output. A planetary set gives a high ratio in a small space."),
        ("Load sharing",
         "Several planets share the load, so each carries less. Even sharing needs careful tooth spacing and accurate parts."),
        ("Compact gearboxes",
         "The load is spread across the planets, and the gears sit inside one another. That makes planetary sets compact for the torque they carry. They are common in automatic transmissions and electric drives."),
        ("Efficiency",
         "Planetary gears are efficient because the load splits between planets. Each meshing point still loses a little power."),
        ("Choosing a train",
         "Designers pick the number of planets and the tooth counts to reach the ratio and the load capacity they need. The design must also fit the space and the cooling the gearbox has."),
    ],
    "test": [
        ("What are the three main parts of a planetary gear train?",
         [("a", "Sun, planets and ring"), ("b", "Wheels, belt and chain"), ("c", "Shaft, key and spline"), ("d", "Spring, damper and strut")], "a"),
        ("What does sharing the load among planets do?",
         [("a", "Adds paint"), ("b", "Stops rotation"), ("c", "Each planet carries less load"), ("d", "Each planet carries more load")], "c"),
        ("Why are planetary sets compact?",
         [("a", "They have no teeth"), ("b", "They use no load"), ("c", "They are large and flat"), ("d", "The load spreads over the planets and the gears sit inside one another")], "d"),
        ("Where are planetary sets common?",
         [("a", "Paint shops"), ("b", "Kitchen tables"), ("c", "Sails"), ("d", "Automatic transmissions and electric drives")], "d"),
        ("What does a planetary set's ratio depend on?",
         [("a", "Colour"), ("b", "Weather"), ("c", "Music"), ("d", "Which part is held, which is driven and which is the output")], "d"),
    ],
}
