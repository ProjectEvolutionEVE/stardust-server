"""Porkchop Plots: charts that show which departure and arrival dates make a planet trip cheapest."""
CODE = "flight4_porkchop"
BOOK = {
    "title": "Porkchop Plots",
    "subtitle": "Departure and arrival dates on one chart",
    "chapters": [
        ("A chart of dates", "A porkchop plot puts the departure date along one side and the arrival date along the other. Every point on the chart is a possible trip. The colour or the lines show how much the trip costs in fuel or speed."),
        ("Contour lines", "The chart is covered in curved lines called contours. Each line joins points that cost the same. Following a line shows which other dates give the same cost."),
        ("The cheapest island", "The lowest cost usually sits in a small region on the chart, often called an island. Planners look for these islands first, because the best dates are inside them."),
        ("Time against fuel", "A quick trip usually costs more fuel, and a slow trip costs less. The chart shows this trade. Planners pick a point that keeps the fuel within the craft's limits while keeping the travel time acceptable."),
        ("Real Mars windows", "Mars and Earth line up for good launches about every twenty-six months. A launch is most efficient inside these windows. A porkchop plot shows the best dates within a window and the trip length each one needs."),
        ("Reading one", "To read a porkchop plot, first find the lowest cost region. Then read the departure and arrival dates along the edges. Check the travel time and the fuel, and choose the date that fits the mission best."),
    ],
    "test": [
        ("What do the two sides of a porkchop plot show?", [("a", "The colours of the planets"), ("b", "The size of the crew"), ("c", "The price of the rocket"), ("d", "The possible departure date and arrival date")], "d"),
        ("What does each contour line join?", [("a", "Points that cost the same"), ("b", "Two planets"), ("c", "The Sun and the Moon"), ("d", "Two spacecraft")], "a"),
        ("Where are the best dates usually found?", [("a", "At the top corner of the chart"), ("b", "Off the edge of the chart"), ("c", "In a small region called the cheapest island"), ("d", "They are the same everywhere")], "c"),
        ("About how often do good Mars launch windows come round?", [("a", "Every day"), ("b", "Every twenty-six months"), ("c", "Every hundred years"), ("d", "Every week")], "b"),
        ("What trade does the chart show?", [("a", "Fuel and speed are never linked"), ("b", "A slow trip always costs more fuel"), ("c", "The planets change size"), ("d", "A quick trip usually costs more fuel")], "d"),
    ],
}
