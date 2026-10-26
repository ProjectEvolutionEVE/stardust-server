"""The Kalman Filter in Plain Words: blending noisy measurements with a prediction to get a better estimate of where you are."""
CODE = "flight4_kalman"
BOOK = {
    "title": "The Kalman Filter in Plain Words",
    "subtitle": "Blending noisy measurements into a better estimate",
    "chapters": [
        ("Noisy measurements", "Every sensor is a little wrong. A reading may jump, lag or drift. The question is how to get the best guess of the true value from many imperfect readings."),
        ("Predict and update", "The Kalman filter works in two steps. First it predicts where the craft should now be, using its last estimate and its known motion. Then it updates that prediction with the new measurement."),
        ("Weighting trust", "The filter weighs how much to trust the prediction and how much to trust the measurement. If the sensor is more reliable, it gets more weight. If the prediction is more reliable, it gets more weight. The blend changes each time."),
        ("Apollo's use", "Filters of this kind were used in the Apollo navigation system, so that the computer could combine radar and star sightings into one better position. Rudolf Kalman described the method in 1960."),
        ("GPS use", "Many satellite navigation systems, including GPS receivers, use a filter of this kind. It blends the signals from several satellites with motion data to give a smooth position."),
        ("Limits", "The filter works best when its model of the craft is good and its noise figures are right. If the model is wrong, the estimate can drift, so engineers test the filter against real data before flight."),
    ],
    "test": [
        ("What does the Kalman filter do with noisy measurements?", [("a", "Throws all of them away"), ("b", "Blends them with a prediction to get a better estimate"), ("c", "Paints them"), ("d", "Sends them to the Moon")], "b"),
        ("What are the two steps of the filter?", [("a", "Paint, then dry"), ("b", "Launch, then land"), ("c", "Eat, then sleep"), ("d", "Predict, then update")], "d"),
        ("Who described the method in 1960?", [("a", "Rudolf Kalman"), ("b", "Isaac Newton"), ("c", "Johannes Kepler"), ("d", "Nikola Tesla")], "a"),
        ("What does a more reliable sensor get in the blend?", [("a", "Less weight always"), ("b", "No weight at all"), ("c", "More weight"), ("d", "A different colour")], "c"),
        ("Where is a filter of this kind used today?", [("a", "Only in toy cars"), ("b", "In satellite navigation receivers"), ("c", "Only in kitchens"), ("d", "Nowhere")], "b"),
    ],
}
