"""Scientific Models and Their Limits: simplified pictures, assumptions, calibration, validation and uncertainty."""
CODE = "science4_method_models"
BOOK = {
    "title": "Scientific Models and Their Limits",
    "subtitle": "Useful simplifications, and where they break down",
    "chapters": [
        ("What a model is for", "A model is a simplified picture of a system, used to explain it or predict it. Every model leaves things out on purpose. The question is whether the parts left out matter for the job."),
        ("Simplifying assumptions", "Assumptions are the choices that keep a model manageable. Some assumptions are harmless, and others change the answer a lot. A good modeller states each assumption and tests its effect."),
        ("Calibration versus validation", "Calibration adjusts a model's settings so it matches a set of data. Validation checks the model against new data it was not tuned to. A model that fits its calibration data is not proven to work elsewhere."),
        ("Model uncertainty", "Uncertainty comes from the data, the parameters and the structure of the model itself. Reporting a range of likely results is more honest than one number. Several models can be compared to show the spread."),
        ("Predictive failure", "A model can fail when conditions move beyond the ones it was built for. Predictions far from the data are the least reliable. Honest models say where they should not be trusted."),
        ("Communicating models", "A clear explanation of a model says what it is for, what it assumes and what it cannot do. Listeners should be able to ask what happens if an assumption is wrong. Good communication helps decision makers use models wisely."),
    ],
    "test": [
        ("What is a scientific model?",
         [("a", "A simplified picture of a system, used to explain or predict it"), ("b", "A fashion item"), ("c", "A type of lab coat"), ("d", "A spreadsheet of salaries")], "a"),
        ("What is a simplifying assumption?",
         [("a", "A promise to finish early"), ("b", "A rule about lab doors"), ("c", "A choice that keeps a model manageable"), ("d", "A way of hiding errors")], "c"),
        ("What is calibration?",
         [("a", "Painting the model"), ("b", "Printing the results"), ("c", "Ordering new equipment"), ("d", "Adjusting a model's settings so it matches a set of data")], "d"),
        ("Why is validation needed?",
         [("a", "To check the model against new data it was not tuned to"), ("b", "To choose a font"), ("c", "To set the room temperature"), ("d", "To cancel the study")], "a"),
        ("Where are model predictions least reliable?",
         [("a", "Close to the data"), ("b", "Far beyond the conditions the model was built for"), ("c", "In every lab"), ("d", "When the model is printed in colour")], "b"),
    ],
}
