"""Reverse Engineering and 3D Scanning: measuring a real part and rebuilding its design, within the law."""
CODE = 'engineering4_reverse_eng'
BOOK = {
    "title": "Reverse Engineering and 3D Scanning",
    "subtitle": "Measuring a real part and rebuilding its design, within the law",
    "chapters": [
        ("Scanning a part",
         "A 3D scanner records a great many points on a surface. The cloud of points is the raw record of the shape, and it can be taken from a part that no drawing exists for."),
        ("Meshing",
         "The points are joined into a mesh of small triangles that describes the surface. A clean mesh is the base for the rebuild, and holes or noise in the scan must be repaired first."),
        ("Rebuilding dimensions",
         "The designer rebuilds the shape as measured solid features with dimensions. Each feature is checked against the scan, so the new model matches the real part closely."),
        ("Legal limits",
         "Copying a protected design can break patent, trademark or copyright law. Reverse engineering for repair, or to make a new design of your own, is a different matter. Check the law before copying anything."),
        ("Checking the rebuilt part",
         "The new part is made and measured against the original. Differences show where the rebuild needs more work. The check is what proves the model is right."),
        ("Accuracy in practice",
         "A scan contains small errors, so the rebuild is checked against measurements. The tolerances that matter for fit guide how close the copy must be."),
    ],
    "test": [
        ("What is a point cloud?",
         [("a", "A cloud in the sky"), ("b", "A painted part"), ("c", "A set of measured points on a surface"), ("d", "A type of mould")], "c"),
        ("What does meshing do?",
         [("a", "Joins points into small triangles that describe the surface"), ("b", "Melts the part"), ("c", "Paints the mesh"), ("d", "Cuts holes in the part")], "a"),
        ("Why check the law before copying a design?",
         [("a", "Because scanners cannot be used"), ("b", "Because mesh files are illegal"), ("c", "Because paint is regulated"), ("d", "Because copying a protected design can break patent, trademark or copyright law")], "d"),
        ("What is the purpose of checking the rebuilt part?",
         [("a", "To remove the scanner"), ("b", "To measure differences from the original and fix them"), ("c", "To save the mesh"), ("d", "To paint it")], "b"),
        ("Is a scan exact?",
         [("a", "No, it has small errors, so the rebuild must be checked"), ("b", "Yes, always exact"), ("c", "Only for plastic parts"), ("d", "Only in the dark")], "a"),
    ],
}
