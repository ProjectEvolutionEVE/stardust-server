"""Coordinate Metrology: Measuring Shapes in 3D. Probing a part in three dimensions and trusting the numbers."""
CODE = 'engineering4_cmm'
BOOK = {
    "title": "Coordinate Metrology: Measuring Shapes in 3D",
    "subtitle": "Probing a part in three dimensions and trusting the numbers",
    "chapters": [
        ("What a CMM does",
         "A coordinate measuring machine moves a probe over a part and records where it touches, in three directions. It gives exact positions for many features at once and is a standard tool for checking parts."),
        ("Probes",
         "The probe touches the surface at many points. Its tip size and shape are set in the software, so the readings are corrected for the tip. A worn or damaged tip gives wrong results."),
        ("Datums",
         "A datum is a reference feature that measurements are taken from. Choosing the datums correctly, as the drawing says, is the first step in any measurement plan."),
        ("Measurement strategy",
         "A plan sets the number of points, the order of measurement and the features to check. A good plan measures what matters on the drawing and nothing that does not."),
        ("Measurement uncertainty",
         "Every measurement has a small uncertainty from the machine, the probe, the room and the part. A result is trusted only when its uncertainty is known and small enough for the job."),
        ("The time cost of inspection",
         "Measuring takes machine time and skilled staff. Inspection is planned so that it catches problems without holding up production more than needed."),
    ],
    "test": [
        ("What does a CMM record?",
         [("a", "The colour of the part"), ("b", "The three-dimensional positions of touch points"), ("c", "The weight of the room"), ("d", "The smell of the oil")], "b"),
        ("What is a datum?",
         [("a", "A type of glue"), ("b", "A loose screw"), ("c", "A lamp on the bench"), ("d", "A reference feature that measurements are taken from")], "d"),
        ("What is measurement uncertainty?",
         [("a", "A wish that results be perfect"), ("b", "An error in the drawing only"), ("c", "A small range of doubt around a measured value, from the machine, probe, room and part"), ("d", "The cost of the machine")], "c"),
        ("What should a good measurement plan measure?",
         [("a", "What matters on the drawing"), ("b", "Every hole in the room"), ("c", "Only the paint"), ("d", "The operator's name")], "a"),
        ("What affects the probe's readings?",
         [("a", "The size of the lunchbox"), ("b", "The day of the week"), ("c", "The colour of the window"), ("d", "The probe tip's size and shape, which the software corrects for")], "d"),
    ],
}
