"""Doppler-Aided Inertial Navigation: using radar velocity to correct inertial drift, with failure modes to watch for."""
CODE = "navigation5_sins_doppler"
BOOK = {
    "title": "Doppler-Aided Inertial Navigation",
    "subtitle": "Using radar velocity to keep inertial drift in check",
    "chapters": [
        ("Inertial drift", "An inertial system drifts over time, so its position error grows. Adding an outside aid keeps those errors small."),
        ("Radar velocity", "A Doppler radar measures the velocity of a vehicle relative to the ground. That velocity can be used to correct an inertial system."),
        ("Aircraft use", "Aircraft often combine Doppler radar with inertial navigation on long flights over land and sea. The pairing limits drift."),
        ("Combining the systems", "The two systems are combined in a filter that estimates the errors in the inertial solution. The filter uses the radar velocity as a measurement."),
        ("Failure modes", "Radar can lose lock over calm water or certain kinds of terrain, and the filter must notice when this happens. A good system detects a radar fault and reduces its trust in the radar."),
        ("Use today", "Doppler-aided inertial navigation remains a useful backup in many designs. Its use depends on the vehicle and the mission."),
    ],
    "test": [
        ("What does an inertial system do over time?",
         [("a", "Drifts"), ("b", "Paints"), ("c", "Dances"), ("d", "Cooks")], "a"),
        ("What does Doppler radar measure in this use?",
         [("a", "Colour"), ("b", "Velocity relative to the ground"), ("c", "Weight"), ("d", "Time")], "b"),
        ("Which kind of vehicle commonly uses this combination?",
         [("a", "Kitchens"), ("b", "Gardens"), ("c", "Aircraft"), ("d", "Desks")], "c"),
        ("How is the radar velocity used in the filter?",
         [("a", "As a colour"), ("b", "As a title"), ("c", "As a price"), ("d", "As a measurement")], "d"),
        ("What should a good system do when the radar fails?",
         [("a", "Ignore it entirely"), ("b", "Turn off the screen"), ("c", "Detect the fault and reduce its trust in the radar"), ("d", "Print a map")], "c"),
    ],
}
