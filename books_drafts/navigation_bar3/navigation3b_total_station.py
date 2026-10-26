"""The Total Station: one instrument that measures angles and distance together."""
CODE = 'navigation3b_total_station'
BOOK = {
    "title": "The Total Station",
    "subtitle": "One instrument that measures angles and distance together",
    "chapters": [
        ("From theodolite to total station",
         "A theodolite measures angles, and a tape or chain measures distance. A total station puts both into one instrument. It measures horizontal and vertical angles, and the distance to a target, in one set of readings."),
        ("Measuring distance with light",
         "The total station measures distance by electronic distance measurement, or EDM. It sends a beam of infrared light toward a target, then times the return or compares the phase of the light when it comes back. The distance follows from the speed of light."),
        ("Why a reflector",
         "A prism reflector sends the light straight back to the instrument, so the reading is strong and exact. Surveyors set a prism on each point they need to measure. Without one, the beam scatters and the reading is weak."),
        ("Coordinates from one set-up",
         "Once the instrument knows where it stands and which way it faces, each reading gives a point in three dimensions: a position across the ground and a height. The points can be stored as coordinates that feed straight into a map."),
        ("Checking the set-up",
         "The total station is set up over a known point and sighted on another known point, called the back-sight. Any error in that set-up carries into every reading, so a careful surveyor checks the back-sight before measuring the rest."),
        ("Weather matters",
         "The speed of light in air depends on temperature, pressure and humidity. Good surveyors enter the air conditions into the instrument. A small error in the speed of light becomes a small error in every distance measured."),
    ],
    "test": [
        ("What does a total station measure?",
         [("a", "Only the weight of rocks"), ("b", "Angles and the distance to a target, together"), ("c", "Only the temperature"), ("d", "Only the depth of rivers")], "b"),
        ("What does EDM stand for, and what does it do?",
         [("a", "Electronic distance measurement, using light to find a distance"), ("b", "A kind of paint"), ("c", "A survey fee"), ("d", "An old map scale")], "a"),
        ("Why does a total station use a reflector prism on each point?",
         [("a", "It makes a clearer picture"), ("b", "It keeps the point warm"), ("c", "It sends the light straight back, so the reading is strong and exact"), ("d", "It hides the point from the wind")], "c"),
        ("Why do air temperature and pressure matter to a total station?",
         [("a", "They change the speed of light, so they affect the distance"), ("b", "They change the colour of the sky"), ("c", "They make the instrument heavier"), ("d", "They change the rock")], "a"),
        ("What must a surveyor check before measuring the rest of the points?",
         [("a", "The colour of the tripod"), ("b", "The name of the crew"), ("c", "The price of the instrument"), ("d", "The set-up, by sighting on a known back-sight point")], "d"),
    ],
}
