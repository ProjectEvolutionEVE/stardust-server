"""Seven-Parameter Helmert Transforms: moving coordinates from one reference frame to another."""
CODE = "navigation4_helmert"
BOOK = {
    "title": "Seven-Parameter Helmert Transforms",
    "subtitle": "Moving coordinates from one frame to another",
    "chapters": [
        ("Why transform coordinates", "Different surveys use different reference frames. Coordinates in one frame must be converted to another before they can be compared. A transformation does that job."),
        ("Three shifts", "Three shifts move the origin of one frame to match the other. They are shifts along the X, Y and Z axes. Together they describe where the centres of the two frames lie."),
        ("Three rotations", "Three small rotations turn one frame to line up with the other. Each rotation is about one of the axes. The angles are usually very small."),
        ("The scale", "One more parameter changes the size of the coordinate system. It is a scale factor, usually very close to one. Together with the shifts and rotations, it makes seven."),
        ("Sign conventions", "Each parameter has a sign convention. The rotation direction and the sign of each shift must be used consistently. Mixing conventions leads to large errors that are hard to spot."),
        ("Estimating and checking", "The parameters are estimated from points known in both frames. Residuals show how well the fit works. Check the residuals before you trust the result."),
    ],
    "test": [
        ("How many parameters make a seven-parameter Helmert transform?",
         [("a", "Two"), ("b", "Four"), ("c", "Five"), ("d", "Seven")], "d"),
        ("What do the three shifts describe?",
         [("a", "The position of one frame's origin relative to the other"), ("b", "The colour of the chart"), ("c", "The speed of the ship"), ("d", "The depth of the sea")], "a"),
        ("What does a scale parameter change?",
         [("a", "The time"), ("b", "The colour of the points"), ("c", "The size of the coordinate system"), ("d", "The number of satellites")], "c"),
        ("Why do sign conventions matter?",
         [("a", "They make the map prettier"), ("b", "They set the time zone"), ("c", "Mixing them causes large, hard-to-spot errors"), ("d", "They only apply to the Moon")], "c"),
        ("What do residuals show?",
         [("a", "The weather"), ("b", "How well the fit works"), ("c", "The price of the survey"), ("d", "The height of the instrument")], "b"),
    ],
}
