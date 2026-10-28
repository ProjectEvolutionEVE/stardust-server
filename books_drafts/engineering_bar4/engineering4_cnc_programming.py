"""CNC programming: coordinate frames, toolpath strategy, feeds and speeds in code, post-processing, simulation checks and cost per part."""
CODE = "engineering4_cnc_programming"
BOOK = {
    "title": "CNC Programming: Toolpaths and Code",
    "subtitle": "Coordinate frames, toolpaths and checking the code",
    "chapters": [
        ("Coordinates and the machine",
         "A CNC machine moves its cutting tool along axes using numbered coordinates. The program sets a zero point, called the work offset, on the part. Every move in the program is measured from that point."),
        ("Toolpath strategy",
         "A toolpath is the route the cutter follows. Engineers choose the path to remove material efficiently and safely. Roughing takes most of the material quickly, and finishing passes give the final size and surface."),
        ("Feeds and speeds",
         "Feed is how fast the tool moves through the material, and speed is how fast the tool surface turns. The programmer sets both in the code. They must suit the material, the tool and the machine."),
        ("Post-processing",
         "A post-processor turns the toolpath from a CAM system into the exact code a particular machine understands. Each machine may need its own post. A wrong post can cause errors that are hard to spot."),
        ("Simulation checks",
         "Before running a program, programmers simulate the toolpath on screen to check for collisions and errors. A simulation shows the cut before any metal is touched. Checking first saves tools, parts and machines."),
        ("Cost per part",
         "The cost of a machined part includes machine time, tooling, labour and setup. Faster feeds can cut time but wear tools sooner. Programmers balance the cycle time against tool life to find the lowest cost per part."),
    ],
    "test": [
        ("What does a work offset set?", [("a", "The price of the material"), ("b", "The colour of the machine"), ("c", "The zero point of the part on the machine"), ("d", "The number of staff")], "c"),
        ("What is a toolpath?", [("a", "A road outside the factory"), ("b", "A path for visitors"), ("c", "The route the cutter follows"), ("d", "A drain in the floor")], "c"),
        ("What is a post-processor?", [("a", "It turns the toolpath into the code a particular machine understands"), ("b", "It paints the finished part"), ("c", "It stores the parts in a box"), ("d", "It cools the machine")], "a"),
        ("Why simulate a toolpath before running it?", [("a", "To skip the program"), ("b", "To make the metal heavier"), ("c", "To change the colour of the tool"), ("d", "To check for collisions and errors before any metal is cut")], "d"),
        ("What do feeds and speeds have to suit?", [("a", "Only the weather"), ("b", "The material, the tool and the machine"), ("c", "Only the colour of the part"), ("d", "Only the staff's shoes")], "b"),
    ],
}
