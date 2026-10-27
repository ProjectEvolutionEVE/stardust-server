"""Plant Layout and Facility Planning: arranging machines, people and material flow so the work moves cleanly."""
CODE = 'engineering4_plant_layout'
BOOK = {
    "title": "Plant Layout and Facility Planning",
    "subtitle": "Arranging machines, people and material flow so the work moves cleanly",
    "chapters": [
        ("Process versus product layout",
         "A process layout groups similar machines together. A product layout places machines in the order that a product passes through them. The right choice depends on the variety and volume of the work."),
        ("Material flow",
         "Plan the route each part takes so that it moves in one direction where possible. Long, crossing routes waste time and handling."),
        ("Space planning",
         "Plan the floor area for each machine, its operator and the material around it. Leave room for the work itself, not just for the machine."),
        ("Aisle widths",
         "Aisles must be wide enough for forklifts, carts and people to pass safely. Narrow aisles cause collisions and delays."),
        ("Room for expansion",
         "Leave space to add machines or a new line later. Fitting new equipment into a crowded plant is costly and slow."),
        ("Checking the plan",
         "Walk the route with cardboard models or a simple drawing before anything is moved. Small errors are cheap to fix on paper."),
    ],
    "test": [
        ("What does a process layout group together?",
         [("a", "Similar machines"), ("b", "Only the offices"), ("c", "The paint"), ("d", "The lunchroom")], "a"),
        ("What is the aim of material flow planning?",
         [("a", "To make parts go backwards"), ("b", "To add crossing routes"), ("c", "To move parts in one direction where possible"), ("d", "To lock the doors")], "c"),
        ("Why are aisles planned carefully?",
         [("a", "To make the floor shiny"), ("b", "To hold paint"), ("c", "To let forklifts, carts and people pass safely"), ("d", "To place the lights")], "c"),
        ("Why leave room for expansion?",
         [("a", "To store waste"), ("b", "To avoid paying rent"), ("c", "To make the floor slippery"), ("d", "Adding machines later in a crowded plant is costly")], "d"),
        ("What is a cheap way to test a layout?",
         [("a", "Walk the route with a simple drawing or cardboard model"), ("b", "Build the whole plant first"), ("c", "Guess"), ("d", "Sell the building")], "a"),
    ],
}
