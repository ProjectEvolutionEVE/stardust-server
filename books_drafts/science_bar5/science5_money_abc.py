"""Activity-Based Costing in Research Labs: tracing overhead costs to the work that really causes them."""
CODE = "science5_money_abc"
BOOK = {
    "title": "Activity-Based Costing in Research Labs",
    "subtitle": "Cost drivers, activity pools, allocations, overhead distortions, cost models and checking accuracy",
    "chapters": [
        ("Why costs need tracing", "A lab shares many overhead costs, such as power, technicians and instrument upkeep, across all its projects. Splitting them by a simple rule can make some projects look cheap and others expensive. Activity-based costing traces each cost to the activities that cause it."),
        ("Cost drivers", "A cost driver is a factor that causes a cost to rise, such as the number of samples processed or the hours of instrument time used. Choosing good drivers is the key step. A driver should really track how the cost is consumed."),
        ("Activity pools", "An activity pool groups the costs linked to one activity, such as setting up instruments or running quality checks. Each pool has its own driver. Grouping costs this way makes the link between work and cost clear."),
        ("Allocations", "Allocation assigns the cost of each pool to projects in proportion to how much each one uses that activity. A project that runs many samples carries more of the sample-handling cost. The result is a fairer picture of what each project costs."),
        ("Overhead distortion", "An overhead distortion happens when a simple method shares overhead unfairly. Some projects then look too cheap and others too dear, which can lead to poor pricing and poor funding choices. Activity-based costing reduces this distortion."),
        ("Checking accuracy", "A cost model should be checked against real records. Compare the costs assigned with the resources actually used, and update the drivers when work patterns change. A model that is never checked can drift away from reality."),
    ],
    "test": [
        ("What is a cost driver?",
         [("a", "A factor that causes a cost to rise, such as the number of samples processed"), ("b", "A type of paint used in the lab"), ("c", "A staff job title"), ("d", "The opening hours of the library")], "a"),
        ("What is an activity pool?",
         [("a", "A swimming pool at the lab's sports club"), ("b", "A group of costs linked to one activity, such as setting up instruments"), ("c", "A list of journals in the library"), ("d", "A store of spare parts")], "b"),
        ("How are pool costs allocated to projects?",
         [("a", "By guessing"), ("b", "In proportion to how much each project uses the activity"), ("c", "By dividing everything equally between projects"), ("d", "By the colour of each project's folder")], "b"),
        ("What is an overhead distortion?",
         [("a", "An overhead cost that is always accurate"), ("b", "A small saving on supplies"), ("c", "A discount offered to customers"), ("d", "When a simple method shares overhead unfairly, so some projects look too cheap or too dear")], "d"),
        ("Why check the accuracy of a cost model?",
         [("a", "Because models never change"), ("b", "So that staff can avoid it"), ("c", "To see whether the costs assigned match the resources really used"), ("d", "Because the funder demands a colour chart")], "c"),
    ],
}
