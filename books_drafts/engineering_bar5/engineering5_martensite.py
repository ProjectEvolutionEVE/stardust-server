"""Martensite Transformation Theory: how steel can change crystal structure without atoms moving far."""
CODE = "engineering5_martensite"
BOOK = {
    "title": "Martensite Transformation Theory",
    "subtitle": "How steel can change crystal structure without its atoms moving far",
    "chapters": [
        ("A change without diffusion",
         "Martensite forms when steel is cooled fast enough, and the atoms shift into a new arrangement without diffusing. The change is very quick."),
        ("Habit planes",
         "New martensite plates grow along particular planes called habit planes, which stay unstretched. The shape change is small and well defined."),
        ("Transformation strain",
         "The change in shape comes with a transformation strain. The surrounding structure must accommodate it, which leaves stress in the material."),
        ("Retained austenite",
         "Some of the original structure can remain untransformed, which is called retained austenite. It can change later and affect the size of a part."),
        ("Sub-zero treatment",
         "Cooling below room temperature turns more of the retained austenite into martensite. This is called sub-zero treatment, and it helps tools keep their size."),
        ("Why engineers care",
         "Martensite is hard and strong, which is why hardened steels rely on it. Its amount and stability must be controlled for reliable parts."),
    ],
    "test": [
        ("What is martensite formed by?",
         [("a", "Slow melting"), ("b", "Paint curing"), ("c", "Fast cooling so atoms shift without diffusing"), ("d", "Adding sugar")], "c"),
        ("What are habit planes?",
         [("a", "Flying routes"), ("b", "Floor boards"), ("c", "Road lanes"), ("d", "Planes along which martensite plates grow and stay unstretched")], "d"),
        ("What is retained austenite?",
         [("a", "A paint"), ("b", "The original structure left untransformed"), ("c", "A sale"), ("d", "A gas")], "b"),
        ("What does sub-zero treatment do?",
         [("a", "Melts the steel"), ("b", "Paints it"), ("c", "Turns more retained austenite into martensite"), ("d", "Adds weight")], "c"),
        ("Why does martensite matter?",
         [("a", "It is hard and strong"), ("b", "It is soft and sticky"), ("c", "It is a colour"), ("d", "It is a price")], "a"),
    ],
}
