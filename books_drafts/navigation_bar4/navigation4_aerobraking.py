"""Aerobraking: using atmospheric drag over repeated periapsis passes, heating, air density, repeated passes and propellant saved."""
CODE = "navigation4_aerobraking"
BOOK = {
    "title": "Aerobraking",
    "subtitle": "Slowing down with the thin air",
    "chapters": [
        ("Using air to slow down", "Aerobraking uses the drag of a thin upper atmosphere to slow a spacecraft. Less fuel is burned than in a braking burn. The method is slow but efficient."),
        ("Periapsis passes", "The craft dips into the air at the closest point of its orbit, called periapsis. Each pass removes a little speed. Between passes, it climbs out of the air."),
        ("Heating", "Each dip heats the craft's surface through friction with the air. Designers protect sensitive parts and monitor temperatures. Heating limits how deep the dips can go."),
        ("Density", "The air density at the dip depends on altitude and on the Sun's activity. Planners predict density to plan the passes. Errors in density change the amount of braking."),
        ("Repeated passes", "Aerobraking takes many passes over weeks or months. Each pass is planned using the results of the last one. Patience is the main requirement."),
        ("Propellant saved", "The fuel saved by aerobraking can be large. This lets a craft carry more payload or reach its target. It trades time for fuel, and its risks are heating and density uncertainty."),
    ],
    "test": [
        ("What does aerobraking use to slow a spacecraft?", [("a", "The drag of a thin upper atmosphere"), ("b", "A net thrown from the ground"), ("c", "Magnets built into the hull"), ("d", "A giant parachute opened in orbit")], "a"),
        ("What is periapsis?", [("a", "The farthest point of an orbit from the Sun"), ("b", "The point where a craft lands"), ("c", "A type of radio antenna"), ("d", "The closest point of an orbit to the body it circles")], "d"),
        ("What is a main concern with each dip?", [("a", "Losing the ability to see the Sun"), ("b", "Blocking the view of the ground"), ("c", "Heating of the craft"), ("d", "Running low on drinking water")], "c"),
        ("Why does air density matter for planning?", [("a", "It changes the colour of the Moon"), ("b", "It sets how much braking each dip gives"), ("c", "It decides the name of the mission"), ("d", "It sets the price of the craft")], "b"),
        ("What is a key feature of aerobraking?", [("a", "It is done in a single second"), ("b", "It needs no planning at all"), ("c", "It is only used on the Moon"), ("d", "It needs many passes over weeks or months")], "d"),
    ],
}
