"""Groundwater Flow Modelling: building a computer model of how water moves underground, calibrating it to measurements and testing predictions."""
CODE = "mining5_gw_model"
BOOK = {
    "title": "Groundwater Flow Modelling",
    "subtitle": "Conceptual models, calibration, predictive runs and uncertainty",
    "chapters": [
        ("Models of hidden water",
         "Groundwater cannot be seen, so models help us reason about it. A groundwater flow model is a computer model of how water moves through rock and soil. It is used to plan pits, drains and water supplies."),
        ("Conceptual model",
         "Before any computer work, the team writes a conceptual model. It describes the layers, faults, recharge and boundaries as they are understood. A wrong conceptual model will give wrong numbers, however well the computer runs."),
        ("Calibration",
         "Calibration adjusts the model's inputs until its results match measured water levels and flows. A model that matches the past is more trusted for the future. Calibration must be checked against data the model was not tuned on."),
        ("Predictive runs",
         "Once calibrated, the model is run forward in time for future mining. Predictive runs show how the water table and inflows may change. Each run answers a specific question about the plan."),
        ("Uncertainty",
         "Many sets of inputs can match the same past data. Teams test a range of plausible models and report the spread of results. Decisions are based on the range, not on one model alone."),
        ("Model codes and review",
         "Well-known model codes are used widely and have been tested over many years. An independent review checks the model's setup, data and results. A review finds errors before they reach the design."),
    ],
    "test": [
        ("What is a groundwater flow model?",
         [("a", "A computer model of how water moves through rock and soil"), ("b", "A model aeroplane"), ("c", "A fashion model"), ("d", "A map of the stars")], "a"),
        ("Why is the conceptual model written first?",
         [("a", "It is only a title page"), ("b", "It replaces the computer"), ("c", "It describes the layers, faults and boundaries the model is built on"), ("d", "It is written after all the results")], "c"),
        ("What does calibration do?",
         [("a", "Paints the model blue"), ("b", "Removes the measured data"), ("c", "Makes the model run backwards"), ("d", "Adjusts inputs until results match measured water levels")], "d"),
        ("Why should the range of plausible models be tested?",
         [("a", "Because one model is always perfect"), ("b", "Because many inputs can match the same past data"), ("c", "Because the range is never needed"), ("d", "Because the computer needs a rest")], "b"),
        ("What does an independent review check?",
         [("a", "The model's setup, data and results"), ("b", "The colour of the office walls"), ("c", "The price of the coffee"), ("d", "The name of the reviewer's dog")], "a"),
    ],
}
