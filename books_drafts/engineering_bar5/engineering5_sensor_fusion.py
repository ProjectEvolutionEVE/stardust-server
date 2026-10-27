"""Multi-Sensor Fusion Architectures: centralised and distributed fusion, time alignment, sensor failures and integrity monitoring."""
CODE = "engineering5_sensor_fusion"
BOOK = {
    "title": "Multi-Sensor Fusion Architectures",
    "subtitle": "Combining many sensors into one trusted picture",
    "chapters": [
        ("Why fuse sensors",
         "No single sensor is perfect. A camera fails in darkness, a radar misses fine detail, and an IMU drifts. Sensor fusion combines readings from several sensors so the result is more accurate and more reliable than any one alone."),
        ("Centralised fusion",
         "In a centralised design, all raw or lightly processed data flows to one central processor, which combines it into a single estimate. This can give the best accuracy. It needs a lot of bandwidth, and the central unit becomes a single point of failure."),
        ("Distributed fusion",
         "In a distributed design, each sensor or node forms its own estimate, and the estimates are then shared and combined. This needs less data to move around, and it keeps working if one node fails. The combined result may be a little less precise."),
        ("Time alignment",
         "Readings from different sensors often arrive at different times and rates. Time alignment makes sure that readings are matched to the same moment before they are combined. Badly aligned data can make a sound system look wrong."),
        ("Sensor failures",
         "Sensors can fail by going silent, sticking at one value or giving wild readings. The fusion system must spot these faults and reduce the weight given to a failing sensor. Good designs can keep working on the remaining sensors."),
        ("Integrity monitoring",
         "Integrity monitoring checks whether the fused answer can be trusted at all. It raises a warning when the sensors disagree too much or the estimate is out of bounds. Safety-critical systems use it to decide when to hand control back or stop."),
    ],
    "test": [
        ("What does sensor fusion combine?",
         [("a", "Paint colours"), ("b", "Recipes"), ("c", "Timetables"), ("d", "Readings from several sensors to give one better estimate")], "d"),
        ("What is time alignment?",
         [("a", "Setting wall clocks"), ("b", "Making sure readings from different sensors refer to the same moment"), ("c", "Painting sensors"), ("d", "Choosing a colour")], "b"),
        ("In centralised fusion, where is the data combined?",
         [("a", "In one central processor"), ("b", "In each sensor separately, never combined"), ("c", "In the paint shop"), ("d", "In the fuel tank")], "a"),
        ("What is integrity monitoring?",
         [("a", "Checking the price"), ("b", "Painting the sensors"), ("c", "Checking that the sensor output is trustworthy and flagging failures"), ("d", "Counting the crew")], "c"),
        ("What is a benefit of distributed fusion?",
         [("a", "It needs no computers"), ("b", "It is always cheaper in paint"), ("c", "It removes the need for sensors"), ("d", "It can keep working if one node fails")], "d"),
    ],
}
