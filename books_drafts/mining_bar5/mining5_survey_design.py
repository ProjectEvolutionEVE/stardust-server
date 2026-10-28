"""Survey Design and Sampling Grids: choosing how far apart to take samples, and how the spacing decides what can be seen."""
CODE = "mining5_survey_design"
BOOK = {
    "title": "Survey Design and Sampling Grids",
    "subtitle": "Grid spacing, aliasing, adaptive sampling and the cost of error",
    "chapters": [
        ("Where to measure",
         "No one can measure every point of the ground. A survey picks a set of points, often on a grid. The spacing of that grid decides what the survey can and cannot show."),
        ("Grid spacing",
         "Close spacing gives detail but costs more. Wide spacing is cheap but can miss small features. The right spacing depends on the size of the target and the question being asked."),
        ("Aliasing",
         "If the spacing is too wide, a feature shorter than about twice the spacing can be missed or shown wrongly. This problem is called aliasing. A survey must be planned so that the targets it wants are not hidden by its own layout."),
        ("Adaptive sampling",
         "Adaptive sampling adds more points where the ground changes quickly and fewer where it is steady. It spends money where the answer is uncertain. The plan is updated as results come in."),
        ("Costs and the cost of error",
         "A cheap survey may miss a deposit, and a costly survey may waste money on detail nobody needs. The real comparison is the cost of the survey against the cost of getting the answer wrong. Good planners weigh both."),
        ("Planning",
         "A good plan writes down the target, the spacing, the method and the decision the survey will support. It also states how the results will be checked. A survey without a clear purpose tends to waste time and money."),
    ],
    "test": [
        ("What does grid spacing decide?",
         [("a", "What the survey can and cannot show"), ("b", "The colour of the report"), ("c", "The shape of the office"), ("d", "The name of the surveyor")], "a"),
        ("What is aliasing?",
         [("a", "A type of drill bit"), ("b", "A word for a mine office"), ("c", "A feature being missed or shown wrongly because the spacing is too wide"), ("d", "A kind of cloud")], "c"),
        ("What does adaptive sampling do?",
         [("a", "Removes all points"), ("b", "Samples only on Sundays"), ("c", "Uses a random colour"), ("d", "Adds points where the ground changes quickly")], "d"),
        ("What is the real comparison when planning a survey?",
         [("a", "The number of pages in the report"), ("b", "The cost of the survey against the cost of getting the answer wrong"), ("c", "The length of the drill rods"), ("d", "The number of people in the team")], "b"),
        ("What should a good survey plan state?",
         [("a", "The target, spacing, method and the decision the survey supports"), ("b", "Only the price of the car"), ("c", "Nothing about its purpose"), ("d", "Only the team's favourite food")], "a"),
    ],
}
