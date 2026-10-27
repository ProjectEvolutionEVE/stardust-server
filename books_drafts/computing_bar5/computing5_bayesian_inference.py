"""Bayesian inference and priors: priors and posteriors, Bayes' theorem, conjugate models, credible intervals and model comparison."""
CODE = 'computing5_bayesian_inference'
BOOK = {
    "title": 'Bayesian Inference and Priors',
    "subtitle": 'Updating what you believe as new evidence arrives',
    "chapters": [
        ('Beliefs that change',
         'Bayesian inference starts with a belief, called the prior, and updates it using the evidence. The result is the posterior, the updated belief.'),
        ("Bayes' theorem",
         "Bayes' theorem combines the prior with the likelihood, which says how likely the evidence is under each possibility. Together they give the posterior."),
        ('Priors matter',
         'A prior can be a strong starting point or a weak one. With lots of evidence the prior matters less, but with little evidence it can shape the answer a lot.'),
        ('Conjugate models',
         'Some pairs of prior and likelihood have a neat form, so the update is a simple formula. A beta prior with binomial data is a classic example.'),
        ('Credible intervals',
         'A credible interval gives a range that contains the unknown value with a stated probability, given the model. It is not the same as a frequentist confidence interval, though the two can look alike.'),
        ('Comparing models',
         'Bayesian methods compare models by how well they explain the evidence, often with Bayes factors or leave-one-out checks. Sensitivity to the prior should always be checked.'),
    ],
    "test": [
        ('What is a prior?',
         [('a', 'The belief held before seeing the evidence'), ('b', 'A kind of printer'), ('c', 'A final answer'), ('d', 'A chart colour')], 'a'),
        ('What is the posterior?',
         [('a', 'A type of server'), ('b', 'A bad guess'), ('c', 'The updated belief after the evidence'), ('d', 'The first draft')], 'c'),
        ('When does a prior matter least?',
         [('a', 'When there is no evidence'), ('b', 'When the prior is printed'), ('c', 'Never'), ('d', 'When there is lots of evidence')], 'd'),
        ('What is a credible interval?',
         [('a', 'A range containing the unknown value with a stated probability'), ('b', 'A break in a meeting'), ('c', 'A time of day'), ('d', 'A cable length')], 'a'),
        ('Why check sensitivity to the prior?',
         [('a', 'To remove the evidence'), ('b', 'To see how much the answer depends on the starting belief'), ('c', 'To make the prior bigger'), ('d', 'To print the result')], 'b'),
    ],
}
