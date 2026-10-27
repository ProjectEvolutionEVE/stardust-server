"""Overland Conveyors and Bulk Handling: moving ore over long distances on belts, with attention to tension, idlers, transfer points and dust."""
CODE = "mining5_conveyor"
BOOK = {
    "title": "Overland Conveyors and Bulk Handling",
    "subtitle": "Belt tension, idlers, transfer points, dust and capacity",
    "chapters": [
        ("Belts over the hills",
         "An overland conveyor carries bulk ore across rough country on a long belt. It can replace many trucks and use less energy per tonne. The belt runs over rollers and between drive pulleys."),
        ("Belt tension",
         "The belt must be held at the right tension. Too little tension lets the belt slip on the drive pulley. Too much tension stresses the belt and the structure and shortens its life."),
        ("Idlers",
         "Idlers are the rollers that support the belt along its length. Worn or stuck idlers add friction and heat, and they can damage the belt. Regular checks keep them turning freely."),
        ("Transfer points",
         "Where one belt passes material to another, there is a transfer point. Transfer points are where spillage and dust are most likely. They need good chutes, skirts and maintenance."),
        ("Dust",
         "Dust from belts and transfer points can harm workers and the environment. Water sprays, enclosures and dust collection reduce it. Monitoring shows whether the controls are working."),
        ("Capacity",
         "Belt capacity depends on belt speed and the cross-section of the load. A wider or faster belt carries more tonnes per hour. Planning for capacity also considers breakdown time and spare parts."),
    ],
    "test": [
        ("What is an overland conveyor used for?",
         [("a", "To carry people to school"), ("b", "To carry bulk ore across rough country on a long belt"), ("c", "To carry water in glass jars"), ("d", "To carry letters")], "b"),
        ("What happens if belt tension is too low?",
         [("a", "The belt can slip on the drive pulley"), ("b", "The belt gets lighter"), ("c", "The belt becomes a rope"), ("d", "The belt turns to dust")], "a"),
        ("What do idlers do?",
         [("a", "Support the belt along its length"), ("b", "Cook the ore"), ("c", "Count the tonnes"), ("d", "Print the schedule")], "a"),
        ("Where is spillage and dust most likely?",
         [("a", "At the office desk"), ("b", "In the canteen"), ("c", "At transfer points"), ("d", "On the top of the hill")], "c"),
        ("What controls belt capacity?",
         [("a", "The colour of the belt"), ("b", "The name of the company"), ("c", "The weather on Friday"), ("d", "Belt speed and the cross-section of the load")], "d"),
    ],
}
