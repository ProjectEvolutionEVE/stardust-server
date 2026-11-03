"""The Lambert Conformal Conic: a cone that sits on the globe along two parallels."""
CODE = "navigation4_lambert_conic"
BOOK = {
    "title": "The Lambert Conformal Conic",
    "subtitle": "A cone that sits on the globe at two parallels",
    "chapters": [
        ("A cone on the globe", "The Lambert conformal conic uses a cone placed over the globe. The cone cuts through the globe along two parallels, called standard parallels. The projection is built from that cone."),
        ("The cone constant", "The cone constant sets how the cone's spread changes the map. It depends on the standard parallels. Getting it right is part of building the projection."),
        ("Mid-latitude charts", "The projection suits areas that run east to west across the middle latitudes. It keeps distortion low across a wide band. That is why it suits many national maps."),
        ("Scale across the sheet", "The scale changes across the sheet. It is slightly less than one between the standard parallels, and it grows beyond them. Careful users check the scale for the area they measure."),
        ("Equal shapes", "The projection is conformal, so small shapes keep their true angles. Small areas look right, even if their size changes a little. This property suits charts for navigation."),
        ("Aviation use", "Many aviation charts use the Lambert conformal conic. Pilots find the straight lines and true angles helpful. The chart stays easy to read over a wide area."),
    ],
    "test": [
        ("How many parallels does the cone cut the globe along?",
         [("a", "One"), ("b", "Two"), ("c", "Four"), ("d", "Ten")], "b"),
        ("What is a conformal projection?",
         [("a", "One that keeps small shapes and angles true"), ("b", "One that paints the sea"), ("c", "One that uses no lines"), ("d", "One that flattens the poles only")], "a"),
        ("Where is the scale slightly less than one?",
         [("a", "At the poles only"), ("b", "Off the edge"), ("c", "Between the standard parallels"), ("d", "On the Moon")], "c"),
        ("What kind of charts is this projection often used for?",
         [("a", "Star charts"), ("b", "Ocean depth charts"), ("c", "Plant charts"), ("d", "Aviation charts")], "d"),
        ("Which region suits the projection best?",
         [("a", "The poles only"), ("b", "The Pacific only"), ("c", "A single point"), ("d", "Areas running east to west across the middle latitudes")], "d"),
    ],
}
