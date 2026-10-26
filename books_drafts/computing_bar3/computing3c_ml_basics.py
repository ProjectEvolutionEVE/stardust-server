"""Machine Learning Basics: how a program learns from examples, and why it must be tested on new ones."""
CODE = "computing3c_ml_basics"
BOOK = {
    "title": "Machine Learning Basics",
    "subtitle": "How a program learns from examples, and why it must be tested on new ones",
    "chapters": [
        ("Learning from examples",
         "Machine learning is a way of writing programs that learn a pattern from examples, instead of following a fixed list of rules. You show the program many examples with the right answers. It adjusts itself until its guesses match those answers well."),
        ("Training data",
         "The examples used to teach the program are the training data. The pattern the program ends up with is called a model. A model is only as good as the quality and variety of its training data."),
        ("Test data",
         "Keep some examples aside, and never show them during training. These are the test data. Scoring the model on them shows how it will do on new cases, which is what really matters."),
        ("Overfitting",
         "A model that memorises its training examples, but fails on new ones, is overfitting. It has learned the quirks of its examples rather than the real pattern. A fair test on fresh data catches overfitting early."),
        ("Bias in the data",
         "A model learns whatever is in its examples, including any unfair gaps. If some kinds of case are rare in the training data, the model may do poorly on them. Check the results for each group of cases, not just the average."),
        ("The cost of learning",
         "Training a large model takes a lot of computer time, which costs money and power. A small, simple model often does the job well for far less. Start simple, and grow only when the test scores show you need to."),
    ],
    "test": [
        ("What is training data?",
         [("a", "A sports schedule"), ("b", "A list of prices"), ("c", "A printed book"), ("d", "Examples with the right answers, used to teach a model")], "d"),
        ("Why keep some examples aside as test data?",
         [("a", "To check how the model does on cases it has never seen"), ("b", "To make the model bigger"), ("c", "To use them as training again"), ("d", "To hide them from the computer forever")], "a"),
        ("What is overfitting?",
         [("a", "Having too little memory"), ("b", "Using too much paper"), ("c", "Learning the examples so closely that it fails on new ones"), ("d", "A computer that runs too cold")], "c"),
        ("Why check results for each group of cases, not just the average?",
         [("a", "Because averages are always wrong"), ("b", "Because a good average can hide poor results for rare kinds of case"), ("c", "Because groups are never in the data"), ("d", "Because the average is always the best")], "b"),
        ("Why start with a simple model?",
         [("a", "Because a large model always costs less"), ("b", "Because simple models cannot learn at all"), ("c", "Because training a large model costs more computer time and money, and a simple one may do the job"), ("d", "Because big models are banned")], "c"),
    ],
}
