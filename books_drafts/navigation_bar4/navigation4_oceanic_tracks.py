"""Oceanic tracks: fixed ocean routes, winds, assigned altitudes, reclearance, oceanic separation and position reporting."""
CODE = "navigation4_oceanic_tracks"
BOOK = {
    "title": "Oceanic Tracks and Ocean Routes",
    "subtitle": "Planned lanes across the open sea",
    "chapters": [
        ("Routes across the ocean", "Oceanic tracks are fixed routes across the oceans. They are set out each day to suit the winds and traffic. Aircraft flying them follow a planned path."),
        ("Wind", "Winds aloft can help or slow an aircraft a lot on long oceanic flights. Track systems are often chosen to make the most of favourable winds. Routes in each direction often differ for this reason."),
        ("Altitudes", "Tracks come with altitudes assigned to keep separation between aircraft. Each altitude is a level the pilot must hold. Changing levels needs permission."),
        ("Reclearance", "Reclearance is a new route or altitude given to an aircraft in flight, often because of weather. Pilots must request it. Controllers may offer a better route to save time."),
        ("Oceanic separation", "Without radar cover, oceanic controllers keep aircraft apart by time, distance or altitude. Separation rules must be met at all times. Position reports help controllers do this."),
        ("Position reporting", "Pilots send position reports at set points along the track. The reports tell controllers where each aircraft is. Accurate reports keep the system safe."),
    ],
    "test": [
        ("What are oceanic tracks?", [("a", "Paths for ships on the seabed"), ("b", "Lines drawn on maps for decoration"), ("c", "Tracks for railway trains"), ("d", "Fixed routes across the ocean")], "d"),
        ("Why are tracks chosen with winds in mind?", [("a", "To avoid all clouds"), ("b", "To match the colour of the sea"), ("c", "To make the most of favourable winds"), ("d", "To reduce the number of pilots")], "c"),
        ("What is an assigned altitude used for?", [("a", "Keeping aircraft apart"), ("b", "Showing the price of fuel"), ("c", "Setting the crew's shift"), ("d", "Changing the colour of the lights")], "a"),
        ("What is reclearance?", [("a", "A repaint of the aircraft"), ("b", "A new route or altitude given to an aircraft in flight"), ("c", "A bill for the flight"), ("d", "A new meal service")], "b"),
        ("Why do oceanic controllers need position reports?", [("a", "Without radar, reports show where each aircraft is"), ("b", "Reports are used to sell tickets"), ("c", "Reports change the flight's name"), ("d", "Reports set the menu")], "a"),
    ],
}
