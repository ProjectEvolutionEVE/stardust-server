"""Coordinate Reference Systems and EPSG Codes: the registry, the codes, and the mistakes that put maps in the wrong place."""
CODE = "navigation4_epsg_codes"
BOOK = {
    "title": "Coordinate Reference Systems and EPSG Codes",
    "subtitle": "Why a map needs a code, and how to avoid putting data in the wrong place",
    "chapters": [
        ("The registry", "The EPSG registry is a public list of coordinate reference systems. Each entry has a numeric code. Software uses the code to know exactly how positions on a map are measured."),
        ("The codes", "EPSG:4326 means latitude and longitude on the WGS 84 datum, the system GPS uses. EPSG:3857 is the Web Mercator system used by many web maps. The same place has different numbers in each."),
        ("Transformations", "Moving data between two systems can need a datum transformation. The result may shift a little, depending on the method. Keep a note of which method you used."),
        ("Metadata", "A dataset should say which code it uses. Without that note, a map may be placed in the wrong spot. Good metadata saves hours of confusion later."),
        ("Common mistakes", "A common mistake is swapping latitude and longitude. Another is assuming a file with no code is in WGS 84. Check the code before you combine two layers."),
        ("Registry changes", "The registry changes over time. Some codes are retired and replaced by newer ones. Older files may still use a retired code, so record the date you made them."),
    ],
    "test": [
        ("What is the EPSG registry?", [("a", "A list of street names"), ("b", "A book of sea songs"), ("c", "A public list of coordinate reference systems with codes"), ("d", "A type of satellite")], "c"),
        ("Which code is the WGS 84 latitude and longitude system?", [("a", "EPSG:3857"), ("b", "EPSG:2056"), ("c", "EPSG:9999"), ("d", "EPSG:4326")], "d"),
        ("What is a datum transformation?", [("a", "Shifting a map between two datums"), ("b", "Painting a map"), ("c", "Printing a legend"), ("d", "Counting map layers")], "a"),
        ("What is a common mistake with coordinates?", [("a", "Using too many colours"), ("b", "Swapping latitude and longitude"), ("c", "Adding a title"), ("d", "Using a large font")], "b"),
        ("What should a dataset say about its code?", [("a", "Its favourite colour"), ("b", "Its owner's name"), ("c", "Which coordinate code it uses"), ("d", "Its file size")], "c"),
    ],
}
