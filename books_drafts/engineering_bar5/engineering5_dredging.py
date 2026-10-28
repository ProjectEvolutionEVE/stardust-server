"""Dredging Equipment and Slurry Pumping: cutter heads, slurry transport, wear, pipe speeds and production rates."""
CODE = "engineering5_dredging"
BOOK = {
    "title": "Dredging Equipment and Slurry Pumping",
    "subtitle": "Cutter heads, slurry lines, wear and production rates",
    "chapters": [
        ("What a dredge does",
         "A dredge digs sand, gravel or mud from the bottom of a river, harbour or sea. Many dredgers use a rotating cutter head to loosen the material. The loosened material is mixed with water to form a slurry, which is then pumped away."),
        ("Slurry transport",
         "A slurry is solid particles carried in water. The pipe must carry it fast enough that the solids do not settle and block the line. Engineers call the lowest safe speed the deposition velocity, and they design the line to run above it."),
        ("Wear",
         "Slurry is abrasive, so it slowly wears away pump casings, impellers and pipe walls. Wear is worst at bends, where the flow changes direction and particles strike the wall. Crews plan regular checks and replace worn parts before they fail."),
        ("Pipe velocity limits",
         "Running much faster than needed wastes energy and speeds up wear. Running too slowly risks blockage. The best speed sits in a band between those two limits, and the band changes with particle size and the amount of solids."),
        ("Pumps for slurry",
         "Slurry pumps are built heavy and thick-walled to take the abuse. Their impellers and liners are often made of hard, wear-resistant materials. Choosing a pump means balancing how long it lasts against what it costs to run."),
        ("Production rates",
         "A dredge's output is the amount of solid material it moves in a given time. Output depends on cutter speed, pump flow, the solids content of the slurry and the time lost to moving and maintenance. Planners use these figures to price a job and set its schedule."),
    ],
    "test": [
        ("What is a slurry in dredging?",
         [("a", "Solid particles carried in water"), ("b", "A dry sand pile"), ("c", "A steel pipe seal"), ("d", "A fuel for the pump")], "a"),
        ("Why must slurry flow stay above a minimum speed?",
         [("a", "So the pump runs hotter"), ("b", "So the cutter head spins faster"), ("c", "So solids do not settle and block the pipe"), ("d", "So the water stays clear")], "c"),
        ("Where is wear usually worst in a slurry pipe?",
         [("a", "On straight, level runs"), ("b", "At bends where the flow changes direction"), ("c", "At the outlet tank"), ("d", "At the inlet valve")], "b"),
        ("What is a cutter head used for?",
         [("a", "To cool the pump"), ("b", "To measure depth"), ("c", "To seal the pipe"), ("d", "To loosen material on the bottom")], "d"),
        ("What happens if slurry runs much faster than needed?",
         [("a", "Energy is wasted and wear speeds up"), ("b", "All wear stops"), ("c", "The pipe gets stronger"), ("d", "The solids are removed")], "a"),
    ],
}
