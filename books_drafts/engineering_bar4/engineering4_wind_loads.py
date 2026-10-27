"""Wind loads on buildings and towers: gusts, pressure coefficients, vortex shedding, cladding, tall shapes and wind testing."""
CODE = "engineering4_wind_loads"
BOOK = {
    "title": "Wind Loads on Buildings and Towers",
    "subtitle": "Gusts, pressure, vortex shedding and tall shapes",
    "chapters": [
        ("Gusts and speed",
         "Wind speed changes from moment to moment, and short gusts can be stronger than the average. Designers use a gust speed for a chosen return period. The wind load grows quickly with the speed, so the gust figure matters."),
        ("Pressure coefficients",
         "A pressure coefficient describes how the wind pushes or pulls on each face of a building. Walls facing the wind are pushed in, while roofs and sides are often pulled outward. Designers combine these coefficients with the gust pressure."),
        ("Vortex shedding",
         "As wind passes a tall, slender structure, it can leave swirling vortices that shed alternately from each side. If the shedding rate matches the structure's natural frequency, the movement can build up. Designers check this for chimneys and tall masts."),
        ("Cladding loads",
         "Cladding, the outer skin of a building, feels the highest local suction at corners and edges. These local loads can be larger than the average load on the whole wall. Fixings must be designed for the peak local load."),
        ("Shape choices for tall structures",
         "Rounded corners, tapered forms and openings can reduce wind loads on a tall tower. A simple change of shape can cut the force on the structure. Designers test shape options early because they are cheaper to change on paper."),
        ("Wind testing",
         "Engineers test scale models in wind tunnels to measure pressures and movement. Tests show loads that rules of thumb may miss, especially for unusual shapes. The results feed into the final design and the cladding fixings."),
    ],
    "test": [
        ("What is a gust?", [("a", "A floor in a tower"), ("b", "A type of building paint"), ("c", "A short burst of wind stronger than the average"), ("d", "A roof tile")], "c"),
        ("What does a pressure coefficient describe?", [("a", "The number of windows"), ("b", "The cost of glass"), ("c", "How the wind pushes or pulls on each face of a building"), ("d", "The age of a tower")], "c"),
        ("What is vortex shedding?", [("a", "Swirling vortices that shed from a structure as wind passes it"), ("b", "Rain falling into a drain"), ("c", "Sand blowing across a road"), ("d", "Ice forming on glass")], "a"),
        ("Where do cladding loads often peak?", [("a", "Under the car park"), ("b", "In the middle of the basement"), ("c", "On the inside of the doors"), ("d", "At corners and edges, where local suction is highest")], "d"),
        ("Why are scale models tested in a wind tunnel?", [("a", "To choose the colour of the cladding"), ("b", "To measure pressures and movement that rules of thumb may miss"), ("c", "To make the wind stronger"), ("d", "To avoid any calculation")], "b"),
    ],
}
