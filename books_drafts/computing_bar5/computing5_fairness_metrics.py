"""Fairness Metrics in Models: the common ways to measure whether a model treats groups of people fairly, and why they conflict."""
CODE = 'computing5_fairness_metrics'
BOOK = {
    "title": 'Fairness Metrics in Models',
    "subtitle": 'Group error rates, demographic parity, and the trade-offs between them',
    "chapters": [
        ('What fairness measures',
         'Fairness metrics compare how a model treats different groups of people. The groups must be defined carefully, and the data about them must be reliable. No single number tells the whole story.'),
        ('Group error rates',
         'A simple check compares error rates across groups, such as the share of wrong decisions for each one. Large gaps are a warning sign. The check needs enough examples in each group to be meaningful.'),
        ('Demographic parity',
         'Demographic parity asks whether each group receives positive decisions at the same rate. It is easy to state but can ignore real differences in the situations being judged. It is one lens among several.'),
        ('Equalised odds',
         'Equalised odds asks for similar true positive and false positive rates across groups. It focuses on whether the model is equally accurate for people who truly qualify and those who do not. It needs reliable labels to check.'),
        ('Trade-offs between metrics',
         'When base rates differ between groups, several fairness criteria cannot all hold at once, except in special cases. Choosing a metric is therefore a value judgement. The trade-off should be stated openly, not hidden in a technical choice.'),
        ('Measurement and governance',
         'Teams must decide who is measured, over what period, and who signs off the trade-off. Good governance records the choice, the reasons and the people accountable. Monitoring continues after launch, because data and behaviour change.'),
    ],
    "test": [
        ('What does a group error rate check compare?',
         [('a', 'The share of wrong decisions across groups'), ('b', "The colour of each group's logo"), ('c', "The size of each group's office"), ('d', 'The number of meetings held')], 'a'),
        ('What does demographic parity ask?',
         [('a', 'Whether the model is written in one language'), ('b', 'Whether the server is cooled'), ('c', 'Whether groups receive positive decisions at the same rate'), ('d', 'Whether the screen is large')], 'c'),
        ('What does equalised odds focus on?',
         [('a', 'The speed of the network card'), ('b', 'Similar true and false positive rates across groups'), ('c', 'The price of the training data'), ('d', 'The number of colours in the interface')], 'b'),
        ('Why can several fairness criteria not all hold at once?',
         [('a', 'Because fairness is never measured'), ('b', 'Because computers cannot add numbers'), ('c', 'Because groups never have members'), ('d', 'When base rates differ between groups, in most cases')], 'd'),
        ('What should happen to a fairness trade-off?',
         [('a', 'It should be stated openly and the people accountable recorded'), ('b', 'It should be hidden in a technical setting'), ('c', 'It should be decided by the weather'), ('d', 'It should be deleted after launch')], 'a'),
    ],
}
