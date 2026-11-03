"""Topology in Spatial Data: nodes, edges, shared boundaries, and the checks that keep a map clean."""
CODE = "navigation4_topology"
BOOK = {
    "title": "Topology in Spatial Data",
    "subtitle": "How features connect, and how to catch the errors that break a map",
    "chapters": [
        ("Nodes and edges", "Topology describes how features connect. A line has nodes at its ends and edges between them. Nodes and edges let software know which lines meet."),
        ("Shared boundaries", "Two neighbouring areas can share one boundary line. Storing the line once keeps the data clean and small. If each area kept its own copy, the two could drift apart."),
        ("Adjacency", "Adjacency means which areas touch each other. Topology lets a program answer questions such as which districts border a river. Those answers come quickly once the links are stored."),
        ("Checks", "Topology checks look for gaps, overlaps and lines that hang loose. A gap between two areas that should meet is an error. Running the checks after each edit catches most problems early."),
        ("Common errors", "Typical errors include tiny slivers, lines that stop just short of each other, and areas that overlap. Snapping points together fixes many of them. A snapping distance set too large can move real features."),
        ("Networks", "Roads, rivers and pipes form networks. Topology lets a program trace a route through the links. It can also check that every street joins the grid. Network rules are a special kind of topology."),
    ],
    "test": [
        ("What does a node mark in topology?", [("a", "The colour of a feature"), ("b", "The end point where lines meet"), ("c", "The date a map was made"), ("d", "The scale of the map")], "b"),
        ("What is one benefit of storing a shared boundary once?", [("a", "The two areas stay consistent"), ("b", "The map becomes larger"), ("c", "All errors disappear"), ("d", "The scale changes")], "a"),
        ("What does adjacency describe?", [("a", "How old a map is"), ("b", "The colour of rivers"), ("c", "Which areas touch each other"), ("d", "The height above sea level")], "c"),
        ("What does a gap between two areas that should meet count as?", [("a", "A correct feature"), ("b", "An error"), ("c", "A new layer"), ("d", "A legend item")], "b"),
        ("Which kind of rule suits roads and pipes?", [("a", "Colour rules"), ("b", "Font rules"), ("c", "Label rules"), ("d", "Network rules")], "d"),
    ],
}
