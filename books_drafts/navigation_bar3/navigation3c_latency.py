"""Old Readings: Latency in Measurements. A reading is always a little old by the time it is used, and a navigator must allow for it."""
CODE = "navigation3c_latency"
BOOK = {
    "title": "Old Readings: Latency in Measurements",
    "subtitle": "A reading is always a little old by the time it is used, and a navigator must allow for it",
    "chapters": [
        ("Readings take time",
         "A sensor reading does not arrive the moment it is taken. It must be sampled, processed, sent along a cable or a data bus, and read by the computer. Each step adds delay, and the total delay is called latency."),
        ("The age of a reading",
         "A position fix that arrives half a second late describes where the craft was half a second ago. At speed that gap matters, because a fast craft covers real distance in that time."),
        ("Time-stamp every reading",
         "The safest approach is to record the time at which each reading was taken, not the time it arrived. The navigation filter can then place each reading at the right moment in its history."),
        ("Waiting does not fix it",
         "A navigator could wait for each reading before acting, but then the craft would respond too slowly. Instead the filter predicts forward through the delay, and corrects with a measurement that is already old."),
        ("Different sensors, different delays",
         "Each sensor has its own delay. A star view may take longer to process than a gyro reading. If those delays are not allowed for, one sensor will pull the estimate out of step with the others."),
        ("Measure the delay",
         "Navigators measure each sensor's delay and check it, rather than assuming it. A small, known delay can be corrected. An unknown one is a hidden error, and hidden errors are the hardest to find."),
    ],
    "test": [
        ("What is latency?",
         [("a", "The delay between a reading being taken and being used"), ("b", "The colour of a sensor"), ("c", "The mass of the craft"), ("d", "The speed of light")], "a"),
        ("Why does a late position fix matter when the craft is moving fast?",
         [("a", "The fix is always louder"), ("b", "It describes where the craft was, which is no longer where it is"), ("c", "Speed makes fixes disappear"), ("d", "Late fixes cost more fuel")], "b"),
        ("What is the safest thing to record with each reading?",
         [("a", "The colour of the room"), ("b", "The name of the crew"), ("c", "The time at which it was taken"), ("d", "The weight of the sensor")], "c"),
        ("Why not simply wait for each reading before acting?",
         [("a", "Readings never arrive"), ("b", "Waiting makes the sensors hotter"), ("c", "Waiting is required by law"), ("d", "Waiting makes the craft respond too slowly")], "d"),
        ("Why is an unknown delay dangerous?",
         [("a", "It is a hidden error that is hard to find"), ("b", "It makes the paint fade"), ("c", "It turns off the hull lights"), ("d", "It has no effect at all")], "a"),
    ],
}
