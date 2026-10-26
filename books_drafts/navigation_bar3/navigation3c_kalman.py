"""The Kalman Filter in Plain Words: how a navigator blends a prediction with a measurement, and why the blend keeps changing."""
CODE = "navigation3c_kalman"
BOOK = {
    "title": "The Kalman Filter in Plain Words",
    "subtitle": "Blending a prediction with a measurement, and why the blend keeps changing",
    "chapters": [
        ("A guess that improves",
         "A Kalman filter keeps a best estimate of something you cannot see directly, such as a craft's position, from readings that are noisy. It works in a loop: predict, measure, correct. Rudolf Kalman described the method in 1960, and navigators have used it ever since."),
        ("Predict",
         "Start with the last best estimate. Use a model of how the craft moves, its speed and the time that has passed, to predict where it is now. The prediction carries an uncertainty too, and that uncertainty grows as time goes by."),
        ("Measure",
         "Take a new reading, such as a star fix or a radio range. Every reading is a little wrong, so the filter treats it as a measurement with its own uncertainty attached."),
        ("Weigh the two",
         "The filter blends the prediction and the measurement. If the prediction is very certain and the reading noisy, it trusts the prediction more. If the prediction is vague and the reading sharp, it trusts the reading more. The weight it gives each one is the Kalman gain."),
        ("Why it is not a plain average",
         "A plain average treats every reading the same. The filter tracks how sure it is about each number, so a sharp reading counts for more. Its answer comes with its own uncertainty, which shrinks after each good measurement."),
        ("A tool, not a magic box",
         "A filter is only as good as its model and its measurement errors. If the model is wrong, or a sensor has a hidden bias, the filter will be confidently wrong. Navigators check its output against independent sources."),
    ],
    "test": [
        ("What are the three steps in the Kalman loop?",
         [("a", "Predict, measure, correct"), ("b", "Launch, land, refuel"), ("c", "Sort, count, store"), ("d", "Sense, fire, rest")], "a"),
        ("What does the blending weight in a Kalman filter depend on?",
         [("a", "The colour of the screen"), ("b", "The number of crew aboard"), ("c", "The uncertainty of the prediction and of the reading"), ("d", "The price of fuel")], "c"),
        ("When should the filter trust a measurement more?",
         [("a", "When the measurement is always noisy"), ("b", "Never, because predictions are always better"), ("c", "When it is night"), ("d", "When the prediction is very vague and the measurement is sharp")], "d"),
        ("What is the problem with a plain average of readings?",
         [("a", "It always gives the wrong answer"), ("b", "It treats every reading the same, however sure each one is"), ("c", "It needs no numbers at all"), ("d", "It cannot be written down")], "b"),
        ("What can make a Kalman filter confidently wrong?",
         [("a", "A model that does not match the craft, or a sensor with a hidden bias"), ("b", "Having too many stars in view"), ("c", "A clean screen"), ("d", "Being checked by a navigator")], "a"),
    ],
}
