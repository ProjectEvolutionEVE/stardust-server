"""Triangulation Networks: building a map of the land one triangle at a time."""
CODE = "navigation4_triangulation_networks"
BOOK = {
    "title": "Triangulation Networks",
    "subtitle": "Building a map one triangle at a time",
    "chapters": [
        ("Chains of triangles", "A triangulation network links points together in a chain of triangles. The angles of each triangle are measured. Knowing the angles and one side lets you work out the others."),
        ("The measured base", "The network starts from a carefully measured base line. Its length sets the scale for the whole network. Any error in the base carries through the rest."),
        ("Angle sums", "The angles of a plane triangle add up to one hundred and eighty degrees. Surveyors use this to check for errors. A triangle that fails the check needs more work."),
        ("Scale growth", "Each new triangle passes the scale on to the next. Small errors can grow along a long chain. Careful work keeps that growth under control."),
        ("Strength of figure", "The strength of a figure describes how well its triangles fix the scale and shape. Well-shaped triangles give stronger results. Long, thin triangles are weaker."),
        ("The great arc", "Long chains of triangles can measure a great arc across the land. Such arcs helped measure the size and shape of the Earth. Careful networks made this possible."),
    ],
    "test": [
        ("What do the angles of a plane triangle add up to?",
         [("a", "Ninety degrees"), ("b", "Two hundred degrees"), ("c", "Three hundred and sixty degrees"), ("d", "One hundred and eighty degrees")], "d"),
        ("What sets the scale of a triangulation network?",
         [("a", "The colour of the paper"), ("b", "The wind"), ("c", "The measured base line"), ("d", "The height of the tower")], "c"),
        ("What do surveyors use the angle sum for?",
         [("a", "To paint triangles"), ("b", "To check for errors"), ("c", "To lengthen the base"), ("d", "To measure the Sun")], "b"),
        ("What happens to scale errors along a long chain?",
         [("a", "They can grow"), ("b", "They always vanish"), ("c", "They turn into angles"), ("d", "They make the chain shorter")], "a"),
        ("What makes a network's strength of figure higher?",
         [("a", "Long, thin triangles"), ("b", "Fewer measurements"), ("c", "Well-shaped triangles"), ("d", "Cloud cover")], "c"),
    ],
}
