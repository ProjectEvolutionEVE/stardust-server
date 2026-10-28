"""Furnace Atmospheres and Heat Treat Control: how the gas inside a furnace changes the surface of the parts, and how to control it."""
CODE = "engineering5_furnace_atmos"
BOOK = {
    "title": "Furnace Atmospheres and Heat Treat Control",
    "subtitle": "Protective gases, carbon potential and dew point",
    "chapters": [
        ("Why the air matters", "In a furnace, the gas around the part changes the surface of the metal. The atmosphere must be controlled, or the surface will change in ways the design did not allow for."),
        ("Protective gases", "Gases such as nitrogen and argon can shield parts from oxygen while they are heated. This keeps the surface clean and free of scale."),
        ("Carbon potential", "In carburising, the carbon potential of the atmosphere sets how much carbon can enter the steel's surface. Controlling it sets the depth and hardness of the case."),
        ("Dew point control", "The dew point measures the water vapour in the furnace gas. Water vapour affects the carbon potential and the surface reactions, so it is watched closely."),
        ("Uniformity", "Parts must be heated evenly to come out consistent. Furnace design and the way parts are loaded both help keep the temperature the same across the load."),
        ("The money side", "Running a furnace uses gas and energy. Good control reduces waste, avoids scrap and keeps each batch within specification."),
    ],
    "test": [
        ("What do protective gases do?", [("a", "Make parts louder"), ("b", "Paint the parts"), ("c", "Cool parts to ice"), ("d", "Shield parts from oxygen while they are heated")], "d"),
        ("What is carbon potential?", [("a", "How much carbon the atmosphere can give to the steel surface"), ("b", "The price of carbon bars"), ("c", "The weight of a steel bar"), ("d", "The colour of coal")], "a"),
        ("What does dew point measure?", [("a", "The weight of the furnace"), ("b", "The brightness of the light"), ("c", "The water vapour in the gas"), ("d", "The number of staff on shift")], "c"),
        ("Why does uniform heating matter?", [("a", "So the furnace is bigger"), ("b", "So the parts come out consistent"), ("c", "So the parts can be painted pink"), ("d", "So the gas costs nothing")], "b"),
        ("What does running a furnace cost?", [("a", "Only paint"), ("b", "Only glass"), ("c", "Only hats for staff"), ("d", "Gas and energy")], "d"),
    ],
}
