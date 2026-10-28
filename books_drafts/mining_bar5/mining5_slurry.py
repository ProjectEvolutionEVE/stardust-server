"""Long-Distance Slurry Pipelines: moving ore or tailings as a water mix over many kilometres, with pumping stations, wear and settling to manage."""
CODE = "mining5_slurry"
BOOK = {
    "title": "Long-Distance Slurry Pipelines",
    "subtitle": "Pump stations, pressure losses, wear, settling and pipe design",
    "chapters": [
        ("Solids carried by water",
         "A slurry pipeline carries fine solids mixed with water over long distances. It can move concentrate, tailings or other material without trucks. Once built, it runs day and night with little labour."),
        ("Pump stations",
         "Pumps along the line add the energy needed to keep the slurry moving. The stations are spaced to suit the pressure and the terrain. Each station needs power, control and maintenance."),
        ("Pressure losses",
         "Friction in the pipe causes a steady loss of pressure along its length. The loss grows with flow speed, pipe roughness and the amount of solids. Designers calculate the losses before choosing pump sizes."),
        ("Wear",
         "Hard particles scour the inside of the pipe, especially at bends and low points. Wear makes the pipe thinner over time. Engineers use thicker pipe, wear-resistant liners and regular checks."),
        ("Settling",
         "If the flow speed drops too low, solids can settle and block the pipe. A pipeline must run above a minimum speed to keep solids in suspension. Stopping and restarting the flow needs careful control."),
        ("Pipe design and costs",
         "Pipe diameter, wall thickness and route are chosen together with the pumps. The cost includes pipe, pumps, power and upkeep for many years. A well-designed line saves money over its whole life."),
    ],
    "test": [
        ("What does a slurry pipeline carry?",
         [("a", "Dry sand by air"), ("b", "Fuel oil only"), ("c", "Passengers"), ("d", "Fine solids mixed with water")], "d"),
        ("What causes pressure losses in a pipeline?",
         [("a", "The colour of the pipe"), ("b", "Friction along the pipe"), ("c", "The name of the pump maker"), ("d", "The number of birds")], "b"),
        ("Where does wear often happen fastest?",
         [("a", "At bends and low points"), ("b", "At the top of the sky"), ("c", "Inside the office"), ("d", "On the water tank lid")], "a"),
        ("What can happen if flow speed drops too low?",
         [("a", "Solids settle and can block the pipe"), ("b", "The pipe becomes lighter"), ("c", "The water turns to ice at once"), ("d", "The pump runs faster")], "a"),
        ("What is included in the cost of a pipeline?",
         [("a", "Only the paint on the pipe"), ("b", "Only the cost of the first day"), ("c", "Pipe, pumps, power and upkeep over many years"), ("d", "Nothing but the name")], "c"),
    ],
}
