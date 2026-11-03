"""The Polar Problem in Mapping: why ordinary projections fail at the poles, and how polar systems solve it."""
CODE = "navigation5_polar_problem"
BOOK = {
    "title": "The Polar Problem in Mapping",
    "subtitle": "Why the poles break ordinary maps, and how they are mapped",
    "chapters": [
        ("The pole", "At the North and South Poles, many projections break down. The Mercator cylinder cannot show the poles, because its scale grows without limit there."),
        ("The stereographic remedy", "The polar stereographic projection places a flat plane at the pole and projects the Earth onto it. It keeps angles true and works well at high latitudes."),
        ("Polar grids", "The Universal Polar Stereographic, or UPS, grid covers the polar areas, while the UTM grid covers the rest of the world between them."),
        ("Antarctic mapping", "Antarctica is mapped with polar stereographic and related systems. Its ice sheets and coasts need careful choices of coordinates."),
        ("Gaps", "Two grid systems can leave gaps or overlaps where they meet. Mapmakers set clear rules at the join to avoid both."),
        ("Practice", "A practical map labels the projection and the grid it uses. Readers should know where a grid's accuracy ends."),
    ],
    "test": [
        ("What happens to the Mercator scale at the poles?",
         [("a", "It becomes zero"), ("b", "It becomes infinite"), ("c", "It stays fixed"), ("d", "It reverses")], "b"),
        ("What does the polar stereographic projection keep true?",
         [("a", "Areas"), ("b", "Distances from the pole"), ("c", "Angles"), ("d", "Weight")], "c"),
        ("Which grid covers the polar areas beyond about 84 degrees north?",
         [("a", "UTM"), ("b", "A Mercator grid"), ("c", "A ladder grid"), ("d", "UPS")], "d"),
        ("Which continent's mapping relies heavily on polar stereographic work?",
         [("a", "Antarctica"), ("b", "Africa"), ("c", "Asia"), ("d", "Australia")], "a"),
        ("What is a common problem where two grid systems meet?",
         [("a", "Too much colour"), ("b", "Gaps or overlaps"), ("c", "Lack of ink"), ("d", "Too many names")], "b"),
    ],
}
