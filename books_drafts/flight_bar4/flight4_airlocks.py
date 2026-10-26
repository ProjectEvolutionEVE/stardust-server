"""Airlocks and Hatches: why a craft needs an airlock, how pressure is balanced, and what station designers learned from hatches."""
CODE = "flight4_airlocks"
BOOK = {
    "title": "Airlocks and Hatches",
    "subtitle": "Moving between air and vacuum safely",
    "chapters": [
        ("Why airlocks", "An airlock lets people move between the air inside a craft and the vacuum outside, without losing the air inside. It is a small room with two doors, and only one door opens at a time."),
        ("Sizes", "An airlock must be big enough for a suited crew member and their tools. It must also be small enough to pump down and refill without wasting too much air."),
        ("Pressure equalisation", "To go out, the airlock is pumped down. To come back in, air is let in slowly until the pressure matches the main cabin. Doing this slowly protects the crew and the seals."),
        ("Seals", "Hatches close against a rubber or metal seal. The seal must stay soft enough to close and firm enough to hold air. Engineers test seals many times before flight."),
        ("Quest and Pirs", "The Quest airlock on the International Space Station was added in 2001 and let crews go out in the same suits used on Shuttle flights. The Pirs module was a Russian docking compartment that also served as an airlock for Russian spacewalks."),
        ("Hatch design lessons", "Hatches are designed to open toward the higher pressure, so that the pressure holds them shut. Station designers also make sure a hatch can be opened from both sides in an emergency."),
    ],
    "test": [
        ("What is an airlock for?", [("a", "To move between inside air and outside vacuum without losing the air"), ("b", "To store food"), ("c", "To cool the engines"), ("d", "To make music")], "a"),
        ("How is pressure balanced before coming back in?", [("a", "The door is opened at once"), ("b", "The crew holds their breath"), ("c", "Water is poured in"), ("d", "Air is let in slowly until it matches the main cabin")], "d"),
        ("When was the Quest airlock added to the International Space Station?", [("a", "In 1901"), ("b", "In 2001"), ("c", "In 2101"), ("d", "It was never added")], "b"),
        ("Why must an airlock have seals that stay soft and firm?", [("a", "So the hatch can float"), ("b", "So it can be painted"), ("c", "So the hatch can close and still hold air"), ("d", "So it is quiet")], "c"),
        ("Why do airlock hatches open toward the higher pressure?", [("a", "So the pressure helps hold them shut"), ("b", "So they fall off"), ("c", "So the air can escape"), ("d", "So the crew can hide")], "a"),
    ],
}
