"""Mercator's 1569 World Map: the new projection, the straight rhumb line, and the cost of its distortion."""
CODE = "navigation4_mercator_1569"
BOOK = {
    "title": "Mercator's 1569 World Map",
    "subtitle": "A world map built for sailors, and what it gets right and wrong",
    "chapters": [
        ("A new kind of map", "In 1569 Gerardus Mercator published a world map made for navigators. Its lines of longitude were straight and evenly spaced. Its lines of latitude grew further apart as they moved toward the poles."),
        ("The straight course", "On this map a rhumb line, a path that keeps one compass bearing, is drawn as a straight line. A navigator could lay a ruler on two points and read the compass direction. That made planning a course simple."),
        ("The price of straight lines", "To keep directions true, the map stretches land far from the equator. Greenland looks about as large as Africa, though Africa is much bigger. The map is a poor guide to size in the far north and south."),
        ("Reception", "Sailors and mapmakers did not accept the new layout at once. Over time it became the standard for sea charts. It was still a tool with known limits."),
        ("The maths later", "Edward Wright, an English mathematician, explained the mathematics of the projection in 1599. His work helped navigators understand exactly how the map worked. It made the map easier to trust and to use."),
        ("Reading the map today", "Use the map to follow a fixed compass bearing, since it keeps direction true. Do not use it to compare the sizes of distant lands. Knowing what a map keeps and what it changes is part of reading it well."),
    ],
    "test": [
        ("What did Gerardus Mercator publish in 1569?", [("a", "A map of the Moon"), ("b", "A book on ship building"), ("c", "A world map made for sailors"), ("d", "A star catalogue")], "c"),
        ("On a Mercator-style map, how does a course of fixed compass bearing appear?", [("a", "As a straight line"), ("b", "As a curve"), ("c", "As a circle"), ("d", "As a dot")], "a"),
        ("What is the main drawback of the projection?", [("a", "Ocean depths are hidden"), ("b", "Its scale changes with the seasons"), ("c", "Lines of longitude curve"), ("d", "Land far from the equator looks too large")], "d"),
        ("Who explained the mathematics of the projection in 1599?", [("a", "Isaac Newton"), ("b", "Edward Wright"), ("c", "Ptolemy"), ("d", "Galileo")], "b"),
        ("Which feature do the lines of longitude have on this map?", [("a", "They are straight and evenly spaced"), ("b", "They are curved"), ("c", "They point to the Sun"), ("d", "They are drawn only at the poles")], "a"),
    ],
}
