"""Photogrammetry: Maps from Overlapping Photos. Measuring the shape of the ground from pictures taken from above."""
CODE = 'navigation3b_photogrammetry'
BOOK = {
    "title": "Photogrammetry: Maps from Overlapping Photos",
    "subtitle": "Measuring the shape of the ground from pictures taken from above",
    "chapters": [
        ("Measuring from pictures",
         "Photogrammetry means taking measurements from photographs. A survey aircraft flies in straight lines and takes many overlapping pictures of the ground. Software then works out where each picture was taken and what the ground looks like."),
        ("Overlap",
         "Each photo overlaps the one before it, typically by around 60 per cent along the flight line and about 30 per cent between lines. So every point on the ground appears in at least two photos, which is what makes it possible to measure."),
        ("Parallax gives height",
         "Two photos taken from different places show a point in slightly different positions, much as two eyes do. The size of that shift depends on height, so the software reads height from it. It is the same parallax idea used for stars, on a far smaller baseline."),
        ("Ground control",
         "Pictures alone do not fix the true scale or position. Surveyors place marked ground control points, measured by a total station or by satellite, and the software ties the photos to them. Without ground control, a model can be right in shape and wrong in size."),
        ("From photos to a map",
         "From the matched photos, the software builds a three-dimensional model of the ground. It can then produce a height grid, a contour map, or an orthophoto: a true-scale image with the camera's tilt and shifts removed."),
        ("Cost and time",
         "A flight over a large area can cover far more ground in a day than a crew on foot. The main costs are the flight hours, the ground control work and the time the computers spend processing the photos."),
    ],
    "test": [
        ("What is photogrammetry?",
         [("a", "Printing money"), ("b", "Cooking with cameras"), ("c", "Taking measurements from photographs"), ("d", "Painting pictures of rocks")], "c"),
        ("Why do survey photos overlap?",
         [("a", "So every point on the ground appears in at least two photos"), ("b", "So the film is saved"), ("c", "So the camera is lighter"), ("d", "So the sky looks blue")], "a"),
        ("What lets software read height from two photos?",
         [("a", "The weight of the aircraft"), ("b", "The number of pilots"), ("c", "The colour of the sky"), ("d", "Parallax, the shift of a point between the two views")], "d"),
        ("What are ground control points used for?",
         [("a", "To make the photos brighter"), ("b", "To tie the photos to the true scale and position"), ("c", "To hold the aircraft up"), ("d", "To count the trees")], "b"),
        ("What is an orthophoto?",
         [("a", "A photo taken at night"), ("b", "A picture of a rain cloud"), ("c", "A true-scale image with the camera's tilt and shifts removed"), ("d", "A printed contour line")], "c"),
    ],
}
