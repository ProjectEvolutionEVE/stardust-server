"""Greenhouse Gas Accounting for Mines: scopes, diesel use, electricity, reporting, targets and offsets."""
CODE = 'mining5_ghg_mine'
BOOK = {
    "title": "Greenhouse Gas Accounting for Mines",
    "subtitle": "Scopes, diesel use, electricity, reporting, targets and offsets",
    "chapters": [
        ("Counting what the mine releases",
         "Greenhouse gas accounting is the habit of counting every source of gases that warm the air. A mine has many sources, from fuel to power to the supply chain. Good accounting starts with a clear list of what is counted and what is not."),
        ("Scope 1: direct emissions",
         "Scope 1 covers emissions from sources the company owns or controls. For a mine, the biggest one is usually the diesel burned in haul trucks, drills and generators. Fuel records make these figures among the most reliable in the report."),
        ("Scope 2: purchased electricity",
         "Scope 2 covers the electricity, heat or steam the mine buys and uses. The emissions depend on how that power was made, so the same mine can show different figures in different places. Buying cleaner power lowers this part of the count."),
        ("Scope 3: the wider chain",
         "Scope 3 covers emissions from the wider chain, both upstream and downstream. It includes goods bought from suppliers, shipping by others, and how customers use the product. It is often the largest scope, and the hardest to measure well."),
        ("Reporting and targets",
         "A fair report uses the same boundaries and a base year each time, and it explains any changes. Targets, both near-term and long-term, show how the company plans to cut its totals. Investors look for targets that are specific, dated and tracked."),
        ("Offsets are not a shortcut",
         "An offset is a credit bought to balance emissions made somewhere else. Offsets can help, but their quality varies, and they do not replace cutting emissions at the source. The rules say cuts come first, and offsets come second."),
    ],
    "test": [
        ("Which scope covers the diesel a mine burns in its own haul trucks?",
         [("a", "Scope 1"), ("b", "Scope 2"), ("c", "Scope 3"), ("d", "Scope 4")], "a"),
        ("What does Scope 2 cover?",
         [("a", "Shipping done by others"), ("b", "The mine's own diesel burned on site"), ("c", "Purchased electricity the mine uses"), ("d", "Waste sent to a landfill by others")], "c"),
        ("Which of these is a Scope 3 example?",
         [("a", "Diesel in an on-site generator"), ("b", "Electricity from the grid"), ("c", "The mine's own haul trucks"), ("d", "Shipping of the ore by a contractor")], "d"),
        ("Why must a report keep the same boundaries and base year?",
         [("a", "So reports are always larger"), ("b", "So results can be compared fairly over time"), ("c", "So offsets are not needed"), ("d", "So the regulator can skip the report")], "b"),
        ("What is an offset?",
         [("a", "A fine for emissions"), ("b", "A cut in diesel use"), ("c", "A credit bought to balance emissions made elsewhere"), ("d", "A permit to burn coal")], "c"),
    ],
}
