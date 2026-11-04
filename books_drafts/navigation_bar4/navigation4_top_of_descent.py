"""Top of descent planning: the descent profile, rate and speed, wind, fuel and arrival."""
CODE = "navigation4_top_of_descent"
BOOK = {
    "title": "Top of Descent Planning",
    "subtitle": "Starting down at the right moment",
    "chapters": [
        ("When to start down", "The top of descent is the point where an aircraft begins its descent to the destination. Starting too late means a steep and fast arrival. Starting too early wastes time and fuel."),
        ("The descent profile", "The descent profile is the planned path down, shown as height against distance. Many aircraft aim for a steady rate of descent. The profile depends on the aircraft and the airspace."),
        ("Rate and speed", "The rate of descent is measured in feet per minute, and the speed is set separately. Both are planned to meet the altitude restrictions. Changing one changes the other."),
        ("Wind", "Headwinds and tailwinds change how far the aircraft travels during the descent. Planners include wind forecasts in the calculation. An accurate forecast keeps the arrival on plan."),
        ("Fuel", "A well-planned descent saves fuel, because engines run at low power for longer. Descending late can mean a steep and costly approach. Efficient descents are part of good flight planning."),
        ("Arrival", "The descent should bring the aircraft to the right point at the right height and speed. Controllers may give headings or speed changes to help. The top of descent is a key point in every flight plan."),
    ],
    "test": [
        ("What is the top of descent?", [("a", "The highest point of the flight"), ("b", "The place where the fuel is loaded"), ("c", "The point where the descent to the destination begins"), ("d", "The start of a taxi")], "c"),
        ("What is a descent profile?", [("a", "A photo of the pilot"), ("b", "The planned path down, height against distance"), ("c", "A list of passengers"), ("d", "A forecast for the next week")], "b"),
        ("What is the rate of descent measured in?", [("a", "Feet per minute"), ("b", "Miles per gallon"), ("c", "Kilograms per second"), ("d", "Litres per hour")], "a"),
        ("How can wind affect a descent?", [("a", "It has no effect at all"), ("b", "It only affects the paint"), ("c", "It makes the aircraft heavier"), ("d", "It changes how far the aircraft travels during it")], "d"),
        ("Why is a well-planned descent good for fuel?", [("a", "Engines are switched off for good"), ("b", "Fuel costs nothing during descent"), ("c", "Engines run at low power for longer"), ("d", "The aircraft carries more passengers")], "c"),
    ],
}
