"""The instrument landing system: localiser, glide path, markers, decision height, approach categories and limits."""
CODE = "navigation4_ils"
BOOK = {
    "title": "The Instrument Landing System",
    "subtitle": "A radio path down to the runway",
    "chapters": [
        ("A guided approach", "The instrument landing system guides an aircraft down to the runway in poor visibility. Radio signals give the pilot a path to follow. It is one of the most important landing aids."),
        ("The localiser", "The localiser gives left and right guidance along the runway's centreline. The pilot keeps the needle centred to stay on track. It works from beyond the runway end."),
        ("The glide path", "The glide path gives up and down guidance on a set slope, usually about three degrees. The pilot keeps the aircraft on this slope down to the runway."),
        ("Markers", "Marker beacons along the approach signal distances from the runway. They help the pilot check position as the aircraft descends."),
        ("Decision height", "Decision height is the point at which the pilot must either see the runway or go around. It is set for each approach. Without the view, the pilot must go around."),
        ("Approach categories and limits", "ILS approaches are grouped into categories, according to how low an aircraft may descend in poor visibility. Limits include signal interference and the need for correct equipment. Pilots and airports must meet each category's rules."),
    ],
    "test": [
        ("What does ILS guide an aircraft to?", [("a", "The runway, in poor visibility"), ("b", "The top of a mountain"), ("c", "The nearest bakery"), ("d", "The surface of the ocean")], "a"),
        ("What does the localiser provide?", [("a", "Up and down guidance only"), ("b", "The weather at the destination"), ("c", "Left and right guidance along the centreline"), ("d", "The fuel quantity")], "c"),
        ("What is the typical glide path angle?", [("a", "About thirty degrees"), ("b", "About three degrees"), ("c", "About ninety degrees"), ("d", "About zero degrees")], "b"),
        ("What is decision height?", [("a", "The height of the control tower"), ("b", "The top of the aircraft's tail"), ("c", "The altitude of cruise flight"), ("d", "The point to see the runway or go around")], "d"),
        ("Why are ILS approach categories set?", [("a", "To choose the colour of the runway lights"), ("b", "To set the price of landing fees"), ("c", "They limit how low an aircraft may descend in poor visibility, by equipment and training"), ("d", "To decide the number of passengers")], "c"),
    ],
}
