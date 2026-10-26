"""Docking at the Starship: bow and stern approaches, the guide lights and the last few metres."""
CODE = "flight2_docking"
BOOK = {
    "title": "Docking at the Starship",
    "subtitle": "Bow and stern approaches, the guide lights and the final stretch",
    "chapters": [
        ("Two ways in",
         "The Starship's belly bay is open at both ends, so you can dock from the bow or from the stern. The autopilot comes in from whichever end you are nearer. The status line tells you which: DOCKING under the bow, or DOCKING in under the stern."),
        ("The guide lights",
         "Each end of the bay has a lane of soft green lights that runs out from the approach point into the mouth of the bay. The lights pulse in turn, moving toward the ship, so the lane shows you the way in. Keep the lane in the middle of your view."),
        ("Lining up on the mouth",
         "Before the last stretch, point the nose straight down the lane. A slight slide to one side can put a craft off the centre line. Use the side thrusters for small corrections, and keep your speed low while you do it."),
        ("The last few metres",
         "The approach ends short of the mouth, so the craft must stop in the right place. Docking is slow for the same reason real docking is slow: at the end there is little room for error. Watch the approach number and go gently."),
        ("Taking over",
         "If the autopilot is flying you in and something is wrong, press and hold to take the controls. Once you have them, line up again slowly. There is no reason to rush a dock."),
        ("Once you are in",
         "When the craft is docked, the status line reads DOCKED, and it is safe to stop. Your quarters are aboard the Starship, not out in space, and the Desk and your Market terminal are there too."),
    ],
    "test": [
        ("How many ends of the Starship's belly bay are open?",
         [("a", "None"), ("b", "One"), ("c", "Two"), ("d", "Four")], "c"),
        ("What does the status line reading DOCKING in under the stern mean?",
         [("a", "You are flying in through the stern end of the bay"), ("b", "The hold is full"), ("c", "The bay is closed for repairs"), ("d", "You have already landed on the deck")], "a"),
        ("What do the guide lights in each lane do?",
         [("a", "Show how many bars you have"), ("b", "Warn you of debris"), ("c", "Pulse toward the ship to show the way in"), ("d", "Count the pieces you collect")], "c"),
        ("What should you do if the autopilot is flying you in and you need to correct?",
         [("a", "Let go and wait"), ("b", "Warp home at once"), ("c", "Unload straight away"), ("d", "Press and hold to take the controls")], "d"),
        ("What does DOCKED mean for your quarters?",
         [("a", "They are out in space"), ("b", "They are sold"), ("c", "They are aboard the Starship"), ("d", "They are closed until morning")], "c"),
    ],
}
