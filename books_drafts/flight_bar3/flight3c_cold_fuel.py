"""Cold Fuel and Boil-Off: keeping super-cold propellant from boiling away before it is used."""
CODE = "flight3c_cold_fuel"
BOOK = {
    "title": "Cold Fuel and Boil-Off",
    "subtitle": "Keeping super-cold propellant from boiling away before it is used",
    "chapters": [
        ("Cold to store more",
         "Some rocket propellants are kept as liquids by making them very cold. Liquid oxygen is about minus 183 degrees Celsius, and liquid hydrogen is colder still, about minus 253. Cold makes a propellant dense, so more of it fits in the same tank."),
        ("Heat always gets in",
         "No tank is perfect. Warmth leaks in from the sunlit side, through the walls and along the pipes. The cold liquid takes in that heat and starts to boil. This slow loss is called boil-off."),
        ("Boil-off is lost fuel",
         "Gas that boils off cannot be burned as liquid propellant, and it builds up pressure in the tank. The crew must vent it or use it, and either way some of the fuel is gone before any burn. The loss is slow, but it never stops."),
        ("Fighting the heat",
         "Engineers fight boil-off with thick insulation, layers of thin shiny sheets, and shade from the Sun. Some craft also carry small coolers that run on the craft's electricity. Each measure adds weight or power, so the choice is always a trade-off."),
        ("Timing matters",
         "A craft that waits a long time before a burn loses more propellant to boil-off. A quick plan with a short wait keeps more fuel for the push itself. On a long trip, boil-off can decide the whole budget."),
        ("A pilot's habit",
         "Treat cold fuel like a bucket of ice on a hot day: it does not stay the same for long. Plan your burns close together where you can, and count the boil-off as a real loss in your budget. The cheapest fuel is the fuel you still have when you need it."),
    ],
    "test": [
        ("Roughly how cold is liquid hydrogen?",
         [("a", "Zero degrees Celsius"), ("b", "Minus 20 degrees Celsius"), ("c", "Minus 253 degrees Celsius"), ("d", "Plus 100 degrees Celsius")], "c"),
        ("Why does cold propellant slowly boil in its tank?",
         [("a", "Pilots open the tank on purpose"), ("b", "Heat leaks in from outside, through walls and pipes"), ("c", "Liquid fuel always fizzes"), ("d", "The engine is always running")], "b"),
        ("Why can boil-off gas not simply be left in the tank?",
         [("a", "It makes the fuel sweeter"), ("b", "It is not needed by anyone"), ("c", "It builds up pressure in the tank"), ("d", "It cools the crew")], "c"),
        ("How do engineers reduce boil-off?",
         [("a", "Make the tank hotter"), ("b", "Add thick insulation and shade from the Sun"), ("c", "Stop using liquid fuel"), ("d", "Fill the tank with sand")], "b"),
        ("Why does a long wait before a burn cost fuel?",
         [("a", "Boil-off keeps eating the propellant"), ("b", "The engine rusts"), ("c", "Fuel expires"), ("d", "Gravity gets stronger")], "a"),
    ],
}
