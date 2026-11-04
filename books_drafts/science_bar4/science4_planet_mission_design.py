"""Spacecraft Mission Design and Gravity Assists: transfer orbits, Hohmann transfers, gravity assists, launch windows, delta-v budgets and instrument selection."""
CODE = "science4_planet_mission_design"
BOOK = {
    "title": "Spacecraft Mission Design and Gravity Assists",
    "subtitle": "Transfer orbits, gravity assists and delta-v",
    "chapters": [
        ("Transfer orbits", "A transfer orbit moves a spacecraft from one orbit to another. Mission planners choose the path that needs the least fuel for the trip."),
        ("Hohmann transfers", "A Hohmann transfer moves a spacecraft between two circular orbits using two engine burns. The first burn raises the far point of the path, and the second burn makes the new orbit circular."),
        ("Gravity assists", "A spacecraft can fly past a planet and gain speed from the planet's motion, much as a ball gains speed from a moving bat. This gravity assist saves fuel on long trips."),
        ("Launch windows", "A launch window is a period when the positions of the planets make a trip efficient. Missing the window can mean waiting many months for the next one."),
        ("Delta-v budgets", "Delta-v is the total change in speed that a spacecraft needs for all its manoeuvres. Engineers add up the delta-v budget before they fix the details of a mission."),
        ("Instrument selection", "Mission planners choose instruments that fit the mass, the power and the science goals of the trip. Every instrument adds mass, so each choice has a cost."),
    ],
    "test": [
        ("What does a transfer orbit do?",
         [("a", "Keeps a spacecraft still"), ("b", "Paints the spacecraft"), ("c", "Moves a spacecraft from one orbit to another"), ("d", "Turns off the engines")], "c"),
        ("What is a Hohmann transfer?",
         [("a", "An efficient two-burn move between two circular orbits"), ("b", "A type of camera"), ("c", "A landing on the Moon"), ("d", "A kind of solar panel")], "a"),
        ("What is a gravity assist?",
         [("a", "Using a planet's pull to slow a spacecraft to a stop"), ("b", "A mechanical arm"), ("c", "A solar flare"), ("d", "Flying past a planet and gaining speed from its motion")], "d"),
        ("What is a launch window?",
         [("a", "A period when planetary positions make a trip efficient"), ("b", "A window on a rocket"), ("c", "A tool for cleaning optics"), ("d", "The moment a rocket lands")], "a"),
        ("What does delta-v measure?",
         [("a", "The colour of a spacecraft"), ("b", "The total change in speed a spacecraft needs for its manoeuvres"), ("c", "The mass of the instruments"), ("d", "The number of crew")], "b"),
    ],
}
