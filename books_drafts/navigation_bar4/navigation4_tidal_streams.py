"""Tidal streams and currents: flow in channels, stream atlases, timing, rate and prediction, and the effect on course."""
CODE = "navigation4_tidal_streams"
BOOK = {
    "title": "Tidal Streams and Currents",
    "subtitle": "Water on the move with the tide",
    "chapters": [
        ("Water on the move", "Tidal streams are the horizontal flow of water that comes with rising and falling tides. They can be strong in narrow channels. A ship must allow for them."),
        ("Flow in channels", "Water is squeezed through narrow channels and speeds up. Headlands and islands also make the flow faster and more turbulent. The effect is strongest at spring tides."),
        ("Stream atlases", "A stream atlas gives the direction and rate of the tidal stream at many points and times. Navigators use it to plan the course. It is a standard reference for coastal waters."),
        ("Timing", "The strength and direction of the stream change through the tide cycle. Passing a headland at the wrong time can mean a strong set against the ship. Timing the passage well saves fuel and time."),
        ("Rate and prediction", "The rate is the speed of the flow, often given in knots. Predictions use the tide's timing and the local pattern. Real flows may differ from predictions in storms."),
        ("The effect on course", "The stream pushes the ship sideways from its intended track. This is called set and drift. Navigators correct the heading to keep the ship on the planned track."),
    ],
    "test": [
        ("What are tidal streams?", [("a", "Rain falling into the sea"), ("b", "Waves caused by ships"), ("c", "Horizontal flow of water that comes with the tide"), ("d", "Ice melting at the poles")], "c"),
        ("Why does tidal flow speed up in a narrow channel?", [("a", "Water is squeezed through the narrow gap"), ("b", "The channel is warmer"), ("c", "The water gets heavier"), ("d", "The Moon pulls only in channels")], "a"),
        ("What does a stream atlas give?", [("a", "The price of fuel at each port"), ("b", "The names of local fish"), ("c", "The height of nearby towers"), ("d", "The direction and rate of the stream at many points and times")], "d"),
        ("Why does timing matter when passing a headland?", [("a", "The headland changes colour"), ("b", "A strong set against the ship may occur"), ("c", "The ship's paint dries"), ("d", "The headland blocks the wind")], "b"),
        ("What term describes a current pushing a ship sideways from its track?", [("a", "Gain"), ("b", "Set"), ("c", "Lift"), ("d", "Pitch")], "b"),
    ],
}
