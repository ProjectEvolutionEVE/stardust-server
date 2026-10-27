"""Financial Models for Scaling Scenarios: how costs and income change as a team grows, and how to test the plan."""
CODE = "computing5_scaling_scenarios"
BOOK = {
    "title": "Financial Models for Scaling Scenarios",
    "subtitle": "Testing how costs and income change as volume grows",
    "chapters": [
        ("Volume drivers",
         "A volume driver is the thing that sets how much work or how many sales a plan must handle. It might be users, orders, or hours of service. Name the driver first, because every other number in the model depends on it."),
        ("Unit costs",
         "A unit cost is the cost to make one item or serve one customer. Some costs stay the same as volume grows, and others rise with each unit. Separate the two kinds, so the model shows what happens when volume doubles."),
        ("Sensitivity tables",
         "A sensitivity table shows how the result changes when one input changes and the others stay put. It is a quick way to find which numbers matter most. If a small change in one input moves the result a lot, check that input with extra care."),
        ("Break-even points",
         "A break-even point is the volume at which income equals total costs. Below it the plan loses money, and above it the plan makes money. Knowing this point tells a team how much it must sell before the plan pays its way."),
        ("Base and stretch cases",
         "A base case uses the numbers the team expects to be most likely. A stretch case is a more ambitious version, with higher volume and a target to aim for. Showing both helps people see the range of outcomes, not just a single guess."),
        ("An assumptions log",
         "An assumptions log lists every number the model uses, where it came from, and who checked it. When a figure changes, the log shows what else must be updated. Keeping one is one of the simplest ways to make a model trustworthy."),
    ],
    "test": [
        ("What is a break-even point?",
         [("a", "The cheapest unit in the plan"), ("b", "The volume at which income equals total costs"), ("c", "The largest single sale"), ("d", "The day a project ends")], "b"),
        ("What does a sensitivity table show?",
         [("a", "A list of staff members"), ("b", "The tax rate for the year"), ("c", "A photograph of the team"), ("d", "How the result changes when one input changes")], "d"),
        ("Why keep an assumptions log?",
         [("a", "So each number and its source can be checked later"), ("b", "To hide the numbers from reviewers"), ("c", "To remove the base case"), ("d", "To speed up printing")], "a"),
        ("What is a stretch case?",
         [("a", "The plan the team expects to be most likely"), ("b", "An insurance policy for the project"), ("c", "An ambitious version with higher volume, used as a target"), ("d", "The cheapest option available")], "c"),
        ("What is a unit cost?",
         [("a", "The cost of the building"), ("b", "The cost to make or serve one unit"), ("c", "A fine for breaking a rule"), ("d", "A yearly total of all spending")], "b"),
    ],
}
