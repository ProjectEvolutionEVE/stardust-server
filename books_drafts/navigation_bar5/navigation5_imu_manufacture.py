"""Manufacturing Tolerances in Inertial Sensors: machining, mass balance, temperature control, testing and yield."""
CODE = "navigation5_imu_manufacture"
BOOK = {
    "title": "Manufacturing Tolerances in Inertial Sensors",
    "subtitle": "How precision is built into a sensor",
    "chapters": [
        ("Precision by hand and machine", "Inertial sensors need very tight tolerances in their parts. Machining, polishing and assembly are all done with great care."),
        ("Mass balance", "An unbalanced mass can make a sensor sensitive to vibration and acceleration. Balance is checked and adjusted during the build."),
        ("Temperature control", "Temperature can shift a sensor's output. Manufacturers control it, or measure it and correct for it, and thermal design is part of the build."),
        ("Testing", "Each unit is tested on a rate table and through temperature cycles. The tests reveal its bias and scale factor values."),
        ("Yield", "Yield is the fraction of units that pass every test. A low yield raises the cost of each good unit."),
        ("Cost", "Tight tolerances and thorough tests cost money. The best design balances performance and price for each use."),
    ],
    "test": [
        ("What do inertial sensors need in their parts?",
         [("a", "Loose fits"), ("b", "Cheese"), ("c", "Rubber"), ("d", "Very tight tolerances")], "d"),
        ("Why is mass balance checked?",
         [("a", "To paint it"), ("b", "To weigh lunch"), ("c", "An unbalanced mass can make a sensor sensitive to vibration"), ("d", "To count pages")], "c"),
        ("What does temperature control do?",
         [("a", "Changes colour"), ("b", "Prevents or corrects shifts in sensor output"), ("c", "Prints"), ("d", "Bounces")], "b"),
        ("What do rate-table tests reveal?",
         [("a", "Bias and scale factor values"), ("b", "The price"), ("c", "The menu"), ("d", "The flavour")], "a"),
        ("What is yield?",
         [("a", "The price of paint"), ("b", "The fraction of units that pass every test"), ("c", "The size of a room"), ("d", "A dance")], "b"),
    ],
}
