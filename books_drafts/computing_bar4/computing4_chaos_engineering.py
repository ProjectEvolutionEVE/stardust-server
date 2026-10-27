"""Chaos Engineering: breaking parts of a system on purpose, in a controlled way, to learn how it really behaves."""
CODE = 'computing4_chaos_engineering'
BOOK = {
    "title": 'Chaos Engineering',
    "subtitle": 'Breaking parts of a system on purpose, in a controlled way, to learn how it really behaves',
    "chapters": [
        ('Steady-state hypotheses',
         'A chaos experiment starts with a steady state, a measurable sign that the system is healthy, such as the share of successful requests. The team then predicts that the steady state will survive a specific fault. The experiment tests that prediction.'),
        ('Injecting faults',
         'Faults might include a server stopping, a network link slowing, or a dependency returning errors. Each fault should be small and specific at first. Starting with a big failure teaches little and can cause real harm.'),
        ('Blast radius',
         'The blast radius is how much of the system, and how many users, an experiment can affect. Keep it small, and have a way to stop the experiment at once. A good experiment is one that teaches without causing a major outage.'),
        ('Game days',
         'A game day is a planned event where a team runs failures together and practises its response. People learn how to communicate and how to use the runbooks. Game days also reveal missing alerts and unclear ownership.'),
        ('Automation',
         'Once the team trusts small experiments, some can run automatically on a schedule. Automated experiments catch new weaknesses as the system changes. Automation still needs stop rules and clear owners.'),
        ('Learning from experiments',
         'Record what was predicted, what happened and what was changed afterwards. A failed prediction is valuable, because it shows a gap in understanding. Share results so that other teams learn the same lessons.'),
    ],
    "test": [
        ('What is a steady-state hypothesis?',
         [('a', 'A prediction that a measurable sign of health will survive a fault'), ('b', 'A rule about desk layouts'), ('c', 'A plan for the holidays'), ('d', 'A type of password')], 'a'),
        ('What is the blast radius of an experiment?',
         [('a', 'The noise made by a server fan'), ('b', 'The size of an explosion in the office'), ('c', 'How much of the system and how many users it can affect'), ('d', 'The number of coffee cups used')], 'c'),
        ('Why start with small faults?',
         [('a', 'Big faults are never worth studying'), ('b', 'They teach something without causing a major outage'), ('c', 'Small faults are always more dangerous'), ('d', 'Faults are only allowed on Fridays')], 'b'),
        ('What is a game day?',
         [('a', 'A holiday for the staff'), ('b', 'A sporting event for customers'), ('c', 'A day with no servers'), ('d', 'A planned event where a team runs failures together and practises its response')], 'd'),
        ('What should an experiment always have?',
         [('a', 'A way to stop it at once'), ('b', 'No record of what happened'), ('c', 'A surprise for the customers'), ('d', 'The largest possible blast radius')], 'a'),
    ],
}
