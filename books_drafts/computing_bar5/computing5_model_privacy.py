"""Model privacy: membership inference, model inversion, model stealing, query limits, differentially private training and auditing."""
CODE = 'computing5_model_privacy'
BOOK = {
    "title": 'Model Privacy and Extraction',
    "subtitle": 'What a trained model can reveal about its training data, and how to limit it',
    "chapters": [
        ('A model can leak',
         'A trained model can sometimes reveal things about the data it learned from. Privacy attacks ask what the model knows, not just what it can predict.'),
        ('Membership inference',
         'In a membership inference attack, someone guesses whether a particular record was in the training set. Models often act more confidently on examples they have seen before.'),
        ('Model inversion and stealing',
         "Model inversion tries to rebuild rough versions of training inputs from the model's answers. Model stealing copies a model by sending many queries and learning from the replies."),
        ('Limiting queries',
         'Services can limit how many questions one user may ask, watch for patterns of probing, and return less detail in each answer. These steps make copying harder and cost the attacker time.'),
        ('Differential privacy',
         "Differentially private training adds carefully measured noise while the model learns, so no single person's record has a large effect on the result. A privacy budget, often written as epsilon, limits how much can be revealed."),
        ('Auditing',
         'Teams test their models by running privacy attacks on them before release. A model that passes these tests is safer, though no test proves that nothing leaks.'),
    ],
    "test": [
        ('What does a membership inference attack try to find out?',
         [('a', "The model's price"), ('b', 'Whether a given record was in the training data'), ('c', 'The colour of the server'), ('d', 'The speed of training')], 'b'),
        ('What is model stealing?',
         [('a', 'Deleting a model from a server'), ('b', 'Paying for a model with cash'), ('c', 'Copying a model by sending it many queries'), ('d', "Printing the model's code on a poster")], 'c'),
        ('What does differentially private training add?',
         [('a', 'Extra copies of each record'), ('b', 'Faster hardware'), ('c', 'A longer list of names'), ('d', 'Carefully measured noise')], 'd'),
        ('Which step makes stealing a model harder?',
         [('a', 'Giving unlimited answers to everyone'), ('b', 'Publishing the training data'), ('c', 'Limiting how many queries one user may make'), ('d', 'Turning off the logs')], 'c'),
        ('What does epsilon measure in differential privacy?',
         [('a', 'The number of people in the room'), ('b', 'The amount of privacy budget, a measure of how much can be revealed'), ('c', "The model's accuracy in percent"), ('d', 'The number of servers used')], 'b'),
    ],
}
