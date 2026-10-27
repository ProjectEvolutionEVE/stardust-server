"""System Identification from Test Data: building a model of a machine from its inputs and outputs, with careful excitation, least squares and validation."""
CODE = "engineering5_sysid"
BOOK = {
    "title": "System Identification from Test Data",
    "subtitle": "Building a model of a machine from what goes in and what comes out",
    "chapters": [
        ("Why identify a system", "Engineers often have no good model of a machine. System identification builds one from measured inputs and outputs. The model is then used for control, simulation or diagnosis."),
        ("Input signals", "The input must excite the machine over the frequencies that matter. A random or swept input often works well. A constant input tells you very little about how the machine moves."),
        ("Parametric models", "A parametric model has a fixed form, with a few unknown numbers. Its structure, such as the order of the equations, is chosen first. The data then give the best values for those numbers."),
        ("Least squares fitting", "Least squares finds the parameter values that make the predicted output closest to the measured output. It minimises the sum of squared errors. It is fast and widely used for linear models."),
        ("Model validation", "A model must be checked on data it was not fitted to. A good model predicts new data well, and its errors look like noise. Engineers compare residuals and plot predictions against measurements."),
        ("Experiment design", "The test should be planned before it is run. The input, the length and the sampling rate all matter. A poor experiment can make even a clever method give a poor model."),
    ],
    "test": [
        ("Why is system identification used?", [("a", "To build a model from measured inputs and outputs"), ("b", "To paint the machine"), ("c", "To count the workers"), ("d", "To cut the cables")], "a"),
        ("What makes a good input signal?", [("a", "A constant input"), ("b", "No input at all"), ("c", "A signal chosen by colour"), ("d", "One that excites the frequencies that matter")], "d"),
        ("What does least squares minimise?", [("a", "The price of the test"), ("b", "The sum of squared errors between predicted and measured outputs"), ("c", "The number of tests"), ("d", "The length of the cable")], "b"),
        ("Where should a model be checked?", [("a", "Only on the data it was fitted to"), ("b", "Nowhere at all"), ("c", "On a picture of the machine"), ("d", "On data it was not fitted to")], "d"),
        ("What does a good model's residual error look like?", [("a", "Like a steady climb"), ("b", "Like a perfect copy of the input"), ("c", "Like noise"), ("d", "Like a square wave of colour")], "c"),
    ],
}
