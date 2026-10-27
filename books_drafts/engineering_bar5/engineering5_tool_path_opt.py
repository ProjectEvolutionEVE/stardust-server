"""Tool-Path Optimisation and Cycle Time: how the route a cutter takes sets how long a part takes and what it costs."""
CODE = "engineering5_tool_path_opt"
BOOK = {
    "title": "Tool-Path Optimisation and Cycle Time",
    "subtitle": "Shorter routes, steadier cuts and the money side of machine time",
    "chapters": [
        ("Why the path matters", "A cutting machine follows a tool path, a list of moves the cutter makes. The path decides how long a part takes and how well it comes out. Two paths can cut the same shape and still differ a lot in time and tool wear."),
        ("Air cuts", "An air cut is a move where the cutter travels without touching material. Air cuts add machine time and add nothing to the part. Short links between cuts and a sensible order of work remove most of them."),
        ("Steady engagement", "Engagement is how much of the cutter touches the material at one moment. A path that keeps engagement steady, instead of spiking in sharp corners, protects the tool and lets the machine run more evenly."),
        ("Simulating first", "A simulation runs the path on screen before any metal is cut. It shows collisions, gouges and wasted moves. Finding a fault on screen costs seconds, while finding it on the machine can cost a tool and a part."),
        ("Cycle time and money", "Cycle time is the time to make one part from start to finish. A machine costs money every hour it runs, so a shorter cycle means more parts from the same machine and a lower cost for each one."),
        ("Putting it together", "Good planning weighs air moves, steady load and a clean simulation together. The aim is the fastest safe path that still gives the finished part the quality the design needs."),
    ],
    "test": [
        ("What is an air cut?", [("a", "A cut made with coolant spray"), ("b", "A move where the cutter travels without touching material"), ("c", "A cut made in soft aluminium only"), ("d", "A cut made by a laser beam")], "b"),
        ("Why does steady tool engagement help?", [("a", "It makes the part heavier"), ("b", "It stops the machine needing any power"), ("c", "It removes the need for a drawing"), ("d", "It avoids sudden load spikes that wear the tool")], "d"),
        ("Why simulate a path before cutting?", [("a", "To find collisions and faults on screen instead of on the machine"), ("b", "To make the metal harder"), ("c", "To change the colour of the part"), ("d", "To skip the quality check")], "a"),
        ("What is cycle time?", [("a", "The time the coolant pump stays on"), ("b", "The age of the machine"), ("c", "The time to make one part from start to finish"), ("d", "The number of tools in the rack")], "c"),
        ("What usually happens to cost per part when the path gets shorter?", [("a", "It goes down, because the machine makes more parts in the same time"), ("b", "It goes up, because the machine works harder"), ("c", "It stays the same, because machine time is free"), ("d", "It doubles")], "a"),
    ],
}
