"""Tool wear and the Taylor equation: wear modes, tool life curves, the cutting speed trade-off, change costs and the cheapest speed."""
CODE = "engineering4_tool_wear"
BOOK = {
    "title": "Tool Wear and the Taylor Equation",
    "subtitle": "Wear modes, tool life and the cheapest cutting speed",
    "chapters": [
        ("How cutting tools wear",
         "Cutting tools wear as they work. Common modes include flank wear on the side of the tool, crater wear on the rake face, and chipping at the edge. The wear mode tells the machinist what is happening at the cutting edge."),
        ("Tool life curves",
         "A tool life curve shows how long a tool lasts at different cutting speeds. Faster cutting wears the tool more quickly. The curve is often drawn on log scales to make the trend easy to read."),
        ("The Taylor equation",
         "The Taylor equation relates cutting speed and tool life in a simple power form. It lets a machinist estimate tool life from a few tests. The constants depend on the tool and the material being cut."),
        ("The speed trade-off",
         "Cutting faster removes metal faster but shortens tool life. Cutting slower makes tools last longer but takes more time. The best speed lies between these two effects."),
        ("Tool change costs",
         "Each tool change costs machine stoppage, labour and the tool itself. A tool change also adds a risk of setup error. These costs are part of the total cost of a machining job."),
        ("Choosing the cheapest speed",
         "The cheapest cutting speed balances the machining cost and the tool cost per part. Engineers combine the Taylor equation with the time and cost of each tool change. The result is the speed that gives the lowest cost per part, not the fastest cut."),
    ],
    "test": [
        ("What is flank wear?", [("a", "A crack in a window"), ("b", "A wear on the paint of the machine"), ("c", "Wear on a floor tile"), ("d", "Wear on the side of the cutting tool")], "d"),
        ("What happens to tool life when cutting speed rises?", [("a", "The tool lasts longer"), ("b", "The tool wears out more quickly"), ("c", "The tool becomes heavier"), ("d", "The tool stops wearing altogether")], "b"),
        ("What does the Taylor equation relate?", [("a", "Rent and staff numbers"), ("b", "Paint colour and sound"), ("c", "Cutting speed and tool life"), ("d", "Weather and tide")], "c"),
        ("Why do tool changes count as a cost?", [("a", "They make the part heavier"), ("b", "They cost nothing at all"), ("c", "They cost machine stoppage, labour and the tool itself"), ("d", "They remove the need for setup")], "c"),
        ("What is the cheapest cutting speed?", [("a", "The speed that gives the lowest cost per part, balancing tool and machine costs"), ("b", "The fastest speed always"), ("c", "The slowest speed always"), ("d", "Any speed at random")], "a"),
    ],
}
