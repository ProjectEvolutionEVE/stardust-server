"""Measuring Inequality: the Lorenz curve, the Gini coefficient, quintile shares, wealth against income, international comparisons and the limits of one number."""
CODE = 'business5_gini'
BOOK = {
    "title": 'Measuring Inequality',
    "subtitle": 'The Lorenz curve, the Gini number and what they miss',
    "chapters": [
        ('Why measure inequality',
         'To talk about inequality, economists need a way to measure it. The simplest question is how income or wealth is shared among people. Several tools answer this, and each shows a different side of the picture.'),
        ('The Lorenz curve',
         'Max Lorenz, in 1905, proposed a curve that plots the share of income held by the poorest people against the population. If everyone had the same income, the curve would be a straight diagonal line. The further the curve bows below that line, the more unequal the society.'),
        ('The Gini coefficient',
         'The Gini coefficient, introduced by the Italian statistician Corrado Gini in 1912, sums up the Lorenz curve in one number. A value of 0 means perfect equality, and a value of 1 means one person has everything. Real countries sit somewhere between.'),
        ('Quintile shares',
         'Another method splits the population into five equal groups, called quintiles, and reports the share of income held by each. The top quintile share and the bottom quintile share give a clear and simple picture. Many official reports use this approach.'),
        ('Wealth against income',
         'Income is what people earn in a year, while wealth is what they own, such as homes, savings and shares. Wealth is usually much more unequal than income. A measure of one may tell a different story from a measure of the other.'),
        ('Limits of one number',
         'A single Gini figure can hide a lot. Two countries with the same number can have very different patterns of poverty and wealth. Careful researchers look at several measures and check what the numbers leave out.'),
    ],
    "test": [
        ('What does a Gini coefficient of 0 mean?',
         [('a', 'Perfect inequality'), ('b', 'Perfect equality'), ('c', 'No data at all'), ('d', 'A measure of rainfall')], 'b'),
        ('Who proposed the Lorenz curve in 1905?',
         [('a', 'Adam Smith'), ('b', 'Karl Marx'), ('c', 'Max Lorenz'), ('d', 'Simon Kuznets')], 'c'),
        ('In what year was the Gini coefficient introduced?',
         [('a', '1776'), ('b', '1999'), ('c', '1848'), ('d', '1912')], 'd'),
        ('What is a quintile?',
         [('a', 'One of five equal groups of the population'), ('b', 'A type of ship'), ('c', 'A coin from Chile'), ('d', 'A gold bar')], 'a'),
        ('Why can one Gini figure hide a lot?',
         [('a', 'Because it is always wrong'), ('b', 'Different countries can share the same number with very different patterns'), ('c', 'Because it measures the Moon'), ('d', 'Because it has no units at all')], 'b'),
    ],
}
