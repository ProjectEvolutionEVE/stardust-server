"""Flood defence and hydrology: rainfall runoff, return periods, levees, flood walls, sluice gates and defence economics."""
CODE = "engineering4_flood"
BOOK = {
    "title": "Flood Defence and Hydrology",
    "subtitle": "Runoff, return periods, levees and the cost of defence",
    "chapters": [
        ("Rainfall and runoff",
         "When rain falls, some soaks into the ground and some runs off the surface into streams and rivers. Hydrologists estimate runoff from the land, its slope and how much is paved. More paving means more runoff and faster floods."),
        ("Return periods",
         "A return period says how often a flood of a given size is expected on average. A one-in-100-year flood has a one percent chance of happening in any given year. The term describes chance, not a fixed schedule."),
        ("Levees and flood walls",
         "A levee is an earth embankment built along a river to keep water in its channel. A flood wall is a solid barrier, often of concrete, that stands on the bank or on the edge of a town. Both must be high enough and strong enough for the chosen flood."),
        ("Sluice gates",
         "A sluice gate controls the flow of water through a channel or a barrier. Gates can let water out at low tide or hold it back during a surge. They must be maintained so they work when needed."),
        ("Defence cost against expected damage",
         "Engineers compare the cost of building a defence with the damage it is expected to prevent over its life. A defence costing less than the expected damage it avoids is usually worth building. The comparison is one part of the decision, not the whole of it."),
        ("Keeping defences working",
         "Defences need inspection, repair and operation over many years. Floods can test a defence and reveal weaknesses such as seepage or erosion. Good records and regular checks keep the defence ready for the next flood."),
    ],
    "test": [
        ("What happens to rainfall on a paved surface?", [("a", "It runs off faster, causing quicker floods"), ("b", "It soaks in completely"), ("c", "It turns to ice"), ("d", "It disappears")], "a"),
        ("What does a one-in-100-year flood mean?", [("a", "It happens exactly every 100 years"), ("b", "It is the smallest flood"), ("c", "It lasts 100 days"), ("d", "It has a one percent chance of happening in any given year")], "d"),
        ("What is a levee?", [("a", "A solid glass wall"), ("b", "An earth embankment built along a river"), ("c", "A type of boat"), ("d", "A kind of paving")], "b"),
        ("What is a sluice gate used for?", [("a", "To store coal"), ("b", "To light a street"), ("c", "To control the flow of water through a channel or barrier"), ("d", "To make paper")], "c"),
        ("How do engineers judge whether a defence is worth building?", [("a", "By the colour of the water"), ("b", "By counting the trees beside it"), ("c", "By comparing its cost with the expected damage it avoids"), ("d", "By ignoring the cost")], "c"),
    ],
}
