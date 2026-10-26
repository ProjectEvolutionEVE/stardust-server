"""Monte Carlo Simulation: running many random trials to see the range of outcomes."""
CODE = "business4_montecarlo"
BOOK = {
    "title": "Monte Carlo Simulation",
    "subtitle": "Running many random trials to see the range of outcomes",
    "chapters": [
        ("The name and its origin",
         "Monte Carlo simulation is named after the casino town in Monaco. The method was developed in the 1940s by scientists including Stanislaw Ulam, John von Neumann and Nicholas Metropolis, who worked at Los Alamos on nuclear problems."),
        ("Random trials",
         "Instead of producing one forecast, the method runs thousands of trials. In each trial, the uncertain inputs are drawn at random from ranges or distributions. The results form a picture of the possible outcomes, rather than a single number."),
        ("Building a model",
         "First write down the relationships, such as income, costs, growth and returns. Then decide which inputs are uncertain, and what range each could take. A model is only as good as its assumptions, so write them down clearly."),
        ("Reading a distribution",
         "The output is a distribution: the chance of each result. Look at the median, the spread and the tails, not only the average. A plan that works in most trials but fails badly in a few should be seen for what it is."),
        ("A retirement example",
         "A retirement model might draw random yearly returns for a portfolio, along with random spending shocks. Repeating the run thousands of times shows the share of runs in which savings last to the end. The answer is a probability, not a promise."),
        ("Honest limits",
         "Results depend on the chosen distributions, and real events can fall outside them. Correlations can shift in a crisis. A simulation shows how sensitive a plan is to its assumptions, and it should be paired with sound judgement."),
    ],
    "test": [
        ("Where does the Monte Carlo name come from?",
         [("a", "A casino town in Monaco"), ("b", "A famous scientist"), ("c", "A type of bond"), ("d", "A river")], "a"),
        ("What does a Monte Carlo simulation produce?",
         [("a", "One exact forecast"), ("b", "A distribution of possible outcomes"), ("c", "A tax bill"), ("d", "A single price")], "b"),
        ("Why look beyond the average in simulation results?",
         [("a", "Tails do not exist"), ("b", "Averages are always right"), ("c", "Spread is a tax"), ("d", "Averages hide spread and tails")], "d"),
        ("In a retirement example, what does the share of runs where savings last show?",
         [("a", "A promise"), ("b", "A probability"), ("c", "A bank rate"), ("d", "A tax rule")], "b"),
        ("What is a limit of simulation?",
         [("a", "It is always certain"), ("b", "It needs no assumptions"), ("c", "Results depend on chosen distributions, which may miss real events"), ("d", "It cannot be run on a computer")], "c"),
    ],
}
