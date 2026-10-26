"""Rendezvous: how one craft meets another in space, and why catching up can mean going faster in a lower orbit."""
CODE = "flight2_rendezvous"
BOOK = {
    "title": "Rendezvous",
    "subtitle": "Meeting another craft at the right place and the right time",
    "chapters": [
        ("Meeting a moving target",
         "A rendezvous is meeting another craft at a planned place and time. Both craft move very fast, so you cannot simply aim and fly straight at the target. You must match its path and its speed first."),
        ("Matching speed",
         "The first job is to match speed and direction, so the two craft move together. Two craft at the same speed in the same direction keep the same gap between them. Only then should you start closing the distance slowly."),
        ("Catching up in orbit",
         "A craft in a lower orbit travels faster than one above it. So to catch a craft that is ahead, a chaser can drop to a lower orbit, move faster, and then rise again to meet it. It sounds backwards, but it is how real craft close in on one another."),
        ("Timing the meeting",
         "A rendezvous depends on timing as well as position. A craft that arrives early or late must wait in orbit or make another burn. Real missions plan their meetings many orbits ahead, so there is time to adjust."),
        ("Fixed targets in the game",
         "In the game, the autopilot flies you to a locked field or to the Starship, and it keeps the nose on the target and slows as it arrives. The targets stay where they are, so the job is simpler. The habit of matching before closing still holds."),
        ("The slow last stretch",
         "The final stretch of any rendezvous is slow. Speed must be close to zero relative to the target by the time you arrive, or the meeting becomes a collision. Plan that stop before you start."),
    ],
    "test": [
        ("What is a rendezvous?",
         [("a", "Meeting another craft at a planned place and time"), ("b", "Hiding from debris"), ("c", "Turning off the scanner"), ("d", "Leaving the Starship for good")], "a"),
        ("What is the first job before you close on a moving target?",
         [("a", "Turn off the lights"), ("b", "Fill the hold"), ("c", "Warp past it"), ("d", "Match its speed and direction")], "d"),
        ("To catch a craft that is ahead of you in a similar orbit, what can you do?",
         [("a", "Stop completely and wait"), ("b", "Turn around and go the other way"), ("c", "Drop to a lower orbit and move faster"), ("d", "Wait for it to come back")], "c"),
        ("Why does a rendezvous need good timing as well as good position?",
         [("a", "The target's position changes as it moves"), ("b", "Radar only works at night"), ("c", "The hold gets heavier over time"), ("d", "Timing only matters for gold")], "a"),
        ("How fast should you be moving relative to the target at the very end?",
         [("a", "Fast, to make an impact"), ("b", "Exactly the speed of light"), ("c", "Whatever speed the autopilot likes"), ("d", "Close to zero")], "d"),
    ],
}
