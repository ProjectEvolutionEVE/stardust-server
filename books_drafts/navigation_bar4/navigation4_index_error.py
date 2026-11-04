"""Index Error and Sextant Checks: finding, measuring and recording a sextant's built-in error."""
CODE = "navigation4_index_error"
BOOK = {
    "title": "Index Error and Sextant Checks",
    "subtitle": "Finding and recording the sextant's built-in error",
    "chapters": [
        ("What index error is", "A sextant should read zero when its two mirrors are set parallel. Often it reads a little off zero. That small error is called index error, and it must be corrected in every sight."),
        ("Measuring on the horizon", "To find index error, point the sextant at a clear horizon and bring the image of the horizon down to the true horizon. Read the angle. Repeat several times and take the average."),
        ("The Sun's limb", "You can also measure the Sun's edge, or limb. Bring the lower edge onto the horizon, then the upper edge. Averaging the two readings cancels out the size of the Sun."),
        ("Side error", "Side error happens when the index mirror is not perpendicular to the frame. It shows as a sideways offset when the image is brought down. Check for it by looking at a star or the horizon from several angles."),
        ("Adjusting the instrument", "Many sextants have small screws that adjust the mirrors. Adjust them carefully, a little at a time, and check each change. Some navigators prefer to leave the instrument alone and record the correction instead."),
        ("Recording the correction", "Write the index correction in your log with the date and the sextant used. Apply it to every sight taken with that instrument. A clear record prevents errors when the instrument is used again."),
    ],
    "test": [
        ("What should a sextant read when its mirrors are parallel?",
         [("a", "Ninety degrees"), ("b", "The latitude"), ("c", "Zero"), ("d", "The time")], "c"),
        ("Where is index error often measured?",
         [("a", "On the Moon's dark side"), ("b", "In the cabin"), ("c", "Only at night"), ("d", "On the horizon or the Sun's edge")], "d"),
        ("What is side error?",
         [("a", "Error from the ship's engine"), ("b", "The index mirror is not perpendicular to the frame"), ("c", "Wind on the sextant"), ("d", "Misreading the tables")], "b"),
        ("Why average the readings on the Sun's two edges?",
         [("a", "It cancels out the Sun's size"), ("b", "It makes the Sun brighter"), ("c", "It removes refraction entirely"), ("d", "It stops the sextant drifting")], "a"),
        ("What should you do with the index correction?",
         [("a", "Throw it away after one sight"), ("b", "Use it only at night"), ("c", "Add it to the time"), ("d", "Record it and apply it to every sight")], "d"),
    ],
}
