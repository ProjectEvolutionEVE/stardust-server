"""Pit Lake Chemistry and Filling: how water collects in a closed open pit, how it layers and changes, and how the filling is managed over time."""
CODE = "mining5_pit_lake"
BOOK = {
    "title": "Pit Lake Chemistry and Filling",
    "subtitle": "Stratification, oxygen, water quality, filling time and closure",
    "chapters": [
        ("A lake in the hole",
         "When a mine closes and the pumps stop, groundwater and rain fill the pit. The result is a pit lake. Its water quality and behaviour must be planned long before the pumps are switched off."),
        ("Stratification",
         "A deep lake can form layers. Warm water sits on top of cold, dense water, and the layers may not mix. Stratification controls where oxygen and chemicals end up in the lake."),
        ("Oxygen",
         "Oxygen is needed by many natural processes. The top of a lake usually has oxygen, while the deep water may not. Low oxygen can release metals from the rock into the water."),
        ("Water quality",
         "Pit lake water can contain metals, sulphate and acidity, depending on the rock. Monitoring the pH and key metals shows how the lake is changing. Water that does not meet the standard must be treated or managed."),
        ("Filling time",
         "Filling can take years to decades, depending on the size of the pit and the inflow of water. Engineers estimate the filling time with models and check it against monitoring. The filling time sets when the lake is safe to use or to discharge."),
        ("Treatment and closure",
         "The closure plan sets the goal for the lake and the steps to reach it. Treatment may be needed for a time, and a long-term plan must cover the water after treatment stops. The closure plan is reviewed as the lake matures."),
    ],
    "test": [
        ("How does a pit lake form?",
         [("a", "Milk is poured into the pit"), ("b", "Ice is trucked in"), ("c", "Groundwater and rain fill a pit after the pumps stop"), ("d", "It is painted blue")], "c"),
        ("What is stratification in a deep lake?",
         [("a", "Stones stacked on the shore"), ("b", "The lake becoming a road"), ("c", "Fish swimming in rows"), ("d", "Layers that may not mix, such as warm water over cold")], "d"),
        ("Why does low oxygen in deep water matter?",
         [("a", "It makes the water sweet"), ("b", "It can release metals from the rock into the water"), ("c", "It makes the pit larger"), ("d", "It makes the sky darker")], "b"),
        ("How long can pit filling take?",
         [("a", "Years to decades, depending on the pit and the inflow"), ("b", "Exactly one minute"), ("c", "Always less than a day"), ("d", "It never fills")], "a"),
        ("What does a closure plan cover?",
         [("a", "The goal for the lake and the steps to reach it, including water after treatment"), ("b", "Only the colour of the fence"), ("c", "Only the name of the car park"), ("d", "Nothing about water")], "a"),
    ],
}
