"""Hydroforming of Tubes and Sheets: internal pressure forming, pressure paths, wall thinning, tooling cost and part design."""
CODE = "engineering5_hydroforming"
BOOK = {
    "title": "Hydroforming of Tubes and Sheets",
    "subtitle": "Shaping metal with fluid pressure instead of hard punches",
    "chapters": [
        ("Pressure instead of punches",
         "In hydroforming, a fluid, usually water with oil or an emulsion, pushes the metal into a die. The fluid presses from the inside or the outside and forms the part without a heavy punch."),
        ("Tubes and sheets",
         "Tube hydroforming pushes a tube out to fill a die, and sheet hydroforming presses a flat blank into a die. Both make complex shapes in one step. Tubes are common in car frames and exhaust parts."),
        ("The pressure path",
         "The pressure must rise in the right order, while the axial push on the tube feeds in more material. This is the pressure path. A poor path bursts the wall or wrinkles it, so the path is planned with great care."),
        ("Wall thinning",
         "As the metal stretches, its wall gets thinner, sometimes too thin in key places. Engineers check the thinning with simulation and test parts. A design that keeps the wall thick enough is a design that will hold up."),
        ("Tooling cost",
         "The dies and pressure equipment are expensive to build. Hydroforming pays off when the part is complex and the run is large. Engineers compare the tooling cost with what the method saves in welds and parts."),
        ("Designing for the process",
         "Parts designed for hydroforming have smooth shapes and gentle bends. Sharp corners thin the wall and cause cracks. Good design makes the process easier and the part stronger."),
    ],
    "test": [
        ("What pushes the metal into the die in hydroforming?",
         [("a", "A wooden hammer"), ("b", "A cold wind"), ("c", "A magnet"), ("d", "A fluid under pressure")], "d"),
        ("What does tube hydroforming do?",
         [("a", "It pushes a tube out to fill a die"), ("b", "It cuts a tube into rings"), ("c", "It melts the tube"), ("d", "It paints the tube")], "a"),
        ("What is the pressure path?",
         [("a", "The road to the factory"), ("b", "The order in which the pressure rises during forming"), ("c", "The list of tool names"), ("d", "The path of the sun")], "b"),
        ("Why does a metal wall thin during hydroforming?",
         [("a", "The metal shrinks in the cold"), ("b", "The metal is painted"), ("c", "The metal stretches as it forms"), ("d", "The metal is cut away")], "c"),
        ("What kind of part design suits hydroforming?",
         [("a", "Very sharp corners everywhere"), ("b", "Holes drilled through every face"), ("c", "Paper-thin walls with no support"), ("d", "Smooth shapes with gentle bends")], "d"),
    ],
}
