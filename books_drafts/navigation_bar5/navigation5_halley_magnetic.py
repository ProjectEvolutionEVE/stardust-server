"""Halley's Magnetic Charts: magnetic variation, isogonic lines, the observations behind them, their use by ships and their impact."""
CODE = "navigation5_halley_magnetic"
BOOK = {
    "title": "Halley's Magnetic Charts",
    "subtitle": "Magnetic variation, isogonic lines and the ships that made them",
    "chapters": [
        ("Magnetic variation",
         "A compass points to magnetic north, which is not the same as true north. The difference is called magnetic variation. Its size changes from place to place, so every chart must allow for it."),
        ("Isogonic lines",
         "An isogonic line joins places that share the same magnetic variation. Drawing these lines on a chart helps a navigator correct the compass reading. Edmond Halley published one of the first such charts around 1700."),
        ("Observations",
         "Halley gathered compass readings taken by ships at sea. Many observations were needed before the lines could be drawn with any confidence. Careful records made the charts better over time."),
        ("Ships",
         "Crews used charts like these to correct their compass courses. Without that correction, a ship could drift far off its planned track. Good charts were valuable on long voyages where a small error grew with every mile."),
        ("Lessons",
         "The charts showed that the Earth's magnetic field is not uniform. They also showed that variation changes over time. Navigators had to check their charts against newer readings."),
        ("Impact",
         "Halley's work helped make the study of the Earth's magnetism a careful science. Later charts of magnetic variation grew from his idea. Magnetic charts are still made and updated today."),
    ],
    "test": [
        ("What does a compass point to?",
         [("a", "Exactly true north"), ("b", "Magnetic north"), ("c", "The Sun"), ("d", "The pole star")], "b"),
        ("What is an isogonic line?",
         [("a", "A line of ships at sea"), ("b", "A line of latitude"), ("c", "A line that shows the coast"), ("d", "A line joining places with the same magnetic variation")], "d"),
        ("What did Halley need in order to draw the lines with confidence?",
         [("a", "One reading only"), ("b", "Guesses"), ("c", "Many observations taken by ships"), ("d", "A new telescope")], "c"),
        ("Why did ships' crews use these charts?",
         [("a", "To correct their compass courses"), ("b", "To find gold"), ("c", "To measure the size of the Sun"), ("d", "To write songs")], "a"),
        ("What did the charts show about the Earth's magnetic field?",
         [("a", "It is perfectly even"), ("b", "It is not uniform and changes over time"), ("c", "It does not exist"), ("d", "It is found only in the north")], "b"),
    ],
}
