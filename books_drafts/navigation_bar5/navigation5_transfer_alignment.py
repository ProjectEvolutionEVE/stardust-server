"""In-Motion Transfer Alignment: starting one inertial unit from a master unit while moving, with lever arms and observability."""
CODE = "navigation5_transfer_alignment"
BOOK = {
    "title": "In-Motion Transfer Alignment",
    "subtitle": "Aligning a unit from a master while on the move",
    "chapters": [
        ("Aligning on the move", "Transfer alignment starts one inertial unit from a master unit that is already aligned. The work is done while the vehicle is moving."),
        ("The master unit", "The master unit is a well-aligned inertial system, such as one carried on a larger aircraft. Its outputs guide the other unit."),
        ("Lever arms", "The two units sit at different places, so the lever arm between them must be taken into account. Rotation and acceleration can differ at each place."),
        ("Matching", "The unit being aligned matches its velocity and attitude with the master over time. A filter estimates the remaining errors."),
        ("Time", "Good alignment takes time, and it needs enough manoeuvre to make the errors observable. A short or straight flight may not be enough."),
        ("Use and observability", "Transfer alignment is used in missiles and in aircraft stores. How well it works depends on the motion of the vehicle."),
    ],
    "test": [
        ("What does transfer alignment start one unit from?",
         [("a", "A unit from a master that is already aligned"), ("b", "A fire"), ("c", "A song"), ("d", "A car")], "a"),
        ("What is a master unit?",
         [("a", "A kitchen tool"), ("b", "A school principal"), ("c", "A paper map"), ("d", "A well-aligned inertial system that guides another")], "d"),
        ("What is a lever arm?",
         [("a", "A gym weight"), ("b", "The offset between the two units' positions"), ("c", "A road"), ("d", "A colour")], "b"),
        ("What does the unit being aligned match with the master?",
         [("a", "Cake"), ("b", "The moon"), ("c", "Velocity and attitude"), ("d", "Ink")], "c"),
        ("What makes the alignment observable?",
         [("a", "A still aircraft"), ("b", "A blank map"), ("c", "A dark room"), ("d", "Enough manoeuvre")], "d"),
    ],
}
