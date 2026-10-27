"""The Forming Limit Diagram: necking and fracture limits, strain paths, measuring limit strains and checking forming feasibility."""
CODE = "engineering5_flc"
BOOK = {
    "title": "The Forming Limit Diagram",
    "subtitle": "A map of how far a sheet can stretch before it fails",
    "chapters": [
        ("A map of stretching",
         "A forming limit diagram, or FLD, is a map of how much a sheet metal can stretch before it fails. It lets engineers check a forming design before the die is cut. Each point on the map is a pair of strains."),
        ("Necking",
         "Necking is the local thinning that comes before a sheet splits. It shows up as a narrow band where the metal starts to thin fast. The forming limit line marks the strain level where necking starts."),
        ("Fracture limits",
         "Beyond the necking limit, the sheet can crack. The fracture limit is the level where the sheet actually splits. The diagram helps engineers see how close a part is to that edge."),
        ("Strain paths",
         "A strain path is the route the strains take as the sheet is formed. A sheet stretched in two directions can hold more strain than one stretched in one direction. Engineers study the path, not only the final shape."),
        ("Measuring limit strains",
         "Limit strains are measured by printing a fine grid on sample sheets and stretching them to failure. Software reads how each circle of the grid has deformed. The results form the limit curve for that alloy and thickness."),
        ("Checking feasibility",
         "Before building a die, engineers plot the strains from a simulation onto the diagram. A point safely below the limit means the part is feasible. A point near or above the limit calls for a design change."),
    ],
    "test": [
        ("What does a forming limit diagram show?",
         [("a", "The price of the sheet"), ("b", "How much sheet metal can stretch before it fails"), ("c", "The number of bolts"), ("d", "The age of the factory")], "b"),
        ("What is necking?",
         [("a", "A type of bolt"), ("b", "A handle on a cup"), ("c", "Local thinning that comes before a sheet splits"), ("d", "A paint colour")], "c"),
        ("What is a strain path?",
         [("a", "A walking trail"), ("b", "The path of a laser"), ("c", "A list of suppliers"), ("d", "The route the strains take during forming")], "d"),
        ("How are limit strains measured?",
         [("a", "By printing a grid on the sheet and stretching it to failure"), ("b", "By weighing the sheet"), ("c", "By listening to the sheet"), ("d", "By freezing the sheet")], "a"),
        ("What does a point well below the limit line suggest?",
         [("a", "The part will always crack"), ("b", "The part is feasible to form"), ("c", "The die must be melted"), ("d", "The sheet is too thick to see")], "b"),
    ],
}
