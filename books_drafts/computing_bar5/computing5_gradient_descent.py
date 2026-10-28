"""Gradient descent in depth: learning rates, momentum, adaptive methods such as Adam, mini-batches and saddle points."""
CODE = 'computing5_gradient_descent'
BOOK = {
    "title": 'Gradient Descent in Depth',
    "subtitle": 'Walking downhill on the error surface, with careful choices of step size and direction',
    "chapters": [
        ('Walking downhill',
         'Gradient descent improves a model by stepping in the direction that lowers the error most quickly. The gradient points uphill, so the step goes the other way.'),
        ('Step size',
         'The learning rate sets how big each step is. Too large and the steps overshoot, too small and training takes forever.'),
        ('Momentum',
         "Momentum keeps some of the previous step's direction, which helps the walk roll through flat areas and past small bumps."),
        ('Adaptive methods',
         'Methods such as Adam, published in 2014, adjust the step size for each weight using recent gradient history. They are a common default for training.'),
        ('Mini-batches',
         'Using a small random batch of examples for each step is cheaper than using all of them, and the noise can help escape poor spots.'),
        ('Saddle points',
         'In high-dimensional problems, many flat spots are saddle points, where some directions go up and others go down. Careful steps and noise help the walk leave them.'),
    ],
    "test": [
        ('Which direction does a gradient descent step go?',
         [('a', 'Downhill, against the gradient'), ('b', 'Uphill, along the gradient'), ('c', 'Sideways only'), ('d', 'Off the screen')], 'a'),
        ('What happens if the learning rate is too large?',
         [('a', 'Training always stops'), ('b', 'The data is deleted'), ('c', 'Steps overshoot the best point'), ('d', 'The model becomes a picture')], 'c'),
        ('What does momentum keep?',
         [('a', 'The old error forever'), ('b', 'Every value at zero'), ('c', 'A copy of the screen'), ('d', "Part of the previous step's direction")], 'd'),
        ('What is Adam?',
         [('a', 'A type of printer'), ('b', 'An adaptive method that adjusts step sizes'), ('c', 'A kind of image'), ('d', 'A password rule')], 'b'),
        ('Why use small random batches?',
         [('a', 'They are cheaper and the noise can help'), ('b', 'They make the error larger'), ('c', 'They stop all learning'), ('d', 'They need no computer')], 'a'),
    ],
}
