"""Robot Calibration and Accuracy: kinematic error models, laser tracker measurements, parameter identification and repeatability."""
CODE = "engineering5_robot_calib"
BOOK = {
    "title": "Robot Calibration and Accuracy",
    "subtitle": "Closing the gap between where the robot thinks it is and where it is",
    "chapters": [
        ("Why calibrate a robot",
         "A robot's controller works from a model of its arm. Real arms differ from the model, because links are slightly longer or shorter and joints sit slightly off. Calibration finds these differences so commanded positions land where intended."),
        ("Kinematic error models",
         "A kinematic error model adds small unknown errors to the nominal link lengths, joint angles and offsets. It describes how these errors shift the tip position. The model gives the calibration a set of unknown numbers to find."),
        ("Laser tracker measurements",
         "A laser tracker measures the 3D position of a target very accurately. The robot moves its tool to many known positions, and the tracker records where the tool really is. These measurements supply the data for calibration."),
        ("Parameter identification",
         "Parameter identification estimates the true values of the model's unknown numbers from the measurements. It is a fitting problem: find the set of values that best explains what was measured. The result is a corrected model."),
        ("Repeatability and accuracy",
         "Repeatability is how close repeated moves land to each other. Accuracy is how close a move lands to the true target. A robot can be very repeatable and still be inaccurate, which is why calibration matters."),
        ("Checking the result",
         "After calibration, the robot is tested at new positions it was not calibrated on. Errors at these fresh points show whether the corrected model is good. Calibration is repeated when the robot is moved, repaired or changed."),
    ],
    "test": [
        ("What does a kinematic error model describe?",
         [("a", "The price of the robot"), ("b", "How errors in link lengths and joint offsets shift the tip position"), ("c", "The paint colour"), ("d", "The lighting")], "b"),
        ("What does a laser tracker measure?",
         [("a", "Colour"), ("b", "Weight"), ("c", "Sound"), ("d", "The 3D position of a target point very accurately")], "d"),
        ("What is parameter identification?",
         [("a", "Labelling cables"), ("b", "Naming parts"), ("c", "Estimating the true model parameters from measurements"), ("d", "Painting numbers")], "c"),
        ("What is the difference between repeatability and accuracy?",
         [("a", "Repeatability is how close repeated moves land to each other; accuracy is how close they land to the true target"), ("b", "They are the same thing"), ("c", "Accuracy is paint"), ("d", "Repeatability is price")], "a"),
        ("Why does calibration improve a robot's accuracy?",
         [("a", "It makes the robot quieter"), ("b", "It corrects the model so commanded positions match real positions"), ("c", "It paints the arm"), ("d", "It cuts the bill")], "b"),
    ],
}
