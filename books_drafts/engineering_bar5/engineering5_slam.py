"""Mapping and Localisation (SLAM): map representation, pose estimation, loop closure, drift and data association."""
CODE = "engineering5_slam"
BOOK = {
    "title": "Mapping and Localisation (SLAM)",
    "subtitle": "Building a map while finding your place in it",
    "chapters": [
        ("The chicken-and-egg problem",
         "To build a map, a robot needs to know where it is. To know where it is, it needs a map. SLAM, short for simultaneous localisation and mapping, solves both at once from the same sensor data."),
        ("Map representation",
         "A map can be stored as an occupancy grid, where each cell says whether it is free or blocked. It can also be stored as a set of landmarks or as a graph of places. The choice depends on the sensors and the task."),
        ("Pose estimation",
         "The robot's pose is its position and heading. Each movement adds a little uncertainty, so the estimate slowly wanders. Each new observation of the surroundings helps pull the estimate back into line."),
        ("Loop closure",
         "When the robot recognises a place it has been before, it can correct the error that built up since then. This is called loop closure. It pulls the whole map back into shape, and it is one of the most powerful tools in SLAM."),
        ("Drift",
         "Drift is the slow growth of error in the pose estimate over time. It comes from small errors in every move and every reading. Loop closure and fixed landmarks are the main ways to keep drift in check."),
        ("Data association",
         "Data association is the task of deciding which feature in one sensor reading matches which feature on the map. Wrong matches can bend the map badly. Good systems test each match and reject the doubtful ones."),
    ],
    "test": [
        ("What does SLAM do?",
         [("a", "Builds a map while locating the robot in it"), ("b", "Paints walls"), ("c", "Counts products"), ("d", "Measures water")], "a"),
        ("What is loop closure?",
         [("a", "A type of lock"), ("b", "A paint finish"), ("c", "Recognising a place already visited, to correct accumulated drift"), ("d", "A tool for cables")], "c"),
        ("What is drift in a pose estimate?",
         [("a", "Floating in water"), ("b", "A slow growth of error over time"), ("c", "A fast moving robot"), ("d", "Light from a window")], "b"),
        ("What is data association?",
         [("a", "Choosing a paint colour"), ("b", "Booking a meeting"), ("c", "Joining two pipes"), ("d", "Matching the same map feature seen in different sensor readings")], "d"),
        ("What is one common way to represent a map?",
         [("a", "An occupancy grid"), ("b", "A recipe"), ("c", "A song"), ("d", "A timetable")], "a"),
    ],
}
