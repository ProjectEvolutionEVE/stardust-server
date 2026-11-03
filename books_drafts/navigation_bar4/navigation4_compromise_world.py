"""Compromise World Projections: why no flat world map is perfect, and how to choose one."""
CODE = "navigation4_compromise_world"
BOOK = {
    "title": "Compromise World Projections",
    "subtitle": "Why no world map is perfect",
    "chapters": [
        ("No perfect world map", "No flat map of the whole Earth can be right in every way. Shape, area, distance and direction cannot all be kept at once. Every map trades one property for another."),
        ("The Robinson design", "The Robinson projection was designed to look pleasing. It is neither equal-area nor conformal. It keeps shapes and sizes reasonably balanced across the whole world."),
        ("The Winkel tripel", "The Winkel tripel is a compromise projection used by many atlases. It balances area, distance and direction. It is often chosen for general world maps."),
        ("Trade-offs", "Area, shape and distance are the main trade-offs. A map that keeps area right will distort shape. A map that keeps distance right will distort something else."),
        ("Choosing one for a purpose", "Choose a map to suit your purpose. A map of ocean currents needs different care than a map of countries. Ask what you most need to measure."),
        ("Reading the chart", "Read the chart's notes to see what it is good at. A compromise map is a fair general picture, not an exact tool. Use the right map for each job."),
    ],
    "test": [
        ("Why is no flat world map perfect?",
         [("a", "Shape, area, distance and direction cannot all be kept at once"), ("b", "Paper is too thin"), ("c", "The Earth has no sides"), ("d", "Maps are always blue")], "a"),
        ("What was the Robinson projection designed to do?",
         [("a", "Measure ships"), ("b", "Look pleasing"), ("c", "Show the Moon"), ("d", "Sell maps")], "b"),
        ("Which compromise projection is used by many atlases?",
         [("a", "Gnomonic"), ("b", "Polyconic"), ("c", "Winkel tripel"), ("d", "Sinusoidal")], "c"),
        ("What is the main trade-off mentioned?",
         [("a", "Colour, font and size"), ("b", "Area, shape and distance"), ("c", "Price, weight and paper"), ("d", "Night and day")], "b"),
        ("How should a compromise map be read?",
         [("a", "As an exact survey"), ("b", "As a navigation chart"), ("c", "As a weather report"), ("d", "As a fair general picture, not an exact tool")], "d"),
    ],
}
