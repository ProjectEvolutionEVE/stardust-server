"""Molniya and Tundra Orbits: long, stretched orbits that let a satellite linger over high latitudes."""
CODE = "flight4_molniya"
BOOK = {
    "title": "Molniya and Tundra Orbits",
    "subtitle": "Stretched orbits for high latitudes",
    "chapters": [
        ("A problem in the north", "A satellite in a normal circular orbit passes quickly over the far north and south. Countries near the poles need coverage for longer. A stretched orbit solves this problem."),
        ("The long loiter", "A Molniya orbit is very stretched. The satellite rushes close to the Earth, then climbs far out and moves slowly near its high point. The slow part is called the loiter, and the satellite spends most of its time over one region."),
        ("The 63-degree tilt", "A Molniya orbit is tilted at about 63.4 degrees. At that tilt the high point stays where it is, so the loiter stays over the same region. It takes about half a day to complete one orbit."),
        ("Russian use history", "The Soviet Union launched the first Molniya satellites in 1965. They gave radio and television links to the far north, where the geostationary belt is low in the sky and hard to reach."),
        ("The eccentricity trade", "The stretch of the orbit is called its eccentricity. A stronger stretch gives a longer loiter, but it also means the satellite is much farther away at its high point, so the signal is weaker there."),
        ("Ground coverage", "A Molniya satellite covers a high-latitude region well for most of its orbit. Several satellites spaced around the orbit can keep a steady link going. Planners choose the number to match the coverage they need."),
    ],
    "test": [
        ("Why does a normal circular orbit serve high latitudes poorly?", [("a", "It never passes over land"), ("b", "It is too cold"), ("c", "It passes quickly over the far north and south"), ("d", "It has no gravity")], "c"),
        ("What is the loiter in a Molniya orbit?", [("a", "The fast dive near Earth"), ("b", "The slow stretch near the high point, over one region"), ("c", "A type of engine"), ("d", "A launch pad")], "b"),
        ("About what tilt does a Molniya orbit use?", [("a", "Zero degrees"), ("b", "About 10 degrees"), ("c", "Ninety degrees exactly"), ("d", "About 63.4 degrees")], "d"),
        ("When did the Soviet Union launch the first Molniya satellites?", [("a", "In 1965"), ("b", "In 1865"), ("c", "In 2065"), ("d", "In 1905")], "a"),
        ("What is the trade with a stronger stretch?", [("a", "A shorter loiter and a stronger signal"), ("b", "No change at all"), ("c", "A longer loiter, but a weaker signal at the far point"), ("d", "The satellite stops")], "c"),
    ],
}
