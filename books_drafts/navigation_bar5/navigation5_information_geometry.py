"""Information Geometry: how families of probability distributions form curved spaces, and how that helps in estimation."""
CODE = 'navigation5_information_geometry'
BOOK = {
    "title": 'Information Geometry',
    "subtitle": 'Manifolds of distributions, the Fisher metric, estimation, bounds and uses',
    "chapters": [
        ('Distributions as points',
         'A probability distribution can be treated as a single point in a space. A family of distributions, such as all normal curves, then forms a shape called a manifold. This view lets us ask how two distributions differ geometrically.'),
        ('Manifolds of distributions',
         'Each member of a family is a point, and moving the settings moves you across the manifold. The family can be curved, which means that equal changes in the settings do not always produce equal changes in the distributions.'),
        ('The Fisher metric',
         'The Fisher metric measures how much a distribution changes when its settings change. It gives a way to measure distance between distributions. It is the natural metric for statistical models.'),
        ('Estimation',
         'Estimating a setting from data is easier when you know the geometry of the model. Methods that follow the curved space can be more accurate than naive ones. Maximum likelihood is one of the central ideas here.'),
        ('Bounds',
         'The Cramer-Rao bound says that no unbiased estimator can be more precise than a limit set by the Fisher information. The bound is a guide to how well any method can do.'),
        ('Uses',
         'Information geometry is used in machine learning, signal processing and the study of sensors. It helps design estimators and understand their limits. It also shows how noise and data quality affect the answer.'),
    ],
    "test": [
        ('What is treated as a point in information geometry?',
         [('a', 'A tin of paint'), ('b', 'A city on a map'), ('c', 'A single probability distribution'), ('d', 'A ship in dock')], 'c'),
        ('What is a manifold of distributions?',
         [('a', 'A family of distributions forming a shape'), ('b', 'A type of boat sail'), ('c', 'A list of prices'), ('d', 'A kind of rain')], 'a'),
        ('What does the Fisher metric measure?',
         [('a', 'The weight of a ship'), ('b', 'How much a distribution changes when its settings change'), ('c', 'The length of a road'), ('d', 'The number of seats')], 'b'),
        ('What does the Cramer-Rao bound limit?',
         [('a', 'The height of a mountain'), ('b', 'The number of sailors'), ('c', 'The price of tea'), ('d', 'How precise any unbiased estimate can be')], 'd'),
        ('Where is information geometry used?',
         [('a', 'Only in cooking'), ('b', 'In machine learning and signal processing'), ('c', 'In painting houses'), ('d', 'In growing vegetables')], 'b'),
    ],
}
