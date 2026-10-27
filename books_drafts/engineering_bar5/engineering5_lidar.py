"""LiDAR Principles and Point Cloud Accuracy: time-of-flight, scanning patterns, range error, reflectance and calibration."""
CODE = "engineering5_lidar"
BOOK = {
    "title": "LiDAR Principles and Point Cloud Accuracy",
    "subtitle": "Timing light pulses to measure distance, and how accurate the cloud is",
    "chapters": [
        ("How LiDAR works",
         "LiDAR sends out short pulses of laser light and times how long each takes to return. Light travels at a known speed, so the time gives the distance. Repeating this millions of times builds a cloud of points that shows the shape of the scene."),
        ("Time of flight",
         "The distance is the speed of light times the travel time, divided by two, because the light goes out and comes back. Very small timing differences matter, since light covers about 30 centimetres in a billionth of a second. Electronics must measure time very precisely."),
        ("Scanning patterns",
         "A LiDAR sweeps its beam in lines, spirals or other patterns to cover the scene. The pattern sets how dense the cloud is and how fast the scan finishes. Designers choose a pattern that suits the task and the speed of the vehicle or machine."),
        ("Range error",
         "No measurement is perfect, so each distance has a small error. The error can grow with range and depends on the sensor's design and the timing electronics. Engineers quote the error and test it against known distances."),
        ("Reflectance",
         "Dark, shiny or wet surfaces reflect the laser differently. Weak returns can make distances less certain, and some surfaces barely return a signal at all. Reflectance is recorded with each point so that users can judge its quality."),
        ("Calibration",
         "The sensor and its mounting must be calibrated, so that each point is placed correctly in space. Small errors in angle or position shift the whole cloud. Regular checks keep the cloud accurate over the sensor's life."),
    ],
    "test": [
        ("How does a LiDAR find the distance to a point?",
         [("a", "By weighing the object"), ("b", "By counting the seconds on a clock"), ("c", "By reading the colour of the surface"), ("d", "By timing how long a laser pulse takes to return")], "d"),
        ("Why must a LiDAR time light very precisely?",
         [("a", "Because light is too heavy to measure"), ("b", "Because light covers about 30 centimetres in a billionth of a second"), ("c", "Because the laser is hot"), ("d", "Because the cloud must be painted")], "b"),
        ("What does a scanning pattern set?",
         [("a", "The density of the cloud and how fast the scan finishes"), ("b", "The colour of the sensor"), ("c", "The name of the operator"), ("d", "The price of the sensor")], "a"),
        ("What is reflectance?",
         [("a", "A type of mirror on the wall"), ("b", "The cost of a laser"), ("c", "How the surface reflects the laser, which affects return strength"), ("d", "The speed of a truck")], "c"),
        ("Why must a LiDAR be calibrated?",
         [("a", "So each point is placed correctly in space"), ("b", "So the sensor is heavier"), ("c", "So the laser is brighter"), ("d", "So the cloud is painted")], "a"),
    ],
}
