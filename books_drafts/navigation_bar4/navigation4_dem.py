"""Digital Elevation Models: the grid of heights, where it comes from, how accurate it is, and what it is used for."""
CODE = "navigation4_dem"
BOOK = {
    "title": "Digital Elevation Models",
    "subtitle": "A grid of heights for the land, and what the numbers can and cannot tell you",
    "chapters": [
        ("The grid of heights", "A digital elevation model is a grid where each cell holds a height. Together the cells describe the shape of the land. It is a simple but powerful way to show terrain."),
        ("Sources", "Heights come from several sources. Laser scanning from aircraft, radar from space and photographs taken from two positions are common ones. Each source has its own strengths and limits."),
        ("Resolution", "Resolution is the size of one cell. A finer grid shows smaller hills and valleys. A finer grid also means a larger file to store and process."),
        ("Vertical error", "Every height in a model has some error. The error is often larger in dense forest or on flat, wet ground. Always ask how accurate the heights are before you rely on them."),
        ("Derived slope", "From the heights you can calculate slope and direction of slope for each cell. Slope shows how steep the ground is. Water flow and walking routes can be worked out from these values."),
        ("Uses", "Elevation models help with flood maps, drainage, road planning and line-of-sight checks. They also give the base for many other maps. Each use depends on how well the model matches the real ground."),
    ],
    "test": [
        ("What does each cell of an elevation model hold?", [("a", "A song"), ("b", "A height"), ("c", "A recipe"), ("d", "A road name")], "b"),
        ("What does a finer grid give?", [("a", "A smaller file every time"), ("b", "No change at all"), ("c", "Smaller hills and valleys shown in more detail"), ("d", "Heights in colour only")], "c"),
        ("Which of these is a common source of heights?", [("a", "A guess from a book"), ("b", "A weather vane"), ("c", "A laser scan from an aircraft"), ("d", "A sundial")], "c"),
        ("What can slope be calculated from?", [("a", "The heights in the grid"), ("b", "The names of the streets"), ("c", "The number of trees"), ("d", "The price of land")], "a"),
        ("Why check the vertical error before use?", [("a", "Heights are always exact"), ("b", "Error only affects colour"), ("c", "The grid has no cells"), ("d", "Every height has some error")], "d"),
    ],
}
