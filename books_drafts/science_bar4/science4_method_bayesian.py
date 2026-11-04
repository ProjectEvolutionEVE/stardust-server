"""Bayesian Reasoning in Experiments: priors, likelihoods, posterior beliefs and credible intervals."""
CODE = "science4_method_bayesian"
BOOK = {
    "title": "Bayesian Reasoning in Experiments",
    "subtitle": "Updating what we believe as evidence arrives",
    "chapters": [
        ("What Bayesian means", "Bayesian reasoning combines what we already believe with new evidence. It gives a clear way to update beliefs as data arrive. The result is a new belief, called the posterior."),
        ("Priors", "A prior is the belief held before the new data. It can come from earlier studies, expert knowledge or a cautious guess. Stating the prior openly lets others check and challenge it."),
        ("Likelihoods", "The likelihood asks how probable the observed data are under each possible explanation. A strong likelihood moves the belief a long way, and a weak one moves it only a little. Likelihoods link the model to the data."),
        ("Updating beliefs", "Bayes' rule multiplies the prior by the likelihood, then rescales so the total is one. This gives the posterior belief. Repeating the process as new data arrive keeps the reasoning up to date."),
        ("Credible intervals", "A credible interval gives a range that contains the parameter with a stated probability, given the data and the prior. It is read directly as a probability statement about the parameter. This differs from the meaning of a confidence interval."),
        ("Choosing priors", "The choice of prior matters most when data are scarce. Weakly informative priors can prevent wild answers without forcing a result. Comparing Bayesian and frequentist answers helps show how much the choice of method matters."),
    ],
    "test": [
        ("What does Bayesian reasoning combine?",
         [("a", "Prior belief with new evidence"), ("b", "Two colours of paint"), ("c", "Lab staff and lunch menus"), ("d", "Sample weight and room temperature only")], "a"),
        ("What is a prior?",
         [("a", "A form signed after the study"), ("b", "The belief held before the new data are considered"), ("c", "A type of microscope"), ("d", "The final report")], "b"),
        ("What does a likelihood measure?",
         [("a", "The cost of the data"), ("b", "The number of pages"), ("c", "The speed of the computer"), ("d", "How probable the observed data are under each explanation")], "d"),
        ("What is a posterior?",
         [("a", "The last page of a book"), ("b", "The first guess only"), ("c", "The updated belief after the data are considered"), ("d", "A lab coat")], "c"),
        ("What does a credible interval state?",
         [("a", "The price of a study"), ("b", "A range that contains the parameter with a stated probability, given the data and prior"), ("c", "The number of staff"), ("d", "The room size")], "b"),
    ],
}
