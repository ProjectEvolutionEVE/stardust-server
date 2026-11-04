"""Lab Capacity Planning and Utilisation: demand forecasts, bench and instrument capacity, utilisation metrics, bottleneck analysis, expansion timing and capacity trade-offs."""
CODE = "science5_lab_capacity"
BOOK = {
    "title": "Lab Capacity Planning and Utilisation",
    "subtitle": "Matching the lab's work to the space, instruments and people it has",
    "chapters": [
        ("What capacity means",
         "Capacity is the amount of work a lab can do in a given time. It depends on bench space, instruments, staff and time. A lab that plans its capacity can take on work with confidence."),
        ("Demand forecasts",
         "A demand forecast estimates how much work will arrive, from which projects and funders. Base it on actual requests and realistic plans. Update it when grants are won or lost."),
        ("Bench and instrument capacity",
         "Bench capacity is the number of workspaces a lab can use. Instrument capacity is how many runs each machine can do. The weaker of these limits controls how much the lab can deliver."),
        ("Utilisation metrics",
         "Utilisation measures how much of the available time or space is used. Very high utilisation leaves no room for repairs or new work. Very low utilisation wastes money. Aim for a balance."),
        ("Bottleneck analysis",
         "A bottleneck is the step that limits the whole flow of work. Find it by following samples or tasks through the lab and noting where they queue. Adding capacity at other steps will not help until the bottleneck is eased."),
        ("Expansion timing and trade-offs",
         "Expansion takes time, so plan it before the queue grows too long. Each option is a trade-off between cost, speed, space and quality. Write down the trade-offs so the decision can be revisited."),
    ],
    "test": [
        ("What does capacity mean for a lab?",
         [("a", "The number of paintings on the wall"), ("b", "The amount of work the lab can do in a given time"), ("c", "The size of the lab's logo"), ("d", "The number of journals subscribed")], "b"),
        ("What is a demand forecast?",
         [("a", "A weather report for the lab"), ("b", "A guess about the lunch order"), ("c", "An estimate of how much work will arrive"), ("d", "A list of machine serial numbers")], "c"),
        ("What is a bottleneck?",
         [("a", "A type of glass bottle"), ("b", "The step that limits the whole flow of work"), ("c", "A bottle of cleaning fluid"), ("d", "A sample holder")], "b"),
        ("What does very high utilisation leave too little room for?",
         [("a", "Repairs and new work"), ("b", "Coffee breaks"), ("c", "Reading journals"), ("d", "Paperwork")], "a"),
        ("Why plan expansion before the queue grows too long?",
         [("a", "Because expansion takes time to deliver"), ("b", "Because queues are always free to clear"), ("c", "Because expansions are never needed"), ("d", "Because long queues improve results")], "a"),
    ],
}
