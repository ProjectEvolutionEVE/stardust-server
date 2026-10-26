"""Escape Energy and C3: how much energy a launch must give to leave a planet and head for another world."""
CODE = "flight4_c3"
BOOK = {
    "title": "Escape Energy and C3",
    "subtitle": "How much a launch must give to head out into space",
    "chapters": [
        ("Escaping a planet", "To leave a planet for good, a craft must have enough energy to get away from its pull. The speed that does this from the surface is called the escape speed. For Earth it is about eleven kilometres every second."),
        ("Characteristic energy", "Planners use a number called the characteristic energy, written C3. It is the energy a craft has left over once it is clear of the planet, for each kilogram of its mass. It tells how fast the craft will head out."),
        ("Hyperbolic excess speed", "Once a craft is far from the planet, it still has some speed. That leftover speed is the hyperbolic excess speed. Its square is the C3 value, so a bigger C3 means a faster start toward the target."),
        ("Launcher capability charts", "Rocket makers publish charts that show how much mass a launcher can send out for each C3 value. A bigger rocket can reach a bigger C3, but only with less mass on board. The chart shows the trade."),
        ("Interplanetary targets", "Different targets need different C3 values. A trip to Mars needs a modest value, while a fast trip to the outer planets needs a much larger one. The planner picks the C3 that matches the target and the travel time."),
        ("Reading a C3 table", "A C3 table lists the launch date, the C3 value and the mass that can be sent. Read along the row for the date you want. Look for the highest mass that keeps the C3 you need, and check the margin."),
    ],
    "test": [
        ("What is the escape speed from Earth's surface, roughly?", [("a", "About one kilometre an hour"), ("b", "About a thousand kilometres a second"), ("c", "About eleven kilometres a second"), ("d", "About a metre a second")], "c"),
        ("What does C3 measure?", [("a", "The colour of a launch"), ("b", "The number of crew"), ("c", "The age of a rocket"), ("d", "The energy a craft has left over once clear of the planet, per kilogram")], "d"),
        ("What is the hyperbolic excess speed?", [("a", "The speed of a spacesuit"), ("b", "The speed a craft keeps once it is far from the planet"), ("c", "The top speed of a car"), ("d", "The speed of sound in space")], "b"),
        ("What is the trade on a launcher chart?", [("a", "The rocket gets heavier as it climbs"), ("b", "Each launch costs the same"), ("c", "A bigger C3 allows a bigger mass only with less mass on board"), ("d", "Mass does not matter")], "c"),
        ("What does a bigger C3 mean for a trip?", [("a", "A faster start toward the target"), ("b", "A slower trip home"), ("c", "No change at all"), ("d", "A craft that cannot leave the planet")], "a"),
    ],
}
