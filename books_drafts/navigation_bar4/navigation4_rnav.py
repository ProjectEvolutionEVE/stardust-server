"""Area navigation (RNAV): routes not tied to ground beacons, waypoints, RNAV routes, fly-by turns, defined areas and accuracy."""
CODE = "navigation4_rnav"
BOOK = {
    "title": "Area Navigation",
    "subtitle": "Flying routes between points you choose",
    "chapters": [
        ("Flying your own route", "Area navigation, or RNAV, lets an aircraft fly routes that are not tied to ground beacons. It uses satellite and inertial data to find its position. Routes can be placed almost anywhere."),
        ("Waypoints", "Waypoints are fixed points defined by coordinates. The aircraft flies from one to the next along a planned path. Waypoints can be named and stored in the navigation system."),
        ("RNAV routes", "RNAV routes join waypoints into airways. These routes can be shorter than the older routes between ground beacons. Shorter routes save fuel and time."),
        ("Fly-by turns", "A fly-by turn starts the turn before the waypoint, so the aircraft rejoins the next leg smoothly. It is common in modern navigation. A fly-over turn instead passes over the point first."),
        ("The defined area", "RNAV needs a performance standard that shows the aircraft stays within a set area around the route. The standard sets how accurate the navigation must be. Operators must meet it."),
        ("Accuracy", "The accuracy requirement depends on the type of route and airspace. Systems check their own accuracy and warn if it drops. Good navigation keeps the aircraft within its required area."),
    ],
    "test": [
        ("What does RNAV allow an aircraft to do?", [("a", "Fly only in circles over a city"), ("b", "Land without a runway"), ("c", "Carry no passengers"), ("d", "Fly routes not tied to ground beacons")], "d"),
        ("What is a waypoint?", [("a", "A fixed point defined by coordinates"), ("b", "A bag for luggage"), ("c", "A small bird that lands on wings"), ("d", "A kind of cloud")], "a"),
        ("What is a benefit of RNAV routes?", [("a", "They need more ground beacons"), ("b", "They are always slower"), ("c", "They can be shorter, saving fuel and time"), ("d", "They make the aircraft heavier")], "c"),
        ("What is a fly-by turn?", [("a", "A turn made on the ground only"), ("b", "A turn that starts early so the aircraft rejoins the next leg smoothly"), ("c", "A turn that is never allowed"), ("d", "A turn that stops the engines")], "b"),
        ("What does a performance standard for RNAV show?", [("a", "The speed of the wind at the top"), ("b", "The number of seats"), ("c", "The colour of the airline's logo"), ("d", "The aircraft stays within a set area around the route")], "d"),
    ],
}
