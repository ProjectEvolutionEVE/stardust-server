"""Kriging and Surrogate Models: building a cheap stand-in for a costly simulation, using spatial correlation, prediction variance and careful checks of accuracy."""
CODE = "engineering5_kriging"
BOOK = {
    "title": "Kriging and Surrogate Models",
    "subtitle": "A fast stand-in for a slow simulation, with an honest estimate of its error",
    "chapters": [
        ("Surrogate models", "A surrogate model is a fast approximation of a slow simulation or test. It is fitted to a set of runs and then used in place of the full model. This saves time when many designs must be checked."),
        ("Spatial correlation", "Kriging assumes that nearby points tend to have similar values. The correlation falls off with distance in a set pattern. This pattern is described by a variogram or a correlation function."),
        ("Prediction and variance", "A kriging model predicts a value at any new point and also gives its prediction variance. The variance is small near sampled points and larger far from them. It tells the designer where the model is trusted."),
        ("Designing the experiments", "The sample points should cover the design space well. Space-filling designs, such as Latin hypercubes, spread the points evenly. Extra points are often added where the variance is largest."),
        ("Checking accuracy", "The model should be tested on points it did not see. Cross-validation leaves out some points and predicts them. Engineers look at the errors before trusting the surrogate."),
        ("Honest use", "A surrogate is only a guide. Its best use is to narrow the search, then check the final design with the full model. Stating the uncertainty keeps the decision honest."),
    ],
    "test": [
        ("What is a surrogate model?", [("a", "A fast approximation of a slow simulation or test"), ("b", "A second copy of the machine"), ("c", "A paint sample"), ("d", "A kind of bolt")], "a"),
        ("What does kriging assume about nearby points?", [("a", "They are always different"), ("b", "They are all zero"), ("c", "They are painted red"), ("d", "They tend to have similar values")], "d"),
        ("What does kriging give besides a prediction?", [("a", "A price list"), ("b", "A prediction variance"), ("c", "A weather map"), ("d", "A shopping list")], "b"),
        ("Where is the prediction variance usually largest?", [("a", "Right on the sampled points"), ("b", "At the sensor cable"), ("c", "In the paint shop"), ("d", "Far from the sampled points")], "d"),
        ("How can surrogate accuracy be checked?", [("a", "By trusting it with no test"), ("b", "By counting the bolts"), ("c", "By testing on points it did not see, such as cross-validation"), ("d", "By asking the weather")], "c"),
    ],
}
