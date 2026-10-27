"""Adversarial machine learning: evasion and poisoning attacks on models, defences, threat models and the limits of robustness."""
CODE = 'computing5_adversarial_ml'
BOOK = {
    "title": 'Adversarial Machine Learning',
    "subtitle": 'How small changes can fool a model, and how teams defend against them',
    "chapters": [
        ('Fooling a model',
         'A machine learning model learns patterns from examples. Researchers found that a tiny change to an input, too small for a person to notice, can make a model give a confident wrong answer.'),
        ('Evasion attacks',
         'An evasion attack changes an input when the model is already in use. A spam filter might be fooled by a message with altered spellings that people still read easily.'),
        ('Poisoning attacks',
         'A poisoning attack happens earlier, during training. An attacker slips bad examples into the training data so the model learns a wrong or hidden rule.'),
        ('Defences',
         'Common defences include training on adversarial examples, cleaning inputs, and checking how a model behaves under many small changes. Each defence helps against some attacks and not others.'),
        ('Threat models',
         "A threat model states who the attacker is and what they know, such as whether they can see the model's inner workings. Robustness testing then checks the model against that picture."),
        ('Limits',
         'Defences often trade some accuracy for robustness, and many early defences were broken by stronger attacks. Security for models is an ongoing contest, not a solved problem.'),
    ],
    "test": [
        ('What is an adversarial example?',
         [('a', 'A model that is too large'), ('b', 'An input changed slightly so the model gives a wrong answer'), ('c', 'A training run that failed'), ('d', 'A chart of model results')], 'b'),
        ('When does an evasion attack happen?',
         [('a', 'Only when the model is turned off'), ('b', 'Before any data is collected'), ('c', 'When the model is already in use'), ('d', 'When the model has no users')], 'c'),
        ('What does a poisoning attack change?',
         [('a', 'The training data, so the model learns a wrong rule'), ('b', 'The colour of the screen'), ('c', 'The speed of the internet'), ('d', "The model's name")], 'a'),
        ('Which is a common defence?',
         [('a', 'Turning off all inputs'), ('b', 'Writing the model on paper'), ('c', 'Using a larger screen'), ('d', 'Training with adversarial examples included')], 'd'),
        ('Why is a threat model useful?',
         [('a', 'It sets the price of a model'), ('b', 'It states what the attacker can do and know'), ('c', "It names the model's author"), ('d', 'It makes training faster')], 'b'),
    ],
}
