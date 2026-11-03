"""Implementing Projections in Software: using trusted libraries, checking parameters, and validating results."""
CODE = "navigation5_projection_software"
BOOK = {
    "title": "Implementing Projections in Software",
    "subtitle": "Calls, parameters and checks that keep a map right",
    "chapters": [
        ("Using a library", "Most people do not write projection formulas from scratch. Well-tested libraries, such as PROJ, provide tried and tested calls."),
        ("Parameters", "A projection needs parameters, such as a central meridian, standard parallels and a datum. A wrong value can move a whole map by many kilometres."),
        ("Test points", "Developers check their code against points with known coordinates. A few well-chosen test points catch many mistakes."),
        ("Common errors", "Common errors include swapped latitude and longitude, wrong units and the wrong datum. Good code checks for these and reports them clearly."),
        ("Standards", "Standard codes, such as EPSG codes, name coordinate systems so that different programs agree. Using a standard code reduces confusion."),
        ("Validation", "Validation compares outputs with trusted reference values across a range of places. Validated code is documented, versioned and tested again after each update."),
    ],
    "test": [
        ("Which of these is a common library for coordinate transformations?",
         [("a", "PROJ"), ("b", "A printer driver"), ("c", "A web browser"), ("d", "A music player")], "a"),
        ("What is a standard parallel?",
         [("a", "A road between two cities"), ("b", "A canal"), ("c", "A line of longitude"), ("d", "A line of latitude where the scale is exact")], "d"),
        ("What is a common error when entering coordinates?",
         [("a", "Using red ink"), ("b", "Swapping latitude and longitude"), ("c", "Using too much paper"), ("d", "A slow printer")], "b"),
        ("What is an EPSG code?",
         [("a", "A train ticket"), ("b", "A battery size"), ("c", "A standard number that names a coordinate system"), ("d", "A password")], "c"),
        ("What is the purpose of validation?",
         [("a", "To change the map's colour"), ("b", "To hide errors"), ("c", "To compare outputs with trusted reference values"), ("d", "To delete the code")], "c"),
    ],
}
