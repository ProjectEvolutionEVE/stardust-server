"""Propagation Error Over Time: why predictions grow less certain the further ahead they reach."""
CODE = 'navigation5_propagation_error'
BOOK = {
    "title": 'Propagation Error Over Time',
    "subtitle": 'Model errors, initial-state errors, growth, covariance, prediction horizon and forecasts',
    "chapters": [
        ('Model errors',
         'A prediction uses a model of the forces and motions involved. No model is perfect, so each step of the prediction adds a small error. These model errors build up as the prediction runs on.'),
        ('Initial-state errors',
         'A prediction starts from an estimated position and velocity. Those starting values are never exact. A small error at the start can grow into a large one later.'),
        ('Growth',
         'Errors often grow slowly at first and then faster. The growth depends on the system and on how sensitive the path is. Some systems are much more sensitive than others.'),
        ('Covariance',
         'The covariance is a measure of uncertainty that grows as the prediction runs forward. It shows how spread out the likely positions are. A wide spread means the forecast is less certain.'),
        ('Prediction horizon',
         'The prediction horizon is how far ahead a forecast is made. Longer horizons carry more uncertainty. Good planning uses the horizon that the accuracy can support.'),
        ('Forecasts',
         'A forecast should always come with its uncertainty. Users need to know how far to trust it. Updating the forecast with new data keeps the uncertainty under control.'),
    ],
    "test": [
        ('What is a propagation error?',
         [('a', 'A typing mistake'), ('b', 'A mistake in a shop'), ('c', 'An error in predicted state that grows as the prediction runs forward in time'), ('d', 'A camera glitch')], 'c'),
        ('What is an initial-state error?',
         [('a', 'A wrong starting position or velocity'), ('b', 'A wrong colour'), ('c', 'A late train'), ('d', 'A typing game')], 'a'),
        ('What is covariance?',
         [('a', 'A shop'), ('b', 'A type of paint'), ('c', 'A wooden box'), ('d', 'A measure of uncertainty that grows with prediction time')], 'd'),
        ('What is a prediction horizon?',
         [('a', 'The view from a hill'), ('b', 'How far ahead the forecast is made'), ('c', 'A horizon line on a map'), ('d', 'A sunrise')], 'b'),
        ('Why do forecasts need an uncertainty?',
         [('a', 'They cost nothing'), ('b', 'They tell users how far to trust a prediction'), ('c', 'They paint pictures'), ('d', 'They remove weather')], 'b'),
    ],
}
