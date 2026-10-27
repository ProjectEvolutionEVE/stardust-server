"""Sheet Metal Bending and Springback: bend radius, the K-factor, grain direction, flat patterns and tool wear."""
CODE = 'engineering4_sheet_metal'
BOOK = {
    "title": "Sheet Metal Bending and Springback",
    "subtitle": "Bend radius, springback, the K-factor and flat patterns",
    "chapters": [
        ("Bending sheet metal",
         "A press brake forms a bend by pushing a punch into the sheet, which then sits over a V-shaped die. The metal is pushed past its elastic limit so it keeps the new angle. The result is a clean bend in a flat sheet."),
        ("Bend radius",
         "The bend radius is the inside curve of the bend. A tight radius can crack the outside of the bend, especially in hard or thick metal. A larger radius is safer, and the tooling is chosen to match the material."),
        ("Springback",
         "When the bending force is released, the metal partly returns toward its flat shape. This is springback. Operators bend a little past the target angle so the part settles at the right angle."),
        ("The K-factor",
         "The K-factor locates the neutral axis, the line inside the sheet that does not stretch or squeeze during the bend. It is used to work out the flat length of metal needed for a bend. Getting it right keeps finished parts the correct size."),
        ("Grain direction and flat patterns",
         "Sheet metal has a grain from rolling, and it bends more easily across the grain than along it. A flat pattern is the unfolded shape of the part, laid out before bending. Good flat patterns save material and avoid errors."),
        ("Tool wear and checking",
         "Punches and dies wear with use, so bends drift over a long run. The first part of a run is checked carefully, and measurements are repeated during the job. Worn tools are replaced before they spoil the parts."),
    ],
    "test": [
        ("What does springback mean?",
         [("a", "The metal stays permanently in the bent shape"), ("b", "The metal partly returns after the bending force is released"), ("c", "The sheet gets thicker"), ("d", "The die breaks")], "b"),
        ("Why is it best to bend across the grain where possible?",
         [("a", "It is cheaper to buy"), ("b", "It lowers the chance of cracking on tight bends"), ("c", "It makes the sheet heavier"), ("d", "It removes the need for a die")], "b"),
        ("What is a flat pattern?",
         [("a", "The finished bent part"), ("b", "A type of press"), ("c", "A paint layer"), ("d", "The unfolded blank laid out flat before bending")], "d"),
        ("To correct springback, a bend is usually:",
         [("a", "Underbent"), ("b", "Left straight"), ("c", "Overbent"), ("d", "Cut in half")], "c"),
        ("What is the risk of a very tight bend?",
         [("a", "Cracking on the outside of the bend"), ("b", "Lighter parts"), ("c", "A brighter surface"), ("d", "A longer flat pattern")], "a"),
    ],
}
