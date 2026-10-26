"""The Approach: closing in on a target slowly and in control, from the first sight of it to the last few metres."""
CODE = "flight2_approach"
BOOK = {
    "title": "The Approach",
    "subtitle": "Closing in slowly and in control, from far away to the final stretch",
    "chapters": [
        ("Start slow, finish slower",
         "Closing speed is how fast the gap between you and a target shrinks. A careful approach is flown slowly near the end, because a fast arrival leaves no time to fix a mistake. Aim to arrive at a crawl, not a rush."),
        ("Read the distance",
         "The large, faint number on the screen shows how far away the thing the scanner is tracking lies. Watch how it falls as you come in. If it falls faster than you want, bring the throttle down before you reach the target."),
        ("Let the autopilot slow",
         "On a long trip the autopilot cruises fast, up to 900 metres a second, and slows as it nears its target. Watch the speed fall as it comes in, and do not fight it near the end unless you must."),
        ("Line up, then set the speed",
         "Before you close in, make sure you are heading straight at the target, and only then set your speed. A craft lined up but moving too fast will sweep past, while a craft slow but off line will never arrive."),
        ("Stopping needs room",
         "A craft keeps moving until something changes its speed, so stopping takes distance. Plan the stopping point before you start the approach, and leave a margin. In the game, turning the throttle down makes the craft coast down to the new speed, so start easing off early."),
        ("Taking back the controls",
         "When the autopilot is flying you in, the status line reads AUTOPILOT, and pressing and holding takes the controls back. Use it when the autopilot cannot see what you can, such as a rock on the line. Then take it slowly and line up again."),
    ],
    "test": [
        ("What is closing speed?",
         [("a", "How loud the scanner is"), ("b", "How fast the gap between you and a target is shrinking"), ("c", "The number of bars you have"), ("d", "The speed of light")], "b"),
        ("Why do careful approaches slow down near the target?",
         [("a", "The radar needs time to scan"), ("b", "The hold fills up at high speed"), ("c", "A fast arrival leaves no time to fix a mistake"), ("d", "Gravity gets stronger near the bay")], "c"),
        ("What does the autopilot do as it nears its target?",
         [("a", "Speeds up to dock"), ("b", "Switches off the scanner"), ("c", "Slows down as it arrives"), ("d", "Turns off the lights in the bay")], "c"),
        ("In the game, what happens when you turn the throttle down under power?",
         [("a", "The craft stops on the spot"), ("b", "The craft turns around"), ("c", "The hold empties"), ("d", "The craft coasts down to the new speed")], "d"),
        ("What does pressing and holding do while the autopilot is flying you in?",
         [("a", "Ends the flight at once"), ("b", "Starts collecting"), ("c", "Calls the Tower"), ("d", "Takes the controls back")], "d"),
    ],
}
