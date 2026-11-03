"""Twilight and the Visible Horizon: civil, nautical and astronomical twilight, the visible horizon, sight timing, constraints, planning and clouds."""
CODE = "navigation5_twilight_horizon"
BOOK = {
    "title": "Twilight and the Visible Horizon",
    "subtitle": "When the horizon and the stars can both be seen",
    "chapters": [
        ("Civil, nautical and astronomical",
         "At dawn, astronomical twilight begins when the Sun is eighteen degrees below the horizon, nautical twilight at twelve, and civil twilight at six. At dusk the same stages come in reverse. Navigators work in nautical twilight, when the horizon is still visible and the stars show."),
        ("The visible horizon",
         "The visible horizon is the line where sea meets sky, as seen from the observer's eye. It sits a little below the true horizon because of the observer's height. A higher observer sees it farther away."),
        ("Sight timing",
         "A sextant sight is timed to take a star or planet with the horizon in view. The time must be recorded accurately. Timing errors show up directly as errors in position."),
        ("Constraints",
         "Sights need enough light to show the horizon and enough darkness to show the stars. Those two needs define a short window each evening and morning. The window varies with latitude and season."),
        ("Planning",
         "Navigators plan their sights ahead, choosing stars that will be well placed within the window. A good plan gives a spread of stars across the sky. Good plans reduce error."),
        ("Clouds",
         "Clouds can hide the horizon or the stars. When clouds block the sights, navigators fall back on other methods. Knowing the limits of sights is part of the craft."),
    ],
    "test": [
        ("At dawn, how far below the horizon is the Sun when nautical twilight begins?",
         [("a", "Six degrees"), ("b", "Twelve degrees"), ("c", "Eighteen degrees"), ("d", "Zero degrees")], "b"),
        ("What makes the visible horizon sit below the true horizon?",
         [("a", "The Moon"), ("b", "The wind"), ("c", "The observer's height"), ("d", "The colour of the sea")], "c"),
        ("What is a sextant sight timed to take?",
         [("a", "A star or planet with the horizon in view"), ("b", "The far side of the Moon"), ("c", "A bird"), ("d", "A cloud")], "a"),
        ("What must sights have?",
         [("a", "No light at all"), ("b", "Only sunlight"), ("c", "Fog"), ("d", "Enough light to show the horizon and enough darkness to show the stars")], "d"),
        ("What can clouds do during a sight?",
         [("a", "Make stars brighter"), ("b", "Help the sight"), ("c", "Stop the sea"), ("d", "Hide the horizon or the stars")], "d"),
    ],
}
