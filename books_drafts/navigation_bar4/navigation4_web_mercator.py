"""Web Maps and Tile Grids: how the maps on a phone or screen are built from small squares."""
CODE = "navigation4_web_mercator"
BOOK = {
    "title": "Web Maps and Tile Grids",
    "subtitle": "How the maps on your phone are built",
    "chapters": [
        ("The tile pyramid", "Most web maps are cut into small square images called tiles. At each zoom level, the world is split into more tiles. The stack of levels looks like a pyramid."),
        ("The Web Mercator choice", "Web Mercator is a version of the Mercator projection used by many web maps. It was chosen because it is simple and fast to draw on screens. Its shape suits zooming and panning."),
        ("Large area errors near the poles", "Web Mercator stretches areas near the poles. Greenland looks much larger than it is. Use an equal-area projection when comparing sizes."),
        ("Zoom levels", "Each zoom level doubles the number of tiles along each side. At zoom level zero, the whole world is a single tile. Higher levels show more detail."),
        ("Tile addressing", "A tile is found by its column, its row and its zoom level. The counting starts at the top-left corner. This address is easy for computers to use."),
        ("Mixing with survey grids", "Survey grids and web maps use different projections. Mixing them without care can shift points. Always check which projection your data uses."),
    ],
    "test": [
        ("What are the small square images on web maps called?",
         [("a", "Tiles"), ("b", "Coins"), ("c", "Bricks"), ("d", "Ropes")], "a"),
        ("What does each zoom level do to the number of tiles?",
         [("a", "It halves them"), ("b", "It keeps them the same"), ("c", "It doubles the number along each side"), ("d", "It removes them")], "c"),
        ("Which feature does Web Mercator distort badly?",
         [("a", "Colours"), ("b", "Text"), ("c", "Areas near the poles"), ("d", "Road names")], "c"),
        ("Why was Web Mercator chosen for many web maps?",
         [("a", "Making maps of the Moon"), ("b", "Printing books"), ("c", "Measuring the ocean"), ("d", "It is simple and fast to draw on screens")], "d"),
        ("What is the first thing to check when mixing data?",
         [("a", "Which projection each dataset uses"), ("b", "The colour of the tiles"), ("c", "The name of the author"), ("d", "The weather")], "a"),
    ],
}
