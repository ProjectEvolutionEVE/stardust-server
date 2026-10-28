"""Convolutional neural networks: filters on images, stacked layers, pooling, receptive fields, residual networks and limits."""
CODE = 'computing5_cnn'
BOOK = {
    "title": 'Convolutional Neural Networks',
    "subtitle": 'Filters that slide over images to find edges, shapes and objects',
    "chapters": [
        ('Filters on images',
         'A convolutional network slides small filters across an image. Each filter responds strongly where its pattern appears, such as an edge.'),
        ('Stacking layers',
         'Early layers find simple edges, and later layers combine them into shapes and parts. Deeper layers see larger areas of the picture.'),
        ('Pooling',
         'Pooling layers shrink the image by keeping a summary of each small area, such as its largest value. This makes the network less sensitive to small shifts.'),
        ('Receptive fields',
         'The receptive field is the area of the original image that affects a unit. It grows with depth, so deep units can respond to whole objects.'),
        ('Residual networks',
         'Residual networks, introduced in 2015, add skip connections that carry the input past a few layers. This makes very deep networks easier to train.'),
        ('Data and limits',
         'These networks need large labelled data sets and a lot of computing power. They can still be fooled by small changes, and they do not understand what the objects mean.'),
    ],
    "test": [
        ('What does a convolutional filter do?',
         [('a', 'Responds strongly where its pattern appears'), ('b', 'Prints the image'), ('c', 'Stores a password'), ('d', 'Changes the colour of the room')], 'a'),
        ('What do early layers usually find?',
         [('a', 'Email addresses'), ('b', 'Simple edges'), ('c', 'Sound waves'), ('d', 'The price of a car')], 'b'),
        ('What does pooling do?',
         [('a', 'Adds noise on purpose'), ('b', 'Deletes the labels'), ('c', 'Turns the image into text'), ('d', 'Shrinks the image by keeping a summary of each area')], 'd'),
        ('What is a receptive field?',
         [('a', 'A field for crops'), ('b', 'A type of cable'), ('c', 'The area of the original image that affects a unit'), ('d', 'A sports pitch')], 'c'),
        ('What do residual networks add?',
         [('a', 'A second screen'), ('b', 'More passwords'), ('c', 'Less data'), ('d', 'Skip connections that help very deep networks train')], 'd'),
    ],
}
