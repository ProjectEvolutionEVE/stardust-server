"""Slope stability and retaining walls: failure surfaces, factor of safety, drainage, wall types and monitoring."""
CODE = "engineering4_slope_stability"
BOOK = {
    "title": "Slope Stability and Retaining Walls",
    "subtitle": "Failure surfaces, safety factors, drainage and monitoring",
    "chapters": [
        ("Why slopes fail",
         "A slope fails when the weight of the ground pulling it down is greater than the strength holding it up. The failure usually runs along a curved or flat surface inside the ground. Engineers look for that surface before they trust the slope."),
        ("Factor of safety",
         "The factor of safety compares the strength available with the stress the ground actually carries. A value above one means the slope is stable on paper. Designers pick a target value that suits the risk to people and property."),
        ("Drainage",
         "Water is the most common trigger for a slope failure. Water in the ground raises the pressure in the pores and weakens the soil. Drains, ditches and surface covers keep water away from the slope."),
        ("Retaining wall types",
         "A retaining wall holds back soil that would otherwise slide. Gravity walls rely on their own weight, while cantilever walls use a base slab to hold the soil. Reinforced soil walls use layers of strips or fabric inside the fill."),
        ("Earth pressure",
         "Soil behind a wall pushes sideways on it. The push depends on the soil's strength, its water content and whether the wall moves. Designers add the water pressure and any load on the ground behind the wall."),
        ("Monitoring over time",
         "Slopes can move slowly for years before they fail. Engineers fit instruments such as inclinometers and survey markers and read them on a schedule. A small, steady movement is an early warning that a slope needs attention."),
    ],
    "test": [
        ("What is a failure surface in a slope?", [("a", "The paint on the top of the hill"), ("b", "The road above the slope"), ("c", "The surface inside the ground along which the slope slides"), ("d", "The top of the water tank")], "c"),
        ("What does a factor of safety above one suggest?", [("a", "The slope is stable on paper, with strength to spare"), ("b", "The slope has already failed"), ("c", "The ground is made of water"), ("d", "The wall must be removed")], "a"),
        ("What is the most common trigger for slope failure?", [("a", "Bright sunshine"), ("b", "Quiet weather"), ("c", "Birds nesting on the wall"), ("d", "Water in the ground")], "d"),
        ("What does a gravity retaining wall rely on?", [("a", "A layer of paint"), ("b", "Its own weight"), ("c", "Water pressure behind it"), ("d", "Metal bolts only")], "b"),
        ("What is an inclinometer used for?", [("a", "Measuring the colour of soil"), ("b", "Cooking food"), ("c", "Tracking slow movement in a slope over time"), ("d", "Setting the wall height")], "c"),
    ],
}
