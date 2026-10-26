"""Radio Beacons: Loran, Decca and VOR. How ground-based radio signals gave sailors and pilots a position before satellites."""
CODE = "navigation3c_radio_beacons"
BOOK = {
    "title": "Radio Beacons: Loran, Decca and VOR",
    "subtitle": "How ground-based radio signals gave sailors and pilots a position before satellites",
    "chapters": [
        ("Before satellites",
         "Long before satellites, navigators used radio beacons on land. A beacon sends a signal, and a receiver on the craft turns it into a position. Several systems were in wide use in the middle of the twentieth century, and VOR still guides aircraft today."),
        ("Time difference",
         "Loran worked by timing. A pair of stations sent pulses, and the receiver measured the small difference in arrival time between them. Every fixed difference lies on a curve, so the navigator could draw a line of position from each pair."),
        ("Phase in Decca",
         "Decca compared the phase of continuous signals from pairs of transmitters. As with Loran, each pair gave a family of curves. The navigator read a position where two of those lines crossed."),
        ("A bearing from a beacon",
         "VOR sends a signal whose direction varies all round the compass. An aircraft's receiver reads the radial, which is the bearing from the beacon, and it can fly along a chosen radial to reach the station."),
        ("Coverage and limits",
         "Radio beacons have limits. Their range depends on height, power, and the land and sea between. Signals can bend, reflect and fade, especially at night, so a fix may be less exact than the chart suggests."),
        ("Why the old systems faded",
         "Satellite systems later gave better accuracy over the whole globe, and many older beacons were closed down. The lesson remains: a position from any signal is only as good as the signal and the chart it is read from."),
    ],
    "test": [
        ("How did a Loran receiver get a line of position?",
         [("a", "By reading the colour of the sky"), ("b", "By timing the small difference in arrival between pulses from a pair of stations"), ("c", "By counting the stars"), ("d", "By weighing the cargo")], "b"),
        ("What did a VOR beacon give an aircraft?",
         [("a", "A radial, the bearing from the beacon"), ("b", "The engine temperature"), ("c", "The captain's name"), ("d", "A colour code")], "a"),
        ("What did Decca compare to find a position?",
         [("a", "The weight of the hull"), ("b", "The height of the Sun"), ("c", "The phase of continuous signals from pairs of transmitters"), ("d", "The name of each port")], "c"),
        ("Why might a radio fix be less exact than the chart suggests?",
         [("a", "Radio is always perfectly steady and exact"), ("b", "Charts are made of paper"), ("c", "Beacons never move"), ("d", "Signals can bend, reflect or fade with distance and weather")], "d"),
        ("What is the main lesson of old radio beacons?",
         [("a", "Any signal is good at any distance"), ("b", "A position is only as good as the signal and the chart it is read from"), ("c", "Beacons should never be used"), ("d", "Only the Sun can give a position")], "b"),
    ],
}
