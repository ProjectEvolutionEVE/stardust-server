"""Kalman Filter Theory for Engineers: state estimation, prediction and update, covariance, noise models and tuning."""
CODE = "engineering5_kalman"
BOOK = {
    "title": "Kalman Filter Theory for Engineers",
    "subtitle": "Predicting, measuring and blending the two in the right proportion",
    "chapters": [
        ("Estimating a state",
         "A state is the set of numbers that describe a system, such as position and speed. Sensors give noisy readings of the state, never the exact value. A Kalman filter combines a model with the readings to find the best estimate."),
        ("Prediction",
         "The filter first predicts where the state will be next, using a model of how the system moves. The prediction also grows less certain with time, because the model is not perfect. This uncertainty is tracked as a covariance."),
        ("Update",
         "When a new reading arrives, the filter compares it with the prediction. It then moves the estimate toward the reading, by an amount set by the Kalman gain. The gain is large when the reading is trusted more, and small when the prediction is trusted more."),
        ("Covariance",
         "The covariance measures how uncertain the estimate is, and how the uncertainties of different values relate. A small covariance means a confident estimate. Tracking it lets the filter know when its answer can be trusted."),
        ("Noise models",
         "The filter needs a model of the process noise, which is the uncertainty in the system's motion, and of the measurement noise, which is the error in the sensor. These models are usually set from data or from the sensor's specification."),
        ("Tuning",
         "Tuning means choosing the noise values so the filter behaves well. Too much trust in the model makes the estimate slow to follow real changes. Too much trust in the sensor makes it jumpy. Engineers test the filter on recorded data to find a good balance."),
    ],
    "test": [
        ("What does a Kalman filter estimate?",
         [("a", "The colour of the sky"), ("b", "The state of a system, such as its position and speed"), ("c", "The price of steel"), ("d", "The number of crew")], "b"),
        ("What happens to the uncertainty during prediction?",
         [("a", "It disappears at once"), ("b", "It turns into a colour"), ("c", "It stays exactly the same forever"), ("d", "It grows, because the model is not perfect")], "d"),
        ("What does the Kalman gain decide?",
         [("a", "The size of the screen"), ("b", "The name of the sensor"), ("c", "How much to trust the reading compared with the prediction"), ("d", "The date of the next test")], "c"),
        ("What does the covariance tell the engineer?",
         [("a", "How uncertain the estimate is"), ("b", "How heavy the sensor is"), ("c", "How many bolts are used"), ("d", "How loud the filter runs")], "a"),
        ("What happens if the filter trusts the sensor too much?",
         [("a", "The estimate becomes perfect"), ("b", "The estimate becomes jumpy"), ("c", "The sensor stops working"), ("d", "The prediction is removed")], "b"),
    ],
}
