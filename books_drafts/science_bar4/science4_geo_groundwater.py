"""Groundwater, Porosity and Aquifers: how water moves through rock and sediment, and what that means for wells and pollution."""
CODE = "science4_geo_groundwater"
BOOK = {
    "title": "Groundwater, Porosity and Aquifers",
    "subtitle": "Pore space, flow through rock and the water beneath our feet",
    "chapters": [
        ("Porosity and permeability",
         "Porosity is the share of a rock’s volume made up of open pore space. Permeability is how easily water can flow through those pores. A rock can be very porous yet hardly permeable if its pores are not connected."),
        ("Darcy’s law",
         "Darcy’s law says the rate of flow through a porous material is proportional to the hydraulic gradient, which is the change in water level over distance, and to the material’s permeability. Water flows from high levels toward low levels. The law is the basic tool for estimating groundwater movement."),
        ("Aquifer types",
         "An aquifer is a body of rock or sediment that holds and transmits useful amounts of water. An unconfined aquifer has its top open to the surface. A confined aquifer is sealed above by a layer that holds the water under pressure."),
        ("Well drawdown",
         "When water is pumped from a well, the water level around it drops. This lowered zone is the cone of depression, and its size depends on how fast the water is pumped and how permeable the aquifer is. Nearby wells can be affected by the drawdown."),
        ("Flow direction from water levels",
         "Water levels measured in several wells can be used to map the water table. Water usually flows at right angles to the contour lines of equal level, from high to low. This simple map shows where groundwater is going."),
        ("Contaminant pathways",
         "Pollutants move with groundwater, usually following its flow direction. How fast they travel depends on the rock, its pores and the chemistry of the pollutant. Knowing the pathway helps engineers decide where to place wells and where to watch for trouble."),
    ],
    "test": [
        ("What does porosity measure?",
         [("a", "How easily water flows through a rock"), ("b", "The weight of the rock"), ("c", "The age of the rock"), ("d", "The share of a rock’s volume made of open pore space")], "d"),
        ("What is permeability?",
         [("a", "How many fossils a rock holds"), ("b", "How easily water can flow through the pores"), ("c", "How hot the rock is"), ("d", "How high a hill stands")], "b"),
        ("What does a confined aquifer have that an unconfined one does not?",
         [("a", "No water at all"), ("b", "An open top to the surface"), ("c", "A top sealed by a layer that holds the water under pressure"), ("d", "A top made of ice")], "c"),
        ("When a well is pumped, what forms around it?",
         [("a", "A new river"), ("b", "A layer of ice"), ("c", "A mountain of sand"), ("d", "A cone of depression, where the water level drops")], "d"),
        ("How does groundwater usually flow relative to the lines of equal water level?",
         [("a", "At right angles to them, from high to low"), ("b", "Along the lines"), ("c", "Upward against gravity"), ("d", "Randomly in all directions")], "a"),
    ],
}
