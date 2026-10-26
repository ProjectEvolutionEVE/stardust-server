"""Layers in a Geographic Information System: stacking maps of roads, soil, water and height so that they line up."""
CODE = 'navigation3b_gis_layers'
BOOK = {
    "title": "Layers in a Geographic Information System",
    "subtitle": "Stacking maps of roads, soil, water and height so that they line up",
    "chapters": [
        ("A map made of layers",
         "A geographic information system, or GIS, keeps a map as a stack of layers. One layer might hold the roads, another the soil, another the rivers, and another the height of the land. Each layer covers the same place, so the layers can be laid on top of each other."),
        ("Shapes and grids",
         "A vector layer stores shapes: points for wells, lines for roads and areas for lakes. A raster layer stores a grid of cells, each with a value, such as the brightness of a photo or the height of the land in that cell. Both kinds can sit in one project."),
        ("The attribute table",
         "Every shape or cell can carry facts about itself in a table. A road can have a name, a width and a speed limit, and a pond can have a depth. The table is what lets the software answer questions such as which lakes are deeper than ten metres."),
        ("Lining up the layers",
         "Layers only work together if they share one coordinate system, with the same datum and the same projection. A road drawn on one datum can sit a little off a field drawn on another. Check the datum and the projection before stacking any layers."),
        ("Asking the stack a question",
         "Overlaying layers answers new questions. A surveyor can find every house within 100 metres of a river that lies on land above a certain height. A planner can find the flat land near a road. Each question is a short walk down the stack."),
        ("Free data, real costs",
         "Many government and satellite data sets are free to download, which saves money on a project. The real costs are the time spent checking the data and the software that runs it. Good GIS work spends its money on checking, not only on buying."),
    ],
    "test": [
        ("What is a GIS layer?",
         [("a", "A paint colour"), ("b", "One set of map information, such as roads or soil, that covers the same place as the others"), ("c", "A sheet of ice"), ("d", "A type of boat")], "b"),
        ("What is the difference between vector and raster layers?",
         [("a", "Vector stores shapes such as points, lines and areas, while raster stores a grid of cells"), ("b", "Vector is in colour and raster is black and white"), ("c", "Raster only works at sea"), ("d", "They are the same thing with different names")], "a"),
        ("What is an attribute table used for?",
         [("a", "Holding the weather"), ("b", "Counting the layers"), ("c", "Storing the paper the map is printed on"), ("d", "Storing facts about each shape or cell")], "d"),
        ("Why must layers share one coordinate system before they are stacked?",
         [("a", "So the printer can print them"), ("b", "So each layer lines up with the same place on the ground"), ("c", "So the file is smaller"), ("d", "So the colours match")], "b"),
        ("What is the main caution about free data sets?",
         [("a", "They are always wrong"), ("b", "They never need checking"), ("c", "Their quality varies, so they need checking before use"), ("d", "They can only be used on paper")], "c"),
    ],
}
