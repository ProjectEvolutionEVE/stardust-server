"""IMU Drift and Inertial Navigation Errors: gyro and accelerometer bias, integration error, calibration and external aiding."""
CODE = "engineering5_imu_drift"
BOOK = {
    "title": "IMU Drift and Inertial Navigation Errors",
    "subtitle": "Why inertial sensors wander, and how to keep them honest",
    "chapters": [
        ("What an IMU measures",
         "An inertial measurement unit, or IMU, holds gyroscopes that measure turning and accelerometers that measure acceleration. From these, a system can track how a vehicle is turning and moving. No outside signal is needed, which makes IMUs useful when GPS is lost."),
        ("Bias",
         "Every gyro and accelerometer has a small steady offset called bias. Even a tiny bias is a fixed error in every reading. The bias can also change slowly with temperature and time."),
        ("Integration error",
         "To find position, the system adds up readings over time, which is called integration. Any error in the readings is added up too, so it grows steadily. Position from an accelerometer gets worse very fast, because it is integrated twice."),
        ("Calibration",
         "Calibration measures the bias and scale errors and corrects them. Engineers test the sensor at known rests and rotations. A well-calibrated IMU drifts much more slowly than an uncalibrated one."),
        ("Aiding from external references",
         "To stop drift from growing without limit, an IMU is often aided by GPS, cameras or a known landmark. Each external fix pulls the estimate back to the truth. The fusion algorithm weighs how much to trust each source."),
        ("Designing for drift",
         "Engineers decide how long the IMU must work alone and how accurate it must be at the end. Cheap sensors suit short trips with frequent fixes, while long trips need better sensors. The right choice is set by the mission."),
    ],
    "test": [
        ("What does an IMU measure?",
         [("a", "Turning and acceleration"), ("b", "Sound and light"), ("c", "Water depth"), ("d", "Air quality")], "a"),
        ("What is bias in a gyro or accelerometer?",
         [("a", "A small steady offset in every reading"), ("b", "A type of battery"), ("c", "A colour code"), ("d", "A mounting bracket")], "a"),
        ("Why does position from an accelerometer get worse so fast?",
         [("a", "Because the sensor is painted"), ("b", "Because the sensor only works in daylight"), ("c", "Because the reading is integrated twice, so errors add up quickly"), ("d", "Because it weighs too much")], "c"),
        ("What does calibration do for an IMU?",
         [("a", "It makes the sensor louder"), ("b", "It measures the bias and scale errors and corrects them"), ("c", "It paints the case"), ("d", "It changes the colour of the readings")], "b"),
        ("What helps stop IMU drift from growing without limit?",
         [("a", "Aiding from GPS, cameras or a known landmark"), ("b", "Turning the sensor off"), ("c", "Heating the case"), ("d", "Adding more paint")], "a"),
    ],
}
