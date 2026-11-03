"""Plate Motion and the Moving Frame: why coordinates change even when nothing seems to move."""
CODE = "navigation4_plate_motion"
BOOK = {
    "title": "Plate Motion and the Moving Frame",
    "subtitle": "Why coordinates change even when nothing seems to move",
    "chapters": [
        ("Continents drift", "The Earth's crust is broken into plates. The plates move slowly, usually a few centimetres each year. Over decades, that movement adds up to a large change."),
        ("A frame fixed to a plate", "A plate-fixed frame moves with the plate. Points on that plate keep nearly the same coordinates in that frame. Points on other plates do not."),
        ("Coordinates changing each year", "In a fixed global frame, coordinates on a moving plate change every year. The change is small but real. Precise work must include it."),
        ("Epoch dates", "A coordinate is given at a particular epoch, which is a date. The coordinate is valid for that date. To use it at a later date, you must update it to the new epoch."),
        ("Velocity models", "A velocity model describes how fast each point moves. It is built from measurements taken over time. Using it, you can estimate a point's position at any date."),
        ("Updating coordinates", "To update a coordinate, multiply the velocity by the time since the epoch, then add the result. Check the units first. A careful update keeps old and new surveys in agreement."),
    ],
    "test": [
        ("What is a typical speed for a tectonic plate?",
         [("a", "A few kilometres per second"), ("b", "A few metres per hour"), ("c", "A few centimetres per year"), ("d", "Not at all")], "c"),
        ("What does a plate-fixed frame do?",
         [("a", "It stays still forever"), ("b", "It moves with the plate"), ("c", "It moves with the Sun"), ("d", "It only shows the oceans")], "b"),
        ("What is an epoch?",
         [("a", "A type of rock"), ("b", "A kind of map"), ("c", "A survey instrument"), ("d", "A particular date for which a coordinate is valid")], "d"),
        ("What does a velocity model give?",
         [("a", "How fast each point moves"), ("b", "The colour of the continents"), ("c", "The depth of the ocean"), ("d", "The name of the satellite")], "a"),
        ("What is the first step to update a coordinate?",
         [("a", "Multiply the velocity by the time since the epoch"), ("b", "Round it to whole metres"), ("c", "Erase the old value"), ("d", "Measure it again from the Moon")], "a"),
    ],
}
