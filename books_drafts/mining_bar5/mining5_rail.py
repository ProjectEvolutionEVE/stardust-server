"""Rail Haulage of Ore: moving ore by train, with attention to axle loads, grades, locomotives, track geometry and scheduling."""
CODE = "mining5_rail"
BOOK = {
    "title": "Rail Haulage of Ore",
    "subtitle": "Rail loads, grades, locomotives, track geometry and scheduling",
    "chapters": [
        ("Ore by train",
         "Rail is an efficient way to move large amounts of ore over long distances. A train can carry many wagons at once, and steel wheels on steel rails roll with little friction. Rail suits routes that run steadily between a mine and a port or mill."),
        ("Rail loads",
         "Each axle carries a load, and the track is designed for a maximum axle load. Heavier loads need stronger track and bridges. Engineers check the loads before a new line is approved."),
        ("Grades",
         "A grade is the steepness of the track. A train climbs slowly on a steep grade and needs more power to do so. Heavy trains on steep grades need extra locomotives or shorter loads."),
        ("Locomotives",
         "Locomotives supply the pulling power. Diesel and electric locomotives are both used. Choosing the right type depends on power supply, route and running costs."),
        ("Track geometry",
         "Curves and the gauge of the track control how smoothly a train runs. Tight curves wear wheels and rails and slow the train. Regular inspection keeps the track within its design limits."),
        ("Scheduling and economics",
         "A rail timetable matches train runs to the mine's output and the port's needs. Trains waiting on sidings cost money. Good scheduling and fuel-efficient running lower the cost per tonne."),
    ],
    "test": [
        ("What does rail haulage move?",
         [("a", "Large amounts of ore by train over long distances"), ("b", "Only letters"), ("c", "Only people on holiday"), ("d", "Only fresh flowers")], "a"),
        ("What is an axle load?",
         [("a", "The load carried by one axle"), ("b", "The name of the train driver"), ("c", "The colour of the locomotive"), ("d", "The price of the ticket")], "a"),
        ("What does a steep grade do to a loaded train?",
         [("a", "It makes the train float"), ("b", "It makes the train lighter"), ("c", "It needs more power to climb"), ("d", "It has no effect")], "c"),
        ("What does track geometry describe?",
         [("a", "The number of stations"), ("b", "The colour of the signals"), ("c", "The size of the ticket office"), ("d", "The curves and gauge that control how smoothly a train runs")], "d"),
        ("What helps lower the cost per tonne on rail?",
         [("a", "Waiting on sidings all day"), ("b", "Good scheduling and fuel-efficient running"), ("c", "Running empty trains"), ("d", "Ignoring the timetable")], "b"),
    ],
}
