"""The Dymaxion Map: Buckminster Fuller's world map on a folded solid, with its design, its strengths and its critics."""
CODE = "navigation5_dymaxion"
BOOK = {
    "title": "The Dymaxion Map",
    "subtitle": "One world on one flat sheet, and what it gives up",
    "chapters": [
        ("One world on one sheet", "Buckminster Fuller published the Dymaxion map in 1943. It shows the whole Earth on one flat sheet. The name was a brand Fuller used for many of his designs."),
        ("Why a solid", "A globe cannot be flattened without cutting or stretching it. Fuller projected the Earth onto the faces of an icosahedron, a solid with twenty triangular faces, and then unfolded those faces into one flat net."),
        ("Ocean and land", "The net cuts the land along the edges of the faces, and it keeps most of the oceans whole. Viewers can see one large connected sea rather than separate ocean basins."),
        ("Connections", "Where two faces meet along an edge, the land on each side is joined as it is on the globe. Cut edges can also place some places next to each other that are far apart on a real globe."),
        ("Distortion", "Like every flat map, the Dymaxion map must distort the Earth. Shapes and areas change, and the change is largest toward the edges of the faces."),
        ("Critiques", "Some cartographers find the cut land hard to read, and they say the distortion makes the map poor for measuring. Others value it for showing the oceans as one area and for its place in design history."),
    ],
    "test": [
        ("Which solid is the Dymaxion map based on?",
         [("a", "A cube"), ("b", "A dodecahedron"), ("c", "An icosahedron"), ("d", "An octahedron")], "c"),
        ("Who designed the Dymaxion map?",
         [("a", "Gerardus Mercator"), ("b", "Ptolemy"), ("c", "Carl Friedrich Gauss"), ("d", "Buckminster Fuller")], "d"),
        ("What is a strength of the Dymaxion layout?",
         [("a", "It shows the oceans as large connected areas"), ("b", "It keeps every shape and size exact"), ("c", "Its outline is a perfect circle"), ("d", "It cuts the land into thin strips only")], "a"),
        ("What kind of error does every flat map have?",
         [("a", "None, when printed well"), ("b", "Distortion of shape, area or distance"), ("c", "Only a colour error"), ("d", "Errors only at the equator")], "b"),
        ("In what year was the Dymaxion map first published?",
         [("a", "1569"), ("b", "1843"), ("c", "1901"), ("d", "1943")], "d"),
    ],
}
