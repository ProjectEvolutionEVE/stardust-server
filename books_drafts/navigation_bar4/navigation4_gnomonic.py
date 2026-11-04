"""Gnomonic Charts and Great Circles: straight lines for the shortest routes."""
CODE = "navigation4_gnomonic"
BOOK = {
    "title": "Gnomonic Charts and Great Circles",
    "subtitle": "Straight lines for the shortest routes",
    "chapters": [
        ("Projection from the centre", "A gnomonic chart is made by projecting the globe's surface from its centre onto a flat sheet. Lines of sight from the centre pass through each point and land on the sheet. The method is simple to picture."),
        ("Straight great circles", "Every great circle appears as a straight line on a gnomonic chart. This makes the shortest route easy to draw. A navigator can lay a straight edge along the route."),
        ("Distortion at the edges", "Distortion grows as you move away from the centre of the chart. Shapes and distances near the edge are stretched. That is why these charts show only part of the globe."),
        ("Route plotting", "To plan a long route, draw a straight line on the gnomonic chart. Then read off the positions along it. Convert those points to a rhumb line route if you prefer steady steering."),
        ("The hemisphere limit", "A gnomonic chart cannot show points more than ninety degrees from its centre. Its useful area is therefore smaller than that of many other charts. Planning must stay within that area."),
        ("Working by hand", "Working by hand on a gnomonic chart uses straight edges and a few simple steps. Plot the start and finish, draw the line, and read off the latitudes and longitudes. Check the result on a second chart."),
    ],
    "test": [
        ("How are gnomonic charts made?",
         [("a", "By melting the globe"), ("b", "By painting the sea"), ("c", "By counting the stars"), ("d", "By projecting the globe's surface from its centre")], "d"),
        ("What do great circles look like on a gnomonic chart?",
         [("a", "Circles"), ("b", "Straight lines"), ("c", "Spirals"), ("d", "Dots")], "b"),
        ("Where does distortion grow on a gnomonic chart?",
         [("a", "At the centre only"), ("b", "Away from the centre of the chart"), ("c", "Nowhere"), ("d", "Only in the sea")], "b"),
        ("Why can't a gnomonic chart show the whole globe?",
         [("a", "Points more than ninety degrees from the centre cannot be projected"), ("b", "The paper is too small"), ("c", "The ink runs out"), ("d", "The equator is missing")], "a"),
        ("What is the first step in planning a route on a gnomonic chart?",
         [("a", "Paint the land"), ("b", "Count the waves"), ("c", "Plot the start and finish"), ("d", "Erase the centre")], "c"),
    ],
}
