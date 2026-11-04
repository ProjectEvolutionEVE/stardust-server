"""Rhumb Lines and Mercator Sailing: steady bearings, straight charts, and the longer way round."""
CODE = "navigation4_rhumb_lines"
BOOK = {
    "title": "Rhumb Lines and Mercator Sailing",
    "subtitle": "Steady bearings, straight charts, and the longer way round",
    "chapters": [
        ("A line of constant bearing", "A rhumb line keeps the same compass bearing all the way along its length. A ship that steers one course follows a rhumb line. It is the easiest path to follow by compass."),
        ("The Mercator stretch", "On a Mercator chart, a rhumb line appears as a straight line. The chart stretches the north-south scale as you move away from the equator. This stretch is what makes the rhumb line straight."),
        ("Meridional parts", "Meridional parts are a table of values that match the Mercator stretch. Using them, you can work out the difference of latitude for a rhumb line on the chart. They make the calculation exact for this kind of line."),
        ("Distance on a rhumb", "The distance along a rhumb line depends on the difference of latitude and the course. Working it out needs the course and the meridional parts. The result is accurate for this kind of route."),
        ("Rhumb versus great circle", "A great circle is the shortest path over the surface of the sphere. A rhumb line is usually longer, but it keeps one bearing. On a long voyage, the great circle can save a lot of distance."),
        ("Choosing the route", "A navigator balances distance against convenience. A great circle route may need frequent changes of course. A rhumb line is simpler to steer, and the right choice depends on the voyage."),
    ],
    "test": [
        ("What does a rhumb line keep constant?",
         [("a", "Its speed"), ("b", "Its distance from the Pole"), ("c", "Its compass bearing"), ("d", "Its height above the sea")], "c"),
        ("How does a rhumb line appear on a Mercator chart?",
         [("a", "As a straight line"), ("b", "As a circle"), ("c", "As a dot"), ("d", "As a spiral")], "a"),
        ("What are meridional parts used for?",
         [("a", "Measuring wind speed"), ("b", "Working out the difference of latitude for a rhumb line"), ("c", "Naming the ship"), ("d", "Finding the time")], "b"),
        ("Which path is the shortest over the sphere?",
         [("a", "A rhumb line"), ("b", "A parallel of latitude"), ("c", "A straight line on the chart"), ("d", "A great circle")], "d"),
        ("Why might a navigator choose a rhumb line?",
         [("a", "It is always the shortest"), ("b", "It follows the Sun"), ("c", "It is simpler to steer on one bearing"), ("d", "It needs no chart")], "c"),
    ],
}
