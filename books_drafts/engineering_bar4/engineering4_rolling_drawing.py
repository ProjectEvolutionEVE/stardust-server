"""Rolling, Drawing and Wire Making: mills, dies and passes that shape metal by squeezing and pulling."""
CODE = 'engineering4_rolling_drawing'
BOOK = {
    "title": "Rolling, Drawing and Wire Making",
    "subtitle": "Mills, dies and passes that shape metal by squeezing and pulling",
    "chapters": [
        ("Rolling metal",
         "Metal is squeezed between turning rolls, which make it thinner and longer. Rolling can be done hot, when the metal is soft, or cold, for a harder finish and tighter sizes."),
        ("Reduction per pass",
         "Each pass takes off only a limited share of the thickness. Taking too much at once can crack the metal or overload the mill. Several gentle passes are safer than one heavy one."),
        ("Annealing between passes",
         "Cold working makes metal hard and brittle. Annealing heats the metal and lets it cool so it softens again, and more passes can follow. It is a simple way to keep working a metal without breaking it."),
        ("Drawing through a die",
         "Wire and rod are pulled through a tapered die, a hole that is slightly smaller than the metal. Each pull makes the wire a little thinner and longer. The die sets the final diameter."),
        ("Wire strength",
         "Cold drawing raises the strength of wire, but it lowers the metal's ability to stretch. Wire that has been drawn too far can become too brittle to use. Annealing can restore some stretch."),
        ("Tooling cost",
         "Rolls and dies wear and must be replaced or ground back. Their cost is spread over the metres or tonnes of metal they make. Planning the number of passes and dies keeps that cost in check."),
    ],
    "test": [
        ("What is the main effect of squeezing metal between rolls?",
         [("a", "It makes the metal thinner and longer"), ("b", "It adds carbon to the metal"), ("c", "It cools the metal to ice"), ("d", "It cuts the metal into pieces")], "a"),
        ("Why is annealing used between passes?",
         [("a", "To paint the metal"), ("b", "To make it heavier"), ("c", "To soften cold-worked metal so it can be worked further"), ("d", "To remove the grain from the metal")], "c"),
        ("What is a drawing die?",
         [("a", "A type of furnace"), ("b", "A paint roller"), ("c", "A tapered hole that wire is pulled through"), ("d", "A saw")], "c"),
        ("What does cold drawing usually do to wire?",
         [("a", "Makes it weaker"), ("b", "Makes it melt"), ("c", "Makes it lighter in colour"), ("d", "Raises its strength")], "d"),
        ("Why take only a limited reduction per pass?",
         [("a", "To make the rolls turn faster"), ("b", "To save paint"), ("c", "To add ore to the metal"), ("d", "To avoid cracking and overloading the mill")], "d"),
    ],
}
