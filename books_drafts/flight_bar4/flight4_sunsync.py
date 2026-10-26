"""Sun-synchronous Orbits: a special tilt that keeps a satellite passing over the ground at the same local time."""
CODE = "flight4_sunsync"
BOOK = {
    "title": "Sun-synchronous Orbits",
    "subtitle": "Passing over the ground at the same time of day",
    "chapters": [
        ("The Sun's yearly turn", "The Earth goes once round the Sun in a year, so the Sun seems to move slowly across the sky over that time. A sun-synchronous orbit turns once a year too, so it keeps pace with the Sun."),
        ("The special tilt", "To turn about once a year, the orbit must be tilted just past a right angle. For a low orbit around the Earth this is close to ninety-eight degrees. The J2 drift from the planet's bulge does the turning."),
        ("Constant lighting", "Because the orbit keeps pace with the Sun, each pass over a place happens at the same local time of day. The light on the ground is similar from one pass to the next. That makes comparisons over time much easier."),
        ("Morning and afternoon passes", "A satellite may pass in the morning or in the afternoon, depending on the chosen orbit. Planners pick the time of day that suits the job, such as a mid-morning pass for clear pictures with good shadows."),
        ("Imaging uses", "Many Earth-watching satellites use these orbits. Farmers, scientists and mapmakers all gain from pictures taken under the same light. Comparing one year with another is far easier this way."),
        ("Limits", "A sun-synchronous orbit has a fixed local time, so it cannot cover every hour of the day. Its height and tilt are also set tightly, and a change of height changes the turn rate, so the design must be exact."),
    ],
    "test": [
        ("What does a sun-synchronous orbit keep pace with?", [("a", "The Moon"), ("b", "A passing comet"), ("c", "The Sun's yearly motion"), ("d", "The rotation of Mars")], "c"),
        ("About what tilt is typical for a low sun-synchronous orbit around Earth?", [("a", "About ninety-eight degrees"), ("b", "Zero degrees"), ("c", "Thirty degrees"), ("d", "Forty degrees")], "a"),
        ("Why is the lighting on the ground similar from pass to pass?", [("a", "The Earth stopped turning"), ("b", "Clouds are removed"), ("c", "The satellite has its own lamp"), ("d", "The orbit keeps the same local time of day")], "d"),
        ("What can a fixed local time limit?", [("a", "Every hour of the day"), ("b", "Which hours of the day the satellite can see"), ("c", "The speed of light"), ("d", "The size of the crew")], "b"),
        ("Which kind of work uses these orbits often?", [("a", "Earth-watching and mapping"), ("b", "Cooking"), ("c", "Playing music"), ("d", "Underwater diving")], "a"),
    ],
}
