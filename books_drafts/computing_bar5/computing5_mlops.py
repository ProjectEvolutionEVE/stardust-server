"""MLOps: Pipelines and Monitoring: running machine learning models in real life, with repeatable training, safe releases and watchful monitoring."""
CODE = 'computing5_mlops'
BOOK = {
    "title": 'MLOps: Pipelines and Monitoring',
    "subtitle": 'Keeping models repeatable, released safely, and watched after launch',
    "chapters": [
        ('Why MLOps exists',
         'A model that works in a notebook is not yet a service. MLOps brings the discipline of software operations to machine learning. The aim is training and release that anyone on the team can repeat.'),
        ('Training pipelines',
         'A training pipeline runs every step from data preparation to evaluation in a fixed order. Each run records the code, the data version and the settings used. That record makes results reproducible and easier to audit.'),
        ('Model registries',
         'A model registry stores trained models with their metadata, test results and approval status. Only approved models move toward production. The registry gives the team one trusted place to find what is live.'),
        ('Drift detection',
         'Drift happens when the data arriving in production differs from the data used in training. It can also happen when the relationship between inputs and outcomes changes. Monitoring compares live inputs and outputs with the baseline and raises an alert when the gap grows.'),
        ('Rollbacks and data versioning',
         'A release should be easy to reverse, so the previous model can return quickly if the new one misbehaves. Data versioning keeps track of which dataset trained which model. Without it, a bad result cannot be traced back to its cause.'),
        ('On-call for models',
         'Someone must answer when a model fails in the night. Runbooks describe the checks, the rollback steps and who decides. Post-incident reviews turn each failure into a better pipeline or a better test.'),
    ],
    "test": [
        ('What does a training pipeline record for each run?',
         [('a', 'The weather in the data centre'), ('b', 'The code, data version and settings used'), ('c', 'The name of the office manager'), ('d', 'The colour of the monitor')], 'b'),
        ('What does a model registry hold?',
         [('a', 'Only photographs of servers'), ('b', 'Customer invoices'), ('c', 'Music tracks'), ('d', 'Trained models with their metadata and approval status')], 'd'),
        ('What is drift?',
         [('a', 'Production data changing away from the training data'), ('b', 'A model learning too fast'), ('c', 'A server moving to another room'), ('d', 'A loss of battery power')], 'a'),
        ('Why does a release need an easy rollback?',
         [('a', 'So the release can be printed'), ('b', 'So no one needs to test it'), ('c', 'So the previous model can return quickly if the new one fails'), ('d', 'So the data is deleted')], 'c'),
        ('What do runbooks give an on-call team?',
         [('a', 'A recipe for lunch'), ('b', 'A list of hardware colours'), ('c', 'A guarantee that no failure will happen'), ('d', 'The checks, rollback steps and who decides')], 'd'),
    ],
}
