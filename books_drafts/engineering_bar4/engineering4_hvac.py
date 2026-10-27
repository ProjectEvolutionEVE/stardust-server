"""Heating, Ventilation and Air Conditioning Design: sizing a building's heating and cooling, and moving air well."""
CODE = 'engineering4_hvac'
BOOK = {
    "title": "Heating, Ventilation and Air Conditioning Design",
    "subtitle": "Sizing a building's heating and cooling, and moving air well",
    "chapters": [
        ("Load calculation",
         "The design starts by working out how much heat a building gains or loses. Walls, windows, people, lights and fresh air all count toward that total."),
        ("Duct layout",
         "Ducts carry air to each room with the least resistance. Short, smooth runs with few sharp bends save fan power."),
        ("Air flow",
         "The air flow must match the needs of each room, so the air is fresh and evenly mixed. Too little air feels stuffy, and too much wastes energy."),
        ("Heat recovery",
         "A heat recovery unit moves heat from outgoing air into the incoming fresh air. This cuts the heating or cooling needed to condition that fresh air."),
        ("Controls",
         "Thermostats, sensors and timers keep the system matched to how the building is used. Good controls stop heating and cooling from fighting each other."),
        ("Running cost of a plant",
         "Running cost depends on the energy used by fans, pumps and compressors, plus maintenance. Efficient design and controls keep it low."),
    ],
    "test": [
        ("What does a load calculation work out?",
         [("a", "The number of chairs"), ("b", "The paint needed"), ("c", "How much heat a building gains or loses"), ("d", "The window colour")], "c"),
        ("Why keep duct runs short and smooth?",
         [("a", "To save fan power by reducing resistance"), ("b", "To add paint"), ("c", "To hide them"), ("d", "To make noise")], "a"),
        ("What does a heat recovery unit do?",
         [("a", "Cools the sky"), ("b", "Burns fuel"), ("c", "Makes ice"), ("d", "Moves heat from outgoing air to incoming air")], "d"),
        ("What happens if the air flow is too low?",
         [("a", "The building is always too cold"), ("b", "The air becomes stuffy"), ("c", "The walls grow"), ("d", "The lights dim")], "b"),
        ("What do good controls prevent?",
         [("a", "Heating and cooling fighting each other"), ("b", "Paint drying"), ("c", "Fire alarms"), ("d", "Shiny floors")], "a"),
    ],
}
