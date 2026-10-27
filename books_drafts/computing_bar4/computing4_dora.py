"""Delivery Metrics: four measures of how well a software team delivers, and how to measure them fairly."""
CODE = 'computing4_dora'
BOOK = {
    "title": 'Delivery Metrics',
    "subtitle": 'Four measures of how well a team delivers, and how to use them fairly',
    "chapters": [
        ('Four key measures',
         'Research by the DORA group, described in the book Accelerate, names four key measures of software delivery. They are deployment frequency, lead time for changes, change failure rate and time to restore service. Together they show both speed and stability.'),
        ('Deployment frequency',
         'Deployment frequency is how often a team releases working changes to users. Teams that release often usually make smaller changes, which are easier to understand and fix. The number is useful only when the releases are real and useful.'),
        ('Lead time for changes',
         'Lead time is the time from a change being committed to it running in production. A short lead time means ideas reach users quickly. Long waits often hide slow reviews, slow tests or slow approvals.'),
        ('Change failure rate',
         'Change failure rate is the share of changes that cause a failure needing a fix, such as a rollback or a hotfix. It measures quality of delivery. A team that moves fast but breaks things often will show a high rate.'),
        ('Time to restore service',
         'Time to restore is how long it takes to recover from a failure in production. A fast recovery often matters more to users than a rare failure. Practice, clear runbooks and good monitoring all shorten this time.'),
        ('Measuring fairly',
         'Measure teams, not individuals, and measure the system, not people. Never compare teams whose work is very different. Use the numbers to start conversations, not to rank people, because pressure on a number changes behaviour.'),
    ],
    "test": [
        ('How many key measures does the DORA research name?',
         [('a', 'Four'), ('b', 'Two'), ('c', 'Nine'), ('d', 'Twelve')], 'a'),
        ('What is lead time for changes?',
         [('a', 'The time spent on lunch'), ('b', 'The number of staff in the team'), ('c', 'The time from commit to the change running in production'), ('d', 'The cost of the office')], 'c'),
        ('What does change failure rate measure?',
         [('a', 'The number of printers broken'), ('b', 'The share of changes that cause a failure needing a fix'), ('c', 'The colour of the code'), ('d', 'The age of the team lead')], 'b'),
        ('Why is time to restore service important?',
         [('a', 'It counts the number of meetings'), ('b', 'It decides salaries alone'), ('c', 'It stops all failures'), ('d', 'Fast recovery often matters a great deal to users')], 'd'),
        ('What is a sensible way to use these measures?',
         [('a', 'To start conversations about the system'), ('b', 'To rank individual people against each other'), ('c', 'To punish teams with high numbers'), ('d', 'To hide bad results from the company')], 'a'),
    ],
}
