"""The 2024 Content Update Outage: a faulty update to endpoint software, crash loops, recovery steps, staged rollouts, cost and lessons."""
CODE = 'computing5_crowdstrike_outage'
BOOK = {
    "title": 'The 2024 Content Update Outage',
    "subtitle": 'One faulty file, and millions of machines that would not start',
    "chapters": [
        ('A faulty content update',
         'In July 2024 a faulty update to a security sensor used on Windows computers caused many machines to crash. The update was a content file meant to add detection rules. Its fault stopped the machines during startup.'),
        ('Crash loops',
         'Affected computers were caught in a loop: they crashed, restarted, and crashed again before they could finish starting up. Airlines, hospitals, banks and broadcasters were among those hit. Recovery was slow because many machines needed hands-on help.'),
        ('Recovery steps',
         'Staff had to start each machine in a special safe mode, remove the faulty file, and restart. Some machines had to be fixed one at a time, and many organisations needed days to restore services fully.'),
        ('Staged rollouts',
         'The incident showed the value of releasing changes in stages, to a small group first, and watching the results before wider release. Sending one change to every machine at once raises the risk.'),
        ('Cost',
         'Estimates of the economic cost ran into billions of dollars across many industries. The outage showed how much modern life depends on a few shared tools.'),
        ('Lessons',
         'Test changes on a range of real systems, roll out in stages, keep rollback plans ready, and treat security tools as critical infrastructure.'),
    ],
    "test": [
        ('What kind of update caused the crashes?',
         [('a', 'A printer driver for a museum'), ('b', 'A content update to a security sensor'), ('c', 'A new computer game'), ('d', 'A holiday greeting card')], 'b'),
        ('What were the affected machines caught in?',
         [('a', 'A traffic jam'), ('b', 'A queue at a shop'), ('c', 'A crash loop, crashing and restarting before they could finish starting'), ('d', 'A deep sleep lasting a week')], 'c'),
        ('What was needed to recover many machines?',
         [('a', 'Starting each one in safe mode, removing the faulty file, and restarting'), ('b', 'Nothing, since they fixed themselves'), ('c', 'Buying new monitors'), ('d', 'Turning the computers into paperweights')], 'a'),
        ('Which practice would have reduced the risk?',
         [('a', 'Sending every change to all machines at once'), ('b', 'Never testing anything'), ('c', 'Ignoring rollback plans'), ('d', 'Releasing changes in stages to a small group first')], 'd'),
        ('How should security tools be viewed?',
         [('a', 'As toys'), ('b', 'As critical infrastructure'), ('c', 'As optional extras'), ('d', 'As marketing slogans')], 'b'),
    ],
}
