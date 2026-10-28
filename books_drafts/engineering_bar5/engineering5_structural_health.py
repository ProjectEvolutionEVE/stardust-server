"""Structural Health Monitoring: watching a structure through sensors so repairs happen at the right time."""
CODE = "engineering5_structural_health"
BOOK = {
    "title": "Structural Health Monitoring",
    "subtitle": "Watching a structure through sensors so repairs happen at the right time",
    "chapters": [
        ("Sensors on the structure",
         "Structural health monitoring fits sensors such as accelerometers, strain gauges and temperature sensors to a structure. The readings show how it behaves over time."),
        ("Modal shift detection",
         "As a structure is damaged, its natural frequencies usually drop a little. Tracking these frequencies can give an early sign of change."),
        ("Damage indices",
         "A damage index combines measured changes into a single number that rises when something is wrong. Setting its alarm level needs care to avoid false alarms."),
        ("Data management",
         "Sensor networks produce large amounts of data. Storing, checking and comparing it needs a plan, including the removal of faulty readings."),
        ("Deciding when to repair",
         "Monitoring helps decide whether to repair now or later, by estimating how the damage will grow. The money side compares the cost of monitoring and repair with the cost of failure."),
        ("Keep it realistic",
         "Monitoring cannot find every flaw, and it depends on good sensor placement. It supports inspection rather than replacing it."),
    ],
    "test": [
        ("What do accelerometers and strain gauges on a monitored structure do?",
         [("a", "Paint it"), ("b", "Heat it"), ("c", "Measure how it behaves over time"), ("d", "Count visitors")], "c"),
        ("What usually happens to natural frequencies as damage grows?",
         [("a", "They drop a little"), ("b", "They rise a lot"), ("c", "They never change"), ("d", "They turn to colour")], "a"),
        ("What does a damage index do?",
         [("a", "Sells parts"), ("b", "Counts days"), ("c", "Paints walls"), ("d", "Combines measured changes into one number that rises when something is wrong")], "d"),
        ("What must a sensor network plan include?",
         [("a", "Only a colour scheme"), ("b", "Removing faulty readings"), ("c", "Nothing"), ("d", "Price tags")], "b"),
        ("What is true of structural health monitoring?",
         [("a", "It cannot find every flaw, and sensor placement matters"), ("b", "It finds every flaw perfectly"), ("c", "It needs no sensors"), ("d", "It replaces all inspection")], "a"),
    ],
}
