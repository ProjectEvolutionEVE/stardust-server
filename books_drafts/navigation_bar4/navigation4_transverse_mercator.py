"""The Transverse Mercator Series: a cylinder wrapped sideways and the grids it produces."""
CODE = "navigation4_transverse_mercator"
BOOK = {
    "title": "The Transverse Mercator Series",
    "subtitle": "A cylinder wrapped sideways, and the grids it makes",
    "chapters": [
        ("A cylinder wrapped sideways", "The Mercator projection wraps a cylinder around the Earth at the equator. The transverse version turns the cylinder so it touches the globe along a meridian. The map is then accurate along that line."),
        ("The central meridian", "The line of contact is called the central meridian. Distortion is smallest there. The further you move from it, the larger the distortion grows."),
        ("Series expansions", "Calculating the projection uses series of terms. Each extra term improves the accuracy. Practical software keeps only the terms needed for the job."),
        ("Scale factor", "The scale factor tells you how much a distance on the map differs from the true distance. The Universal Transverse Mercator system uses 0.9996 on its central meridian, a little less than one. The scale grows away from that line."),
        ("Zone width", "Zones divide the world into strips of a set width. The Universal Transverse Mercator system uses zones six degrees wide. Each zone has its own central meridian."),
        ("Accuracy away from the centre", "Accuracy is best near the centre of a zone and gets worse toward the edges. Surveyors choose a zone that keeps their work near its centre. Good planning keeps the errors small."),
    ],
    "test": [
        ("In the transverse version, what does the cylinder touch the globe along?",
         [("a", "A meridian"), ("b", "The North Pole"), ("c", "A cloud"), ("d", "The Sun")], "a"),
        ("What is the central meridian?",
         [("a", "The equator"), ("b", "The line where the projection is most accurate"), ("c", "The coastline"), ("d", "The city hall line")], "b"),
        ("How wide are Universal Transverse Mercator zones?",
         [("a", "One degree"), ("b", "Two degrees"), ("c", "Ten degrees"), ("d", "Six degrees")], "d"),
        ("What is the scale factor?",
         [("a", "The height of a mountain"), ("b", "The number of zones"), ("c", "How much a map distance differs from the true distance"), ("d", "The price of paper")], "c"),
        ("Where is accuracy best within a zone?",
         [("a", "At the very edge"), ("b", "Only at the poles"), ("c", "Near the centre of the zone"), ("d", "Off the map")], "c"),
    ],
}
