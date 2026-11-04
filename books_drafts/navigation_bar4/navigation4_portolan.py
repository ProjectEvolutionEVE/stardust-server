"""Portolan charts: Mediterranean sea charts, rhumb-line grids, compass roses, materials, accuracy and the transition to newer charts."""
CODE = "navigation4_portolan"
BOOK = {
    "title": "Portolan Charts",
    "subtitle": "Sea charts drawn for sailors who stayed near the coast",
    "chapters": [
        ("Charts for sailors", "Portolan charts were sea charts made in the Mediterranean from the late Middle Ages. They showed coasts, harbours and bearings. Sailors used them to find their way along the shore."),
        ("The rhumb-line grid", "A web of lines radiated from compass roses across the chart. These lines are rhumb lines, paths of constant compass bearing. Navigators used dividers and a compass to read courses."),
        ("Compass roses", "Compass roses were drawn on the chart to show directions. They helped sailors find bearings between ports. Some were decorated with fine detail."),
        ("Materials", "Portolan charts were often drawn on vellum, a fine prepared animal skin. Inks and paints were chosen to last at sea. Their quality made them valuable."),
        ("Accuracy", "Portolan charts were fairly accurate for coastal distances and bearings. They were less accurate inland and over long distances. Errors in position grew over long voyages."),
        ("The transition", "Over time, charts used map projections and measured positions, and portolan charts gave way to newer charts. The shift was gradual. Both styles informed mariners for a long time."),
    ],
    "test": [
        ("Where were portolan charts mainly made?", [("a", "The Arctic ice"), ("b", "Inland deserts"), ("c", "The middle of the Pacific"), ("d", "The Mediterranean")], "d"),
        ("What are rhumb lines?", [("a", "Paths of constant compass bearing"), ("b", "Lines showing the depth of the sea"), ("c", "Lines marking national borders"), ("d", "Lines drawn by the sun")], "a"),
        ("What were compass roses on a chart for?", [("a", "To hold the chart flat"), ("b", "To show directions and bearings"), ("c", "To sell the chart to tourists"), ("d", "To mark the location of gold")], "b"),
        ("What were portolan charts often drawn on?", [("a", "Glass"), ("b", "Tin plates"), ("c", "Vellum"), ("d", "Clay tablets")], "c"),
        ("Where were portolan charts least accurate?", [("a", "Inland and over long distances"), ("b", "Along well-known coasts"), ("c", "Near harbour entrances"), ("d", "For bearings between nearby ports")], "a"),
    ],
}
