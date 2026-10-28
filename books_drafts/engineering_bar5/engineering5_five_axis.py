"""Five-Axis Machining Kinematics: rotary axes, tool orientation, singularities, collision checks and programming strategies."""
CODE = "engineering5_five_axis"
BOOK = {
    "title": "Five-Axis Machining Kinematics",
    "subtitle": "Moving a tool in five directions to reach a complex part",
    "chapters": [
        ("Three lines and two turns",
         "A five-axis machine moves the tool along three straight axes and turns the part or the tool on two rotary axes. The extra turns let the tool reach a surface from many angles in one set-up."),
        ("Rotary axes",
         "The two rotary axes are usually a table that turns and tilts, or a head that turns and tilts. Their design sets how the tool can be oriented and how far it can swing. The machine's kinematics describe that motion."),
        ("Tool orientation",
         "The tool must point the right way for the surface and the cut. Changing the tilt changes the reach and the cutting conditions. Good programming keeps the tool at a sensible angle through the whole path."),
        ("Singularities",
         "A singularity is a position where two rotary axes line up and lose a degree of freedom. Near a singularity, small moves demand huge rotary motion. Programs must avoid those positions or route around them."),
        ("Collision checks",
         "The tool holder, spindle head and table can strike the part or the fixture when the axes turn. Collision checks run the full motion on a computer before any cutting starts. This saves the cost of a crash."),
        ("Programming strategies",
         "Five-axis programmers choose strategies such as tilting the tool to keep it short and steady. A good strategy cuts time and tool wear. The cost of the programming effort is weighed against the time it saves on the shop floor."),
    ],
    "test": [
        ("How many axes does a five-axis machine move?",
         [("a", "Two straight and two rotary"), ("b", "Five straight"), ("c", "Three straight and two rotary"), ("d", "One straight only")], "c"),
        ("What does tool orientation affect?",
         [("a", "The colour of the coolant"), ("b", "The name of the program"), ("c", "The number of chairs"), ("d", "The reach and the cutting conditions")], "d"),
        ("What is a singularity in five-axis motion?",
         [("a", "A position where two rotary axes line up and lose a degree of freedom"), ("b", "A broken spindle"), ("c", "A type of coolant"), ("d", "A tool that never wears")], "a"),
        ("Why do programmers run collision checks first?",
         [("a", "To count the chips"), ("b", "To find clashes between the machine and the part before cutting"), ("c", "To paint the table"), ("d", "To test the lights")], "b"),
        ("What can a good five-axis strategy save?",
         [("a", "The need for any programming"), ("b", "The need for any tools"), ("c", "Cutting time and tool wear"), ("d", "The price of the building")], "c"),
    ],
}
