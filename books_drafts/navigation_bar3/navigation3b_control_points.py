"""Control Points and Benchmarks: fixed marks that hold every survey in place, and how small errors add up."""
CODE = 'navigation3b_control_points'
BOOK = {
    "title": "Control Points and Benchmarks",
    "subtitle": "Fixed marks that hold every survey in place, and how small errors add up",
    "chapters": [
        ("Marks that stay put",
         "A control point is a marked spot whose position has been measured very carefully against the wider network. A benchmark is a control point whose height is known. Surveyors set these marks in concrete, stone or metal, so they can be found again year after year."),
        ("A network, not a single point",
         "Control points are linked into a network, so each new measurement can be checked against several known points. A survey that stands alone has no check on itself. A network gives a way to test the work."),
        ("Traverses and misclosure",
         "A traverse is a chain of measured legs running from one control point to the next. If it ends back at a known point, the gap between the calculated position and the known one is the misclosure. A small misclosure is a sign of good work."),
        ("How errors add up",
         "Every leg carries a small error, and the errors build up along a long traverse. That is why surveyors keep traverses short and tie them back to control often."),
        ("Adjusting the work",
         "When the misclosure is small, the surveyor spreads the error back over the whole traverse, so every point moves a little. This is called adjustment. The adjusted points then become control for the next job."),
        ("Why a good mark pays",
         "A well-set benchmark costs more at the start, but each later survey that uses it saves the time of setting a new one. One careful job can serve many later jobs."),
    ],
    "test": [
        ("What is a benchmark?",
         [("a", "A control point whose height is known"), ("b", "A kind of boat"), ("c", "A map drawn in the dark"), ("d", "A survey fee")], "a"),
        ("Why are control points linked into a network?",
         [("a", "To make the map look busy"), ("b", "So the tripods can be sold"), ("c", "So each new measurement can be checked against several known points"), ("d", "So the paint stays wet")], "c"),
        ("What is a misclosure?",
         [("a", "A kind of map colour"), ("b", "The gap between where a traverse ends and the known point it should reach"), ("c", "A broken instrument"), ("d", "The name of a survey crew")], "b"),
        ("What is adjustment in surveying?",
         [("a", "Painting new marks"), ("b", "Turning off the instrument"), ("c", "Moving the Moon"), ("d", "Spreading a small error back over a traverse so the points fit the known positions")], "d"),
        ("Why do surveyors keep traverses short and tie them back to control?",
         [("a", "Because errors build up along long chains"), ("b", "Because long chains are cheaper"), ("c", "Because short chains look better"), ("d", "Because control points are always wrong")], "a"),
    ],
}
