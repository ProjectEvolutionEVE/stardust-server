"""Neural networks and backpropagation: layers and weights, activation functions, loss, the chain rule and vanishing gradients."""
CODE = 'computing5_neural_networks'
BOOK = {
    "title": 'Neural Networks and Backpropagation',
    "subtitle": 'Layers of simple units, and how errors flow backward to improve them',
    "chapters": [
        ('Layers of units',
         'A neural network is built from layers of simple units. Each unit multiplies its inputs by weights, adds a bias, and passes the result through an activation function.'),
        ('Activation functions',
         'Activation functions add a bend to the output, so the network can learn curved patterns. The ReLU function, which outputs zero for negative inputs and the input itself otherwise, is widely used.'),
        ('Measuring error',
         'A loss function measures how far the output is from the right answer. The goal of training is to make this loss smaller.'),
        ('The chain rule',
         'The chain rule from calculus says how a change in one step affects the next. It lets errors be traced back through each layer.'),
        ('Backpropagation',
         'Backpropagation uses the chain rule to work out how much each weight should change. Those changes are applied, so the network improves a little on each pass.'),
        ('Vanishing gradients and starting points',
         'In deep networks with some activation functions, the signals passed back can shrink toward zero, so early layers learn slowly. Good starting values for weights, such as He or Xavier initialisation, help.'),
    ],
    "test": [
        ('What does each unit in a layer do?',
         [('a', 'Multiplies inputs by weights, adds a bias, and applies an activation'), ('b', 'Prints the output'), ('c', 'Stores the training data'), ('d', 'Deletes old layers')], 'a'),
        ('What does an activation function add?',
         [('a', 'A colour'), ('b', 'A copy of the data'), ('c', 'A password'), ('d', 'A bend, so the network can learn curved patterns')], 'd'),
        ('What is backpropagation used for?',
         [('a', 'Sending email'), ('b', 'Computing how each weight should change'), ('c', 'Drawing graphs'), ('d', 'Playing sound')], 'b'),
        ('What does the chain rule do here?',
         [('a', 'Counts layers'), ('b', 'Stops training'), ('c', 'Traces the effect of a change through each layer'), ('d', 'Changes the colour of errors')], 'c'),
        ('What is the vanishing gradient problem?',
         [('a', 'Signals passed back shrink, so early layers learn slowly'), ('b', 'The network grows too large to store'), ('c', 'The network forgets its name'), ('d', 'The screen goes blank')], 'a'),
    ],
}
