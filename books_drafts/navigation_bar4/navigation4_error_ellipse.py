"""Error Ellipses and Confidence: drawing how sure we are of a point's position."""
CODE = "navigation4_error_ellipse"
BOOK = {
    "title": "Error Ellipses and Confidence",
    "subtitle": "Drawing how sure we are of a point",
    "chapters": [
        ("Uncertainty as a shape", "No measured point is exact. Its uncertainty can be drawn as an ellipse around it. The ellipse shows the area where the true point probably lies."),
        ("The axes", "The ellipse has two axes, a longest and a shortest. The longest shows the direction of greatest uncertainty. The shortest shows the direction of least uncertainty."),
        ("Confidence levels", "The size of the ellipse depends on the confidence level chosen. A higher confidence level draws a larger ellipse for the same survey. Surveyors always state the level they use."),
        ("The covariance matrix", "The covariance matrix holds the variances and covariances of the coordinates. The ellipse's size and shape are worked out from it. This matrix comes from the adjustment."),
        ("The orientation", "The orientation is the direction of the ellipse's axes. It shows which way the uncertainty leans. Two points can have the same size of ellipse but different orientations."),
        ("Comparing networks", "Error ellipses let you compare the strength of networks. Smaller ellipses mean a stronger network. Compare ellipses at the same confidence level."),
    ],
    "test": [
        ("What does an error ellipse show?",
         [("a", "The shape of a bird"), ("b", "The price of the survey"), ("c", "The area where the true point probably lies"), ("d", "The route of a ship")], "c"),
        ("What do the longest and shortest axes show?",
         [("a", "The ship's length and width"), ("b", "The colour of the ellipse"), ("c", "The height of the surveyor"), ("d", "The greatest and least uncertainty directions")], "d"),
        ("What does a higher confidence level do to the ellipse?",
         [("a", "Makes it larger"), ("b", "Less paper"), ("c", "A faster computer"), ("d", "A new base line")], "a"),
        ("What does the covariance matrix hold?",
         [("a", "The names of the stations"), ("b", "The variances and covariances of the coordinates"), ("c", "The menu of the ship"), ("d", "The weather history")], "b"),
        ("What does the orientation of an ellipse show?",
         [("a", "Which way the uncertainty leans"), ("b", "The month of the survey"), ("c", "The number of birds"), ("d", "The price per metre")], "a"),
    ],
}
