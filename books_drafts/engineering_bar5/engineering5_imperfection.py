"""Imperfection Sensitivity and Post-Buckling: why real structures give way before the perfect model says they should."""
CODE = "engineering5_imperfection"
BOOK = {
    "title": "Imperfection Sensitivity and Post-Buckling",
    "subtitle": "Why real structures give way before the perfect model says they should",
    "chapters": [
        ("Perfect and real shapes",
         "A perfect model of a structure assumes an exact shape and exact loads. Real structures always carry small errors in shape, load or material, and these matter a great deal in buckling."),
        ("Post-buckling paths",
         "After buckling, some structures keep carrying load with reduced stiffness, while others lose load quickly. The path after buckling shows how safe the structure is beyond its critical load."),
        ("Sensitivity",
         "Some shells are very sensitive, so a small shape error lowers their strength a great deal. Others are stable and barely change. Knowing which type you have is central to safe design."),
        ("Initial imperfections",
         "Imperfections can be measured by scanning a built shape and comparing it with the design. The worst likely imperfection sets the design case."),
        ("Design knockdown factors",
         "Design codes often apply a knockdown factor, a reduction in the perfect-shape strength, to allow for imperfections. It is a simple way to cover the gap between the perfect and the real."),
        ("Balance",
         "A good design does not rely on perfect shapes, and does not waste material by overcompensating. The aim is a known margin for the imperfections that really occur."),
    ],
    "test": [
        ("What do real structures always have?",
         [("a", "A perfect shape"), ("b", "Small initial errors in shape, load or material"), ("c", "No loads"), ("d", "Infinite strength")], "b"),
        ("What is a post-buckling path?",
         [("a", "A path to the store"), ("b", "A walking trail"), ("c", "The route of a pipe"), ("d", "The way a structure behaves after it buckles")], "d"),
        ("What is a knockdown factor?",
         [("a", "A discount on steel"), ("b", "A reduction in the perfect-shape strength to allow for imperfections"), ("c", "A sale price"), ("d", "A test for paint")], "b"),
        ("Why are some shells sensitive to imperfections?",
         [("a", "They have no load"), ("b", "They are painted"), ("c", "A small shape error can lower their strength a great deal"), ("d", "They never buckle")], "c"),
        ("What is the best way to get a value for imperfections?",
         [("a", "Guessing"), ("b", "Measuring a built shape against the design"), ("c", "Using a colour chart"), ("d", "Ignoring them")], "b"),
    ],
}
