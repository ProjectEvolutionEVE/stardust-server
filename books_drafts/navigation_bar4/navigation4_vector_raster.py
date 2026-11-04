"""Vector and Raster Data: points and lines against grid cells, how to choose a model, and what changes when you convert."""
CODE = "navigation4_vector_raster"
BOOK = {
    "title": "Vector and Raster Data",
    "subtitle": "Two ways to store a map, and how to pick the right one",
    "chapters": [
        ("Points and lines", "Vector data stores features as points, lines and areas. Each feature has exact coordinates. A road, a river or a property boundary is a good fit for vector data."),
        ("Grid cells", "Raster data stores a map as a grid of cells, like the pixels in a photograph. Each cell holds one value. Satellite images and elevation grids are usually stored as rasters."),
        ("Choosing a model", "Choose vector when features have clear edges and you need exact shapes. Choose raster when the values change smoothly across the land. Ask what the data will be used for before you decide."),
        ("Conversion", "You can turn vector data into a raster, or a raster into vector. Each change needs a rule, such as which cell a line falls in. The rule affects the result."),
        ("Information loss", "Converting data always risks losing detail. A thin line may vanish when it is turned into cells. A raster converted to vector may gain edges that were never there. Keep the original copy."),
        ("Storage", "A raster stores a value for every cell, even where nothing changes, so large grids take up much space. Vector data is often smaller for sharp features. Storage size is one more reason to pick the right model."),
    ],
    "test": [
        ("What does vector data store features as?", [("a", "Points, lines and areas with exact coordinates"), ("b", "Photographs of the land"), ("c", "A grid of colours only"), ("d", "Sound recordings")], "a"),
        ("What is a raster made of?", [("a", "Loose sentences"), ("b", "Exact road names"), ("c", "Grid cells, each with a value"), ("d", "Lines with no coordinates")], "c"),
        ("Which data is usually stored as a raster?", [("a", "Property boundaries"), ("b", "Road centre lines"), ("c", "Named points of interest"), ("d", "Satellite images")], "d"),
        ("What is a risk when you convert between the two models?", [("a", "The map becomes free of errors"), ("b", "The coordinates always improve"), ("c", "The file grows smaller every time"), ("d", "Some detail may be lost")], "d"),
        ("Why can a raster take up more space?", [("a", "It stores only the names of places"), ("b", "It stores a value for every cell, even where nothing changes"), ("c", "It has no coordinates"), ("d", "It uses a single line")], "b"),
    ],
}
